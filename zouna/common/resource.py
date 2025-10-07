from ...blender.imp import import_resource
from pathlib import Path
from typing import Union, Iterable, Any

classes = [
    "Animation_Z",
    "AnimationGraph_Z",
    "AnimationGraphOverride_Z",
    "AnimFrame_Z",
    "AreaLight_Z",
    "Binary_Z",
    "Bitmap_Z",
    "Camera_Z",
    "CameraZone_Z",
    "CollisionVol_Z",
    "CollisionVolData_Z",
    "Conductor_Z",
    "Decal_Z",
    "DialogEvent_Z",
    "Entity_Z",
    "Flare_Z",
    "FlareData_Z",
    "FogVolume_Z",
    "Fonts_Z",
    "FxParticles_Z",
    "FxParticlesData_Z",
    "GameObj_Z",
    "GenWorld_Z",
    "Graph_Z",
    "GwRoad_Z",
    "HFog_Z",
    "HFogData_Z",
    "HullSplineZone_Z",
    "Light_Z",
    "LightData_Z",
    "LightProbeVolume_Z",
    "Lod_Z",
    "LodData_Z",
    "MassInstancingVolume_Z",
    "Material_Z",
    "MaterialAnim_Z",
    "MaterialCollect_Z",
    "MaterialObj_Z",
    "Mesh_Z",
    "MeshData_Z",
    "NetBingObj_Z",
    "Node_Z",
    "Occluder_Z",
    "Omni_Z",
    "OmniData_Z",
    "Override_Z",
    "Particles_Z",
    "ParticlesData_Z",
    "Prefab_Z",
    "PrefabRef_Z",
    "ReflectionProbe_Z",
    "RotShape_Z",
    "RotShapeData_Z",
    "Rtc_Z",
    "Shader_Z",
    "Skel_Z",
    "Skin_Z",
    "SkinData_Z",
    "Sound_Z",
    "SoundEvent_Z",
    "SpecialEffectNode_Z",
    "Spline_Z",
    "SplineGraph_Z",
    "SplineZone_Z",
    "Surface_Z",
    "SurfaceDatas_Z",
    "Terrain_Z",
    "Texture_Z",
    "Txt_Z",
    "UserDefine_Z",
    "UserDefineScript_Z",
    "Warp_Z",
    "World_Z",
    "WorldRef_Z",
    "XRefNode_Z",
]


def load_dependencies(
    resource_path: str,
    names: Iterable[Union[str, int]],
) -> list[Any | None]:
    """
    For each name in `names`, tries in order each class in `classes` to find:
        <resources_dir>/<name>.<class>.d/resource.json
    Returns a list of the imported objects (via import_resource), or None if not found.
    """
    base = Path(resource_path).parent.parent
    if not base.is_dir():
        raise FileNotFoundError(f"Resources folder not found: {base!r}")

    results: list[Any | None] = []
    for name in names:
        key = str(name)
        key = key.replace(":", "_").replace(">", "_")
        loaded: Any | None = None

        for cls in classes:
            candidate = base / f"{key}.{cls}.d" / "resource.json"
            if candidate.is_file():
                print(f"---- LOADING DEPENDENCY {str(candidate)} -----")
                loaded = import_resource(str(candidate))
                print(f"---- LOADED DEPENDENCY {str(candidate)} -----")
                break

        results.append(loaded)

    return results
