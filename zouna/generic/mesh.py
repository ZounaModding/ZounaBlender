from ..bff.io import SphereCol, BoxCol, CylindreCol
from ..common.mesh import (
    add_collision_obj,
    create_box,
    create_cylinder,
    create_sphere,
    xyz_zouna_to_blender,
    normal_byte_to_float,
)
from .material import Material
from .object import Object

import bpy
from mathutils import Vector, Matrix
from dataclasses import dataclass


@dataclass
class Vertex:
    position_id: int
    normal_id: int
    uv_id: int
    luv_id: int | None = None


@dataclass
class Face:
    vertices: list[Vertex]
    material_id: int


class Mesh(Object):
    positions: list[list[float]]
    normals: list[list[float]]
    uvs: list[list[float]]
    luvs: list[list[float]]
    materials: list[Material]
    faces: list[Face]
    col_spheres: list[SphereCol]
    col_boxes: list[BoxCol]
    col_cylindres: list[CylindreCol]

    @staticmethod
    def from_blender(blender_mesh):
        mesh = Mesh()
        # load data from blender mesh
        return mesh

    def to_blender(self):
        """
        Import self.positions, self.faces, self.uvs, self.luvs, self.normals
        into a new Blender Mesh without using bmesh.
        """

        def pos_tuple(pid):
            return (
                tuple(self.positions[pid])
                if (self.positions and 0 <= pid < len(self.positions))
                else None
            )

        def norm_tuple(nid):
            return (
                tuple(self.normals[nid])
                if (nid is not None and self.normals and 0 <= nid < len(self.normals))
                else None
            )

        def uv_tuple(uid):
            return (
                tuple(self.uvs[uid])
                if (uid is not None and self.uvs and 0 <= uid < len(self.uvs))
                else None
            )

        def luv_tuple(lid):
            return (
                tuple(self.luvs[lid])
                if (lid is not None and self.luvs and 0 <= lid < len(self.luvs))
                else None
            )

        pos_map = {}
        verts = []

        def ensure_pos_index(pid):
            p = pos_tuple(pid)
            if p is None:
                key = (0.0, 0.0, 0.0)
            else:
                key = tuple(p)
            idx = pos_map.get(key)
            if idx is None:
                idx = len(verts)
                pos_map[key] = idx
                verts.append(xyz_zouna_to_blender(Vector(key)))
            return idx

        faces_idx = []
        face_loop_attrs = []
        face_materials = []

        for face in self.faces:
            pos_ids = [v.position_id for v in face.vertices]
            if len(set(pos_ids)) != len(pos_ids):
                continue

            local_pos_idxs = [ensure_pos_index(v.position_id) for v in face.vertices]

            faces_idx.append([local_pos_idxs[2], local_pos_idxs[1], local_pos_idxs[0]])

            corner_attrs = []
            for v in face.vertices:
                corner_attrs.append(
                    (
                        uv_tuple(v.uv_id),
                        luv_tuple(v.luv_id),
                        norm_tuple(v.normal_id),
                    )
                )
            face_loop_attrs.append([corner_attrs[2], corner_attrs[1], corner_attrs[0]])
            face_materials.append(face.material_id)

        mesh = bpy.data.meshes.new(self.name)
        for m in getattr(self, "materials", []) or []:
            if m is not None:
                mesh.materials.append(m.to_blender())

        mesh.from_pydata(verts, [], faces_idx)

        uv_layer = None
        luv_layer = None
        if self.uvs:
            uv_layer = mesh.uv_layers.new(name="UVMap")
        if self.luvs:
            luv_layer = mesh.uv_layers.new(name="LightmapUV")

        for poly in mesh.polygons:
            poly.material_index = face_materials[poly.index]
            loop_attrs = face_loop_attrs[poly.index]

            for li, attrs in zip(poly.loop_indices, loop_attrs):
                uv, luv, norm = attrs
                if uv and uv_layer:
                    uv_layer.data[li].uv = (uv[0], 1.0 - uv[1])
                if luv and luv_layer:
                    luv_layer.data[li].uv = (luv[0], 1.0 - luv[1])

        if self.normals:
            loop_normals = []
            for poly_attrs in face_loop_attrs:
                for uv, luv, norm in poly_attrs:
                    if norm is not None:
                        n_vec = normal_byte_to_float(Vector(norm))
                        loop_normals.append(xyz_zouna_to_blender(n_vec))
                    else:
                        loop_normals.append(Vector((0.0, 0.0, 1.0)))

            if len(loop_normals) == len(mesh.loops):
                mesh.normals_split_custom_set(loop_normals)
            else:
                pass

        if uv_layer:
            try:
                mesh.calc_tangents()
            except Exception:
                pass

        mesh.validate(clean_customdata=False)
        mesh.update()

        obj = bpy.data.objects.new(self.name, mesh)
        bpy.context.collection.objects.link(obj)

        for i, sph in enumerate(getattr(self, "col_spheres", [])):
            radius = sph.col_sph.radius
            add_collision_obj(obj, sph, f"col_sphere_{i}", create_sphere, radius)

        for i, box in enumerate(getattr(self, "col_boxes", [])):
            add_collision_obj(obj, box, f"col_box_{i}", create_box, box)

        for i, cyl in enumerate(getattr(self, "col_cylindres", [])):
            radius = cyl.col_cylindre.radius
            height = cyl.col_cylindre.seg.length
            add_collision_obj(obj, cyl, f"col_cyl_{i}", create_cylinder, radius, height)

        return obj
