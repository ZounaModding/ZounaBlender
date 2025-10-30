import bpy
import time
from bpy.utils import register_class, unregister_class


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
