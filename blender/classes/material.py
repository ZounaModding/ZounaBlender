import bpy
from bpy.types import PropertyGroup, Material, Image
from bpy.utils import register_class, unregister_class

from ...common.constants import (
    RatSurfaceTypes,
    RatSoundTypes,
    rat_surface_types,
    rat_sound_types,
)
from ..shared.collision import update_zouna_collision_properties
from ...common.util import get_material_from_context
from ...common.material import create_zouna_material_node_tree
from .resource import ZounaResourceProperty
from ..handlers import make_handler
from ...zouna.v1_06_63_02_pc.material import MaterialV1_06_63_02_PC
from ...zouna.v1_291_03_06_pc.material import MaterialV1_291_03_06_PC
from ...zouna.bff.io import Platform


def material_menu_tabs(_self, context):
    items = ["Parameters", "Sources", "Collision", "Render"]
    return [(item, item, item) for item in items]


def update_zouna_material_property(self, context):
    mat = get_material_from_context(context)
    if mat is not None and mat.is_zouna and mat.zouna_material == self:
        create_zouna_material_node_tree(mat)
    else:
        print(f"material was not found")


def update_zouna_material_image_property(self, context):
    if self.diffuse is not None:
        if not self.diffuse.preview:
            self.diffuse.preview_ensure()
    if self.envmap is not None:
        if not self.envmap.preview:
            self.envmap.preview_ensure()
    if self.normal is not None:
        if not self.normal.preview:
            self.normal.preview_ensure()
    if self.specular is not None:
        if not self.specular.preview:
            self.specular.preview_ensure()
    update_zouna_material_property(self, context)


# TODO: Add missing properties from other games (FUEL), remember handling UI depending on game being used
class ZounaMaterialProperty(ZounaResourceProperty):
    diffuse_color: bpy.props.FloatVectorProperty(
        name="Diffuse Color",
        description="RGBA components of the diffuse color of the material",
        subtype="COLOR",
        min=0.0,
        max=1.0,
        size=4,
        default=[1.0, 1.0, 1.0, 1.0],
        update=update_zouna_material_property,
    )

    emissive_color: bpy.props.FloatVectorProperty(
        name="Emissive Color",
        description="RGB components of the emissive color of the material",
        subtype="COLOR",
        min=0.0,
        max=1.0,
        size=3,
        default=[0.0, 0.0, 0.0],
        update=update_zouna_material_property,
    )

    specular_color: bpy.props.FloatVectorProperty(
        name="Specular Color",
        description="RGB components of the specular color of the material",
        subtype="COLOR",
        min=0.0,
        max=1.0,
        size=3,
        default=[0.0, 0.0, 0.0],
        update=update_zouna_material_property,
    )

    specular_exponent: bpy.props.FloatProperty(
        name="Specular Exponent",
        description="Also known as shininess, the exponent of the specular term in the blinn-phong equation used for specular reflection",
        min=0.0,
        default=0.0,
        update=update_zouna_material_property,
    )

    params: bpy.props.FloatVectorProperty(
        name="Params",
        description="Generic parameters, only known use is by water surfaces (no effect on meshes)",
        subtype="NONE",
        size=4,
        default=[0.015, -431602080.0, -431602080.0, -431602080.0],
        update=update_zouna_material_property,
    )

    uv_rotation: bpy.props.FloatProperty(
        name="UV Rotation",
        description="Rotation of the textures",
        min=-360.0,
        max=360.0,
        default=0.0,
        update=update_zouna_material_property,
    )

    uv_offset_u: bpy.props.FloatProperty(
        name="UV Offset U",
        description="Translation in the U direction of the textures",
        min=-10.0,
        max=10.0,
        default=0.0,
        update=update_zouna_material_property,
    )

    uv_offset_v: bpy.props.FloatProperty(
        name="UV Offset V",
        description="Translation in the V direction of the textures",
        min=-10.0,
        max=10.0,
        default=0.0,
        update=update_zouna_material_property,
    )

    uv_tiling_u: bpy.props.FloatProperty(
        name="UV Tiling U",
        description="Tiling (Scale) in the U direction of the textures",
        min=-10.0,
        max=10.0,
        default=1.0,
        update=update_zouna_material_property,
    )

    uv_tiling_v: bpy.props.FloatProperty(
        name="UV Tiling V",
        description="Tiling (Scale) in the V direction of the textures",
        min=-10.0,
        max=10.0,
        default=1.0,
        update=update_zouna_material_property,
    )

    diffuse: bpy.props.PointerProperty(
        type=Image,
        description="The image associated with the diffuse texture",
        name="Image",
        update=update_zouna_material_image_property,
    )

    envmap: bpy.props.PointerProperty(
        type=Image,
        description="The image associated with the envmap texture",
        name="Image",
        update=update_zouna_material_image_property,
    )

    normal: bpy.props.PointerProperty(
        type=Image,
        description="The image associated with the normal texture",
        name="Image",
        update=update_zouna_material_image_property,
    )

    specular: bpy.props.PointerProperty(
        type=Image,
        description="The image associated with the specular texture",
        name="Image",
        update=update_zouna_material_image_property,
    )

    # General Render Settings

    env_alpha_mask: bpy.props.BoolProperty(
        name="Alpha Mask for Envmap",
        description="Use diffuse texture alpha as mask to apply envmap",
        default=False,
        options=set(),
        update=update_zouna_material_property,
    )

    invisible: bpy.props.BoolProperty(
        name="Invisible",
        description="Invisible material",
        default=False,
        options=set(),
        update=update_zouna_material_property,
    )

    uv_clamp_u: bpy.props.BoolProperty(
        name="Clamp UV U",
        description="Clamp textures in the U direction",
        default=False,
        options=set(),
        update=update_zouna_material_property,
    )

    uv_clamp_v: bpy.props.BoolProperty(
        name="Clamp UV V",
        description="Clamp textures in the V direction",
        default=False,
        options=set(),
        update=update_zouna_material_property,
    )

    blend_additive: bpy.props.BoolProperty(
        name="Additive Blending",
        description="Use additive blending for the material",
        default=False,
    )

    blend_subtractive: bpy.props.BoolProperty(
        name="Subtractive Blending",
        description="Use subtractive blending for the material",
        default=False,
    )

    blend_dest_additive: bpy.props.BoolProperty(
        name="Destination Additive Blending",
        description="Use destination additive blending for the material",
        default=False,
    )

    double_sided: bpy.props.BoolProperty(
        name="Double Sided",
        description="Disable back face culling",
        default=False,
        options=set(),
        update=update_zouna_material_property,
    )

    # Game specific settings

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

    # Rat Render Settings

    # UI

    menu_tab: bpy.props.EnumProperty(items=material_menu_tabs)


material_classes = [ZounaMaterialProperty]


def register_material():
    for cls in material_classes:
        register_class(cls)

    Material.is_zouna = bpy.props.BoolProperty()
    Material.zouna_material = bpy.props.PointerProperty(type=ZounaMaterialProperty)


def unregister_material():
    del Material.zouna_material
    del Material.is_zouna

    for cls in reversed(material_classes):
        unregister_class(cls)


material_versions = [
    (
        MaterialV1_06_63_02_PC,
        Platform.PC,
        "v1.06.63.02 - Asobo Studio - Internal Cross Technology",
        "material",
    ),
    (
        MaterialV1_291_03_06_PC,
        Platform.PC,
        "v1.291.03.06 - Asobo Studio - Internal Cross Technology",
        "material",
    ),
]


def initialize_material_handlers():
    for version_class, platform, version_str, member_name in material_versions:
        make_handler(version_class, platform, version_str, member_name)
