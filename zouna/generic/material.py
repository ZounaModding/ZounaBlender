from enum import Enum

from ...common.constants import (
    RatSoundTypes,
    RatSurfaceTypes,
)
from ...common.material import create_zouna_material_node_tree
from .resource import Resource
from .bitmap import Bitmap

import bpy


class Material(Resource):
    diffuse_color: tuple[float, float, float] = (1.0, 1.0, 1.0)
    opacity: float = 1.0
    emissive_color: tuple[float, float, float] = (0.0, 0.0, 0.0)
    specular_color: tuple[float, float, float] = (1.0, 1.0, 1.0)
    specular_power: float = 1.0

    uv_rotation: float = 0.0
    uv_translation: tuple[float, float] = (0.0, 0.0)
    uv_scale: tuple[float, float] = (1.0, 1.0)

    envmap_factor: float = -1.0
    specular_factor: float = -1.0
    bump_factor: float = -1.0

    tex_diffuse: Bitmap = None
    tex_envmap: Bitmap = None
    tex_normal: Bitmap = None
    tex_specular: Bitmap = None
    tex_add_normal: Bitmap = None
    tex_occlusion: Bitmap = None
    tex_dirt: Bitmap = None
    tex_normal_local: Bitmap = None

    env_alpha_mask: bool = False
    invisible: bool = False
    uv_clamp_u: bool = False
    uv_clamp_v: bool = False
    double_sided: bool = False

    rat_params: list[float] = [
        0.015,
        -431602080.0,
        -431602080.0,
        -431602080.0,
    ]  # Not sure if it's rat specific or not but for now
    rat_surface_type: RatSurfaceTypes = RatSurfaceTypes.SOLID
    rat_sound_type: RatSoundTypes = RatSoundTypes.STONE
    rat_deep_water: bool = False
    rat_footprints_while_on: bool = False
    rat_footprints_while_off: bool = False
    rat_ice: bool = False

    def setup_zouna_material(self):
        mat_name = self.name or "ZounaMaterial"
        mat = bpy.data.materials.new(name=mat_name)
        mat.use_nodes = True
        mat.is_zouna = True
        mat.zouna_material.init_resource(self)
        mat.zouna_material.diffuse_color = (*self.diffuse_color, self.opacity)
        mat.zouna_material.emissive_color = self.emissive_color
        mat.zouna_material.specular_color = self.specular_color
        mat.zouna_material.specular_exponent = self.specular_power
        mat.zouna_material.params = self.rat_params
        mat.zouna_material.uv_rotation = self.uv_rotation
        mat.zouna_material.uv_offset_u = self.uv_translation[0]
        mat.zouna_material.uv_offset_v = self.uv_translation[1]
        mat.zouna_material.uv_tiling_u = self.uv_scale[0]
        mat.zouna_material.uv_tiling_v = self.uv_scale[1]
        if self.tex_diffuse:
            mat.zouna_material.diffuse = self.tex_diffuse.to_blender()
        if self.tex_envmap:
            mat.zouna_material.envmap = self.tex_envmap.to_blender()
        if self.tex_normal:
            mat.zouna_material.normal = self.tex_normal.to_blender()
        if self.tex_specular:
            mat.zouna_material.specular = self.tex_specular.to_blender()
        mat.zouna_material.env_alpha_mask = self.env_alpha_mask
        mat.zouna_material.invisible = self.invisible
        mat.zouna_material.uv_clamp_u = self.uv_clamp_u
        mat.zouna_material.uv_clamp_v = self.uv_clamp_v
        mat.zouna_material.double_sided = self.double_sided
        mat.zouna_material.rat_surface_type = self.rat_surface_type
        mat.zouna_material.rat_sound_type = self.rat_sound_type
        mat.zouna_material.rat_deep_water = self.rat_deep_water
        mat.zouna_material.rat_footprints_while_on = self.rat_footprints_while_on
        mat.zouna_material.rat_footprints_while_off = self.rat_footprints_while_off
        mat.zouna_material.rat_ice = self.rat_ice
        return mat

    @staticmethod
    def from_blender(blender_material):
        """
        Create a Material (generic Zouna resource) from a Blender Material
        that was created via setup_zouna_material / zouna pipeline.
        Returns a Material instance or None on invalid input.
        """
        if blender_material is None:
            print("Material.from_blender: blender_material is None")
            return None

        try:
            if not blender_material.is_zouna:
                print(
                    f"Material.from_blender: Blender material '{blender_material.name}' is not marked as a Zouna material (is_zouna False)"
                )
                return None
        except AttributeError:
            print(
                "Material.from_blender: blender_material missing 'is_zouna' attribute"
            )
            return None

        try:
            zouna_properties = blender_material.zouna_material
        except AttributeError:
            print(
                f"Material.from_blender: Blender material '{blender_material.name}' missing 'zouna_material' property group"
            )
            return None

        material = Material()

        material.name = blender_material.name

        try:
            material.file_path = zouna_properties.file_path
        except AttributeError:
            print(
                f"Material.file_path: Blender material '{blender_material.name}' missing 'file_path' property"
            )
            return None

        # TODO: Check if it makes sense (together with other TODO in Mesh.from_generic)
        try:
            material.file_name = zouna_properties.file_name if zouna_properties.file_name != "DefaultFileName" else blender_material.name
        except AttributeError:
            print(
                f"Material.file_path: Blender material '{blender_material.name}' missing 'file_path' property"
            )
            return None

        diffuse_color = zouna_properties.diffuse_color
        material.diffuse_color = (
            float(diffuse_color[0]),
            float(diffuse_color[1]),
            float(diffuse_color[2]),
        )
        material.opacity = float(diffuse_color[3])

        emissive_color = zouna_properties.emissive_color
        material.emissive_color = (
            float(emissive_color[0]),
            float(emissive_color[1]),
            float(emissive_color[2]),
        )

        specular_color = zouna_properties.specular_color
        material.specular_color = (
            float(specular_color[0]),
            float(specular_color[1]),
            float(specular_color[2]),
        )

        material.specular_power = float(zouna_properties.specular_exponent)

        param = zouna_properties.params
        material.rat_params = [
            float(param[0]),
            float(param[1]),
            float(param[2]),
            float(param[3]),
        ]

        material.uv_rotation = float(zouna_properties.uv_rotation)
        material.uv_translation = (
            float(zouna_properties.uv_offset_u),
            float(zouna_properties.uv_offset_v),
        )
        material.uv_scale = (
            float(zouna_properties.uv_tiling_u),
            float(zouna_properties.uv_tiling_v),
        )

        diffuse_image = zouna_properties.diffuse
        if diffuse_image:
            material.tex_diffuse = Bitmap.from_blender(diffuse_image)

        envmap_image = zouna_properties.envmap
        if envmap_image:
            material.tex_envmap = Bitmap.from_blender(envmap_image)

        normal_image = zouna_properties.normal
        if normal_image:
            material.tex_normal = Bitmap.from_blender(normal_image)

        specular_image = zouna_properties.specular
        if specular_image:
            material.tex_specular = Bitmap.from_blender(specular_image)

        material.env_alpha_mask = zouna_properties.env_alpha_mask
        material.invisible = zouna_properties.invisible
        material.uv_clamp_u = zouna_properties.uv_clamp_u
        material.uv_clamp_v = zouna_properties.uv_clamp_v
        material.double_sided = zouna_properties.double_sided
        material.rat_surface_type = zouna_properties.rat_surface_type
        material.rat_sound_type = zouna_properties.rat_sound_type
        material.rat_deep_water = zouna_properties.rat_deep_water
        material.rat_footprints_while_on = zouna_properties.rat_footprints_while_on
        material.rat_footprints_while_off = zouna_properties.rat_footprints_while_off
        material.rat_ice = zouna_properties.rat_ice

        return material

    def to_blender(self):
        print(self)
        mat = self.setup_zouna_material()
        return create_zouna_material_node_tree(mat)

    def to_string(self, detailed_textures: bool = False) -> str:
        """Return a human-friendly multi-line string describing this material."""

        def fmt_enum(v):
            if v is None:
                return "None"
            if isinstance(v, Enum):
                try:
                    intval = int(v)
                    return f"{v.name} ({intval})"
                except (TypeError, ValueError):
                    return f"{v.name} ({v.value!r})"
            return repr(v)

        def fmt_texture(tex):
            if tex is None:
                return "None"
            candidates = []
            for attr in ("name", "file_path", "filepath", "image", "source"):
                if hasattr(tex, attr):
                    val = getattr(tex, attr)
                    if val.__class__ and hasattr(val, "name"):
                        candidates.append(f"{attr}={val.name!r}")
                    else:
                        candidates.append(f"{attr}={val!r}")
            if not candidates:
                candidates.append(tex.__class__.__name__)
            return (
                ", ".join(candidates)
                if not detailed_textures
                else ", ".join(candidates)
            )

        lines = []
        lines.append("Material:")
        lines.append(f"  name: {self.name!r}")
        lines.append(f"  diffuse_color: {self.diffuse_color!r}")
        lines.append(f"  opacity: {self.opacity!r}")
        lines.append(f"  emissive_color: {self.emissive_color!r}")
        lines.append(f"  specular_color: {self.specular_color!r}")
        lines.append(f"  specular_power: {self.specular_power!r}")
        lines.append(f"  uv_rotation: {self.uv_rotation!r}")
        lines.append(f"  uv_translation: {self.uv_translation!r}")
        lines.append(f"  uv_scale: {self.uv_scale!r}")
        lines.append(f"  envmap_factor: {self.envmap_factor!r}")
        lines.append(f"  specular_factor: {self.specular_factor!r}")
        lines.append(f"  bump_factor: {self.bump_factor!r}")

        lines.append("  textures:")
        lines.append(
            f"    tex_diffuse: {fmt_texture(self.tex_diffuse)}"
        )
        lines.append(
            f"    tex_envmap: {fmt_texture(self.tex_envmap)}"
        )
        lines.append(
            f"    tex_normal: {fmt_texture(self.tex_normal)}"
        )
        lines.append(
            f"    tex_specular: {fmt_texture(self.tex_specular)}"
        )
        lines.append(
            f"    tex_add_normal: {fmt_texture(self.tex_add_normal)}"
        )
        lines.append(
            f"    tex_occlusion: {fmt_texture(self.tex_occlusion)}"
        )
        lines.append(f"    tex_dirt: {fmt_texture(self.tex_dirt)}")
        lines.append(
            f"    tex_normal_local: {fmt_texture(self.tex_normal_local)}"
        )

        lines.append("  flags:")
        lines.append(
            f"    env_alpha_mask: {bool(self.env_alpha_mask)}"
        )
        lines.append(f"    invisible: {bool(self.invisible)}")
        lines.append(f"    uv_clamp_u: {bool(self.uv_clamp_u)}")
        lines.append(f"    uv_clamp_v: {bool(self.uv_clamp_v)}")
        lines.append(f"    double_sided: {bool(self.double_sided)}")

        lines.append("  rat specifics:")
        lines.append(f"    rat_params: {self.rat_params!r}")
        lines.append(
            f"    rat_surface_type: {fmt_enum(self.rat_surface_type)}"
        )
        lines.append(
            f"    rat_sound_type: {fmt_enum(self.rat_sound_type)}"
        )
        lines.append(
            f"    rat_deep_water: {bool(self.rat_deep_water)}"
        )
        lines.append(
            f"    rat_footprints_while_on: {bool(self.rat_footprints_while_on)}"
        )
        lines.append(
            f"    rat_footprints_while_off: {bool(self.rat_footprints_while_off)}"
        )
        lines.append(f"    rat_ice: {bool(self.rat_ice)}")

        if detailed_textures:
            lines.append("  (detailed texture info shown)")

        return "\n".join(lines)

    def __str__(self) -> str:
        return self.to_string(detailed_textures=False)

    def __repr__(self) -> str:
        return self.to_string(detailed_textures=True)
