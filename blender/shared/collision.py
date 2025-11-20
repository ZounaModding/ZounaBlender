import bpy
import bmesh
import gpu
from gpu_extras.batch import batch_for_shader
from bpy.utils import register_class, unregister_class
from bpy.types import Object
from mathutils import Vector, Matrix
from math import radians
from typing import Dict

from ...common.constants import (
    ColPrimitiveType,
    ColPrimitiveCategory,
    RatSurfaceTypes,
    RatSoundTypes,
    CATEGORY_COLORS,
)
from ...common.util import (
    get_selected_verts_world_pos,
    get_verts_bbox,
    get_material_from_context,
)


def create_collision_dummy(col_prim_type: ColPrimitiveType) -> bpy.types.Object:
    """
    Create an Empty (Dummy) object without using bpy.ops.

    Parameters:
        col_prim_type (ColPrimitiveType): The type of collision primitive.

    Returns:
        bpy.types.Object: The created empty object.
    """
    if col_prim_type == ColPrimitiveType.NONE:
        raise ValueError("Cannot create dummy for ColPrimitiveType.NONE")
    name = "Zouna Primitive Collision"
    empty_obj = bpy.data.objects.new(name, None)
    empty_obj.is_zouna = True
    empty_obj.zouna_property.col_primitive_type = col_prim_type
    empty_obj.zouna_property.col_primitive_category = ColPrimitiveCategory.COLLIDER
    empty_obj.zouna_property.rat_surface_type = RatSurfaceTypes.SOLID
    empty_obj.zouna_property.rat_sound_type = RatSoundTypes.STONE
    empty_obj.show_in_front = True
    empty_obj.empty_display_size = 0
    return empty_obj


def set_collision_dummy_scale(dummy: bpy.types.Object, scale: list[float]):
    for i, s in enumerate(scale):
        if s <= 0:
            scale[i] = 0.01

    col_prim_type = dummy.zouna_property.col_primitive_type
    if col_prim_type == ColPrimitiveType.BOX:
        dummy.scale = scale
    elif col_prim_type == ColPrimitiveType.SPHERE:
        max_value = max(scale)
        dummy.scale = [max_value] * 3
    elif col_prim_type == ColPrimitiveType.CYLINDER:
        max_value = max(scale[:2])
        dummy.scale = [max_value, max_value, scale[2]]


def set_collision_dummy_transform(dummy, center, scale, parent=None):
    dummy.location = center
    set_collision_dummy_scale(dummy, scale)
    bpy.context.view_layer.update()
    if parent:
        dummy.parent = parent
        dummy.matrix_parent_inverse = parent.matrix_world.inverted()


def add_collision_dummy_under_obj(col_prim_type: ColPrimitiveType, parent):
    """Create a Zouna collision that fits provided parent.

    Args:
        context: Current Context.
        parent: Mesh to parent collision.
    """
    if not parent.type == "MESH":
        return

    dummy = create_collision_dummy(col_prim_type)

    for collection in parent.users_collection:
        collection.objects.link(dummy)

    center = [0, 0, 0]
    scale = [1, 1, 1]

    verts_world_pos = get_selected_verts_world_pos(parent)
    if verts_world_pos:
        center, scale = get_verts_bbox(verts_world_pos)

    set_collision_dummy_transform(dummy, center, scale, parent)
    return dummy


def add_collision_dummy(col_prim_type: ColPrimitiveType):
    dummy = create_collision_dummy(col_prim_type)
    bpy.context.collection.objects.link(dummy)
    return dummy


class ZounaCollisionPrimitive(bpy.types.Gizmo):
    bl_idname = "zouna.collision_primitive"
    bl_label = "Zouna Collision Primitive"
    bl_options = {"UNDO", "SELECT"}

    UNSELECTED_COLOR = list(bpy.context.preferences.themes[0].view_3d.empty)
    SELECTED_COLOR = list(bpy.context.preferences.themes[0].view_3d.object_selected)
    ACTIVE_COLOR = list(bpy.context.preferences.themes[0].view_3d.object_active)

    def setup(self):
        self.empty = None
        self.batch = None
        self.line_width = 2.0

    def create_custom_shape(self):
        self.batch = None

        if (
            not self.empty
            or self.empty.zouna_property.col_primitive_type == ColPrimitiveType.NONE
        ):
            return

        mesh = bpy.data.meshes.new("ZounaColTmp")
        bm = bmesh.new()

        col = self.empty.zouna_property.col_primitive_type

        if col == ColPrimitiveType.SPHERE:
            bmesh.ops.create_circle(bm, segments=32, radius=1)
            bmesh.ops.create_circle(
                bm, segments=32, radius=1, matrix=Matrix.Rotation(radians(90), 4, "X")
            )
            bmesh.ops.create_circle(
                bm, segments=32, radius=1, matrix=Matrix.Rotation(radians(90), 4, "Y")
            )

        elif col == ColPrimitiveType.BOX:
            bmesh.ops.create_cube(bm, size=2)

        elif col == ColPrimitiveType.CYLINDER:
            bmesh.ops.create_cone(
                bm,
                cap_ends=False,
                segments=32,
                radius1=1,
                radius2=1,
                depth=2,
            )

        bm.to_mesh(mesh)
        bm.free()

        coords = []
        for e in mesh.edges:
            coords.append(mesh.vertices[e.vertices[0]].co.copy())
            coords.append(mesh.vertices[e.vertices[1]].co.copy())

        bpy.data.meshes.remove(mesh)

        self.shader = gpu.shader.from_builtin("UNIFORM_COLOR")

        self.batch = batch_for_shader(self.shader, "LINES", {"pos": coords})

    def draw(self, context):
        try:
            if not self.empty or not self.empty.is_zouna or not self.batch:
                return
        except ReferenceError:
            return

        try:
            if self.empty.hide_get():
                return

            if not self.empty.visible_get(view_layer=context.view_layer):
                return

            # parent = self.empty.parent
            # if parent:
            #     if parent.hide_get():
            #         return

            #     if not parent.visible_get(view_layer=context.view_layer):
            #         return

        except (ReferenceError, AttributeError):
            return

        try:
            zp = self.empty.zouna_property
            category = zp.col_primitive_category

            is_active = self.empty == context.view_layer.objects.active
            is_selected = self.empty.select_get()

            if is_active and is_selected:
                col = self.ACTIVE_COLOR
            elif is_selected:
                col = self.SELECTED_COLOR
            elif category and category in CATEGORY_COLORS:
                col = CATEGORY_COLORS[category]
            else:
                col = self.UNSELECTED_COLOR

        except (ReferenceError, AttributeError):
            return

        shader = self.shader
        shader.bind()
        shader.uniform_float("color", (col[0], col[1], col[2], 1.0))

        try:
            if self.empty.show_in_front:
                gpu.state.depth_test_set("NONE")
            else:
                gpu.state.depth_test_set("LESS_EQUAL")
        except ReferenceError:
            return

        gpu.state.blend_set("ALPHA")
        gpu.state.line_width_set(self.line_width)

        try:
            mvp = context.region_data.perspective_matrix @ self.empty.matrix_world
        except ReferenceError:
            return

        shader.uniform_float("ModelViewProjectionMatrix", mvp)

        try:
            self.batch.draw(shader)
        except ReferenceError:
            return

        gpu.state.depth_test_set("LESS_EQUAL")
        gpu.state.line_width_set(1.0)


class ZounaCollisionPrimitiveGroup(bpy.types.GizmoGroup):
    bl_idname = "zouna.collision_primitive_group"
    bl_label = "Zouna Collision Primitive Group"
    bl_space_type = "VIEW_3D"
    bl_region_type = "WINDOW"
    bl_options = {"3D", "PERSISTENT", "SHOW_MODAL_ALL", "SELECT", "DEPTH_3D", "SCALE"}

    empties: dict[str, bpy.types.Gizmo] = {}

    @classmethod
    def poll(cls, context):
        for blender_object in context.view_layer.objects:
            if (
                blender_object.type == "EMPTY"
                and blender_object.is_zouna
                and blender_object.zouna_property.col_primitive_type
                != ColPrimitiveType.NONE.name
            ):
                return True
        return False

    def setup(self, context):
        for blender_object in context.view_layer.objects:
            if blender_object.type != "EMPTY" or not blender_object.is_zouna:
                continue

            if (
                blender_object.zouna_property.col_primitive_type
                == ColPrimitiveType.NONE.name
            ):
                continue

            if blender_object.name in self.empties:
                continue

            gizmo = self.gizmos.new(ZounaCollisionPrimitive.bl_idname)
            gizmo.empty = blender_object
            gizmo.create_custom_shape()

            # store by name
            self.empties[blender_object.name] = gizmo

    def cleanup_invalid(self):
        invalid_keys = []

        for name, gizmo in self.empties.items():
            empty = gizmo.empty
            try:
                if not empty or empty.as_pointer() == 0:
                    invalid_keys.append(name)
            except ReferenceError:
                invalid_keys.append(name)

        for name in invalid_keys:
            self.empties.pop(name, None)

    def refresh(self, context):
        self.cleanup_invalid()

        found_empties = []
        for blender_object in context.view_layer.objects:
            if (
                blender_object.type == "EMPTY"
                and blender_object.zouna_property.col_primitive_type
                != ColPrimitiveType.NONE.name
            ):
                found_empties.append(blender_object)

        found_names = {obj.name for obj in found_empties}

        for empty_obj in found_empties:
            if empty_obj.name not in self.empties:
                self.setup(context)

        existing_names = list(self.empties.keys())

        for name in existing_names:
            if name not in found_names:
                gizmo = self.empties.pop(name, None)
                if gizmo:
                    try:
                        self.gizmos.remove(gizmo)
                    except ReferenceError:
                        pass


collision_classes = [ZounaCollisionPrimitive, ZounaCollisionPrimitiveGroup]


_is_updating_collision_properties = False


def update_zouna_collision_properties(self, context):
    global _is_updating_collision_properties
    if _is_updating_collision_properties:
        return
    _is_updating_collision_properties = True

    try:
        obj = context.object
        if obj is None:
            return

        if obj.type == "EMPTY" and obj.is_zouna:
            is_material = False
            zp = obj.zouna_property
        else:
            mat = get_material_from_context(context)
            if mat is None or not mat.is_zouna:
                return
            is_material = True
            zp = mat.zouna_material

        new_surface = zp.rat_surface_type
        old_surface = zp.last_rat_surface_type
        default_sound = RatSoundTypes.STONE

        zp.last_rat_surface_type = new_surface

        # print(f"!!!COMPARING TO WATER!!!")
        # print(f"!!!OLD SURFACE: {old_surface}!!!")
        # print(f"!!!NEW SURFACE: {new_surface}!!!")
        if (
            old_surface == RatSurfaceTypes.WATER
            and new_surface != RatSurfaceTypes.WATER
        ):
            # print(f"!!!SOUND TYPE: {zp.rat_sound_type}!!!")
            if zp.rat_sound_type == RatSoundTypes.WATER:
                # print(f"!!!SETTING TO STONE!!!")
                zp.rat_sound_type = default_sound

        if new_surface == RatSurfaceTypes.NONE:
            zp.rat_sound_type = default_sound

            if not is_material:
                if zp.col_primitive_category in (
                    ColPrimitiveCategory.COLLIDER,
                    ColPrimitiveCategory.COLLECT,
                    ColPrimitiveCategory.COLLECTABLE,
                ):
                    zp.col_primitive_category = ColPrimitiveCategory.SHADOW

            return

        if new_surface == RatSurfaceTypes.COLLECT:
            if not is_material:
                zp.col_primitive_category = ColPrimitiveCategory.COLLECT
            zp.rat_sound_type = default_sound
            return

        if new_surface == RatSurfaceTypes.COLLECTABLE:
            if not is_material:
                zp.col_primitive_category = ColPrimitiveCategory.COLLECTABLE
            zp.rat_sound_type = default_sound
            return

        if new_surface == RatSurfaceTypes.WATER:
            if not is_material:
                zp.col_primitive_category = ColPrimitiveCategory.COLLIDER
            zp.rat_sound_type = RatSoundTypes.WATER
            return

        if not is_material:
            zp.col_primitive_category = ColPrimitiveCategory.COLLIDER
    finally:
        _is_updating_collision_properties = False


def register_collision():
    for cls in collision_classes:
        register_class(cls)


def unregister_collision():
    for cls in reversed(collision_classes):
        unregister_class(cls)
