from .resource_panel import register_panel, unregister_panel
from .material import register_material, unregister_material
from .mesh import register_mesh, unregister_mesh
from .collision import register_collision, unregister_collision
from .util import register_util, unregister_util
from .common import register_common_ui, unregister_common_ui


def register_ui():
    register_util()
    register_common_ui()
    register_material()
    register_mesh()
    register_panel()
    register_collision()


def unregister_ui():
    unregister_collision()
    unregister_panel()
    unregister_mesh()
    unregister_material()
    unregister_common_ui()
    unregister_util()
