import bpy, os


def get_material_from_context(context: bpy.types.Context):
    """
    Return the active Zouna material or None.
    """
    obj = context.object
    if obj is None:
        return None

    if obj.active_material is not None:
        return obj.active_material

    for slot in getattr(obj, "material_slots", []):
        if slot.material is not None:
            return slot.material

    return None


def file_mtime(filepath):
    """
    Helper for file modification time.
    """
    try:
        p = bpy.path.abspath(filepath)
        if p and os.path.exists(p):
            return int(os.path.getmtime(p))
    except Exception:
        pass
    return None
