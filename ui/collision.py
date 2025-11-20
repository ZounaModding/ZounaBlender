import bpy
from bpy.types import Operator, Panel, Menu, VIEW3D_MT_add, VIEW3D_MT_mesh_add
from bpy.utils import register_class, unregister_class
from ..blender.shared.collision import (
    add_collision_dummy,
    add_collision_dummy_under_obj,
)
from ..common.constants import (
    ColPrimitiveType,
    RatSurfaceTypes,
    ColPrimitiveCategory,
)
from .common.sound_dropdown import draw_sound_ui
from .util import ui_labeled_row


class ZounaAddCollisionPrimitive(Operator):
    bl_idname = "zouna.add_collision_primitive"
    bl_label = "Add Zouna Collision Primitive"
    bl_options = {"REGISTER", "UNDO"}

    col_primitive_type: bpy.props.StringProperty() = "NONE"

    def execute(self, context):
        parent = context.view_layer.objects.active
        if parent and parent.select_get():
            dummy = add_collision_dummy_under_obj(self.col_primitive_type, parent)
        else:
            dummy = add_collision_dummy(self.col_primitive_type)

        if bpy.context.mode == "OBJECT":
            for obj in context.view_layer.objects:
                obj.select_set(False)
            dummy.select_set(True)
            context.view_layer.objects.active = dummy

        return {"FINISHED"}


class ZounaCollisionAddMenu(Menu):
    bl_idname = "zouna.collision_add_menu"
    bl_label = "Zouna Collision Primitives"

    def draw(self, context):
        self.layout.operator(
            ZounaAddCollisionPrimitive.bl_idname,
            text="Sphere Collision",
            icon="MESH_UVSPHERE",
        ).col_primitive_type = ColPrimitiveType.SPHERE.name

        self.layout.operator(
            ZounaAddCollisionPrimitive.bl_idname, text="Box Collision", icon="MESH_CUBE"
        ).col_primitive_type = ColPrimitiveType.BOX.name

        self.layout.operator(
            ZounaAddCollisionPrimitive.bl_idname,
            text="Cylinder Collision",
            icon="MESH_CYLINDER",
        ).col_primitive_type = ColPrimitiveType.CYLINDER.name


def draw_menu(self, context):
    self.layout.menu(ZounaCollisionAddMenu.bl_idname, icon="SHADING_BBOX")


class ZounaCollisionPrimitiveTypeMenu(Menu):
    bl_idname = "zouna.collision_primitive_type_menu"
    bl_label = "Collision Primitive Type"

    def draw(self, context):
        add = self.layout.operator
        add("zouna.set_collision_primitive_type", text="Sphere").value = (
            ColPrimitiveType.SPHERE.name
        )
        add("zouna.set_collision_primitive_type", text="Box").value = (
            ColPrimitiveType.BOX.name
        )
        add("zouna.set_collision_primitive_type", text="Cylinder").value = (
            ColPrimitiveType.CYLINDER.name
        )


class ZounaSetCollisionPrimitiveTypeOperator(Operator):
    bl_idname = "zouna.set_collision_primitive_type"
    bl_label = "Set Collision Primitive Type"

    value: bpy.props.StringProperty()

    def execute(self, context):
        context.object.zouna_property.col_primitive_type = self.value

        for area in context.screen.areas:
            if area.type == "VIEW_3D":
                area.tag_redraw()

        return {"FINISHED"}


class ZounaCollisionCategoryMenu(Menu):
    bl_idname = "zouna.collision_category_menu"
    bl_label = "Collision Special Category"

    def draw(self, context):
        layout = self.layout
        zp = context.object.zouna_property

        if zp.rat_surface_type != RatSurfaceTypes.NONE:
            return

        specials = [
            ColPrimitiveCategory.SHADOW,
            ColPrimitiveCategory.LOD,
            ColPrimitiveCategory.STRENGTH,
            ColPrimitiveCategory.KICK,
            ColPrimitiveCategory.NFADE,
            ColPrimitiveCategory.FADE,
            ColPrimitiveCategory.ACTION,
            ColPrimitiveCategory.MAGNET,
            ColPrimitiveCategory.INTER,
            ColPrimitiveCategory.REPULSE,
        ]

        for cat in specials:
            op = layout.operator("zouna.set_collision_category", text=cat.value.title())
            op.value = cat.value


class ZounaSetCollisionCategoryOperator(Operator):
    bl_idname = "zouna.set_collision_category"
    bl_label = "Set Collision Category"

    value: bpy.props.StringProperty()

    def execute(self, context):
        zp = context.object.zouna_property
        if zp.rat_surface_type == RatSurfaceTypes.NONE:
            zp.col_primitive_category = self.value
        return {"FINISHED"}


class ZounaCollisionPanel(Panel):
    bl_label = "Zouna Collision"
    bl_idname = "zouna.collision_panel"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "object"
    bl_options = {"HIDE_HEADER"}

    @classmethod
    def poll(cls, context):
        obj = context.object
        return obj and obj.is_zouna and obj.type == "EMPTY"

    def draw(self, context):
        layout = self.layout
        obj = context.object
        zp = obj.zouna_property

        collision_box = layout.box()
        collision_box.label(text="Zouna Collision", icon="MESH_CUBE")

        ui_labeled_row(
            collision_box,
            "Primitive:",
            lambda col: col.menu(
                "zouna.collision_primitive_type_menu",
                text=zp.col_primitive_type.capitalize(),
            ),
            "object",
        )

        ui_labeled_row(
            collision_box,
            "Surface Type:",
            lambda col: col.prop(zp, "rat_surface_type", text=""),
            "object",
        )

        draw_sound_ui(collision_box, zp, "object")

        if zp.rat_surface_type == RatSurfaceTypes.NONE:
            ui_labeled_row(
                collision_box,
                "Special Category:",
                lambda col: col.menu(
                    "zouna.collision_category_menu",
                    text=zp.col_primitive_category.title(),
                ),
                "object",
            )

        if zp.rat_surface_type == RatSurfaceTypes.WATER:
            ui_labeled_row(
                collision_box,
                "Deep Water:",
                lambda col: col.prop(zp, "rat_deep_water", text=""),
                "object",
            )

        collision_box.separator()

        collision_box.prop(zp, "rat_footprints_while_on", text="Footprints While On")
        collision_box.prop(zp, "rat_footprints_while_off", text="Footprints While Off")


classes = (
    ZounaAddCollisionPrimitive,
    ZounaCollisionAddMenu,
    ZounaCollisionPrimitiveTypeMenu,
    ZounaSetCollisionPrimitiveTypeOperator,
    ZounaCollisionCategoryMenu,
    ZounaSetCollisionCategoryOperator,
    ZounaCollisionPanel,
)


def register_collision():
    for cls in classes:
        register_class(cls)
    VIEW3D_MT_add.append(draw_menu)
    VIEW3D_MT_mesh_add.append(draw_menu)


def unregister_collision():
    VIEW3D_MT_add.remove(draw_menu)
    VIEW3D_MT_mesh_add.remove(draw_menu)
    for cls in reversed(classes):
        unregister_class(cls)
