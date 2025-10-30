import bpy
from bpy.props import StringProperty
from bpy.types import Operator, Panel
from bpy.utils import register_class, unregister_class

from ..blender.imp import import_resource
import traceback


class ImportResourceOperator(Operator):
    bl_idname = "zouna.import_resource"
    bl_label = "Import Resource"
    filepath: StringProperty(subtype="FILE_PATH")

    def execute(self, context):
        try:
            print(f"---- IMPORTING RESOURCE {self.filepath} -----")
            generic_class = import_resource(self.filepath)
            generic_class.to_blender()
            self.report({"INFO"}, f"Imported resource: {self.filepath}")
            print(f"---- IMPORTED RESOURCE {self.filepath} -----")
        except Exception as e:
            print("Failed to import:")
            traceback.print_exc()
            self.report({"ERROR"}, f"Failed to import: {e}")
        return {"FINISHED"}

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {"RUNNING_MODAL"}


class ResourcePanel(Panel):
    bl_idname = "ZOUNA_PT_Resource_Panel"
    bl_label = "Zouna Panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Zouna"

    def draw(self, context):
        layout = self.layout
        layout.label(text="Zouna")

        layout.operator("zouna.import_resource", text="Import Resource")
        layout.operator("zouna.save_mesh", text="Save Active Zouna Mesh")
        layout.operator("zouna.save_material", text="Save Active Zouna Material")

        layout.separator()

        layout.label(text="Export options:")
        layout.prop(context.scene, "zouna_game", text="Game")
        layout.prop(context.scene, "zouna_platform", text="Platform")

        layout.separator()

        layout.label(text="Render options:")
        layout.prop(context.scene, "zouna_envmap_toggle", text="Render with Envmap")


panel_classes = [
    ImportResourceOperator,
    ResourcePanel,
]


def register_panel():
    for cls in panel_classes:
        register_class(cls)


def unregister_panel():
    for cls in reversed(panel_classes):
        try:
            unregister_class(cls)
        except Exception:
            traceback.print_exc()
