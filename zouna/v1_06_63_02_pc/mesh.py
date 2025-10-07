from ..generic.mesh import Mesh, Vertex, Face
from ..bff.io import MeshV106_63_02PCBody, MeshV106_63_02_PC
from ..common.mesh import decode_vertex_buffer
from ..common.resource import load_dependencies


class MeshV1_06_63_02_PC:
    file_path: str
    mesh: MeshV106_63_02_PC

    def __init__(self, mesh: MeshV106_63_02_PC = None):
        if mesh is not None:
            self.mesh = mesh.mesh_v1_06_63_02_pc
            self.file_path = mesh.file_path
            print(f"self.file_path: {self.file_path}")

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
