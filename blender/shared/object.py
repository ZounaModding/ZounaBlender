import bpy
from bpy.types import Object, PropertyGroup
from bpy.utils import register_class, unregister_class
from ...common.constants import (
    RatSurfaceTypes,
    RatSoundTypes,
    rat_surface_types,
    rat_sound_types,
)
from ...common.constants import (
    ColPrimitiveType,
    col_primitive_types,
    ColPrimitiveCategory,
    col_primitive_categories,
)
from ..shared.collision import update_zouna_collision_properties
from .collision import ZounaCollisionPrimitiveGroup
from ...blender.shared.collision import (
    set_collision_dummy_scale,
    set_collision_dummy_transform,
)
from ...common.util import get_verts_bbox, get_selected_verts_world_pos


def update_col_prim_type(self, context):
    obj = context.object

    if obj is None or obj.type != "EMPTY" or not obj.is_zouna:
        return

    col_type = obj.zouna_property.col_primitive_type
    if col_type == ColPrimitiveType.NONE:
        return

    empties = ZounaCollisionPrimitiveGroup.empties
    gizmo = empties.get(obj.name)
    if gizmo is None:
        return

    parent = obj.parent

    if parent and parent.type == "MESH":
        verts_world = get_selected_verts_world_pos(parent)

        if verts_world:
            center, scale = get_verts_bbox(verts_world)

            set_collision_dummy_transform(
                obj, center=center, scale=scale, parent=parent
            )
        else:
            set_collision_dummy_scale(obj, obj.scale[:])
    else:
        set_collision_dummy_scale(obj, obj.scale[:])

    def deferred_update():
        try:
            if gizmo.empty and gizmo.empty.as_pointer() != 0:
                gizmo.create_custom_shape()
        except ReferenceError:
            pass
        return None

    bpy.app.timers.register(deferred_update, first_interval=0.0)

    for area in context.screen.areas:
        if area.type == "VIEW_3D":
            area.tag_redraw()


class ZounaProperty(PropertyGroup):
    # Collision Settings

    col_primitive_type: bpy.props.EnumProperty(
        name="Collision Primitive Type",
        description="The type of collision primitive used",
        items=col_primitive_types,
        default=ColPrimitiveType.NONE.name,
        update=update_col_prim_type,
    )

    col_primitive_category: bpy.props.EnumProperty(
        name="Collision Category",
        description="The collision category for this object",
        items=col_primitive_categories,
        default=ColPrimitiveCategory.COLLIDER.name,
        update=update_zouna_collision_properties,
    )

    # Rat Collision Settings
    # There are more unknown ones, like affecting particles

    last_rat_surface_type: bpy.props.EnumProperty(
        items=rat_surface_types,
        default=RatSurfaceTypes.NONE,
    )

    rat_surface_type: bpy.props.EnumProperty(
        name="Surface Type",
        description="Determines the type of surface and the interactions with the player",
        items=rat_surface_types,
        default=RatSurfaceTypes.NONE,
        update=update_zouna_collision_properties,
    )

    rat_sound_type: bpy.props.EnumProperty(
        name="Sound Type",
        description="Determines the sound that will play when the player walks on the surface",
        items=rat_sound_types,
        default=RatSoundTypes.STONE,
        update=update_zouna_collision_properties,
    )

    # Only show if rat surface is water
    rat_deep_water: bpy.props.BoolProperty(
        name="Deep Water",
        description="Will collide with water if under the surface",
        default=False,
    )

    rat_footprints_while_on: bpy.props.BoolProperty(
        name="Footprints on Surface",
        description="Leave footprints while on the surface",
        default=False,
    )

    rat_footprints_while_off: bpy.props.BoolProperty(
        name="Footprints After Leaving",
        description="Leave footprints after leaving the surface",
        default=False,
    )


object_classes = [ZounaProperty]


def register_object():
    for cls in object_classes:
        register_class(cls)

    Object.is_zouna = bpy.props.BoolProperty(
        name="Is Zouna Object",
        description="Whether the object is a Zouna object",
        default=False,
    )
    Object.zouna_property = bpy.props.PointerProperty(type=ZounaProperty)


def unregister_object():
    del Object.is_zouna
    del Object.zouna_property

    for cls in reversed(object_classes):
        unregister_class(cls)
