from collections import defaultdict
from ..generic.mesh import Mesh, Vertex, Face
from ..bff.io import (
    MeshV106_63_02PCBody,
    MeshV106_63_02_PC,
    PrimInfoElement,
    LayoutNoBlendElement,
    MagentaSchema,
    FriskySchema,
    Vertices,
    PurpleMeshBuffers,
    CameraZoneV106_63_02PCLinkHeader,
    AABBCol,
    PurplePoints,
    PurpleMorpher,
    Box,
    Sphere,
    TypeEnum,
)
from ..common.mesh import decode_vertex_buffer
from ..common.resource import load_dependencies, save_dependencies
from ...common.util import safe_int


class MeshV1_06_63_02_PC:
    file_path: str
    mesh: MeshV106_63_02_PC

    def __init__(self, mesh: MeshV106_63_02_PC = None):
        if mesh is not None:
            self.mesh = mesh.mesh_v1_06_63_02_pc
            self.file_path = mesh.file_path
            print(f"self.file_path: {self.file_path}")

    @staticmethod
    def from_generic(generic_mesh: Mesh):
        """
        Converts a generic Mesh object into the specific MeshV106_63_02_PC format structure.

        It handles material-based vertex grouping, PrimInfo generation, LayoutNoBlend
        population, and material dependency saving.
        """

        faces_by_material = defaultdict(list)
        for face in generic_mesh.faces:
            faces_by_material[face.material_id].append(face)

        final_normals: list[list[int]] = []
        final_uvs: list[list[float]] = []
        final_luvs: list[list[float]] = []
        final_all_tris: list[list[int]] = []
        final_prim_infos: list[PrimInfoElement] = []
        final_layout_no_blend: list[LayoutNoBlendElement] = []

        current_vertex_offset = 0
        index_buffer_offset_in_shorts = 0

        for mat_id in sorted(faces_by_material.keys()):
            faces = faces_by_material[mat_id]

            vertex_map = {}
            material_vertices_data: list[
                tuple[list[float], list[int], list[float], list[float]]
            ] = []

            for face in faces:
                local_face_indices = []

                for v in face.vertices:
                    key = (
                        v.position_id,
                        v.normal_id if v.normal_id is not None else -1,
                        v.uv_id if v.uv_id is not None else -1,
                        v.luv_id if v.luv_id is not None else -1,
                    )

                    if key not in vertex_map:
                        new_local_index = len(material_vertices_data)
                        vertex_map[key] = new_local_index
                        local_face_indices.append(new_local_index)

                        pos = generic_mesh.positions[v.position_id]
                        norm = (
                            generic_mesh.normals[v.normal_id]
                            if v.normal_id is not None
                            else [0, 0, 0]
                        )
                        uv = (
                            generic_mesh.uvs[v.uv_id]
                            if v.uv_id is not None
                            else [0.0, 0.0]
                        )
                        luv = (
                            generic_mesh.luvs[v.luv_id]
                            if v.luv_id is not None
                            else [0.0, 0.0]
                        )

                        material_vertices_data.append((pos, norm, uv, luv))
                    else:
                        local_face_indices.append(vertex_map[key])

                final_all_tris.append(
                    [idx + current_vertex_offset for idx in local_face_indices]
                )

            material_vertex_count = len(material_vertices_data)

            prim = PrimInfoElement(
                face_count=len(faces),
                index_buffer_offset_in_shorts=index_buffer_offset_in_shorts,
                placeholder_pointers=[0, 0, 0],
                prim_type=4,
                shader_type=0,
                unused0=52685,
                unused1=3452816845,
                vertex_buffer_offset=current_vertex_offset,
                vertex_buffer_range_begin=current_vertex_offset,
                vertex_count=material_vertex_count,
                vertex_size=36,
            )
            final_prim_infos.append(prim)

            for pos, norm, uv, luv in material_vertices_data:
                final_normals.append(norm)
                final_uvs.append(uv)

                luv_out = luv if luv is not None else [0.0, 0.0]
                if luv is not None:
                    final_luvs.append(luv)

                # TODO: Support other vertex types
                element = LayoutNoBlendElement(
                    luv=luv_out,
                    normal=norm,
                    normal_w=0,
                    position=pos,
                    tangent=[0, 0, 0],
                    tangent_w=0,
                    uv=uv,
                )
                final_layout_no_blend.append(element)

            current_vertex_offset += material_vertex_count
            index_buffer_offset_in_shorts += len(faces) * 3

        dependencies_to_save = [
            mat for mat in generic_mesh.materials if mat is not None
        ]
        material_names = save_dependencies(generic_mesh.file_path, dependencies_to_save)

        index_buffer = [MagentaSchema(tris=final_all_tris)]
        vertices_container = Vertices(
            layout_position=None,
            layout_position_uv=None,
            layout_no_blend=final_layout_no_blend,
            layout1_blend=None,
            layout4_blend=None,
            layout_unknown=None,
        )
        vertex_buffers = [FriskySchema(vertices=vertices_container)]
        mesh_buffers = PurpleMeshBuffers(
            index_buffers=index_buffer,
            prim_infos=final_prim_infos,
            vertex_buffers=vertex_buffers,
        )
        link_header = CameraZoneV106_63_02PCLinkHeader(
            b_box=generic_mesh.b_box,
            b_sphere=generic_mesh.b_sphere,
            data_name=generic_mesh.data_name,
            fade_out_dist=generic_mesh.fade_out_dist,
            flags=generic_mesh.flags,
            link_name=safe_int(generic_mesh.name),
            names=material_names,  # Use saved keys
            type=TypeEnum.MESH,
        )
        body = MeshV106_63_02PCBody(
            aabb_col=AABBCol(
                collision_aabb_nodes=[], collision_faces=[]
            ),  # TODO: Implement
            aabb_vertices=[],
            box_cols=generic_mesh.col_boxes,
            cylindre_cols=generic_mesh.col_cylindres,
            sphere_cols=generic_mesh.col_spheres,
            strips=[],
            unk6=None,  # TODO: should be saved as null
            unk_uints=[i for i in range(len(final_prim_infos))],
            unused4_s=[],
            points=PurplePoints(
                morpher=PurpleMorpher(morph_target_descs=[], morpher_relateds=[]),
                positions=[],
                tb_vtxs=[],
            ),
            related_to_counts=[0, 0, 0],  # placeholder
            shadow_related=0,  # placeholder
            zero2=0,
            drawing_cutoff_distance=0.0,
            drawing_start_distance=0.0,
            material_names=material_names,
            mesh_buffers=mesh_buffers,
            normal_count=0,
            normals=[],
            uv_count=0,
            uvs=[],
        )
        mesh_pc_structure = MeshV106_63_02_PC(
            body=body,
            class_name="Mesh_Z",
            link_header=link_header,
            link_name=safe_int(generic_mesh.name),
            name=safe_int(generic_mesh.file_name),
        )
        mesh_pc = MeshV1_06_63_02_PC()
        mesh_pc.file_path = generic_mesh.file_path
        mesh_pc.mesh = mesh_pc_structure
        return mesh_pc

    def to_generic(self) -> Mesh:
        body: MeshV106_63_02PCBody = self.mesh.body
        generic_mesh = Mesh()

        generic_materials = load_dependencies(self.file_path, list(body.material_names))
        for material in generic_materials:
            if material is not None:
                print(f"{material.file_name!r} ->", str(material.name))
            else:
                print(f"material was not found")

        generic_mesh.file_path = self.file_path
        generic_mesh.file_name = str(self.mesh.name)
        generic_mesh.name = str(self.mesh.link_header.link_name)
        generic_mesh.b_box = self.mesh.link_header.b_box
        generic_mesh.b_sphere = self.mesh.link_header.b_sphere
        generic_mesh.data_name = str(self.mesh.link_header.data_name)
        generic_mesh.fade_out_dist = self.mesh.link_header.fade_out_dist
        generic_mesh.flags = self.mesh.link_header.flags
        generic_mesh.materials = list(generic_materials)

        generic_mesh.col_spheres = list(body.sphere_cols)
        generic_mesh.col_boxes = list(body.box_cols)
        generic_mesh.col_cylindres = list(body.cylindre_cols)

        tris = body.mesh_buffers.index_buffers[0].tris
        vbuf = body.mesh_buffers.vertex_buffers[0]
        pos_chunk, norm_chunk, uv_chunk, luv_chunk = decode_vertex_buffer(vbuf)

        generic_mesh.positions = [list(pos) for pos in pos_chunk] if pos_chunk else []
        generic_mesh.normals = [list(norm) for norm in norm_chunk] if norm_chunk else []
        generic_mesh.uvs = [list(uv) for uv in uv_chunk] if uv_chunk else []
        generic_mesh.luvs = [list(luv) for luv in luv_chunk] if luv_chunk else []

        generic_mesh.faces = []
        prim_infos = body.mesh_buffers.prim_infos

        for mat_id, prim in enumerate(prim_infos):
            start = prim.index_buffer_offset_in_shorts // 3
            for i in range(prim.face_count):
                tri = tris[start + i]
                face_verts = []

                for offset in tri:
                    vert = Vertex(
                        position_id=offset,
                        normal_id=(offset if norm_chunk else None),
                        uv_id=(offset if uv_chunk else None),
                        luv_id=(offset if luv_chunk else None),
                    )
                    face_verts.append(vert)

                generic_mesh.faces.append(Face(vertices=face_verts, material_id=mat_id))

        return generic_mesh
