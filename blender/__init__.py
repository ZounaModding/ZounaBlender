from .classes import register_classes, unregister_classes
import bpy


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

            for obj in bpy.context.scene.objects:
                if obj.type != "MESH" or obj.mode != "OBJECT":
                    continue
                mat = obj.active_material
                if mat and getattr(mat, "is_zouna", False):
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


def register_blender():
    register_classes()
    register_draw_handler()


def unregister_blender():
    unregister_classes()
    unregister_draw_handler()
