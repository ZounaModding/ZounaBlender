from math import sqrt
from ..bff.io import SphereCol, BoxCol, CylindreCol, Box, Sphere
from ..common.mesh import (
    add_collision_obj,
    create_box,
    create_cylinder,
    create_sphere,
    xyz_zouna_to_blender,
    xyz_blender_to_zouna,
    normal_byte_to_float,
    normal_float_to_byte,
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
        mesh.name = blender_mesh.name
        mesh.data_name = (
            ""  # TODO: Actually support mesh data. Placeholder, can be set as needed
        )
        mesh.fade_out_dist = 0.0  # TODO: Set fade out distance if needed
        mesh.flags = 4193840  # TODO: Set proper mesh flags
        temp_mesh = blender_mesh.data.copy()

        mesh.positions = []
        mesh.normals = []
        mesh.uvs = []
        mesh.luvs = []
        mesh.materials = []
        mesh.faces = []

        pos_map = {}
        norm_map = {}
        uv_map = {}
        luv_map = {}

        temp_mesh.calc_loop_triangles()

        main_uv_layer = None
        if temp_mesh.uv_layers:
            main_uv_layer = temp_mesh.uv_layers[0]
        light_uv_layer = temp_mesh.uv_layers.get("LightmapUV")

        for mat_slot in blender_mesh.material_slots:
            zouna_mat = (
                Material.from_blender(mat_slot.material)
                if mat_slot.material
                else Material()
            )
            mesh.materials.append(zouna_mat)

        for tri_poly in temp_mesh.loop_triangles:
            face_vertices = []

            for loop_idx in tri_poly.loops:
                loop = temp_mesh.loops[loop_idx]
                vert = temp_mesh.vertices[loop.vertex_index]

                pos_zouna = xyz_blender_to_zouna(vert.co)
                pos_key = tuple(pos_zouna)
                if pos_key not in pos_map:
                    pos_map[pos_key] = len(mesh.positions)
                    mesh.positions.append(list(pos_zouna))
                position_id = pos_map[pos_key]

                norm_blender = Vector(loop.normal).normalized()
                norm_zouna_float = xyz_blender_to_zouna(norm_blender)
                norm_bytes_list = normal_float_to_byte(norm_zouna_float)
                norm_key = tuple(norm_bytes_list)
                if norm_key not in norm_map:
                    norm_map[norm_key] = len(mesh.normals)
                    mesh.normals.append(list(norm_bytes_list))
                normal_id = norm_map[norm_key]

                uv_id = None
                if main_uv_layer:
                    uv_data = main_uv_layer.data[loop_idx].uv
                    uv_zouna = (uv_data[0], 1.0 - uv_data[1])
                    uv_key = uv_zouna
                    if uv_key not in uv_map:
                        uv_map[uv_key] = len(mesh.uvs)
                        mesh.uvs.append(list(uv_key))
                    uv_id = uv_map[uv_key]

                luv_id = None
                if light_uv_layer:
                    luv_data = light_uv_layer.data[loop_idx].uv
                    luv_zouna = (luv_data[0], 1.0 - luv_data[1])
                    luv_key = luv_zouna
                    if luv_key not in luv_map:
                        luv_map[luv_key] = len(mesh.luvs)
                        mesh.luvs.append(list(luv_key))
                    luv_id = luv_map[luv_key]

                face_vertices.append(
                    Vertex(
                        position_id=position_id,
                        normal_id=normal_id,
                        uv_id=uv_id,
                        luv_id=luv_id,
                    )
                )

            mesh.faces.append(
                Face(vertices=face_vertices[::-1], material_id=tri_poly.material_index)
            )

        bpy.data.meshes.remove(temp_mesh)

        final_positions = mesh.positions
        if final_positions:
            min_x = min(p[0] for p in final_positions)
            min_y = min(p[1] for p in final_positions)
            min_z = min(p[2] for p in final_positions)

            max_x = max(p[0] for p in final_positions)
            max_y = max(p[1] for p in final_positions)
            max_z = max(p[2] for p in final_positions)

            center_x = (min_x + max_x) / 2.0
            center_y = (min_y + max_y) / 2.0
            center_z = (min_z + max_z) / 2.0

            half_extent_x = (max_x - min_x) / 2.0
            half_extent_y = (max_y - min_y) / 2.0
            half_extent_z = (max_z - min_z) / 2.0

            max_radius_sq = 0.0
            for p in final_positions:
                dx = p[0] - center_x
                dy = p[1] - center_y
                dz = p[2] - center_z
                max_radius_sq = max(max_radius_sq, dx * dx + dy * dy + dz * dz)

            radius = sqrt(max_radius_sq)

            mesh.b_sphere = Sphere(
                center=[center_x, center_y, center_z],
                radius=radius,
            )
            mesh.b_box = Box(
                matrix=[
                    [1.0, 0.0, 0.0, center_x],
                    [0.0, 1.0, 0.0, center_y],
                    [0.0, 0.0, 1.0, center_z],
                ],
                scale=max(half_extent_x, half_extent_y, half_extent_z),
                vec=[half_extent_x, half_extent_y, half_extent_z],
            )
        else:
            mesh.b_sphere = Sphere(
                center=[0.0, 0.0, 0.0],
                radius=1.0,
            )
            mesh.b_box = Box(
                matrix=[
                    [1.0, 0.0, 0.0, 0.0],
                    [0.0, 1.0, 0.0, 0.0],
                    [0.0, 0.0, 1.0, 0.0],
                ],
                scale=1.0,
                vec=[1.0, 1.0, 1.0],
            )

        mesh.col_spheres = []
        mesh.col_boxes = []
        mesh.col_cylindres = []

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
        for mat in self.materials:
            if mat is not None:
                mesh.materials.append(mat.to_blender())

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

        # TODO: Fix this code using gizmos (MSFS2024) and support AABBCol

        for i, sph in enumerate(self.col_spheres):
            radius = sph.col_sph.radius
            add_collision_obj(obj, sph, f"col_sphere_{i}", create_sphere, radius)

        for i, box in enumerate(self.col_boxes):
            add_collision_obj(obj, box, f"col_box_{i}", create_box, box)

        for i, cyl in enumerate(self.col_cylindres):
            radius = cyl.col_cylindre.radius
            height = cyl.col_cylindre.seg.length
            add_collision_obj(obj, cyl, f"col_cyl_{i}", create_cylinder, radius, height)

        return obj
