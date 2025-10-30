import bpy
import os
import traceback
from bpy.types import Operator, Panel
from bpy.utils import register_class, unregister_class
from pathlib import Path

from ..zouna.generic.mesh import Mesh as GenericMesh
from ..blender.exp import export_resource


class SaveZounaMeshOperator(bpy.types.Operator):
    bl_idname = "zouna.save_mesh"
    bl_label = "Save Zouna Mesh"
    bl_options = {"REGISTER"}

    filepath: bpy.props.StringProperty(subtype="FILE_PATH")

    def execute(self, context):
        try:
            mesh_object = context.active_object
            if mesh_object is None or mesh_object.type != "MESH":
                self.report({"ERROR"}, "No active mesh object selected.")
                return {"CANCELLED"}

            generic_mesh = GenericMesh.from_blender(mesh_object)

            folder = os.path.dirname(self.filepath)
            if folder and not os.path.exists(folder):
                os.makedirs(folder, exist_ok=True)

            mesh_path = Path(self.filepath)

            dependency_suffix = ".Mesh_Z.d"
            parent_dir_name = mesh_path.parent.name
            if parent_dir_name.endswith(dependency_suffix):
                base_name = parent_dir_name[: -len(dependency_suffix)]
                generic_mesh.file_name = base_name
            else:
                generic_mesh.file_name = mesh_path.stem

            print(f"---- EXPORTING RESOURCE {self.filepath} -----")
            export_resource(generic_mesh, self.filepath)
            self.report({"INFO"}, f"Exported mesh: {self.filepath}")
            print(f"---- EXPORTED RESOURCE {self.filepath} -----")

            self.report({"INFO"}, f"Saved Zouna mesh to: {self.filepath}")
            return {"FINISHED"}
        except Exception as exc:
            traceback.print_exc()
            self.report({"ERROR"}, f"Failed to save mesh: {exc}")
            return {"CANCELLED"}

    def invoke(self, context, event):
        mesh_object = context.active_object
        suggested_filename = "mesh.json"
        if mesh_object is not None and mesh_object.type == "MESH":
            suggested_filename = f"resource.json"

        base_directory = (
            bpy.path.abspath("//") if bpy.data.filepath else os.path.expanduser("~")
        )
        default_path = os.path.join(base_directory, suggested_filename)
        self.filepath = default_path

        context.window_manager.fileselect_add(self)
        return {"RUNNING_MODAL"}


mesh_classes = [SaveZounaMeshOperator]


def register_mesh():
    for cls in mesh_classes:
        register_class(cls)


def unregister_mesh():
    for cls in mesh_classes:
        unregister_class(cls)
