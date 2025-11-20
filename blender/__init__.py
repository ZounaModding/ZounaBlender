import bpy
import traceback
from bpy.app.handlers import persistent

from .classes import register_classes, unregister_classes
from .shared import register_shared, unregister_shared
from ..common.constants import (
    Game,
    supported_games_for_platform,
    supported_platforms_for_game,
)
from ..zouna.bff.io import Platform


def matrices_are_close(mat1, mat2, tol=1e-6):
    """Compare two matrices with tolerance."""
    for i in range(4):
        for j in range(4):
            if abs(mat1[i][j] - mat2[i][j]) > tol:
                return False
    return True


LAST_VIEW_MATRIX = {}


def update_envmap_uv(obj, region3d):
    """
    Compute per-corner reflection-derived debug UVs using existing split (loop) normals.
    """
    mesh = obj.data

    attr = mesh.attributes.get("envmap_uv")
    if attr is None:
        attr = mesh.attributes.new(
            name="envmap_uv", type="FLOAT_VECTOR", domain="CORNER"
        )
    else:
        if (
            attr.domain != "CORNER"
            or attr.data_type != "FLOAT_VECTOR"
            or len(attr.data) != len(mesh.loops)
        ):
            try:
                mesh.attributes.remove(attr)
            except Exception:
                pass
            attr = mesh.attributes.new(
                name="envmap_uv", type="FLOAT_VECTOR", domain="CORNER"
            )

    attr_data = mesh.attributes["envmap_uv"].data

    # Equivalent to shader's EYE_LOCAL: viewport camera position in object-local space
    cam_world = region3d.view_matrix.inverted().translation
    eye_local = obj.matrix_world.inverted() @ cam_world

    for loop_index, loop in enumerate(mesh.loops):
        v_idx = loop.vertex_index
        pos = mesh.vertices[v_idx].co

        n = loop.normal
        n = n.normalized()

        eye_vec = eye_local - pos
        eye_vec = eye_vec.normalized()

        reflect = 2.0 * n.dot(eye_vec) * n - eye_vec

        u = reflect.x * 0.5 + 0.5
        v = reflect.y * 0.5 + 0.5

        attr_data[loop_index].vector = (u, v, v)

    mesh.update()


handler_ref = None


def viewport_update():
    """
    Called every redraw of the 3D view; only updates if camera moved.
    """
    # print(f"Viewport update called")
    for area in bpy.context.window.screen.areas:
        if area.type != "VIEW_3D":
            continue
        for space in area.spaces:
            if space.type != "VIEW_3D":
                continue
            region3d = space.region_3d
            region_id = id(region3d)

            current_matrix = region3d.view_matrix.copy()
            last_matrix = LAST_VIEW_MATRIX.get(region_id)

            if last_matrix is not None and matrices_are_close(
                current_matrix, last_matrix
            ):
                continue

            LAST_VIEW_MATRIX[region_id] = current_matrix
            # print(f"Viewport update called 2")
            for obj in bpy.context.scene.objects:
                if obj.type != "MESH" or obj.mode != "OBJECT":
                    continue
                mat = obj.active_material
                if mat and mat.is_zouna:
                    update_envmap_uv(obj, region3d)


def register_draw_handler():
    global handler_ref
    if handler_ref is None:
        handler_ref = bpy.types.SpaceView3D.draw_handler_add(
            viewport_update, (), "WINDOW", "POST_VIEW"
        )


def unregister_draw_handler():
    global handler_ref
    if handler_ref is not None:
        bpy.types.SpaceView3D.draw_handler_remove(handler_ref, "WINDOW")
        handler_ref = None


game_items = [(g.value, g.value, g.value) for g in Game]

platform_items = [(p.value, p.value, p.value) for p in Platform]


def update_game(scene, context):
    try:
        game = Game(scene.zouna_game)

        plats = supported_platforms_for_game(game)
        if not plats:
            first_plat = list(Platform)[0]
            if scene.zouna_platform != first_plat.name:
                scene.zouna_platform = first_plat.name
            return

        current_platform = Platform(scene.zouna_platform)
        if current_platform not in plats:
            scene.zouna_platform = plats[0].name
    except Exception:
        traceback.print_exc()


def update_platform(scene, context):
    try:
        current_game = Game(scene.zouna_game)
        selected_platform = Platform(scene.zouna_platform)
        valid_platforms = supported_platforms_for_game(current_game)

        prev_platform_value = scene.zouna_prev_platform

        if selected_platform in valid_platforms:
            scene.zouna_prev_platform = selected_platform.value
            return

        bpy.ops.zouna.show_warning(
            "INVOKE_DEFAULT",
            message=f"'{selected_platform.value}' is not supported for '{current_game.value}'.",
        )

        fallback_value = None
        if prev_platform_value and any(
            p.value == prev_platform_value for p in valid_platforms
        ):
            fallback_value = prev_platform_value
        elif valid_platforms:
            fallback_value = valid_platforms[0].value

        if fallback_value and scene.zouna_platform != fallback_value:
            scene.zouna_platform = fallback_value
            scene.zouna_prev_platform = fallback_value
        else:
            bpy.ops.zouna.show_warning(
                "INVOKE_DEFAULT",
                message=f"No valid platform available for '{current_game.value}'. Keeping current selection.",
            )

    except Exception:
        traceback.print_exc()


def update_envmap_toggle(scene, context):
    """
    Update callback for the BoolProperty on the Scene.
    'scene' here is the bpy.types.Scene instance whose property changed.
    """
    try:
        if scene.zouna_envmap_toggle:
            register_draw_handler()
        else:
            unregister_draw_handler()
    except Exception:
        traceback.print_exc()


@persistent
def zouna_on_load_post(dummy):
    """After a file is loaded, check scenes and register handler if needed."""
    try:
        for s in bpy.data.scenes:
            if getattr(s, "zouna_envmap_toggle", False):
                register_draw_handler()
                break
    except Exception:
        traceback.print_exc()


def register_blender():
    if not hasattr(bpy.types.Scene, "zouna_envmap_toggle"):
        bpy.types.Scene.zouna_envmap_toggle = bpy.props.BoolProperty(
            name="Render with Envmap",
            description="(Expensive) Properly renders reflections for Envmap testing",
            default=False,
            update=update_envmap_toggle,
        )
    if not hasattr(bpy.types.Scene, "zouna_game"):
        bpy.types.Scene.zouna_game = bpy.props.EnumProperty(
            name="Game",
            description="Select the game to export for",
            items=game_items,
            default=Game.RATATOUILLE,
            update=update_game,
        )
    if not hasattr(bpy.types.Scene, "zouna_platform"):
        bpy.types.Scene.zouna_platform = bpy.props.EnumProperty(
            name="Platform",
            description="Select the platform to export for",
            items=platform_items,
            default=Platform.PC.value,
            update=update_platform,
        )
    if not hasattr(bpy.types.Scene, "zouna_prev_platform"):
        bpy.types.Scene.zouna_prev_platform = bpy.props.StringProperty(
            name="Previous Platform",
            description="Stores last valid platform for game",
            default="",
            options={"HIDDEN"},
        )
    register_shared()
    register_classes()

    if zouna_on_load_post not in bpy.app.handlers.load_post:
        bpy.app.handlers.load_post.append(zouna_on_load_post)


def unregister_blender():
    try:
        unregister_draw_handler()
    except Exception:
        traceback.print_exc()
    unregister_classes()
    unregister_shared()
    for prop_name in (
        "zouna_envmap_toggle",
        "zouna_game",
        "zouna_platform",
        "zouna_prev_platform",
    ):
        if hasattr(bpy.types.Scene, prop_name):
            try:
                delattr(bpy.types.Scene, prop_name)
            except Exception:
                traceback.print_exc()
