from os.path import isfile
import json
from ..zouna.bff.io import bff_class_from_dict, BffClass
from .handlers import get_handler


def load_json(content):
    """
    Loads a json from string to a python object.
    """

    def bad_constant(val):
        raise ImportError("Bad constant: %s" % val)

    try:
        text = str(content, encoding="utf-8")
        return json.loads(text, parse_constant=bad_constant)
    except ValueError as e:
        raise ImportError("Bad: %s" % e.args[0])


def dispatch(bff_class: BffClass):
    """
    Handles a resource load for a given BffClass according to its properties (platform, version, class).
    """
    platform = bff_class.header.platform
    version = str(bff_class.header.version)
    inner_class = bff_class.bff_class_class

    member_name = None
    for name, value in vars(inner_class).items():
        if not name.startswith("_") and value is not None:
            member_name = name
            break

    if member_name is None:
        raise ValueError("No member is set on Class!")

    handler = get_handler(platform, version, member_name)
    if handler is None:
        raise KeyError(f"No handler for {(platform, version, member_name)!r}")

    resource_class = getattr(inner_class, member_name)
    resource_class.file_path = bff_class.file_path

    return handler(resource_class)


def import_resource(filename):
    if not isfile(filename):
        raise ImportError("Please select a file")

    with open(filename, "rb") as f:
        content = memoryview(f.read())
        resource = load_json(content)
    try:
        bff_class = bff_class_from_dict(resource)
        print(f"Filname {filename}")
        bff_class.file_path = filename
        print(f"Bff class filepath: {bff_class.file_path}")
        return dispatch(bff_class)
    except AssertionError:
        import traceback

        traceback.print_exc()
        raise ImportError("Error loading BFF resource")
