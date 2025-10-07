from ..bff.io import BitmapV1291_03_06PCBody, BitmapV1291_03_06_PC
from ..generic.bitmap import Bitmap


class BitmapV1_291_03_06_PC:
    file_path: str
    bitmap: BitmapV1291_03_06_PC

    def __init__(self, bitmap: BitmapV1291_03_06_PC = None):
        if bitmap is not None:
            self.bitmap = bitmap.bitmap_v1_291_03_06_pc
            self.file_path = bitmap.file_path
            print(f"self.file_path: {self.file_path}")

    def to_generic(self) -> Bitmap:
        body: BitmapV1291_03_06PCBody = self.bitmap.body
        gb = Bitmap()

        gb.file_path = self.file_path
        gb.file_name = str(self.bitmap.name)
        gb.name = str(self.bitmap.link_header.link_name)
        # TODO: Set rest of fields

        return gb
