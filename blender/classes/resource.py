import bpy
from bpy.types import PropertyGroup


class ZounaResourceProperty(PropertyGroup):
    file_path: bpy.props.StringProperty(
        name="File Path",
        description="File path of the resource on disk",
        subtype="NONE",
        default="",
    )
    file_name: bpy.props.StringProperty(
        name="File Name_Z",
        description="Name/Crc32 of the file",
        subtype="NONE",
        default="DefaultFileName",
    )
    name: bpy.props.StringProperty(
        name="Resource Name_Z",
        description="Name/Crc32 of the resource",
        subtype="NONE",
        default="DefaultName",
    )

    def init_resource(self, resource):
        self.file_path = resource.file_path
        self.file_name = resource.file_name
        self.name = resource.name
