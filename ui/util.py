import bpy
import time
from bpy.utils import register_class, unregister_class


def ui_labeled_row(box, label, draw_fn, panel_type):
    """
    Reusable aligned label:value layout.

    panel_type → "object" or "material", keeps separate split factor caches.

    draw_fn(column) draws the UI element (prop/menu/etc).
    """

    if not hasattr(ui_labeled_row, "_factors"):
        ui_labeled_row._factors = {
            "object": 0.32,
            "material": 0.32,
        }

    factor = ui_labeled_row._factors.get(panel_type, 0.32)

    row = box.row(align=True)
    split = row.split(factor=factor)

    col_label = split.column()
    col_label.alignment = "RIGHT"
    col_label.label(text=label)

    col_value = split.column()
    col_value.separator(factor=0.3)
    draw_fn(col_value)


# TODO: FIX
class ZounaShowWarning(bpy.types.Operator):
    """Non-blocking warning popup that auto-closes safely"""

    bl_idname = "zouna.show_warning"
    bl_label = "Zouna Warning"

    message: bpy.props.StringProperty(default="")

    def execute(self, context):
        self.report({"INFO"}, self.message)
        return {"FINISHED"}


util_classes = [ZounaShowWarning]


def register_util():
    for cls in util_classes:
        register_class(cls)


def unregister_util():
    for cls in util_classes:
        unregister_class(cls)
