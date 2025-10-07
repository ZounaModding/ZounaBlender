from ...common.constants import BmTransp
from ..bff.io import (
    BitmapV106_63_02PCBody,
    BitmapV106_63_02_PC,
    AnimationV1291_03_06PCLinkHeader,
)
from ..generic.bitmap import Bitmap


class BitmapV1_06_63_02_PC:
    file_path: str
    bitmap: BitmapV106_63_02_PC

    def __init__(self, bitmap: BitmapV106_63_02_PC = None):
        if bitmap is not None:
            self.bitmap = bitmap.bitmap_v1_06_63_02_pc
            self.file_path = bitmap.file_path
            print(f"self.file_path: {self.file_path}")

    @staticmethod
    def from_generic(generic_bitmap: Bitmap):
        """
        Convert a generic Bitmap into a BitmapV1_06_63_02_PC instance,
        using the proper constructor for both body and container.
        """
        if generic_bitmap is None:
            return None

        body = BitmapV106_63_02PCBody(
            flag=0,
            format=getattr(generic_bitmap, "format", 12),
            format_copy=getattr(generic_bitmap, "format", 12),
            four=0,
            height=getattr(generic_bitmap, "height", 0),
            mipmap_count=getattr(generic_bitmap, "mip_count", 1),
            palette_format=0,
            precalculated_size=0,
            transp_format=getattr(
                generic_bitmap, "transp_format", BmTransp.BM_NO_TRANSP
            ),
            width=getattr(generic_bitmap, "width", 0),
        )

        link_header = AnimationV1291_03_06PCLinkHeader(
            link_name=generic_bitmap.name or "", names=[], links=[]
        )

        versioned_bitmap = BitmapV106_63_02_PC(
            body=body,
            class_name="Bitmap_Z",
            link_header=link_header,
            link_name=None,
            name=generic_bitmap.file_name or "",
        )

        bmp = BitmapV1_06_63_02_PC()
        bmp.file_path = generic_bitmap.file_path
        bmp.bitmap = versioned_bitmap

        return bmp

    def to_generic(self) -> Bitmap:
        body: BitmapV106_63_02PCBody = self.bitmap.body
        generic_bitmap = Bitmap()

        generic_bitmap.file_path = self.file_path
        generic_bitmap.file_name = str(self.bitmap.name)
        generic_bitmap.name = str(self.bitmap.link_header.link_name)
        generic_bitmap.transp_format = BmTransp(body.transp_format)

        return generic_bitmap
