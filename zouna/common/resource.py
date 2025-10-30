import re
from ...blender.imp import import_resource
from pathlib import Path
from typing import List, Union, Iterable, Any
from ...blender.exp import export_resource, member_name_from_generic
from ...common.util import safe_int
from ...zouna.generic.resource import Resource

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


def save_dependencies(
    resource_path: str,
    generic_resources: list[Resource],
) -> list[Union[str, int]]:
    """
    Exports a list of generic resource objects to the dependency file structure
    and returns the canonical link keys (names) of the successfully exported resources.
    """
    base = Path(resource_path).parent.parent
    if not base.is_dir():
        raise FileNotFoundError(f"Resources folder not found: {base!r}")

    exported_keys: list[Union[str, int]] = []
    # TODO: Add a config option to enable this branch
    if False:
        for generic in generic_resources:
            resource_name = generic.file_name
            if not resource_name:
                print(
                    f"Warning: Resource {generic!r} skipped, no 'file_name' attribute found."
                )
                continue
            exported_keys.append(safe_int(resource_name))

        print(f"Skipping export; returning {len(exported_keys)} dependency keys.")
        return exported_keys

    for generic in generic_resources:
        resource_name = None
        try:
            resource_name = generic.file_name
            if not resource_name:
                print(
                    f"Warning: Resource {generic!r} skipped, no 'file_name' attribute found."
                )
                continue

            member_name = member_name_from_generic(generic)
            print(f"Resource name: {resource_name}, Member name: {member_name}")

            base_key = str(resource_name)
            base_key = re.sub(r"\.\d+$", "", base_key)
            base_key = base_key.replace(":", "_").replace(">", "_")
            generic_class_name = generic.__class__.__name__
            dependency_suffix = f"{generic_class_name}_Z"
            current_key = base_key
            dependency_dir = base / f"{current_key}.{dependency_suffix}.d"
            counter = 2

            while dependency_dir.is_dir():
                print(
                    f"Warning: Dependency folder already exists: {dependency_dir.name}. Attempting to rename..."
                )
                current_key = f"{base_key}__{counter}"
                new_dir_name = f"{current_key}.{dependency_suffix}.d"
                dependency_dir = base / new_dir_name
                counter += 1

            generic.file_name = current_key
            final_key_name = current_key
            print(f"Set generic.file_name to: {final_key_name}")
            destination_path = dependency_dir / "resource.json"
            print(f"---- EXPORTING DEPENDENCY {str(destination_path)} -----")
            link_key = export_resource(generic, str(destination_path))
            print(f"---- EXPORTED DEPENDENCY {str(destination_path)} -----")

            exported_keys.append(safe_int(link_key))

        except Exception as e:
            print(f"Error saving dependency for resource {resource_name}: {e}")

    print(f"Finished saving {len(exported_keys)} dependencies.")
    return exported_keys


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
