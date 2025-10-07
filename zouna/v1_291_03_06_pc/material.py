from ..bff.io import MaterialV1291_03_06PCBody, MaterialV1291_03_06_PC
from ..common.resource import load_dependencies
from ..generic.material import Material


class MaterialV1_291_03_06_PC:
    file_path: str
    material: MaterialV1291_03_06_PC

    def __init__(self, material: MaterialV1291_03_06_PC = None):
        if material is not None:
            self.material = material.material_v1_291_03_06_pc
            self.file_path = material.file_path
            print(f"self.file_path: {self.file_path}")

    def to_generic(self) -> Material:
        body: MaterialV1291_03_06PCBody = self.material.body
        gm = Material()

        gm.file_path = self.file_path
        gm.file_name = str(self.material.name)
        gm.name = str(self.material.link_header.link_name)
        # TODO: Set rest of fields

        return gm
