from ...common.constants import BmFormat, BmTransp
from .resource import Resource

from pathlib import Path
import bpy
import json


class Bitmap(Resource):
    width: float = (0.0,)
    height: float = (0.0,)
    format: BmFormat = (BmFormat.BM_8888,)
    transp_format: BmTransp = (BmTransp.BM_NO_TRANSP,)
    mip_count: int

    def setup_zouna_bitmap(self, dds_path):
        try:
            image = bpy.data.images.load(str(dds_path))
        except RuntimeError as e:
            print(f"Failed to load DDS {dds_path}: {e}")
            return None

        image.name = self.name or dds_path.stem
        image.is_zouna = True
        image.zouna_bitmap.init_resource(self)
        image.zouna_bitmap.transp_format = self.transp_format.name

        return image

    @staticmethod
    def from_blender(blender_image):
        """
        Construct a Bitmap from a bpy.types.Image.
        """
        if blender_image is None:
            return None

        bitmap = Bitmap()

        image_path_str = blender_image.filepath
        image_path = Path(image_path_str)
        parent_dir = image_path.parent
        resource_json = parent_dir / "resource.json"
        if resource_json.is_file():
            with open(resource_json, "r", encoding="utf-8") as f:
                data = json.load(f)

            bitmap_data = next(iter(data.get("class", {}).get("Bitmap", {}).values()))
            link_header = bitmap_data.get("link_header", {})
            link_name = link_header.get("link_name")

            bitmap.file_path = str(resource_json)
            bitmap.name = str(link_name)
        else:
            print("Error: no resource json")
            return None

        parent_dir_name = parent_dir.name
        if ".Bitmap" in parent_dir_name:
            bitmap.file_name = parent_dir_name.split(".Bitmap", 1)[0]
        else:
            maybe_container = parent_dir.parent.name
            if ".Bitmap" in maybe_container:
                bitmap.file_name = maybe_container.split(".Bitmap", 1)[0]
            else:
                print("Error: no resource folder")
                return None

        w, h = blender_image.size
        bitmap.width = float(w)
        bitmap.height = float(h)

        bitmap.mip_count = int(getattr(blender_image, "mipmaps", 1) or 1)

        bitmap.format = BmFormat.BM_8888

        if bitmap.transp_format is None:
            channels = (
                blender_image.channels if hasattr(blender_image, "channels") else 4
            )
            bitmap.transp_format = (
                BmTransp.BM_TRANSP if int(channels) >= 4 else BmTransp.BM_NO_TRANSP
            )

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
