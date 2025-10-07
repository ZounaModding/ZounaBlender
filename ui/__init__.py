from .resource_panel import register_panel, unregister_panel
from .material import register_material, unregister_material


def register_ui():
    register_material()
    register_panel()


def unregister_ui():
    unregister_panel()
    unregister_material()
