import inspect
from dataclasses import dataclass
from enum import Enum
from typing import Any, Callable, Dict, Optional, Tuple
from ..zouna.bff.io import BffClassHeader, BffClass, Class, Material, Mesh, Bitmap

class_members = [
    "animation",
    "animation_graph",
    "animation_graph_override",
    "anim_frame",
    "area_light",
    "binary",
    "bitmap",
    "camera",
    "camera_zone",
    "collision_vol",
    "collision_vol_data",
    "conductor",
    "decal",
    "dialog_event",
    "entity",
    "flare",
    "flare_data",
    "fog_volume",
    "fonts",
    "fx_particles",
    "fx_particles_data",
    "game_obj",
    "gen_world",
    "graph",
    "gw_road",
    "h_fog",
    "h_fog_data",
    "hull_spline_zone",
    "light",
    "light_data",
    "light_probe_volume",
    "lod",
    "lod_data",
    "mass_instancing_volume",
    "material",
    "material_anim",
    "material_collect",
    "material_obj",
    "mesh",
    "mesh_data",
    "net_bing_obj",
    "node",
    "occluder",
    "omni",
    "omni_data",
    "override",
    "particles",
    "particles_data",
    "prefab",
    "prefab_ref",
    "reflection_probe",
    "rot_shape",
    "rot_shape_data",
    "rtc",
    "shader",
    "skel",
    "skin",
    "skin_data",
    "sound",
    "sound_event",
    "special_effect_node",
    "spline",
    "spline_graph",
    "spline_zone",
    "surface",
    "surface_datas",
    "terrain",
    "texture",
    "txt",
    "user_define",
    "user_define_script",
    "warp",
    "world",
    "world_ref",
    "x_ref_node",
]

resource_wrapper_class_map = {
    "material": Material,
    "mesh": Mesh,
    "bitmap": Bitmap,
}

Handler = Callable[[Any], Any]


@dataclass
class HandlerPair:
    """
    Container for import/export handlers for a given (platform, version, member_name).
    Either handler may be None.
    """

    import_handler: Optional[Handler] = None
    export_handler: Optional[Handler] = None


_handlers: Dict[Tuple[Enum, str, str], HandlerPair] = {}


def register_handler(
    platform: Enum, version: str, member_name: str, *, direction: str = "import"
) -> Callable[[Handler], Handler]:
    """
    Decorator to register a handler for the specific (platform, version, member_name).

    direction: "import" (default) or "export".
      - import handler will be stored as HandlerPair.import_handler
      - export handler will be stored as HandlerPair.export_handler

    Backwards-compatible: calling without `direction` registers an import handler.
    """

    direction = direction.lower()
    if direction not in ("import", "export"):
        raise ValueError("direction must be 'import' or 'export'")

    def decorator(fn: Handler) -> Handler:
        key = (platform, version, member_name)
        pair = _handlers.get(key)
        if pair is None:
            pair = HandlerPair()
            _handlers[key] = pair

        if direction == "import":
            if pair.import_handler is not None:
                raise KeyError(f"Import handler already registered for {key!r}")
            pair.import_handler = fn
        else:
            if pair.export_handler is not None:
                raise KeyError(f"Export handler already registered for {key!r}")
            pair.export_handler = fn

        return fn

    return decorator


def get_import_handler(
    platform: Enum, version: str, member_name: str
) -> Optional[Handler]:
    """
    Return the import handler for the combination, or None if not present.
    """
    pair = _handlers.get((platform, version, member_name))
    return pair.import_handler if pair is not None else None


def get_export_handler(
    platform: Enum, version: str, member_name: str
) -> Optional[Handler]:
    """
    Return the export handler for the combination, or None if not present.
    """
    pair = _handlers.get((platform, version, member_name))
    return pair.export_handler if pair is not None else None


def make_handler(
    version_class: Any, platform: Enum, version_str: str, member_name: str
):
    """
    Helper function called for each combination to automatically generate handlers.

    Behavior:
      - If `version_class` has a callable `to_generic(self)` instance method, register an
        import handler which constructs `version_class(bff_value)` and calls `.to_generic()`.
      - If `version_class` has a callable `from_generic(...)` classmethod or function, register
        an export handler which calls `version_class.from_generic(generic_value)`.

    Returns the import handler if one was created, otherwise returns the export handler if only
    that was created, otherwise None.
    """

    created_import = None
    created_export = None

    if hasattr(version_class, "__init__") and hasattr(version_class, "to_generic"):
        @register_handler(platform, version_str, member_name, direction="import")
        def import_handler(bff_value):
            return version_class(bff_value).to_generic()

        created_import = import_handler

    if hasattr(version_class, "__init__") and hasattr(version_class, "from_generic"):
        resource_wrapper_class = resource_wrapper_class_map.get(member_name)
        if resource_wrapper_class is None:
            print(
                f"Warning: Could not define Bff export handler for '{member_name}'. Missing entry in resource_wrapper_class_map."
            )
            return created_import or created_export

        try:
            wrapper_sig = inspect.signature(resource_wrapper_class.__init__)
            all_wrapper_fields = list(wrapper_sig.parameters.keys())[1:]

            if not all_wrapper_fields:
                raise ValueError(
                    "Wrapper class has no positional arguments for __init__ (excluding self)."
                )

        except Exception as e:
            print(
                f"Error inspecting wrapper class {resource_wrapper_class.__name__} for fields: {e}"
            )
            return created_import or created_export

        version_part = version_str.split(" ")[0].split(" - ")[0]
        version_tag_safe = version_part.replace(".", "_").replace("-", "_").lower()
        expected_wrapper_field_name = f"{member_name}_{version_tag_safe}_pc"

        @register_handler(platform, version_str, member_name, direction="export")
        def export_handler(generic_value):
            """
            Returns the fully wrapped BffClass object.
            Accesses all_wrapper_fields and expected_wrapper_field_name from enclosing scope.
            """

            platform_resource = version_class.from_generic(generic_value)

            inner_resource = getattr(platform_resource, member_name)
            if not inner_resource:
                raise ValueError(
                    f"Exported platform resource is missing inner '{member_name}' attribute."
                )

            all_wrapper_args = {}
            for field in all_wrapper_fields:
                if field == expected_wrapper_field_name:
                    all_wrapper_args[field] = inner_resource
                else:

                    all_wrapper_args[field] = None

            wrapped_resource = resource_wrapper_class(**all_wrapper_args)

            header = BffClassHeader(platform=platform, version=version_str)

            class_members_args = {}
            for member in class_members:
                if member == member_name:
                    class_members_args[member] = wrapped_resource
                else:
                    class_members_args[member] = None

            return BffClass(
                bff_class_class=Class(**class_members_args),
                header=header,
            )

        created_export = export_handler

    return created_import or created_export
