import bpy
from os.path import dirname, exists, join
from os import makedirs
import json
import traceback

from ..zouna.generic.resource import Resource
from ..zouna.bff.io import Platform, BffClass, bff_class_to_dict
from ..common.constants import Game, VERSION_MAP, resolve_game_platform
from ..common.util import safe_int
from .handlers import get_export_handler


def member_name_from_generic(generic: Resource) -> str:
    """
    Determine the bff member name for a generic resource.
    Preferred sources (in order):
      - class name with lowercase first letter (same heuristic you used before)
    """
    clsname = generic.__class__.__name__
    print(f"Generic class name: {clsname}")
    if clsname:
        return clsname[0].lower() + clsname[1:]
    raise KeyError(
        "Cannot determine member name for resource; please set `bff_member` on the resource or implement a stable mapping."
    )


def dispatch_export(generic_class: Resource, game: Game, platform: Platform) -> dict:
    """
    Convert `generic_class` to a serialisable BFF-style dict using the
    export handler registered for the resolved (platform, version, member_name).

    Returns a dict ready to json.dump.
    Raises KeyError if no export handler available or mapping missing.
    """
    game, platform = resolve_game_platform(game, platform)

    version_str = VERSION_MAP.get((game, platform))
    if version_str is None:
        raise KeyError(f"No version mapping for {(game, platform)!r}")

    member_name = member_name_from_generic(generic_class)

    handler = get_export_handler(platform, str(version_str), member_name)
    if handler is None:
        raise KeyError(
            f"No export handler registered for {(platform, version_str, member_name)!r}"
        )

    return handler(generic_class)


def export_resource(generic_class: Resource, filename: str):
    """
    Export the given generic resource to filename (pretty JSON).
    If generic_class has binary data, writes the binary file to the same directory.
    Returns the canonical link key (processed by safe_int) on success.
    """
    dir_path = dirname(filename)
    if not exists(dir_path):
        try:
            makedirs(dir_path, exist_ok=True)
        except OSError as exc:
            raise Exception(f"Failed to create directory '{dir_path}': {exc}")

    try:
        scene = bpy.context.scene

        generic_class.file_path = filename
        target_game = Game(scene.zouna_game)
        target_platform = Platform(scene.zouna_platform)

        bff_class = dispatch_export(generic_class, target_game, target_platform)

        member_name = member_name_from_generic(generic_class)
        resource_wrapper = getattr(bff_class.bff_class_class, member_name)

        versioned_resource = None
        for key, value in resource_wrapper.__dict__.items():
            if value is not None:
                versioned_resource = value
                break

        if versioned_resource is None:
            raise AttributeError(
                f"Could not find any active versioned resource inside the '{member_name}' wrapper for linking."
            )

        resource_key = versioned_resource.name

        if resource_key is None:
            raise AttributeError(
                f"Versioned resource object ({versioned_resource.__class__.__name__}) is missing a 'name' attribute for linking."
            )

        resource_dict = bff_class_to_dict(bff_class)

        with open(filename, "wb") as f:
            text = json.dumps(resource_dict, ensure_ascii=False, indent=2, default=str)
            f.write(text.encode("utf-8"))

        print(f"Exported BFF resource to {filename}")

        resource_data = generic_class.data
        data_ext = generic_class.data_ext

        if resource_data and data_ext:
            data_filename = join(dir_path, f"data.{data_ext.lower()}")

            with open(data_filename, "wb") as f:
                f.write(resource_data)

            print(f"Exported binary data to {data_filename}")
        # ------------------------------------------

        return safe_int(resource_key)

    except Exception:
        traceback.print_exc()
        raise Exception("Error exporting BFF resource")
