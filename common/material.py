from .constants import (
    ZounaShaderNodeNames,
    ZounaShaderNodeTypes,
)

import bpy


def create_zouna_material_node_tree(mat):
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links

    for n in list(nodes):
        nodes.remove(n)

    out_node = nodes.new(type=ZounaShaderNodeTypes.OutputMaterial)
    out_node.name = ZounaShaderNodeNames.OutputMaterial
    out_node.location = (640, 25)

    bsdf_diff = nodes.new(type=ZounaShaderNodeTypes.BsdfDiffuse)
    bsdf_diff.name = ZounaShaderNodeNames.BsdfDiffuse
    bsdf_diff.location = (400, 0)

    # --- Diffuse texture ---

    base_color_source = None
    diffuse_alpha = None
    if mat.zouna_material.diffuse:
        diffuse_tex_node = nodes.new(type=ZounaShaderNodeTypes.DiffuseTexture)
        diffuse_tex_node.name = ZounaShaderNodeNames.DiffuseTexture
        diffuse_tex_node.location = (-800, -80)
        diffuse_tex_node.image = mat.zouna_material.diffuse
        diffuse_tex_node.image.colorspace_settings.name = "sRGB"

        diffuse_color_node = nodes.new(ZounaShaderNodeTypes.DiffuseColor)
        diffuse_color_node.name = ZounaShaderNodeNames.DiffuseColor
        diffuse_color_node.location = (-75, 10)
        diffuse_color_node.blend_type = "MULTIPLY"
        diffuse_color_node.inputs["Fac"].default_value = 1.0
        diffuse_color_node.inputs["Color2"].default_value = (
            mat.zouna_material.diffuse_color
        )

        links.new(
            diffuse_tex_node.outputs["Color"], diffuse_color_node.inputs["Color1"]
        )

        base_color_source = diffuse_color_node.outputs["Color"]
        diffuse_alpha = diffuse_tex_node.outputs["Alpha"]
    else:
        bsdf_diff.inputs["Color"].default_value = mat.zouna_material.diffuse_color

    if base_color_source is not None:
        links.new(base_color_source, bsdf_diff.inputs["Color"])

    # --- Envmap texture ---
    if mat.zouna_material.envmap:
        envmap_tex_node = nodes.new(ZounaShaderNodeTypes.EnvmapTexture)
        envmap_tex_node.name = ZounaShaderNodeNames.EnvmapTexture
        envmap_tex_node.location = (-805, -495)
        envmap_tex_node.image = mat.zouna_material.envmap
        envmap_tex_node.image.colorspace_settings.name = "sRGB"

        envmap_uv_node = nodes.new(type=ZounaShaderNodeTypes.EnvmapUV)
        envmap_uv_node.name = ZounaShaderNodeNames.EnvmapUV
        envmap_uv_node.location = (-1025, -695)
        envmap_uv_node.attribute_name = "envmap_uv"

        envmap_curve_node = nodes.new(type=ZounaShaderNodeTypes.EnvmapCurve)
        envmap_curve_node.name = ZounaShaderNodeNames.EnvmapCurve
        envmap_curve_node.location = (-445, -445)
        envmap_curve_c = envmap_curve_node.mapping.curves[3]
        envmap_curve_c.points[0].location = (0.00, 0.00)
        envmap_curve_c.points[1].location = (0.02, 0.25)
        envmap_curve_node.inputs["Fac"].default_value = 0.1

        links.new(envmap_uv_node.outputs["Vector"], envmap_tex_node.inputs["Vector"])
        links.new(envmap_tex_node.outputs["Color"], envmap_curve_node.inputs["Color"])
        envmap_color = envmap_curve_node.outputs["Color"]

        if diffuse_alpha and mat.zouna_material.env_alpha_mask:
            envmap_alpha_mask_node = nodes.new(
                type=ZounaShaderNodeTypes.EnvmapAlphaMask
            )
            envmap_alpha_mask_node.name = ZounaShaderNodeNames.EnvmapAlphaMask
            envmap_alpha_mask_node.location = (-80, -275)
            envmap_alpha_mask_node.operation = "MULTIPLY"

            links.new(diffuse_alpha, envmap_alpha_mask_node.inputs[0])
            links.new(envmap_color, envmap_alpha_mask_node.inputs[1])

            envmap_color = envmap_alpha_mask_node.outputs[0]

        add_diffuse_envmap_node = nodes.new(type=ZounaShaderNodeTypes.AddDiffuseEnvmap)
        add_diffuse_envmap_node.name = ZounaShaderNodeNames.AddDiffuseEnvmap
        add_diffuse_envmap_node.location = (170, -25)
        add_diffuse_envmap_node.blend_type = "ADD"
        add_diffuse_envmap_node.inputs["Fac"].default_value = 1.0

        if base_color_source is not None:
            links.new(base_color_source, add_diffuse_envmap_node.inputs["Color1"])
        else:
            add_diffuse_envmap_node.inputs["Color1"].default_value = (
                mat.zouna_material.diffuse_color
            )

        links.new(envmap_color, add_diffuse_envmap_node.inputs["Color2"])
        links.new(add_diffuse_envmap_node.outputs["Color"], bsdf_diff.inputs["Color"])

    # --- Normal texture ---
    if mat.zouna_material.normal:
        # Not implemented
        pass

    # --- Specular texture ---
    if mat.zouna_material.specular:
        # Not implemented
        pass

    if mat.zouna_material.diffuse_color[3] < 1.0:
        mat.blend_method = "BLEND"
        try:
            col = bsdf_diff.inputs["Color"].default_value
            bsdf_diff.inputs["Color"].default_value = (
                col[0],
                col[1],
                col[2],
                mat.zouna_material.diffuse_color[3],
            )
        except Exception:
            pass

    links.new(bsdf_diff.outputs["BSDF"], out_node.inputs["Surface"])

    return mat
