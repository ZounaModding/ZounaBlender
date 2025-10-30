import bpy, os
import struct


def get_material_from_context(context: bpy.types.Context):
    """
    Return the active Zouna material or None.
    """
    obj = context.object
    if obj is None:
        return None

    if obj.active_material is not None:
        return obj.active_material

    for slot in obj.material_slots:
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


def safe_int(val):
    try:
        return int(val)
    except (ValueError, TypeError):
        return val


def read_dds_mipmap_count(data: bytes) -> int:
    """
    Reads the mipmap count from the raw DDS header data.
    Returns 1 if reading fails or no mipmaps are specified.
    """
    MIPMAP_COUNT_OFFSET = 28
    DDS_HEADER_SIZE = 128

    if len(data) < DDS_HEADER_SIZE:
        raise Exception("DDS data is too short to contain a valid header.")
    count_bytes = data[MIPMAP_COUNT_OFFSET : MIPMAP_COUNT_OFFSET + 4]

    try:
        mip_count = struct.unpack("<I", count_bytes)[0]

        return max(0, mip_count)

    except struct.error:
        raise Exception("DDS data is too short to contain a valid header.")


def read_dds_fourcc(data: bytes) -> str:
    FOURCC_OFFSET = 84
    try:
        return data[FOURCC_OFFSET : FOURCC_OFFSET + 4].decode("ascii")
    except:
        return ""
