import bpy, os, bmesh
from bpy.types import Object
from mathutils import Vector, Matrix
from math import radians
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


def get_selected_verts_world_pos(obj: bpy.types.Object) -> list[Vector]:
    """
    Get world positions of selected vertices.
    """
    if not obj.type == "MESH":
        return []

    if bpy.context.mode == "EDIT_MESH":
        obj.update_from_editmode()
        mesh = obj.data
        bm = bmesh.new()

        bm.from_mesh(mesh, face_normals=False, vertex_normals=False)
        verts_world_pos = []

        for vert in bm.verts:
            if not vert.select:
                continue
            world_pos = obj.matrix_world @ vert.co
            verts_world_pos.append(world_pos)

        bm.free()
        return verts_world_pos
    elif bpy.context.mode == "OBJECT":
        mesh = obj.data
        bm = bmesh.new()
        bm.from_mesh(mesh, face_normals=False, vertex_normals=False)
        verts_world_pos = []
        for vert in bm.verts:
            world_pos = obj.matrix_world @ vert.co
            verts_world_pos.append(world_pos)
        bm.free()
        return verts_world_pos
    else:
        return []


def get_verts_bbox(verts_world_pos: list[Vector]) -> tuple[float, Vector]:
    """
    Calculate world bounding box of vertices.
    """
    min_coord = Vector((float("inf"), float("inf"), float("inf")))
    max_coord = Vector((float("-inf"), float("-inf"), float("-inf")))

    for world_pos in verts_world_pos:
        min_coord = Vector(
            (
                min(min_coord.x, world_pos.x),
                min(min_coord.y, world_pos.y),
                min(min_coord.z, world_pos.z),
            )
        )
        max_coord = Vector(
            (
                max(max_coord.x, world_pos.x),
                max(max_coord.y, world_pos.y),
                max(max_coord.z, world_pos.z),
            )
        )

    center = (min_coord + max_coord) / 2
    scale = (max_coord - min_coord) / 2

    return center, scale
