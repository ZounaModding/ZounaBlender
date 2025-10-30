from .resource_panel import register_panel, unregister_panel
from .material import register_material, unregister_material
from .mesh import register_mesh, unregister_mesh
from .util import register_util, unregister_util


def register_ui():
    register_util()
    register_material()
    register_mesh()
    register_panel()


def unregister_ui():
    unregister_panel()
    unregister_mesh()
    unregister_material()
    unregister_util()
