from ...common.constants import (
    RatMaterialCollisionFlags,
    RatMaterialRenderFlags,
    RatMaterialCodeFlags,
    RatSurfaceTypes,
    collision_flag_to_rat_surface_type,
    collision_flag_to_rat_sound_type,
    rat_values_to_collision_flag,
)
from ..bff.io import (
    MaterialV106_63_02PCBody,
    MaterialV106_63_02_PC,
    AnimationV1291_03_06PCLinkHeader,
)
from ..common.resource import load_dependencies, save_dependencies
from ...common.util import safe_int
from ..generic.material import Material


class MaterialV1_06_63_02_PC:
    file_path: str
    material: MaterialV106_63_02_PC

    def __init__(self, material: MaterialV106_63_02_PC = None):
        if material is not None:
            self.material = material.material_v1_06_63_02_pc
            self.file_path = material.file_path
            print(f"self.file_path: {self.file_path}")

    @staticmethod
    def from_generic(generic_material: Material):
        """
        Convert a generic Material into a MaterialV1_06_63_02_PC instance.
        """
        if generic_material is None:
            return None

        body = MaterialV106_63_02PCBody(
            cdcdcdcd=0xCDCDCDCD,
            collision_flag=0,
            diffuse=[1.0, 1.0, 1.0, 1.0],
            emission=[0.0, 0.0, 0.0],
            general_flag=0,
            object_flag=0,
            params=0,
            render_flag=0x800000,
            rotation=0.0,
            scale=[1.0, 1.0],
            specular=[0.0, 0.0, 0.0],
            specular_pow=1.0,
            textures=[""] * 4,
            translation=[0.0, 0.0],
            uv_transform_matrix=None,
        )

        link_header = AnimationV1291_03_06PCLinkHeader(
            link_name=safe_int(generic_material.name), names=[], links=[]
        )

        material_pc = MaterialV1_06_63_02_PC()
        material_pc.file_path = generic_material.file_path
        material_pc.material = MaterialV106_63_02_PC(
            body=body,
            class_name="Material_Z",
            link_header=link_header,
            link_name=safe_int(generic_material.file_name or ""),
            name=safe_int(generic_material.file_name or ""),
        )

        material_pc.material.name = safe_int(generic_material.file_name or "")
        material_pc.material.link_header.link_name = safe_int(
            generic_material.name or ""
        )

        diffuse_color = generic_material.diffuse_color
        opacity = generic_material.opacity
        body.diffuse = [diffuse_color[0], diffuse_color[1], diffuse_color[2], opacity]

        body.emission = list(generic_material.emissive_color)
        body.specular = list(generic_material.specular_color)
        body.specular_pow = generic_material.specular_power
        body.params = generic_material.rat_params
        body.rotation = generic_material.uv_rotation
        body.translation = list(generic_material.uv_translation)
        body.scale = list(generic_material.uv_scale)

        import math

        tx, ty = body.translation
        sx, sy = body.scale
        theta = body.rotation
        cos_r = math.cos(theta)
        sin_r = math.sin(theta)

        body.uv_transform_matrix = [
            [sx * cos_r, -sy * sin_r, 0.0, tx],
            [sx * sin_r, sy * cos_r, 0.0, ty],
            [-1.0, -1.0, 1.0, 0.0],
        ]

        body.render_flag = RatMaterialRenderFlags.DEFAULT
        if generic_material.env_alpha_mask:
            body.render_flag |= RatMaterialRenderFlags.ALPHA_MASK
        if generic_material.invisible:
            body.render_flag |= RatMaterialRenderFlags.INVISIBLE
        if generic_material.uv_clamp_u:
            body.render_flag |= RatMaterialRenderFlags.UV_CLAMP_U
        if generic_material.uv_clamp_v:
            body.render_flag |= RatMaterialRenderFlags.UV_CLAMP_V
        if generic_material.blend_additive:
            body.render_flag |= RatMaterialRenderFlags.BLEND_ADDITIVE
        if generic_material.blend_subtractive:
            body.render_flag |= RatMaterialRenderFlags.BLEND_SUBTRACTIVE
        if generic_material.blend_dest_additive:
            body.render_flag |= RatMaterialRenderFlags.BLEND_DEST_ADDITIVE
        if generic_material.double_sided:
            body.render_flag |= RatMaterialRenderFlags.DOUBLE_SIDED

        collision_flag = rat_values_to_collision_flag(
            generic_material.rat_surface_type,
            generic_material.rat_sound_type,
            generic_material.rat_footprints_while_off,
            generic_material.rat_footprints_while_on,
        )

        body.collision_flag = collision_flag

        texture_slots = ["tex_diffuse", "tex_envmap", "tex_normal", "tex_specular"]
        slot_to_flag = {
            "tex_diffuse": RatMaterialCodeFlags.DIFFUSE,
            "tex_envmap": RatMaterialCodeFlags.ENVMAP,
            "tex_normal": RatMaterialCodeFlags.NORMAL,
            "tex_specular": RatMaterialCodeFlags.SPECULAR,
        }

        body.textures = []
        generic_bitmaps_to_save = []
        export_attempted_slots = [False] * len(texture_slots)

        for i, slot_name in enumerate(texture_slots):
            generic_bitmap = getattr(generic_material, slot_name, None)

            if generic_bitmap is not None:
                generic_bitmaps_to_save.append(generic_bitmap)
                export_attempted_slots[i] = True

        exported_keys = []
        if generic_bitmaps_to_save:
            exported_keys = save_dependencies(
                generic_material.file_path, generic_bitmaps_to_save
            )

        key_index = 0
        for i, slot_name in enumerate(texture_slots):
            if export_attempted_slots[i]:
                if key_index < len(exported_keys):
                    final_key = exported_keys[key_index]

                    body.textures.append(final_key)
                    material_pc.material.link_header.names.append(final_key)
                    body.general_flag |= slot_to_flag[slot_name]

                    key_index += 1
                else:
                    body.textures.append("")

            else:
                body.textures.append("")

        return material_pc

    def to_generic(self) -> Material:
        body: MaterialV106_63_02PCBody = self.material.body
        generic_material = Material()

        generic_material.file_path = self.file_path
        generic_material.file_name = str(self.material.name)
        generic_material.name = str(self.material.link_header.link_name)

        for i, texture in enumerate(list(body.textures)):
            print(f"Texture {i}: {texture}")
        generic_bitmaps = load_dependencies(self.file_path, list(body.textures))
        for bitmap in generic_bitmaps:
            if bitmap is not None:
                print(f"{bitmap.file_name!r} ->", str(bitmap.name))
            else:
                print(f"bitmap was not found")

        generic_material.diffuse_color = tuple(body.diffuse[:3])
        generic_material.opacity = body.diffuse[3]
        generic_material.emissive_color = tuple(body.emission)
        generic_material.specular_color = tuple(body.specular)
        generic_material.specular_power = body.specular_pow
        generic_material.rat_params = body.params
        generic_material.uv_rotation = body.rotation
        generic_material.uv_translation = tuple(body.translation)
        generic_material.uv_scale = tuple(body.scale)

        # Render flags
        generic_material.env_alpha_mask = bool(
            body.render_flag & RatMaterialRenderFlags.ALPHA_MASK
        )
        generic_material.invisible = bool(
            body.render_flag & RatMaterialRenderFlags.INVISIBLE
        )
        generic_material.uv_clamp_u = bool(
            body.render_flag & RatMaterialRenderFlags.UV_CLAMP_U
        )
        generic_material.uv_clamp_v = bool(
            body.render_flag & RatMaterialRenderFlags.UV_CLAMP_V
        )
        generic_material.blend_additive = bool(
            body.render_flag & RatMaterialRenderFlags.BLEND_ADDITIVE
        )
        generic_material.blend_subtractive = bool(
            body.render_flag & RatMaterialRenderFlags.BLEND_SUBTRACTIVE
        )
        generic_material.blend_dest_additive = bool(
            body.render_flag & RatMaterialRenderFlags.BLEND_DEST_ADDITIVE
        )
        generic_material.double_sided = bool(
            body.render_flag & RatMaterialRenderFlags.DOUBLE_SIDED
        )

        # Collision flags
        collision_flag = body.collision_flag
        generic_material.rat_surface_type = collision_flag_to_rat_surface_type(
            collision_flag
        )
        generic_material.rat_sound_type = collision_flag_to_rat_sound_type(
            collision_flag
        )
        generic_material.rat_deep_water = bool(
            generic_material.rat_surface_type == RatSurfaceTypes.WATER
            and collision_flag & RatMaterialCollisionFlags.SOUND_1
        )
        generic_material.rat_footprints_while_off = bool(
            collision_flag & RatMaterialCollisionFlags.FOOTPRINTS_OFF
        )
        generic_material.rat_footprints_while_on = bool(
            collision_flag & RatMaterialCollisionFlags.FOOTPRINTS_ON
        )

        slots = ["tex_diffuse", "tex_envmap", "tex_normal", "tex_specular"]
        for slot_name, bitmap in zip(slots, generic_bitmaps):
            setattr(generic_material, slot_name, bitmap)

        return generic_material
