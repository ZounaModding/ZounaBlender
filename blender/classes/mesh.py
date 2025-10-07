from ..handlers import make_handler
from ...zouna.v1_06_63_02_pc.mesh import MeshV1_06_63_02_PC
from ...zouna.v1_291_03_06_pc.mesh import MeshV1_291_03_06_PC
from ...zouna.bff.io import Platform

mesh_versions = [
    (
        MeshV1_06_63_02_PC,
        Platform.PC,
        "v1.06.63.02 - Asobo Studio - Internal Cross Technology",
        "mesh",
    ),
    (
        MeshV1_291_03_06_PC,
        Platform.PC,
        "v1.291.03.06 - Asobo Studio - Internal Cross Technology",
        "mesh",
    ),
]


def initialize_mesh_handlers():
    for version_class, platform, version_str, member_name in mesh_versions:
        make_handler(version_class, platform, version_str, member_name)
