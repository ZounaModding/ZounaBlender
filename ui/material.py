from pathlib import Path
from ..common.material import create_zouna_material_node_tree
from ..common.constants import RatSurfaceTypes
from ..common.util import get_material_from_context
from ..zouna.generic.material import Material as GenericMaterial
from ..zouna.v1_06_63_02_pc.material import MaterialV1_06_63_02_PC
from ..zouna.bff.io import (
    BffClassHeader,
    BffClass,
    Class,
    Platform,
    Material as BffMaterial,
)
from ..blender.exp import export_resource

import bpy
import os
import json
import traceback
from bpy.types import Operator, Panel
from bpy.utils import register_class, unregister_class


class CreateZounaMaterialOperator(Operator):
    bl_idname = "object.create_zouna_material"
    bl_label = "Create Zouna Material"
    bl_options = {"REGISTER", "UNDO", "PRESET"}
    mat_name: bpy.props.StringProperty(
        name="Name",
        description="Name for the new Zouna material",
        default="ZounaMaterial",
    )

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "mat_name")

    def execute(self, context):
        obj = bpy.context.view_layer.objects.active
        if obj is None:
            self.report({"ERROR"}, "No active object selected")
            return {"CANCELLED"}
        else:
            name = self.mat_name.strip()
            if not name:
                self.report({"ERROR"}, "Material name must not be empty")
                return {"CANCELLED"}
            mat = bpy.data.materials.new(name=self.mat_name)
            mat.use_nodes = True
            mat.is_zouna = True
            create_zouna_material_node_tree(mat)
            self.report({"INFO"}, "Created new Zouna material")
        return {"FINISHED"}


class SaveZounaMaterialOperator(bpy.types.Operator):
    bl_idname = "zouna.save_material"
    bl_label = "Save Zouna Material"
    bl_options = {"REGISTER"}

    filepath: bpy.props.StringProperty(subtype="FILE_PATH")

    def execute(self, context):
        try:
            material = get_material_from_context(context)
            print(str(material))
            if material is None or material.zouna_material is None:
                self.report(
                    {"ERROR"},
                    "No active Zouna material found. Select a Zouna material first.",
                )
                return {"CANCELLED"}

            folder = os.path.dirname(self.filepath)
            if folder and not os.path.exists(folder):
                os.makedirs(folder, exist_ok=True)

            mat_path = Path(self.filepath)
            parent_dir = mat_path.parent
            parent_dir_name = parent_dir.name
            if ".Material" in parent_dir_name:
                material.zouna_material.file_name = parent_dir_name.split(
                    ".Material", 1
                )[0]
            print(f"FileName: {material.zouna_material.file_name}")

            generic_material = GenericMaterial.from_blender(material)
            print(f"---- EXPORTING RESOURCE {self.filepath} -----")
            export_resource(generic_material, self.filepath)
            self.report({"INFO"}, f"Exported resource: {self.filepath}")
            print(f"---- EXPORTED RESOURCE {self.filepath} -----")

            self.report({"INFO"}, f"Saved Zouna material to: {self.filepath}")
            return {"FINISHED"}
        except Exception as exc:
            traceback.print_exc()
            self.report({"ERROR"}, f"Failed to save material: {exc}")
            return {"CANCELLED"}

    def invoke(self, context, event):
        material = get_material_from_context(context)
        suggested_filename = "resource.json"
        if material is not None:
            base_directory = (
                bpy.path.abspath("//") if bpy.data.filepath else os.path.expanduser("~")
            )
            default_path = os.path.join(base_directory, suggested_filename)
            self.filepath = default_path
        else:
            self.filepath = os.path.join(os.path.expanduser("~"), suggested_filename)

        context.window_manager.fileselect_add(self)
        return {"RUNNING_MODAL"}


class ZounaMaterialPanel(Panel):
    bl_label = "Zouna Material"
    bl_idname = "ZOUNA_PT_Material_Panel"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "material"
    bl_options = {"HIDE_HEADER"}

    def draw(self, context):
        layout = self.layout

        layout.operator(CreateZounaMaterialOperator.bl_idname, icon="PLUS")

        material = context.material
        if material is None:
            return
        elif not material.use_nodes or not material.is_zouna:
            layout.label(text="This is not a Zouna material")
            return

        zouna_properties = material.zouna_material

        layout.separator()
        tabs_row = layout.row()
        tabs_row.prop(zouna_properties, "menu_tab", expand=True)

        if zouna_properties.menu_tab == "Parameters":
            parameters_box = layout.box()
            parameters_box.label(text="Colors & Lighting", icon="LIGHT")
            parameters_box.prop(zouna_properties, "diffuse_color", text="Diffuse")
            parameters_box.prop(zouna_properties, "emissive_color", text="Emissive")
            parameters_box.prop(zouna_properties, "specular_color", text="Specular")
            parameters_box.prop(zouna_properties, "specular_exponent", text="Shininess")
            parameters_box.separator()

            parameters_box.label(text="Generic Parameters")
            parameters_box.prop(zouna_properties, "params", text="Params")

            parameters_box.separator()
            parameters_box.label(text="UV Transform")
            uv_transform_row_top = parameters_box.row(align=True)
            uv_transform_row_top.prop(zouna_properties, "uv_rotation", text="Rotation")
            uv_transform_row_top.prop(zouna_properties, "uv_offset_u", text="Offset U")
            uv_transform_row_top.prop(zouna_properties, "uv_offset_v", text="Offset V")

            uv_transform_row_bottom = parameters_box.row(align=True)
            uv_transform_row_bottom.prop(
                zouna_properties, "uv_tiling_u", text="Tiling U"
            )
            uv_transform_row_bottom.prop(
                zouna_properties, "uv_tiling_v", text="Tiling V"
            )

        elif zouna_properties.menu_tab == "Sources":
            textures_box = layout.box()
            textures_box.label(text="Textures", icon="TEXTURE")

            texture_column = textures_box.column(align=True)

            texture_column.label(text="Diffuse")
            texture_column.template_ID(zouna_properties, "diffuse", open="image.open")
            diffuse_image = zouna_properties.diffuse
            if diffuse_image:
                texture_column.template_icon(diffuse_image.preview.icon_id, scale=6)

            texture_column.separator()
            texture_column.label(text="Envmap")
            texture_column.template_ID(zouna_properties, "envmap", open="image.open")
            envmap_image = zouna_properties.envmap
            if envmap_image:
                texture_column.template_icon(envmap_image.preview.icon_id, scale=6)

            texture_column.separator()
            texture_column.label(text="Normal")
            texture_column.template_ID(zouna_properties, "normal", open="image.open")
            normal_image = zouna_properties.normal
            if normal_image:
                texture_column.template_icon(normal_image.preview.icon_id, scale=6)

            texture_column.separator()
            texture_column.label(text="Specular")
            texture_column.template_ID(zouna_properties, "specular", open="image.open")
            specular_image = zouna_properties.specular
            if specular_image:
                texture_column.template_icon(specular_image.preview.icon_id, scale=6)

        elif zouna_properties.menu_tab == "Collision":
            collision_box = layout.box()
            collision_box.label(text="Surface / Sound", icon="MESH_CUBE")
            collision_box.prop(
                zouna_properties, "rat_surface_type", text="Surface Type"
            )
            collision_box.prop(zouna_properties, "rat_sound_type", text="Sound Type")

            collision_box.separator()

            collision_box.prop(
                zouna_properties, "rat_footprints_while_on", text="Footprints While On"
            )
            collision_box.prop(
                zouna_properties,
                "rat_footprints_while_off",
                text="Footprints While Off",
            )
            collision_box.prop(zouna_properties, "rat_ice", text="Ice/Glass")
            if zouna_properties.rat_surface_type == RatSurfaceTypes.WATER:
                collision_box.prop(
                    zouna_properties, "rat_deep_water", text="Deep Water"
                )

        elif zouna_properties.menu_tab == "Render":
            render_box = layout.box()
            render_box.label(text="Render / Misc Flags", icon="RENDER_STILL")
            render_box.prop(
                zouna_properties, "env_alpha_mask", text="Envmap Alpha Mask"
            )
            render_box.prop(zouna_properties, "invisible", text="Invisible")
            render_box.prop(zouna_properties, "uv_clamp_u", text="Clamp U")
            render_box.prop(zouna_properties, "uv_clamp_v", text="Clamp V")
            render_box.prop(zouna_properties, "double_sided", text="Double Sided")


material_classes = [
    CreateZounaMaterialOperator,
    SaveZounaMaterialOperator,
    ZounaMaterialPanel,
]


def register_material():
    for cls in material_classes:
        register_class(cls)


def unregister_material():
    for cls in material_classes:
        unregister_class(cls)
