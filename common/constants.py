from enum import Enum, StrEnum, IntFlag, IntEnum
from typing import Dict, Tuple, Any
from ..zouna.bff.io import Platform

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


# Mesh constants


class ColPrimitiveType(StrEnum):
    NONE = "NONE"
    SPHERE = "SPHERE"
    BOX = "BOX"
    CYLINDER = "CYLINDER"


class ColPrimitiveCategory(StrEnum):
    COLLIDER = "COLLIDER"
    SHADOW = "SHADOW"
    COLLECT = "COLLECT"
    COLLECTABLE = "COLLECTABLE"
    LOD = "LOD"
    STRENGTH = "STRENGTH"
    KICK = "KICK"
    NFADE = "NFADE"
    FADE = "FADE"
    ACTION = "ACTION"
    MAGNET = "MAGNET"
    INTER = "INTER"
    REPULSE = "REPULSE"


CATEGORY_COLORS = {
    "COLLIDER": (0.0, 1.0, 0.0, 1.0),  # green
    "SHADOW": (1.0, 1.0, 1.0, 1.0),  # white
    "COLLECT": (0.0, 0.0, 1.0, 1.0),  # blue
    "COLLECTABLE": (0.0, 0.9, 0.9, 1.0),  # teal-cyan
    "LOD": (1.0, 0.3, 0.0, 1.0),  # bright orange
    "STRENGTH": (0.6, 0.0, 0.8, 1.0),  # deep violet
    "KICK": (0.2, 0.9, 0.4, 1.0),  # vivid spring green
    "NFADE": (1.0, 0.2, 0.0, 1.0),  # red-orange
    "FADE": (1.0, 0.9, 0.3, 1.0),  # warm yellow
    "ACTION": (0.9, 0.1, 0.1, 1.0),  # red
    "MAGNET": (0.9, 0.0, 0.9, 1.0),  # bright magenta
    "INTER": (0.1, 0.6, 0.9, 1.0),  # sky blue
    "REPULSE": (1.0, 1.0, 0.0, 1.0),  # yellow
}

col_primitive_categories = [
    (ColPrimitiveCategory.COLLIDER.name, "Collider", "Collision primitive"),
    (ColPrimitiveCategory.SHADOW.name, "Shadow", "Shadow primitive"),
    (ColPrimitiveCategory.COLLECT.name, "Collect", "Collect primitive"),
    (ColPrimitiveCategory.COLLECTABLE.name, "Collectable", "Collectable primitive"),
    (ColPrimitiveCategory.LOD.name, "LOD", "Level of Detail primitive"),
    (ColPrimitiveCategory.STRENGTH.name, "Strength", "Strength primitive"),
    (ColPrimitiveCategory.KICK.name, "Kick", "Kick primitive"),
    (ColPrimitiveCategory.NFADE.name, "NFade", "Near Fade primitive"),
    (ColPrimitiveCategory.FADE.name, "Fade", "Fade primitive"),
    (ColPrimitiveCategory.ACTION.name, "Action", "Action primitive"),
    (ColPrimitiveCategory.MAGNET.name, "Magnet", "Magnet primitive"),
    (ColPrimitiveCategory.INTER.name, "Inter", "Inter primitive"),
    (ColPrimitiveCategory.REPULSE.name, "Repulse", "Repulse primitive"),
]

col_primitive_types = [
    (ColPrimitiveType.NONE.name, "NoPrimitive", "No collision primitive"),
    (ColPrimitiveType.BOX.name, "Box", "Box collision primitive"),
    (ColPrimitiveType.SPHERE.name, "Sphere", "Sphere collision primitive"),
    (ColPrimitiveType.CYLINDER.name, "Cylinder", "Cylinder collision primitive"),
]


# Rat constants


class RatSurfaceTypes(StrEnum):
    NONE = "NONE"
    SOLID = "SOLID"
    COLLECT = "COLLECT"
    COLLECTABLE = "COLLECTABLE"
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


rat_surface_types = [
    (RatSurfaceTypes.NONE, "None", "No collision"),
    (RatSurfaceTypes.SOLID, "Ground", "Solid ground that can be walked on"),
    (RatSurfaceTypes.COLLECT, "Collect", "Collect surface (collects)"),
    (
        RatSurfaceTypes.COLLECTABLE,
        "Collectable",
        "Collectable surface (that can be collected)",
    ),
    # Breaks Alpha Mask for Envmap (textures that expect that will be shown broken)
    (
        RatSurfaceTypes.WATER,
        "Water",
        "Water surface which will damage the player when in contact",
    ),
    (
        RatSurfaceTypes.SLIPPERY,
        "Slippery",
        "Slippery surface that will cause the player to slip",
    ),
    (
        RatSurfaceTypes.STICKY,
        "Sticky",
        "Sticky surface that will cause the player to slow down",
    ),
    (
        RatSurfaceTypes.SLIDE_JUMP,
        "Slide",
        "Slide surface that will cause the player to slide",
    ),
    (
        RatSurfaceTypes.SLIDE_NO_JUMP,
        "Slide No Jump",
        "Slide surface that will cause the player to slide, disables jumping",
    ),
]


rat_sound_types = [
    (RatSoundTypes.STONE, "Stone", "Stone sound"),
    (RatSoundTypes.WOOD, "Wood", "Wood sound"),
    (RatSoundTypes.DIRT, "Dirt", "Dirt sound"),
    (RatSoundTypes.GRASS, "Grass", "Grass sound"),
    (RatSoundTypes.METAL, "Metal", "Metal sound"),
    (RatSoundTypes.WATER, "Water", "Water sound"),
    (RatSoundTypes.MUD, "Mud", "Mud sound"),
    (RatSoundTypes.SQUEAKY, "Squeaky", "Squeaky sound"),
    (RatSoundTypes.POPPING, "Popping", "Popping sound"),
]


class RatMaterialRenderFlags(IntFlag):
    NONE = 0x0
    ALPHA_MASK = 0x1
    UNK_2_USED = 0x2
    UNK_4_USED = 0x4
    UNK_20_USED = 0x20
    INVISIBLE = 0x80
    UV_CLAMP_U = 0x100
    UV_CLAMP_V = 0x200
    BLEND_ADDITIVE = 0x1000
    BLEND_SUBTRACTIVE = 0x2000
    BLEND_DEST_ADDITIVE = 0x4000
    DOUBLE_SIDED = 0x20000
    UNK_800000_USED = 0x800000
    DEFAULT = UNK_800000_USED


class RatMaterialCollisionFlags(IntFlag):
    NONE = 0x0
    UNK_1_USED = 0x1
    COLLIDABLE = 0x2
    UNK_4_USED = 0x4
    NO_WALKING = 0x8
    COLLECT = 0x8000
    COLLECTABLE = 0x20000
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
    DEFAULT = UNK_1_USED | UNK_4_USED
    SOLID = UNK_1_USED | COLLIDABLE | UNK_4_USED
    SOUND_WATER = SOUND_1
    SOUND_DIRT = SOUND_2
    SOUND_WOOD = SOUND_3
    SOUND_MUD = SOUND_4  # MEAT sound?
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


# Platform and Game enums, and version mapping


class Game(StrEnum):
    RATATOUILLE = "Ratatouille"
    WALL_E = "Wall-E"


class Version(StrEnum):
    V1_06_63_02 = "v1.06.63.02 - Asobo Studio - Internal Cross Technology"
    V1_291_03_06 = "v1.291.03.06 - Asobo Studio - Internal Cross Technology"


VERSION_MAP: Dict[Tuple[Game, Platform], str] = {
    (Game.RATATOUILLE, Platform.PC): Version.V1_06_63_02,
    (Game.WALL_E, Platform.PC): Version.V1_291_03_06,
}


def supported_platforms_for_game(game: Game):
    """Return list of Platform that have a VERSION_MAP entry for this game."""
    return [p for (g, p) in VERSION_MAP.keys() if g == game]


def supported_games_for_platform(platform: Platform):
    """Return list of Game that have a VERSION_MAP entry for this platform."""
    return [g for (g, p) in VERSION_MAP.keys() if p == platform]


def resolve_game_platform(game: Game, platform: Platform):
    """
    Validate (game, platform) against VERSION_MAP.
    If exact pair exists, return it.
    If platform invalid for game -> pick first platform supported by game (if any).
    If game invalid for platform -> pick first game that supports that platform.
    As last resort return the first mapped pair available.
    """
    if (game, platform) in VERSION_MAP:
        return game, platform

    plats = supported_platforms_for_game(game)
    if plats:
        return game, plats[0]

    games = supported_games_for_platform(platform)
    if games:
        return games[0], platform

    if len(VERSION_MAP) > 0:
        first_game, first_platform = next(iter(VERSION_MAP.keys()))
        return first_game, first_platform

    raise KeyError(
        "No version mapping available. Fill VERSION_MAP with at least one (game,platform)->version entry."
    )


def collision_flag_to_rat_surface_type(collision_flag: int) -> RatSurfaceTypes:
    """
    Maps the collision flag int value to the proper surface type enum.
    """
    flag = RatMaterialCollisionFlags(collision_flag)

    solid_bits = RatMaterialCollisionFlags.SOLID
    has_solid = (flag & solid_bits) == solid_bits

    if has_solid:
        if (flag & RatMaterialCollisionFlags.WATER) == RatMaterialCollisionFlags.WATER:
            return RatSurfaceTypes.WATER
        if (
            flag & RatMaterialCollisionFlags.SLIPPERY
        ) == RatMaterialCollisionFlags.SLIPPERY:
            return RatSurfaceTypes.SLIPPERY
        if (
            flag & RatMaterialCollisionFlags.STICKY
        ) == RatMaterialCollisionFlags.STICKY:
            return RatSurfaceTypes.STICKY
        if (flag & RatMaterialCollisionFlags.SLIDE_JUMP) != 0:
            return RatSurfaceTypes.SLIDE_JUMP
        if (flag & RatMaterialCollisionFlags.SLIDE_NO_JUMP) != 0:
            return RatSurfaceTypes.SLIDE_NO_JUMP
        return RatSurfaceTypes.SOLID
    if (flag & RatMaterialCollisionFlags.COLLECT) == RatMaterialCollisionFlags.COLLECT:
        return RatSurfaceTypes.COLLECT
    if (
        flag & RatMaterialCollisionFlags.COLLECTABLE
    ) == RatMaterialCollisionFlags.COLLECTABLE:
        return RatSurfaceTypes.COLLECTABLE
    if collision_flag != RatMaterialCollisionFlags.DEFAULT:
        parts = [m.name for m in RatMaterialCollisionFlags if flag & m]

        print(
            "ERROR: Flag wasn't default but did not match any surface type",
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


def rat_values_to_collision_flag(
    rat_surface_type: RatSurfaceTypes,
    rat_sound_type: RatSoundTypes,
    foot_on: bool,
    foot_off: bool,
) -> int:
    """Build the integer collision flag from the collision UI properties."""

    collision_flag = RatMaterialCollisionFlags.NONE

    print(f"rat_surface_type: {rat_surface_type}")
    rat_surface = rat_surface_type
    surface_map = {
        RatSurfaceTypes.NONE: RatMaterialCollisionFlags.DEFAULT,
        RatSurfaceTypes.SOLID: RatMaterialCollisionFlags.SOLID,
        RatSurfaceTypes.COLLECT: RatMaterialCollisionFlags.COLLECT,
        RatSurfaceTypes.COLLECTABLE: RatMaterialCollisionFlags.COLLECTABLE,
        RatSurfaceTypes.WATER: RatMaterialCollisionFlags.WATER
        | RatMaterialCollisionFlags.SOLID,
        RatSurfaceTypes.SLIPPERY: RatMaterialCollisionFlags.SLIPPERY
        | RatMaterialCollisionFlags.SOLID,
        RatSurfaceTypes.STICKY: RatMaterialCollisionFlags.STICKY
        | RatMaterialCollisionFlags.SOLID,
        RatSurfaceTypes.SLIDE_JUMP: RatMaterialCollisionFlags.SLIDE_JUMP
        | RatMaterialCollisionFlags.SOLID,
        RatSurfaceTypes.SLIDE_NO_JUMP: RatMaterialCollisionFlags.SLIDE_NO_JUMP
        | RatMaterialCollisionFlags.SOLID,
    }
    collision_flag |= surface_map.get(rat_surface, 0)
    print(f"collision_flag after surface: {collision_flag}")

    rat_sound = rat_sound_type
    sound_map = {
        RatSoundTypes.WOOD: RatMaterialCollisionFlags.SOUND_WOOD,
        RatSoundTypes.DIRT: RatMaterialCollisionFlags.SOUND_DIRT,
        RatSoundTypes.GRASS: RatMaterialCollisionFlags.SOUND_GRASS,
        RatSoundTypes.METAL: RatMaterialCollisionFlags.SOUND_METAL,
        RatSoundTypes.WATER: RatMaterialCollisionFlags.SOUND_WATER,
        RatSoundTypes.MUD: RatMaterialCollisionFlags.SOUND_MUD,
        RatSoundTypes.SQUEAKY: RatMaterialCollisionFlags.SOUND_SQUEAKY,
        RatSoundTypes.POPPING: RatMaterialCollisionFlags.SOUND_POPPING,
    }
    if rat_sound is not None and rat_sound is not RatSoundTypes.STONE:
        collision_flag |= sound_map.get(rat_sound, 0)

    if foot_off:
        collision_flag |= RatMaterialCollisionFlags.FOOTPRINTS_OFF
    if foot_on:
        collision_flag |= RatMaterialCollisionFlags.FOOTPRINTS_ON

    return collision_flag


def export_collision_name(col_primitive_category: ColPrimitiveCategory) -> str:
    """
    Export the collision 'name' field for SphereCol/BoxCol/CylindreCol.

    - COLLIDER  -> "DURL"
    - everything else: use the enum string as-is
    """
    if col_primitive_category == ColPrimitiveCategory.COLLIDER.name:
        return "DURL"

    return col_primitive_category
