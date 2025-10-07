from .blender import register_blender, unregister_blender
from .ui import register_ui, unregister_ui


def register():
    register_blender()
    register_ui()
    return


def unregister():
    unregister_ui()
    unregister_blender()
    return


if __name__ == "__main__":
    register()
