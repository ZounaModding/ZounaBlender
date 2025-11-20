import bmesh
import bpy
from mathutils import Vector, Matrix

from ...common.constants import (
    collision_flag_to_rat_surface_type,
    collision_flag_to_rat_sound_type,
)
from ...blender.shared.collision import add_collision_dummy_under_obj
from ...common.constants import (
    ColPrimitiveCategory,
    ColPrimitiveType,
    rat_values_to_collision_flag,
    export_collision_name,
)
from ..bff.io import SphereCol, BoxCol, CylindreCol, Box, Sphere, Cylindre, Segment

COL_NAME_HASHES = {
    -2060499066: "DURL",
    1584874963: "DUR",
    -320555891: "DUR_ADD",
    -792408287: "DURL+METAL",
    79534474: "DURL+TERRE",
    -1644635630: "DURL+WATER",
    294492196: "DURL+BOIS",
    85066795: "SHADOW",
    1356414537: "LOD",
    -1530038390: "COLLECT",
    1939328761: "COLLECTABLE",
    -755234770: "STRENGTH",
    -278048728: "KICK",
    -65458158: "NFADE",
    -289060822: "FADE",
    592079238: "ACTION",
    -112942011: "MAGNET",
    898187702: "INTER",
    -787325161: "REPULSE",
}

NAME_TO_CATEGORY = {
    "SHADOW": ColPrimitiveCategory.SHADOW.name,
    "LOD": ColPrimitiveCategory.LOD.name,
    "COLLECT": ColPrimitiveCategory.COLLECT.name,
    "COLLECTABLE": ColPrimitiveCategory.COLLECTABLE.name,
    "STRENGTH": ColPrimitiveCategory.STRENGTH.name,
    "KICK": ColPrimitiveCategory.KICK.name,
    "FADE": ColPrimitiveCategory.FADE.name,
    "NFADE": ColPrimitiveCategory.NFADE.name,
    "ACTION": ColPrimitiveCategory.ACTION.name,
    "MAGNET": ColPrimitiveCategory.MAGNET.name,
    "INTER": ColPrimitiveCategory.INTER.name,
    "REPULSE": ColPrimitiveCategory.REPULSE.name,
    "DURL": ColPrimitiveCategory.COLLIDER.name,
    "DUR": ColPrimitiveCategory.COLLIDER.name,
    "DUR_ADD": ColPrimitiveCategory.COLLIDER.name,
    "DURL+METAL": ColPrimitiveCategory.COLLIDER.name,
    "DURL+TERRE": ColPrimitiveCategory.COLLIDER.name,
    "DURL+WATER": ColPrimitiveCategory.COLLIDER.name,
    "DURL+BOIS": ColPrimitiveCategory.COLLIDER.name,
}


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


def import_sphere_collision(parent_obj, sph, index):
    dummy = add_collision_dummy_under_obj(ColPrimitiveType.SPHERE, parent_obj)
    dummy.name = f"Zouna Collision Primitive"
    dummy.is_zouna = True

    zp = dummy.zouna_property
    zp.col_primitive_type = ColPrimitiveType.SPHERE.name

    center = Vector(sph.col_sph.center)
    radius = sph.col_sph.radius

    dummy.location = xyz_zouna_to_blender(center)
    dummy.scale = Vector((radius, radius, radius))

    apply_collision_metadata(dummy, sph)
    return dummy


def import_box_collision(parent_obj, box, index):
    dummy = add_collision_dummy_under_obj(ColPrimitiveType.BOX, parent_obj)
    dummy.name = f"{parent_obj.name}_col_box_{index}"
    dummy.is_zouna = True

    zp = dummy.zouna_property
    zp.col_primitive_type = ColPrimitiveType.BOX.name

    b = box.col_box

    m = b.matrix
    t = Vector((m[0][3], m[1][3], m[2][3]))
    dummy.location = xyz_zouna_to_blender(t)

    R_store = Matrix(
        (
            (m[0][0], m[0][1], m[0][2]),
            (m[1][0], m[1][1], m[1][2]),
            (m[2][0], m[2][1], m[2][2]),
        )
    )

    R_z = R_store.transposed()
    B_z2b = Matrix(
        (
            (1, 0, 0),
            (0, 0, -1),
            (0, 1, 0),
        )
    )
    B_b2z = B_z2b.transposed()

    R_bl = B_z2b @ R_z @ B_z2b.transposed()

    dummy.rotation_euler = R_bl.to_euler()

    sx, sy, sz = b.vec
    dummy.scale = Vector((sx, sz, sy))

    apply_collision_metadata(dummy, box)
    return dummy


def import_cylinder_collision(parent_obj, cyl, index):
    """
    Zouna Cylindre → Blender dummy.
    Blender cylinder uses +Z as height axis.
    """

    dummy = add_collision_dummy_under_obj(ColPrimitiveType.CYLINDER, parent_obj)
    dummy.name = f"{parent_obj.name}_col_cyl_{index}"
    dummy.is_zouna = True

    zp = dummy.zouna_property
    zp.col_primitive_type = ColPrimitiveType.CYLINDER.name

    cyl_data = cyl.col_cylindre
    seg = cyl_data.seg

    origin_z = Vector(seg.origin)
    dir_z = Vector(seg.direction)
    length = float(seg.length)
    radius = float(cyl_data.radius)

    if dir_z.length_squared == 0.0:
        dir_z = Vector((0, 1, 0))
    dir_z.normalize()

    origin_b = xyz_zouna_to_blender(origin_z)
    dir_b = xyz_zouna_to_blender(dir_z)
    dir_b.normalize()

    half_h = length * 0.5
    center_b = origin_b + dir_b * half_h
    dummy.location = center_b

    dummy.scale = Vector((radius, radius, half_h))

    up = Vector((0, 0, 1))

    if dir_b.length_squared == 0.0:
        R = Matrix.Identity(3)
    else:
        dir_b.normalize()

        if (up - dir_b).length < 1e-6:
            R = Matrix.Identity(3)
        elif (up + dir_b).length < 1e-6:
            R = Matrix.Rotation(3.141592653589793, 3, "X")
        else:
            axis = up.cross(dir_b)
            axis.normalize()
            angle = up.angle(dir_b)
            R = Matrix.Rotation(angle, 3, axis)

    dummy.rotation_euler = R.to_euler()

    apply_collision_metadata(dummy, cyl)
    return dummy


def export_sphere_collision(child):
    """Convert a sphere collision dummy (EMPTY) into a SphereCol."""

    loc_zn = xyz_blender_to_zouna(child.location)

    radius = child.scale.x

    sphere = Sphere(center=[loc_zn.x, loc_zn.y, loc_zn.z], radius=radius)

    return SphereCol(
        col_sph=sphere,
        flag=rat_values_to_collision_flag(
            child.zouna_property.rat_surface_type,
            child.zouna_property.rat_sound_type,
            child.zouna_property.rat_footprints_while_on,
            child.zouna_property.rat_footprints_while_off,
        ),
        name=export_collision_name(
            child.zouna_property.col_primitive_category,
        ),
    )


def export_box_collision(child):
    center_bl = child.location
    center_zn = xyz_blender_to_zouna(center_bl)

    R_bl = child.matrix_world.to_quaternion().to_matrix()

    B_z2b = Matrix(
        (
            (1, 0, 0),
            (0, 0, -1),
            (0, 1, 0),
        )
    )
    B_b2z = Matrix(
        (
            (1, 0, 0),
            (0, 0, 1),
            (0, -1, 0),
        )
    )

    R_z = B_b2z @ R_bl @ B_z2b
    R_store = R_z.transposed()

    sx_b, sy_b, sz_b = child.scale

    sx = sx_b
    sy = sz_b
    sz = sy_b
    vec = [sx, sy, sz]

    scale = max(sx, sy, sz)

    matrix = [
        [R_store[0][0], R_store[0][1], R_store[0][2], center_zn.x],
        [R_store[1][0], R_store[1][1], R_store[1][2], center_zn.y],
        [R_store[2][0], R_store[2][1], R_store[2][2], center_zn.z],
    ]

    box = Box(matrix=matrix, scale=scale, vec=vec)

    return BoxCol(
        col_box=box,
        flag=rat_values_to_collision_flag(
            child.zouna_property.rat_surface_type,
            child.zouna_property.rat_sound_type,
            child.zouna_property.rat_footprints_while_on,
            child.zouna_property.rat_footprints_while_off,
        ),
        name=export_collision_name(child.zouna_property.col_primitive_category),
    )


def export_cylinder_collision(child):
    """
    Blender cylinder dummy → Zouna Cylindre.
    Blender convention:
        axis        = local +Z
        scale.x     = radius
        scale.y     = radius
        scale.z     = half-height
        center      = location
    """

    center_b = child.location
    center_z = xyz_blender_to_zouna(center_b)

    m3 = child.matrix_world.to_3x3()
    axis_local_z = Vector((0, 0, 1))
    dir_b = m3 @ axis_local_z

    if dir_b.length_squared == 0.0:
        dir_b = Vector((0, 0, 1))
    dir_b.normalize()

    dir_z = xyz_blender_to_zouna(dir_b)
    dir_z.normalize()

    radius = float(child.scale.x)
    half_h = float(child.scale.z)
    height = half_h * 2.0

    origin_z = center_z - dir_z * half_h

    seg = Segment(
        origin=[origin_z.x, origin_z.y, origin_z.z],
        direction=[dir_z.x, dir_z.y, dir_z.z],
        pad=0.0,
        length=height,
    )

    cyl_struct = Cylindre(radius=radius, seg=seg)

    return CylindreCol(
        col_cylindre=cyl_struct,
        flag=rat_values_to_collision_flag(
            child.zouna_property.rat_surface_type,
            child.zouna_property.rat_sound_type,
            child.zouna_property.rat_footprints_while_on,
            child.zouna_property.rat_footprints_while_off,
        ),
        name=export_collision_name(child.zouna_property.col_primitive_category),
    )


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


def resolve_collision_name(raw):
    """Return name string whether raw is int hash or already a string."""
    if isinstance(raw, int):
        return COL_NAME_HASHES.get(raw, None)
    elif isinstance(raw, str):
        return raw
    return None


def apply_collision_metadata(dummy, col_data):
    zp = dummy.zouna_property

    flag = int(col_data.flag)
    zp.rat_surface_type = collision_flag_to_rat_surface_type(flag)
    zp.rat_sound_type = collision_flag_to_rat_sound_type(flag)

    resolved = resolve_collision_name(col_data.name)

    if resolved:
        for key, enum_name in NAME_TO_CATEGORY.items():
            if key == resolved or key in resolved:
                zp.col_primitive_category = enum_name
                break
        else:
            zp.col_primitive_category = ColPrimitiveCategory.COLLIDER.name
    else:
        zp.col_primitive_category = ColPrimitiveCategory.COLLIDER.name
    dummy.name = f"Zouna Collision Primitive ({zp.col_primitive_category})"
