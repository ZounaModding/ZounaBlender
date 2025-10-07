from ..generic.mesh import Mesh, Vertex, Face
from ..bff.io import MeshV1291_03_06PCBody, MeshV1291_03_06_PC
from ..common.mesh import decode_vertex_buffer
from ..common.resource import load_dependencies


class MeshV1_291_03_06_PC:
    file_path: str
    mesh: MeshV1291_03_06_PC

    def __init__(self, mesh: MeshV1291_03_06_PC = None):
        if mesh is not None:
            self.mesh = mesh.mesh_v1_291_03_06_pc
            self.file_path = mesh.file_path
            print(f"self.file_path: {self.file_path}")

    def to_generic(self) -> Mesh:
        body: MeshV1291_03_06PCBody = self.mesh.body
        gm = Mesh()

        generic_materials = load_dependencies(self.file_path, list(body.material_names))
        for material in generic_materials:
            if material is not None:
                print(f"{material.file_name!r} ->", str(material.name))
            else:
                print(f"material was not found")

        gm.file_path = self.file_path
        gm.file_name = str(self.mesh.name)
        gm.name = str(self.mesh.link_name)
        gm.b_box = self.mesh.link_header.b_box
        gm.b_sphere = self.mesh.link_header.b_sphere
        gm.data_name = str(self.mesh.link_header.data_name)
        gm.fade_out_dist = self.mesh.link_header.fade_out_dist
        gm.flags = self.mesh.link_header.flags
        gm.materials = list(generic_materials)

        gm.col_spheres = list(body.sphere_cols)
        gm.col_boxes = list(body.box_cols)
        gm.col_cylindres = list(body.cylindre_cols)

        idx_buf_schema = body.mesh_buffers.index_buffers[0]
        tris = idx_buf_schema.tris

        vbuf = body.mesh_buffers.vertex_buffers[0]

        pos_chunk, norm_chunk, uv_chunk, luv_chunk = decode_vertex_buffer(vbuf)

        gm.positions = pos_chunk
        gm.normals = norm_chunk
        gm.uvs = uv_chunk
        gm.luvs = luv_chunk

        gm.faces = []

        prim_infos = body.mesh_buffers.vertex_groups
        for i, prim in enumerate(prim_infos):
            start = prim.index_buffer_index_begin // 3
            face_ct = prim.face_count

            for t in range(face_ct):
                tri = tris[start + t]
                o0, o1, o2 = tri
                verts = [
                    Vertex(
                        position_id=o0,
                        normal_id=o0,
                        uv_id=o0,
                        luv_id=(o0 if luv_chunk else None),
                    ),
                    Vertex(
                        position_id=o1,
                        normal_id=o1,
                        uv_id=o1,
                        luv_id=(o1 if luv_chunk else None),
                    ),
                    Vertex(
                        position_id=o2,
                        normal_id=o2,
                        uv_id=o2,
                        luv_id=(o2 if luv_chunk else None),
                    ),
                ]
                gm.faces.append(Face(vertices=verts, material_id=i))

        return gm
