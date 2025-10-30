import os
from ...common.constants import BmFormat, BmTransp, PalFormat
from .resource import Resource
from ...common.util import read_dds_mipmap_count, read_dds_fourcc

from pathlib import Path
import bpy
import json


class Bitmap(Resource):
    width: int = 0
    height: int = 0
    format: BmFormat = BmFormat.BM_8888
    palette_format: PalFormat = PalFormat.PAL_8888
    transp_format: BmTransp = BmTransp.BM_NO_TRANSP
    precalculated_size: int = 0
    mip_count: int = 0

    def setup_zouna_bitmap(self, dds_path):
        try:
            image = bpy.data.images.load(str(dds_path))
        except RuntimeError as e:
            print(f"Failed to load DDS {dds_path}: {e}")
            return None

        image.name = self.name or dds_path.stem
        print(f"Image name {image.name}")
        image.is_zouna = True
        image.zouna_bitmap.init_resource(self)
        image.zouna_bitmap.transp_format = self.transp_format.name

        return image

    @staticmethod
    def from_blender(blender_image):
        """
        Construct a Bitmap from a bpy.types.Image, reading the raw file data
        from the image's linked filepath.
        """
        if blender_image is None:
            return None

        bitmap = Bitmap()

        image_path_str = blender_image.filepath_raw
        if not image_path_str:
            print(
                f"Error: Blender image '{blender_image.name}' has no linked file path."
            )
            return None

        image_path = Path(bpy.path.abspath(image_path_str))

        base_name, extension = os.path.splitext(blender_image.name)
        bitmap.name = base_name
        bitmap.file_name = base_name

        try:
            with open(image_path, "rb") as f:
                bitmap.data = f.read()

        except FileNotFoundError:
            print(f"Error: Raw image file not found at {image_path}")
            bitmap.data = b""
        except Exception as e:
            print(f"Error reading raw file data for {blender_image.name}: {e}")
            bitmap.data = b""

        bitmap.data_ext = "dds"
        bitmap.precalculated_size = len(bitmap.data) if bitmap.data else 0

        w, h = blender_image.size
        bitmap.width = w
        bitmap.height = h

        if bitmap.data:
            mipmap_count = read_dds_mipmap_count(bitmap.data)
            if mipmap_count > 0:
                bitmap.mip_count = mipmap_count - 1
            else:
                bitmap.mip_count = 0

            fourcc = read_dds_fourcc(bitmap.data)

            if fourcc == "DXT5":
                bitmap.format = BmFormat.BM_8888
                # TODO: This can be other but for now it's fine
                bitmap.transp_format = BmTransp.BM_NO_TRANSP
            elif fourcc == "DXT1":
                bitmap.format = BmFormat.BM_888
                bitmap.transp_format = BmTransp.BM_NO_TRANSP
            else:
                bitmap.format = BmFormat.BM_8888

        else:
            bitmap.mip_count = 0
            bitmap.format = BmFormat.BM_8888

        bitmap.palette_format = PalFormat.PAL_8888

        return bitmap

    def to_blender(self):
        """
        Loads the DDS file located in the same folder as self.file_path/resource.json
        into a Blender image datablock.
        """
        resource_dir = Path(self.file_path).parent
        dds_path = resource_dir / "data.dds"

        if not dds_path.is_file():
            msg = f"Bitmap type not supported or missing DDS: {dds_path}"
            self._error(msg)
            print(msg)
            return None

        image = self.setup_zouna_bitmap(dds_path)

        return image
