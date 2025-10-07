from enum import Enum, StrEnum, IntFlag, IntEnum

# Material constants


class ZounaShaderNodeTypes(StrEnum):
    OutputMaterial = "ShaderNodeOutputMaterial"
    BsdfDiffuse = "ShaderNodeBsdfDiffuse"
    DiffuseTexture = "ShaderNodeTexImage"
    DiffuseColor = "ShaderNodeMixRGB"
    EnvmapTexture = "ShaderNodeTexImage"
    EnvmapUV = "ShaderNodeAttribute"
    EnvmapCurve = "ShaderNodeRGBCurve"
    EnvmapAlphaMask = "ShaderNodeVectorMath"
    AddDiffuseEnvmap = "ShaderNodeMixRGB"


class ZounaShaderNodeNames(StrEnum):
    OutputMaterial = "OUTPUT_MATERIAL"
    BsdfDiffuse = "DIFFUSE_BSDF"
    DiffuseTexture = "DIFFUSE_TEXTURE"
    DiffuseColor = "DIFFUSE_COLOR"
    EnvmapTexture = "ENVMAP_TEXTURE"
    EnvmapUV = "ENVMAP_UV"
    EnvmapCurve = "ENVMAP_CURVE"
    EnvmapAlphaMask = "ENVMAP_ALPHA_MASK"
    AddDiffuseEnvmap = "ADD_DIFFUSE_ENVMAP"


class BmFormat(IntEnum):
    BM_4 = 0x01  # 4 Bits Indexed RGB
    BM_8 = 0x02  # 8 Bits Indexed RGB
    BM_5551 = 0x07  # 16 RGBA
    BM_565 = 0x08  # 16 RGB
    BM_4444 = 0x0A  # 16 RGBA
    BM_1555 = 0x0B  # .TGA compatibility
    BM_8888 = 0x0C  # 32 RGBA - DXT5
    BM_888 = 0x0D  # 24 RGB - DXT1
    BM_CMPR = 0x0E  # S3TC
    BM_I4A4 = 0x0F  # I4A4
    BM_I8A8 = 0x10  # I4A4


class PalFormat(IntEnum):
    PAL_3444 = 0x01  # 16 ARGB
    PAL_565 = 0x02  # 16 RGB
    PAL_8888 = 0x03  # 32 RGBA
    PAL_LUM = 0x04  # Luminance
    PAL_ALPHA = 0x05  # Alpha
    PAL_DXT1 = 0x11  # DXT1 (OPAQUE)
    PAL_DXT3 = 0x12  # DXT3 (ALPHA)
    PAL_DXT5 = 0x13  # DXT5 (ALPHA)


class BmTransp(IntEnum):
    BM_NO_TRANSP = 0
    BM_TRANSP_ONE = 1
    BM_TRANSP = 2


# Rat constants


class RatSurfaceTypes(StrEnum):
    NONE = "NONE"
    SOLID = "SOLID"
    WATER = "WATER"
    SLIPPERY = "SLIPPERY"
    STICKY = "STICKY"
    SLIDE_JUMP = "SLIDE_JUMP"
    SLIDE_NO_JUMP = "SLIDE_NO_JUMP"


class RatSoundTypes(StrEnum):
    STONE = "STONE"
    WOOD = "WOOD"
    DIRT = "DIRT"
    GRASS = "GRASS"
    METAL = "METAL"
    WATER = "WATER"
    MUD = "MUD"
    SQUEAKY = "SQUEAKY"
    POPPING = "POPPING"


class RatMaterialRenderFlags(IntFlag):
    NONE = 0x0
    ALPHA_MASK = 0x1
    UNK_2_USED = 0x2
    UNK_4_USED = 0x4
    UNK_20_USED = 0x20
    INVISIBLE = 0x80
    UV_CLAMP_U = 0x100
    UV_CLAMP_V = 0x200
    ICE = 0x1000  # not sure if ice, and not rat specific def
    DOUBLE_SIDED = 0x20000
    UNK_800000_USED = 0x800000


class RatMaterialCollisionFlags(IntFlag):
    NONE = 0x0
    UNK_1_USED = 0x1
    COLLIDABLE = 0x2
    UNK_4_USED = 0x4
    NO_WALKING = 0x8
    UNK_20000_USED = 0x20000
    SOUND_1 = 0x40000
    SOUND_2 = 0x80000
    SOUND_3 = 0x100000
    SOUND_4 = 0x200000
    SLIDE_JUMP = 0x400000
    SLIDE_NO_JUMP = 0x800000
    SURFACE_1 = 0x1000000
    FOOTPRINTS_ON = 0x10000000
    FOOTPRINTS_OFF = 0x20000000
    WATER = NO_WALKING | SLIDE_JUMP | SLIDE_NO_JUMP
    SLIPPERY = SLIDE_JUMP | SURFACE_1
    STICKY = SLIDE_NO_JUMP | SURFACE_1
    SOLID = UNK_1_USED | COLLIDABLE | UNK_4_USED
    SOUND_WATER = SOUND_1
    SOUND_DIRT = SOUND_2
    SOUND_WOOD = SOUND_3
    SOUND_MUD = SOUND_4
    SOUND_GRASS = SOUND_1 | SOUND_2
    SOUND_METAL = SOUND_1 | SOUND_3
    SOUND_SQUEAKY = SOUND_2 | SOUND_3
    SOUND_STONE2 = SOUND_1 | SOUND_4
    SOUND_DIRT2 = SOUND_2 | SOUND_4
    SOUND_STONE3 = SOUND_3 | SOUND_4
    SOUND_POPPING = SOUND_1 | SOUND_2 | SOUND_3
    SOUND_STONE4 = SOUND_1 | SOUND_2 | SOUND_4
    SOUND_STONE5 = SOUND_1 | SOUND_3 | SOUND_4
    SOUND_STONE6 = SOUND_2 | SOUND_3 | SOUND_4
    SOUND_STONE7 = SOUND_1 | SOUND_2 | SOUND_3 | SOUND_4


class RatMaterialCodeFlags(IntFlag):
    NONE = 0x0
    DIFFUSE = 0x1
    ENVMAP = 0x2
    NORMAL = 0x4
    SPECULAR = 0x8


def collision_flag_to_rat_surface_type(collision_flag: int) -> RatSurfaceTypes:
    """
    Maps the collision flag int value to the proper surface type enum.
    """
    flag = RatMaterialCollisionFlags(collision_flag)

    solid_bits = RatMaterialCollisionFlags.SOLID
    has_solid = (flag & solid_bits) == solid_bits

    if (
        has_solid
        and (flag & RatMaterialCollisionFlags.WATER) == RatMaterialCollisionFlags.WATER
    ):
        return RatSurfaceTypes.WATER
    if (
        has_solid
        and (flag & RatMaterialCollisionFlags.SLIPPERY)
        == RatMaterialCollisionFlags.SLIPPERY
    ):
        return RatSurfaceTypes.SLIPPERY
    if (
        has_solid
        and (flag & RatMaterialCollisionFlags.STICKY)
        == RatMaterialCollisionFlags.STICKY
    ):
        return RatSurfaceTypes.SLIPPERY
    if has_solid and (flag & RatMaterialCollisionFlags.SLIDE_JUMP) != 0:
        return RatSurfaceTypes.SLIDE_JUMP
    if has_solid and (flag & RatMaterialCollisionFlags.SLIDE_NO_JUMP) != 0:
        return RatSurfaceTypes.SLIDE_NO_JUMP
    if has_solid:
        return RatSurfaceTypes.SOLID

    if collision_flag != 0:
        parts = []
        for name, member in (
            ("UNK_1_USED", RatMaterialCollisionFlags.UNK_1_USED),
            ("COLLIDABLE", RatMaterialCollisionFlags.COLLIDABLE),
            ("UNK_4_USED", RatMaterialCollisionFlags.UNK_4_USED),
            ("NO_WALKING", RatMaterialCollisionFlags.NO_WALKING),
            ("SLIDE_JUMP", RatMaterialCollisionFlags.SLIDE_JUMP),
            ("SLIDE_NO_JUMP", RatMaterialCollisionFlags.SLIDE_NO_JUMP),
            ("STICKY", RatMaterialCollisionFlags.STICKY),
            ("FOOTPRINTS_ON", RatMaterialCollisionFlags.FOOTPRINTS_ON),
            ("FOOTPRINTS_OFF", RatMaterialCollisionFlags.FOOTPRINTS_OFF),
        ):
            if int(flag) & int(member):
                parts.append(name)

        print(
            "ERROR: Flag wasn't empty but did not match any surface type",
            f"raw=0x{collision_flag:x}",
            f"bits={parts}",
        )

    return RatSurfaceTypes.NONE


def collision_flag_to_rat_sound_type(collision_flag: int) -> RatSoundTypes:
    """
    Maps the collision flag int value to the proper sound type enum.
    """
    SOUND_BITS = (
        RatMaterialCollisionFlags.SOUND_1
        | RatMaterialCollisionFlags.SOUND_2
        | RatMaterialCollisionFlags.SOUND_3
        | RatMaterialCollisionFlags.SOUND_4
    )
    masked_value = int(collision_flag) & int(SOUND_BITS)
    flag = RatMaterialCollisionFlags(masked_value)

    if flag == RatMaterialCollisionFlags.SOUND_POPPING:
        return RatSoundTypes.POPPING
    if flag == RatMaterialCollisionFlags.SOUND_SQUEAKY:
        return RatSoundTypes.SQUEAKY
    if flag == RatMaterialCollisionFlags.SOUND_METAL:
        return RatSoundTypes.METAL
    if flag == RatMaterialCollisionFlags.SOUND_GRASS:
        return RatSoundTypes.GRASS
    if flag == RatMaterialCollisionFlags.SOUND_WATER:
        return RatSoundTypes.WATER
    if flag == RatMaterialCollisionFlags.SOUND_DIRT:
        return RatSoundTypes.DIRT
    if flag == RatMaterialCollisionFlags.SOUND_WOOD:
        return RatSoundTypes.WOOD
    if flag == RatMaterialCollisionFlags.SOUND_MUD:
        return RatSoundTypes.MUD

    if masked_value != 0:
        parts = []
        if masked_value & int(RatMaterialCollisionFlags.SOUND_1):
            parts.append("SOUND_1")
        if masked_value & int(RatMaterialCollisionFlags.SOUND_2):
            parts.append("SOUND_2")
        if masked_value & int(RatMaterialCollisionFlags.SOUND_3):
            parts.append("SOUND_3")
        if masked_value & int(RatMaterialCollisionFlags.SOUND_4):
            parts.append("SOUND_4")

        print(
            f"Unhandled sound combo: masked={masked_value} "
            f"(bits: {', '.join(parts)})"
        )

    return RatSoundTypes.STONE
