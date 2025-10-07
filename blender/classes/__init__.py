from .bitmap import register_bitmap, unregister_bitmap
from .material import (
    register_material,
    unregister_material,
    initialize_material_handlers,
)
from .mesh import initialize_mesh_handlers
from .bitmap import initialize_bitmap_handlers
from ..handlers import _handlers


def register_classes():
    _handlers.clear()
    register_bitmap()
    register_material()

    initialize_bitmap_handlers()
    initialize_material_handlers()
    initialize_mesh_handlers()


def unregister_classes():
    unregister_material()
    unregister_bitmap()
