from .object import register_object, unregister_object
from .collision import register_collision, unregister_collision


def register_shared():
    register_object()
    register_collision()


def unregister_shared():
    unregister_collision()
    unregister_object()
