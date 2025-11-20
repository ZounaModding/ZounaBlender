import bpy
from bpy.types import Menu, Operator
from ...common.constants import RatSurfaceTypes, RatSoundTypes
from ..util import ui_labeled_row


class ZounaSoundMenu(Menu):
    bl_idname = "zouna.sound_menu"
    bl_label = "Sound Type"

    def draw(self, context):
        layout = self.layout

        if context.material and context.material.is_zouna:
            zp = context.material.zouna_material
        else:
            zp = context.object.zouna_property

        if zp.rat_surface_type not in (
            RatSurfaceTypes.SOLID,
            RatSurfaceTypes.SLIPPERY,
            RatSurfaceTypes.STICKY,
            RatSurfaceTypes.SLIDE_JUMP,
            RatSurfaceTypes.SLIDE_NO_JUMP,
        ):
            layout.label(text="Sound auto-set by Surface", icon="INFO")
            return

        for snd in RatSoundTypes:
            op = layout.operator("zouna.set_sound_type", text=snd.value.title())
            op.value = snd.value


class ZounaSetSoundTypeOperator(Operator):
    bl_idname = "zouna.set_sound_type"
    bl_label = "Set Sound Type"

    value: bpy.props.StringProperty()

    def execute(self, context):
        if context.material and context.material.is_zouna:
            zp = context.material.zouna_material
        else:
            zp = context.object.zouna_property

        if zp.rat_surface_type in (
            RatSurfaceTypes.SOLID,
            RatSurfaceTypes.SLIPPERY,
            RatSurfaceTypes.STICKY,
            RatSurfaceTypes.SLIDE_JUMP,
            RatSurfaceTypes.SLIDE_NO_JUMP,
        ):
            zp.rat_sound_type = self.value

        return {"FINISHED"}


def draw_sound_ui(box, zp, panel_type):
    st = zp.rat_surface_type

    if st in (
        RatSurfaceTypes.NONE,
        RatSurfaceTypes.COLLECT,
        RatSurfaceTypes.COLLECTABLE,
        RatSurfaceTypes.WATER,
    ):
        return

    ui_labeled_row(
        box,
        "Sound Type:",
        lambda col: col.prop(zp, "rat_sound_type", text=""),
        panel_type,
    )


classes = (
    ZounaSoundMenu,
    ZounaSetSoundTypeOperator,
)


def register_sound_dropdown():
    for c in classes:
        bpy.utils.register_class(c)


def unregister_sound_dropdown():
    for c in reversed(classes):
        bpy.utils.unregister_class(c)
