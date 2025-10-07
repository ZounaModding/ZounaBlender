import bpy
from bpy.types import PropertyGroup, Image
from bpy.utils import register_class, unregister_class

from .resource import ZounaResourceProperty
from ...common.constants import BmTransp
from ..handlers import make_handler
from ...zouna.v1_06_63_02_pc.bitmap import BitmapV1_06_63_02_PC
from ...zouna.v1_291_03_06_pc.bitmap import BitmapV1_291_03_06_PC
from ...zouna.bff.io import Platform

transp_formats = [
    (BmTransp.BM_NO_TRANSP.name, "NoTransp", "Does not support transparency"),
    (BmTransp.BM_TRANSP_ONE.name, "TranspOne", "Supports full opacity or zero opacity"),
    (BmTransp.BM_TRANSP.name, "Transp", "Supports transparency"),
]


class ZounaBitmapProperty(ZounaResourceProperty):
    transp_format: bpy.props.EnumProperty(
        name="Transparency format",
        description="The image associated with this texture",
        items=transp_formats,
        default=BmTransp.BM_NO_TRANSP.name,
    )


bitmap_classes = [ZounaBitmapProperty]


def register_bitmap():
    for cls in bitmap_classes:
        register_class(cls)

    Image.is_zouna = bpy.props.BoolProperty()
    Image.zouna_bitmap = bpy.props.PointerProperty(type=ZounaBitmapProperty)


def unregister_bitmap():
    for cls in reversed(bitmap_classes):
        unregister_class(cls)


bitmap_versions = [
    (
        BitmapV1_06_63_02_PC,
        Platform.PC,
        "v1.06.63.02 - Asobo Studio - Internal Cross Technology",
        "bitmap",
    ),
    (
        BitmapV1_291_03_06_PC,
        Platform.PC,
        "v1.291.03.06 - Asobo Studio - Internal Cross Technology",
        "bitmap",
    ),
]


def initialize_bitmap_handlers():
    for version_class, platform, version_str, member_name in bitmap_versions:
        make_handler(version_class, platform, version_str, member_name)
