import bmesh
import bpy
from mathutils import Vector, Matrix


def xyz_zouna_to_blender(v: Vector) -> Vector:
    return Vector((v.x, -v.z, v.y))


def xyz_blender_to_zouna(v: Vector) -> Vector:
    return Vector((v.x, v.z, -v.y))


def decode_vertex_buffer(vbuf) -> tuple[
    list[list[float]],
    list[list[float]],
    list[list[float]],
    list[list[float]],
]:
    verts = vbuf.vertices

    if verts.layout_position is not None:
        elems = verts.layout_position
        pos = [e.position[:] for e in elems]
        return pos, [], [], []
    if verts.layout_position_uv is not None:
        elems = verts.layout_position_uv
        pos = [e.position[:] for e in elems]
        uv = [e.uv[:] for e in elems]
        return pos, [], uv, []
    if verts.layout_no_blend is not None:
        elems = verts.layout_no_blend
        pos = [e.position[:] for e in elems]
        norm = [e.normal[:] for e in elems]
        uv = [e.uv[:] for e in elems]
        return pos, norm, uv, []
    if verts.layout1_blend is not None:
        elems = verts.layout1_blend
        pos = [e.position[:] for e in elems]
        norm = [e.normal[:] for e in elems]
        uv = [e.uv[:] for e in elems]
        return pos, norm, uv, []
    if verts.layout4_blend is not None:
        elems = verts.layout4_blend
        pos = [e.position[:] for e in elems]
        norm = [e.normal[:] for e in elems]
        uv = [e.uv[:] for e in elems]
        return pos, norm, uv, []

    raise RuntimeError("Unknown vertex layout")


def float_to_byte(num):
    return round(((num + 1) / 2) * 255)


def byte_to_float(num):
    return ((num / 255) * 2) - 1


def normal_byte_to_float(vec):
    return Vector((byte_to_float(vec.z), byte_to_float(vec.y), byte_to_float(vec.x)))


def normal_float_to_byte(vec):
    return [float_to_byte(vec.z), float_to_byte(vec.y), float_to_byte(vec.x)]


def create_box(name, box):
    """
    Create a box mesh from a box.col_box structure.

    box.col_box must have:
    - matrix: 3x4 list of floats (row-major)
    - vec: tuple or Vector of 3 floats representing scale (x, y, z)
    """

    sign_combos = [
        (+1, +1, +1),
        (+1, +1, -1),
        (-1, +1, -1),
        (-1, +1, +1),
        (+1, -1, +1),
        (+1, -1, -1),
        (-1, -1, -1),
        (-1, -1, +1),
    ]

    sx, sy, sz = box.col_box.vec

    m = box.col_box.matrix
    t = Vector((m[0][3], m[1][3], m[2][3]))
    m = Matrix(
        [
            [m[0][0], m[0][1], m[0][2]],
            [m[1][0], m[1][1], m[1][2]],
            [m[2][0], m[2][1], m[2][2]],
        ]
    )
    m.transpose()

    corners = []
    for sx_sign, sy_sign, sz_sign in sign_combos:
        dx = sx_sign * sx
        dy = sy_sign * sy
        dz = sz_sign * sz

        v = Vector((dx, dy, dz))
        pos = m @ v + t

        corners.append(xyz_zouna_to_blender(pos))

    bm = bmesh.new()
    verts = [bm.verts.new(c) for c in corners]
    bm.verts.ensure_lookup_table()

    faces_idx = [
        (0, 1, 2, 3),  # top
        (4, 5, 6, 7),  # bottom
        (0, 1, 5, 4),  # front
        (2, 3, 7, 6),  # back
        (0, 3, 7, 4),  # left
        (1, 2, 6, 5),  # right
    ]
    for f in faces_idx:
        bm.faces.new([verts[i] for i in f])

    mesh = bpy.data.meshes.new(name)
    bm.to_mesh(mesh)
    bm.free()
    return mesh


def create_sphere(name, radius=1, segments=16, rings=8):
    bm = bmesh.new()
    bmesh.ops.create_uvsphere(bm, u_segments=segments, v_segments=rings, radius=radius)
    mesh = bpy.data.meshes.new(name)
    bm.to_mesh(mesh)
    bm.free()
    return mesh


def create_cylinder(name, radius=1, depth=2, vertices=16):
    bm = bmesh.new()
    bmesh.ops.create_circle(bm, segments=vertices, radius=radius)
    ret = bmesh.ops.extrude_edge_only(bm, edges=bm.edges)
    verts_extrude = [ele for ele in ret["geom"] if isinstance(ele, bmesh.types.BMVert)]
    bmesh.ops.translate(bm, verts=verts_extrude, vec=Vector((0, 0, depth)))
    mesh = bpy.data.meshes.new(name)
    bm.to_mesh(mesh)
    bm.free()
    return mesh


def add_collision_obj(parent, col_obj, name, create_func, *args):
    col_mesh = create_func(name, *args)
    col_obj_blender = bpy.data.objects.new(name, col_mesh)
    col_obj_blender.parent = parent

    if hasattr(col_obj, "col_sph"):
        center = col_obj.col_sph.center
    elif hasattr(col_obj, "col_cylindre"):
        center = col_obj.col_cylindre.seg.origin
    else:
        center = (0, 0, 0)

    col_obj_blender.location = Vector((center[0], center[2], center[1]))
    bpy.context.collection.objects.link(col_obj_blender)
