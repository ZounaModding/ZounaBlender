from .sound_dropdown import register_sound_dropdown, unregister_sound_dropdown


def register_common_ui():
    register_sound_dropdown()


def unregister_common_ui():
    unregister_sound_dropdown()
