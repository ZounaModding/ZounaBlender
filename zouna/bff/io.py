from enum import Enum


def from_int(x):
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_float(x):
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def to_float(x):
    assert isinstance(x, (int, float))
    return x


def from_list(f, x):
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_enum(c, x):
    assert isinstance(x, c)
    return x.value


def to_class(c, x):
    assert isinstance(x, c)
    return x.to_dict()


def from_str(x):
    assert isinstance(x, str)
    return x


import traceback


def from_union(fs, x):
    errors = []
    for f in fs:
        try:
            return f(x)
        except Exception as e:
            tb = traceback.format_exc()
            errors.append(
                f"Function {f.__name__ if hasattr(f, '__name__') else str(f)} failed:\n{tb}"
            )
    raise ValueError(
        f"All from_union parsers failed for input: {repr(x)}\n\n" + "\n".join(errors)
    )


def from_none(x):
    assert x is None
    return x


def from_dict(f, x):
    assert isinstance(x, dict)
    return {k: f(v) for (k, v) in x.items()}


class InterpolationType(Enum):
    LINEAR = "Linear"
    SMOOTH = "Smooth"
    SQUARE = "Square"
    UNKNOWN17 = "Unknown17"
    UNKNOWN4 = "Unknown4"
    UNKNOWN8 = "Unknown8"


class KeyframerFloatComp0Keyframe:
    def __init__(self, tangent_in, tangent_out, time, value):
        self.tangent_in = tangent_in
        self.tangent_out = tangent_out
        self.time = time
        self.value = value

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        tangent_in = from_int(obj.get("tangent_in"))
        tangent_out = from_int(obj.get("tangent_out"))
        time = from_float(obj.get("time"))
        value = from_int(obj.get("value"))
        return KeyframerFloatComp0Keyframe(tangent_in, tangent_out, time, value)

    def to_dict(self):
        result = {}
        result["tangent_in"] = from_int(self.tangent_in)
        result["tangent_out"] = from_int(self.tangent_out)
        result["time"] = to_float(self.time)
        result["value"] = from_int(self.value)
        return result


class KeyframerFloatComp0:
    def __init__(self, interpolation_type, keyframes):
        self.interpolation_type = interpolation_type
        self.keyframes = keyframes

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        interpolation_type = InterpolationType(obj.get("interpolation_type"))
        keyframes = from_list(
            KeyframerFloatComp0Keyframe.from_dict, obj.get("keyframes")
        )
        return KeyframerFloatComp0(interpolation_type, keyframes)

    def to_dict(self):
        result = {}
        result["interpolation_type"] = to_enum(
            InterpolationType, self.interpolation_type
        )
        result["keyframes"] = from_list(
            lambda x: to_class(KeyframerFloatComp0Keyframe, x), self.keyframes
        )
        return result


class KeyframerVec3Comp0Keyframe:
    def __init__(self, tangent_in, tangent_out, time, value):
        self.tangent_in = tangent_in
        self.tangent_out = tangent_out
        self.time = time
        self.value = value

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        tangent_in = from_list(from_float, obj.get("tangent_in"))
        tangent_out = from_list(from_float, obj.get("tangent_out"))
        time = from_float(obj.get("time"))
        value = from_list(from_float, obj.get("value"))
        return KeyframerVec3Comp0Keyframe(tangent_in, tangent_out, time, value)

    def to_dict(self):
        result = {}
        result["tangent_in"] = from_list(to_float, self.tangent_in)
        result["tangent_out"] = from_list(to_float, self.tangent_out)
        result["time"] = to_float(self.time)
        result["value"] = from_list(to_float, self.value)
        return result


class KeyframerVec3Comp0:
    def __init__(self, interpolation_type, keyframes):
        self.interpolation_type = interpolation_type
        self.keyframes = keyframes

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        interpolation_type = InterpolationType(obj.get("interpolation_type"))
        keyframes = from_list(
            KeyframerVec3Comp0Keyframe.from_dict, obj.get("keyframes")
        )
        return KeyframerVec3Comp0(interpolation_type, keyframes)

    def to_dict(self):
        result = {}
        result["interpolation_type"] = to_enum(
            InterpolationType, self.interpolation_type
        )
        result["keyframes"] = from_list(
            lambda x: to_class(KeyframerVec3Comp0Keyframe, x), self.keyframes
        )
        return result


class AnimationMaterial:
    def __init__(
        self,
        keyframer_float_comp0,
        keyframer_float_comp1,
        keyframer_float_comp2,
        keyframer_vec3_comp0,
        keyframer_vec3_comp1,
    ):
        self.keyframer_float_comp0 = keyframer_float_comp0
        self.keyframer_float_comp1 = keyframer_float_comp1
        self.keyframer_float_comp2 = keyframer_float_comp2
        self.keyframer_vec3_comp0 = keyframer_vec3_comp0
        self.keyframer_vec3_comp1 = keyframer_vec3_comp1

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        keyframer_float_comp0 = KeyframerFloatComp0.from_dict(
            obj.get("keyframer_float_comp0")
        )
        keyframer_float_comp1 = KeyframerFloatComp0.from_dict(
            obj.get("keyframer_float_comp1")
        )
        keyframer_float_comp2 = KeyframerFloatComp0.from_dict(
            obj.get("keyframer_float_comp2")
        )
        keyframer_vec3_comp0 = KeyframerVec3Comp0.from_dict(
            obj.get("keyframer_vec3_comp0")
        )
        keyframer_vec3_comp1 = KeyframerVec3Comp0.from_dict(
            obj.get("keyframer_vec3_comp1")
        )
        return AnimationMaterial(
            keyframer_float_comp0,
            keyframer_float_comp1,
            keyframer_float_comp2,
            keyframer_vec3_comp0,
            keyframer_vec3_comp1,
        )

    def to_dict(self):
        result = {}
        result["keyframer_float_comp0"] = to_class(
            KeyframerFloatComp0, self.keyframer_float_comp0
        )
        result["keyframer_float_comp1"] = to_class(
            KeyframerFloatComp0, self.keyframer_float_comp1
        )
        result["keyframer_float_comp2"] = to_class(
            KeyframerFloatComp0, self.keyframer_float_comp2
        )
        result["keyframer_vec3_comp0"] = to_class(
            KeyframerVec3Comp0, self.keyframer_vec3_comp0
        )
        result["keyframer_vec3_comp1"] = to_class(
            KeyframerVec3Comp0, self.keyframer_vec3_comp1
        )
        return result


class AnimationMaterialModifierElement:
    def __init__(
        self,
        flag,
        keyframer_float_comp0_frame_count,
        keyframer_float_comp0_start_frame,
        keyframer_float_comp1_frame_count,
        keyframer_float_comp1_start_frame,
        keyframer_float_comp2_frame_count,
        keyframer_float_comp2_start_frame,
        keyframer_vec3_comp0_frame_count,
        keyframer_vec3_comp0_start_frame,
        keyframer_vec3_comp1_frame_count,
        keyframer_vec3_comp1_start_frame,
        material_id,
        material_link_name,
    ):
        self.flag = flag
        self.keyframer_float_comp0_frame_count = keyframer_float_comp0_frame_count
        self.keyframer_float_comp0_start_frame = keyframer_float_comp0_start_frame
        self.keyframer_float_comp1_frame_count = keyframer_float_comp1_frame_count
        self.keyframer_float_comp1_start_frame = keyframer_float_comp1_start_frame
        self.keyframer_float_comp2_frame_count = keyframer_float_comp2_frame_count
        self.keyframer_float_comp2_start_frame = keyframer_float_comp2_start_frame
        self.keyframer_vec3_comp0_frame_count = keyframer_vec3_comp0_frame_count
        self.keyframer_vec3_comp0_start_frame = keyframer_vec3_comp0_start_frame
        self.keyframer_vec3_comp1_frame_count = keyframer_vec3_comp1_frame_count
        self.keyframer_vec3_comp1_start_frame = keyframer_vec3_comp1_start_frame
        self.material_id = material_id
        self.material_link_name = material_link_name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        flag = from_int(obj.get("flag"))
        keyframer_float_comp0_frame_count = from_int(
            obj.get("keyframer_float_comp0_frame_count")
        )
        keyframer_float_comp0_start_frame = from_int(
            obj.get("keyframer_float_comp0_start_frame")
        )
        keyframer_float_comp1_frame_count = from_int(
            obj.get("keyframer_float_comp1_frame_count")
        )
        keyframer_float_comp1_start_frame = from_int(
            obj.get("keyframer_float_comp1_start_frame")
        )
        keyframer_float_comp2_frame_count = from_int(
            obj.get("keyframer_float_comp2_frame_count")
        )
        keyframer_float_comp2_start_frame = from_int(
            obj.get("keyframer_float_comp2_start_frame")
        )
        keyframer_vec3_comp0_frame_count = from_int(
            obj.get("keyframer_vec3_comp0_frame_count")
        )
        keyframer_vec3_comp0_start_frame = from_int(
            obj.get("keyframer_vec3_comp0_start_frame")
        )
        keyframer_vec3_comp1_frame_count = from_int(
            obj.get("keyframer_vec3_comp1_frame_count")
        )
        keyframer_vec3_comp1_start_frame = from_int(
            obj.get("keyframer_vec3_comp1_start_frame")
        )
        material_id = from_int(obj.get("material_id"))
        material_link_name = from_union(
            [from_int, from_str], obj.get("material_link_name")
        )
        return AnimationMaterialModifierElement(
            flag,
            keyframer_float_comp0_frame_count,
            keyframer_float_comp0_start_frame,
            keyframer_float_comp1_frame_count,
            keyframer_float_comp1_start_frame,
            keyframer_float_comp2_frame_count,
            keyframer_float_comp2_start_frame,
            keyframer_vec3_comp0_frame_count,
            keyframer_vec3_comp0_start_frame,
            keyframer_vec3_comp1_frame_count,
            keyframer_vec3_comp1_start_frame,
            material_id,
            material_link_name,
        )

    def to_dict(self):
        result = {}
        result["flag"] = from_int(self.flag)
        result["keyframer_float_comp0_frame_count"] = from_int(
            self.keyframer_float_comp0_frame_count
        )
        result["keyframer_float_comp0_start_frame"] = from_int(
            self.keyframer_float_comp0_start_frame
        )
        result["keyframer_float_comp1_frame_count"] = from_int(
            self.keyframer_float_comp1_frame_count
        )
        result["keyframer_float_comp1_start_frame"] = from_int(
            self.keyframer_float_comp1_start_frame
        )
        result["keyframer_float_comp2_frame_count"] = from_int(
            self.keyframer_float_comp2_frame_count
        )
        result["keyframer_float_comp2_start_frame"] = from_int(
            self.keyframer_float_comp2_start_frame
        )
        result["keyframer_vec3_comp0_frame_count"] = from_int(
            self.keyframer_vec3_comp0_frame_count
        )
        result["keyframer_vec3_comp0_start_frame"] = from_int(
            self.keyframer_vec3_comp0_start_frame
        )
        result["keyframer_vec3_comp1_frame_count"] = from_int(
            self.keyframer_vec3_comp1_frame_count
        )
        result["keyframer_vec3_comp1_start_frame"] = from_int(
            self.keyframer_vec3_comp1_start_frame
        )
        result["material_id"] = from_int(self.material_id)
        result["material_link_name"] = from_union(
            [from_int, from_str], self.material_link_name
        )
        return result


class AnimationMesh:
    def __init__(self, keyframer_float_comp):
        self.keyframer_float_comp = keyframer_float_comp

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        keyframer_float_comp = KeyframerFloatComp0.from_dict(
            obj.get("keyframer_float_comp")
        )
        return AnimationMesh(keyframer_float_comp)

    def to_dict(self):
        result = {}
        result["keyframer_float_comp"] = to_class(
            KeyframerFloatComp0, self.keyframer_float_comp
        )
        return result


class AnimationMeshModifierElement:
    def __init__(
        self,
        flag,
        keyframer_float_comp_frame_count,
        keyframer_float_comp_start_frame,
        mesh_id,
        mesh_link_name,
    ):
        self.flag = flag
        self.keyframer_float_comp_frame_count = keyframer_float_comp_frame_count
        self.keyframer_float_comp_start_frame = keyframer_float_comp_start_frame
        self.mesh_id = mesh_id
        self.mesh_link_name = mesh_link_name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        flag = from_int(obj.get("flag"))
        keyframer_float_comp_frame_count = from_int(
            obj.get("keyframer_float_comp_frame_count")
        )
        keyframer_float_comp_start_frame = from_int(
            obj.get("keyframer_float_comp_start_frame")
        )
        mesh_id = from_int(obj.get("mesh_id"))
        mesh_link_name = from_union([from_int, from_str], obj.get("mesh_link_name"))
        return AnimationMeshModifierElement(
            flag,
            keyframer_float_comp_frame_count,
            keyframer_float_comp_start_frame,
            mesh_id,
            mesh_link_name,
        )

    def to_dict(self):
        result = {}
        result["flag"] = from_int(self.flag)
        result["keyframer_float_comp_frame_count"] = from_int(
            self.keyframer_float_comp_frame_count
        )
        result["keyframer_float_comp_start_frame"] = from_int(
            self.keyframer_float_comp_start_frame
        )
        result["mesh_id"] = from_int(self.mesh_id)
        result["mesh_link_name"] = from_union([from_int, from_str], self.mesh_link_name)
        return result


class AnimationMorph:
    def __init__(self, keyframer_float_comp):
        self.keyframer_float_comp = keyframer_float_comp

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        keyframer_float_comp = KeyframerFloatComp0.from_dict(
            obj.get("keyframer_float_comp")
        )
        return AnimationMorph(keyframer_float_comp)

    def to_dict(self):
        result = {}
        result["keyframer_float_comp"] = to_class(
            KeyframerFloatComp0, self.keyframer_float_comp
        )
        return result


class AnimationMorphModifierElement:
    def __init__(
        self,
        flag,
        keyframer_float_comp_frame_count,
        keyframer_float_comp_start_frame,
        mesh_id,
        mesh_link_name,
    ):
        self.flag = flag
        self.keyframer_float_comp_frame_count = keyframer_float_comp_frame_count
        self.keyframer_float_comp_start_frame = keyframer_float_comp_start_frame
        self.mesh_id = mesh_id
        self.mesh_link_name = mesh_link_name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        flag = from_int(obj.get("flag"))
        keyframer_float_comp_frame_count = from_int(
            obj.get("keyframer_float_comp_frame_count")
        )
        keyframer_float_comp_start_frame = from_int(
            obj.get("keyframer_float_comp_start_frame")
        )
        mesh_id = from_int(obj.get("mesh_id"))
        mesh_link_name = from_union([from_int, from_str], obj.get("mesh_link_name"))
        return AnimationMorphModifierElement(
            flag,
            keyframer_float_comp_frame_count,
            keyframer_float_comp_start_frame,
            mesh_id,
            mesh_link_name,
        )

    def to_dict(self):
        result = {}
        result["flag"] = from_int(self.flag)
        result["keyframer_float_comp_frame_count"] = from_int(
            self.keyframer_float_comp_frame_count
        )
        result["keyframer_float_comp_start_frame"] = from_int(
            self.keyframer_float_comp_start_frame
        )
        result["mesh_id"] = from_int(self.mesh_id)
        result["mesh_link_name"] = from_union([from_int, from_str], self.mesh_link_name)
        return result


class KeyframerBezierRot:
    def __init__(self, keyframes):
        self.keyframes = keyframes

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        keyframes = from_list(
            KeyframerVec3Comp0Keyframe.from_dict, obj.get("keyframes")
        )
        return KeyframerBezierRot(keyframes)

    def to_dict(self):
        result = {}
        result["keyframes"] = from_list(
            lambda x: to_class(KeyframerVec3Comp0Keyframe, x), self.keyframes
        )
        return result


class ValueElement:
    def __init__(self, c, message_class, message_name, parameter, reciever_name):
        self.c = c
        self.message_class = message_class
        self.message_name = message_name
        self.parameter = parameter
        self.reciever_name = reciever_name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        c = from_int(obj.get("c"))
        message_class = from_int(obj.get("message_class"))
        message_name = from_union([from_int, from_str], obj.get("message_name"))
        parameter = from_float(obj.get("parameter"))
        reciever_name = from_union([from_int, from_str], obj.get("reciever_name"))
        return ValueElement(c, message_class, message_name, parameter, reciever_name)

    def to_dict(self):
        result = {}
        result["c"] = from_int(self.c)
        result["message_class"] = from_int(self.message_class)
        result["message_name"] = from_union([from_int, from_str], self.message_name)
        result["parameter"] = to_float(self.parameter)
        result["reciever_name"] = from_union([from_int, from_str], self.reciever_name)
        return result


class Unknown30Keyframe:
    def __init__(self, time, value):
        self.time = time
        self.value = value

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        time = from_float(obj.get("time"))
        value = from_list(ValueElement.from_dict, obj.get("value"))
        return Unknown30Keyframe(time, value)

    def to_dict(self):
        result = {}
        result["time"] = to_float(self.time)
        result["value"] = from_list(lambda x: to_class(ValueElement, x), self.value)
        return result


class KeyframerMessage:
    def __init__(self, keyframes):
        self.keyframes = keyframes

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        keyframes = from_list(Unknown30Keyframe.from_dict, obj.get("keyframes"))
        return KeyframerMessage(keyframes)

    def to_dict(self):
        result = {}
        result["keyframes"] = from_list(
            lambda x: to_class(Unknown30Keyframe, x), self.keyframes
        )
        return result


class KeyframerRotKeyframe:
    def __init__(self, time, value):
        self.time = time
        self.value = value

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        time = from_float(obj.get("time"))
        value = from_list(from_float, obj.get("value"))
        return KeyframerRotKeyframe(time, value)

    def to_dict(self):
        result = {}
        result["time"] = to_float(self.time)
        result["value"] = from_list(to_float, self.value)
        return result


class KeyframerRot:
    def __init__(self, keyframes):
        self.keyframes = keyframes

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        keyframes = from_list(KeyframerRotKeyframe.from_dict, obj.get("keyframes"))
        return KeyframerRot(keyframes)

    def to_dict(self):
        result = {}
        result["keyframes"] = from_list(
            lambda x: to_class(KeyframerRotKeyframe, x), self.keyframes
        )
        return result


class AnimationNode:
    def __init__(
        self,
        keyframer_bezier_rot,
        keyframer_message,
        keyframer_rot,
        keyframer_scale,
        keyframer_translation,
        unknown,
    ):
        self.keyframer_bezier_rot = keyframer_bezier_rot
        self.keyframer_message = keyframer_message
        self.keyframer_rot = keyframer_rot
        self.keyframer_scale = keyframer_scale
        self.keyframer_translation = keyframer_translation
        self.unknown = unknown

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        keyframer_bezier_rot = KeyframerBezierRot.from_dict(
            obj.get("keyframer_bezier_rot")
        )
        keyframer_message = KeyframerMessage.from_dict(obj.get("keyframer_message"))
        keyframer_rot = KeyframerRot.from_dict(obj.get("keyframer_rot"))
        keyframer_scale = KeyframerVec3Comp0.from_dict(obj.get("keyframer_scale"))
        keyframer_translation = KeyframerVec3Comp0.from_dict(
            obj.get("keyframer_translation")
        )
        unknown = from_int(obj.get("unknown"))
        return AnimationNode(
            keyframer_bezier_rot,
            keyframer_message,
            keyframer_rot,
            keyframer_scale,
            keyframer_translation,
            unknown,
        )

    def to_dict(self):
        result = {}
        result["keyframer_bezier_rot"] = to_class(
            KeyframerBezierRot, self.keyframer_bezier_rot
        )
        result["keyframer_message"] = to_class(KeyframerMessage, self.keyframer_message)
        result["keyframer_rot"] = to_class(KeyframerRot, self.keyframer_rot)
        result["keyframer_scale"] = to_class(KeyframerVec3Comp0, self.keyframer_scale)
        result["keyframer_translation"] = to_class(
            KeyframerVec3Comp0, self.keyframer_translation
        )
        result["unknown"] = from_int(self.unknown)
        return result


class AnimationNodeModifierElement:
    def __init__(
        self,
        bezier_frame_count,
        bezier_start_frame,
        bone_id,
        bone_name,
        flag,
        message_frame_count,
        message_start_frame,
        rot_frame_count,
        rot_start_frame,
        scale_frame_count,
        scale_start_frame,
        translation_frame_count,
        translation_start_frame,
    ):
        self.bezier_frame_count = bezier_frame_count
        self.bezier_start_frame = bezier_start_frame
        self.bone_id = bone_id
        self.bone_name = bone_name
        self.flag = flag
        self.message_frame_count = message_frame_count
        self.message_start_frame = message_start_frame
        self.rot_frame_count = rot_frame_count
        self.rot_start_frame = rot_start_frame
        self.scale_frame_count = scale_frame_count
        self.scale_start_frame = scale_start_frame
        self.translation_frame_count = translation_frame_count
        self.translation_start_frame = translation_start_frame

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        bezier_frame_count = from_int(obj.get("bezier_frame_count"))
        bezier_start_frame = from_int(obj.get("bezier_start_frame"))
        bone_id = from_int(obj.get("bone_id"))
        bone_name = from_union([from_int, from_str], obj.get("bone_name"))
        flag = from_int(obj.get("flag"))
        message_frame_count = from_int(obj.get("message_frame_count"))
        message_start_frame = from_int(obj.get("message_start_frame"))
        rot_frame_count = from_int(obj.get("rot_frame_count"))
        rot_start_frame = from_int(obj.get("rot_start_frame"))
        scale_frame_count = from_int(obj.get("scale_frame_count"))
        scale_start_frame = from_int(obj.get("scale_start_frame"))
        translation_frame_count = from_int(obj.get("translation_frame_count"))
        translation_start_frame = from_int(obj.get("translation_start_frame"))
        return AnimationNodeModifierElement(
            bezier_frame_count,
            bezier_start_frame,
            bone_id,
            bone_name,
            flag,
            message_frame_count,
            message_start_frame,
            rot_frame_count,
            rot_start_frame,
            scale_frame_count,
            scale_start_frame,
            translation_frame_count,
            translation_start_frame,
        )

    def to_dict(self):
        result = {}
        result["bezier_frame_count"] = from_int(self.bezier_frame_count)
        result["bezier_start_frame"] = from_int(self.bezier_start_frame)
        result["bone_id"] = from_int(self.bone_id)
        result["bone_name"] = from_union([from_int, from_str], self.bone_name)
        result["flag"] = from_int(self.flag)
        result["message_frame_count"] = from_int(self.message_frame_count)
        result["message_start_frame"] = from_int(self.message_start_frame)
        result["rot_frame_count"] = from_int(self.rot_frame_count)
        result["rot_start_frame"] = from_int(self.rot_start_frame)
        result["scale_frame_count"] = from_int(self.scale_frame_count)
        result["scale_start_frame"] = from_int(self.scale_start_frame)
        result["translation_frame_count"] = from_int(self.translation_frame_count)
        result["translation_start_frame"] = from_int(self.translation_start_frame)
        return result


class AnimationV1291_03_06PCBody:
    def __init__(
        self,
        animation_material,
        animation_material_modifiers,
        animation_mesh,
        animation_mesh_modifiers,
        animation_morph,
        animation_morph_modifiers,
        animation_node,
        animation_node_modifiers,
        blending,
        duration,
        unknown,
    ):
        self.animation_material = animation_material
        self.animation_material_modifiers = animation_material_modifiers
        self.animation_mesh = animation_mesh
        self.animation_mesh_modifiers = animation_mesh_modifiers
        self.animation_morph = animation_morph
        self.animation_morph_modifiers = animation_morph_modifiers
        self.animation_node = animation_node
        self.animation_node_modifiers = animation_node_modifiers
        self.blending = blending
        self.duration = duration
        self.unknown = unknown

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        animation_material = AnimationMaterial.from_dict(obj.get("animation_material"))
        animation_material_modifiers = from_list(
            AnimationMaterialModifierElement.from_dict,
            obj.get("animation_material_modifiers"),
        )
        animation_mesh = AnimationMesh.from_dict(obj.get("animation_mesh"))
        animation_mesh_modifiers = from_list(
            AnimationMeshModifierElement.from_dict, obj.get("animation_mesh_modifiers")
        )
        animation_morph = AnimationMorph.from_dict(obj.get("animation_morph"))
        animation_morph_modifiers = from_list(
            AnimationMorphModifierElement.from_dict,
            obj.get("animation_morph_modifiers"),
        )
        animation_node = AnimationNode.from_dict(obj.get("animation_node"))
        animation_node_modifiers = from_list(
            AnimationNodeModifierElement.from_dict, obj.get("animation_node_modifiers")
        )
        blending = from_float(obj.get("blending"))
        duration = from_float(obj.get("duration"))
        unknown = from_int(obj.get("unknown"))
        return AnimationV1291_03_06PCBody(
            animation_material,
            animation_material_modifiers,
            animation_mesh,
            animation_mesh_modifiers,
            animation_morph,
            animation_morph_modifiers,
            animation_node,
            animation_node_modifiers,
            blending,
            duration,
            unknown,
        )

    def to_dict(self):
        result = {}
        result["animation_material"] = to_class(
            AnimationMaterial, self.animation_material
        )
        result["animation_material_modifiers"] = from_list(
            lambda x: to_class(AnimationMaterialModifierElement, x),
            self.animation_material_modifiers,
        )
        result["animation_mesh"] = to_class(AnimationMesh, self.animation_mesh)
        result["animation_mesh_modifiers"] = from_list(
            lambda x: to_class(AnimationMeshModifierElement, x),
            self.animation_mesh_modifiers,
        )
        result["animation_morph"] = to_class(AnimationMorph, self.animation_morph)
        result["animation_morph_modifiers"] = from_list(
            lambda x: to_class(AnimationMorphModifierElement, x),
            self.animation_morph_modifiers,
        )
        result["animation_node"] = to_class(AnimationNode, self.animation_node)
        result["animation_node_modifiers"] = from_list(
            lambda x: to_class(AnimationNodeModifierElement, x),
            self.animation_node_modifiers,
        )
        result["blending"] = to_float(self.blending)
        result["duration"] = to_float(self.duration)
        result["unknown"] = from_int(self.unknown)
        return result


class AnimationV1291_03_06PCLinkHeader:
    def __init__(self, link_name, links, names):
        self.link_name = link_name
        self.links = links
        self.names = names

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        link_name = from_union([from_int, from_str], obj.get("link_name"))
        links = from_list(from_int, obj.get("links"))
        names = from_list(
            lambda x: from_union([from_int, from_str], x), obj.get("names")
        )
        return AnimationV1291_03_06PCLinkHeader(link_name, links, names)

    def to_dict(self):
        result = {}
        result["link_name"] = from_union([from_int, from_str], self.link_name)
        result["links"] = from_list(from_int, self.links)
        result["names"] = from_list(
            lambda x: from_union([from_int, from_str], x), self.names
        )
        return result


class AnimationV1291_03_06_PC:
    def __init__(self, body, class_name, link_header, link_name, name):
        self.body = body
        self.class_name = class_name
        self.link_header = link_header
        self.link_name = link_name
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        body = AnimationV1291_03_06PCBody.from_dict(obj.get("body"))
        class_name = from_union([from_int, from_str], obj.get("class_name"))
        link_header = AnimationV1291_03_06PCLinkHeader.from_dict(obj.get("link_header"))
        link_name = from_union([from_none, from_int, from_str], obj.get("link_name"))
        name = from_union([from_int, from_str], obj.get("name"))
        return AnimationV1291_03_06_PC(body, class_name, link_header, link_name, name)

    def to_dict(self):
        result = {}
        result["body"] = to_class(AnimationV1291_03_06PCBody, self.body)
        result["class_name"] = from_union([from_int, from_str], self.class_name)
        result["link_header"] = to_class(
            AnimationV1291_03_06PCLinkHeader, self.link_header
        )
        if self.link_name is not None:
            result["link_name"] = from_union(
                [from_none, from_int, from_str], self.link_name
            )
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class AnimationV1381_67_09PCBody:
    def __init__(
        self,
        animation_material,
        animation_material_modifiers,
        animation_mesh,
        animation_mesh_modifiers,
        animation_morph,
        animation_morph_modifiers,
        animation_node,
        animation_node_modifiers,
        blending,
        duration,
        unknown,
    ):
        self.animation_material = animation_material
        self.animation_material_modifiers = animation_material_modifiers
        self.animation_mesh = animation_mesh
        self.animation_mesh_modifiers = animation_mesh_modifiers
        self.animation_morph = animation_morph
        self.animation_morph_modifiers = animation_morph_modifiers
        self.animation_node = animation_node
        self.animation_node_modifiers = animation_node_modifiers
        self.blending = blending
        self.duration = duration
        self.unknown = unknown

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        animation_material = AnimationMaterial.from_dict(obj.get("animation_material"))
        animation_material_modifiers = from_list(
            AnimationMaterialModifierElement.from_dict,
            obj.get("animation_material_modifiers"),
        )
        animation_mesh = AnimationMesh.from_dict(obj.get("animation_mesh"))
        animation_mesh_modifiers = from_list(
            AnimationMeshModifierElement.from_dict, obj.get("animation_mesh_modifiers")
        )
        animation_morph = AnimationMorph.from_dict(obj.get("animation_morph"))
        animation_morph_modifiers = from_list(
            AnimationMorphModifierElement.from_dict,
            obj.get("animation_morph_modifiers"),
        )
        animation_node = AnimationNode.from_dict(obj.get("animation_node"))
        animation_node_modifiers = from_list(
            AnimationNodeModifierElement.from_dict, obj.get("animation_node_modifiers")
        )
        blending = from_float(obj.get("blending"))
        duration = from_float(obj.get("duration"))
        unknown = from_int(obj.get("unknown"))
        return AnimationV1381_67_09PCBody(
            animation_material,
            animation_material_modifiers,
            animation_mesh,
            animation_mesh_modifiers,
            animation_morph,
            animation_morph_modifiers,
            animation_node,
            animation_node_modifiers,
            blending,
            duration,
            unknown,
        )

    def to_dict(self):
        result = {}
        result["animation_material"] = to_class(
            AnimationMaterial, self.animation_material
        )
        result["animation_material_modifiers"] = from_list(
            lambda x: to_class(AnimationMaterialModifierElement, x),
            self.animation_material_modifiers,
        )
        result["animation_mesh"] = to_class(AnimationMesh, self.animation_mesh)
        result["animation_mesh_modifiers"] = from_list(
            lambda x: to_class(AnimationMeshModifierElement, x),
            self.animation_mesh_modifiers,
        )
        result["animation_morph"] = to_class(AnimationMorph, self.animation_morph)
        result["animation_morph_modifiers"] = from_list(
            lambda x: to_class(AnimationMorphModifierElement, x),
            self.animation_morph_modifiers,
        )
        result["animation_node"] = to_class(AnimationNode, self.animation_node)
        result["animation_node_modifiers"] = from_list(
            lambda x: to_class(AnimationNodeModifierElement, x),
            self.animation_node_modifiers,
        )
        result["blending"] = to_float(self.blending)
        result["duration"] = to_float(self.duration)
        result["unknown"] = from_int(self.unknown)
        return result


class AnimationV1381_67_09PCLinkHeader:
    def __init__(self, link_name):
        self.link_name = link_name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        link_name = from_union([from_int, from_str], obj.get("link_name"))
        return AnimationV1381_67_09PCLinkHeader(link_name)

    def to_dict(self):
        result = {}
        result["link_name"] = from_union([from_int, from_str], self.link_name)
        return result


class AnimationV1381_67_09_PC:
    def __init__(self, body, class_name, link_header, link_name, name):
        self.body = body
        self.class_name = class_name
        self.link_header = link_header
        self.link_name = link_name
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        body = AnimationV1381_67_09PCBody.from_dict(obj.get("body"))
        class_name = from_union([from_int, from_str], obj.get("class_name"))
        link_header = AnimationV1381_67_09PCLinkHeader.from_dict(obj.get("link_header"))
        link_name = from_union([from_none, from_int, from_str], obj.get("link_name"))
        name = from_union([from_int, from_str], obj.get("name"))
        return AnimationV1381_67_09_PC(body, class_name, link_header, link_name, name)

    def to_dict(self):
        result = {}
        result["body"] = to_class(AnimationV1381_67_09PCBody, self.body)
        result["class_name"] = from_union([from_int, from_str], self.class_name)
        result["link_header"] = to_class(
            AnimationV1381_67_09PCLinkHeader, self.link_header
        )
        if self.link_name is not None:
            result["link_name"] = from_union(
                [from_none, from_int, from_str], self.link_name
            )
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class Animation:
    def __init__(self, animation_v1_291_03_06_pc, animation_v1_381_67_09_pc):
        self.animation_v1_291_03_06_pc = animation_v1_291_03_06_pc
        self.animation_v1_381_67_09_pc = animation_v1_381_67_09_pc

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        animation_v1_291_03_06_pc = from_union(
            [AnimationV1291_03_06_PC.from_dict, from_none],
            obj.get("AnimationV1_291_03_06PC"),
        )
        animation_v1_381_67_09_pc = from_union(
            [AnimationV1381_67_09_PC.from_dict, from_none],
            obj.get("AnimationV1_381_67_09PC"),
        )
        return Animation(animation_v1_291_03_06_pc, animation_v1_381_67_09_pc)

    def to_dict(self):
        result = {}
        if self.animation_v1_291_03_06_pc is not None:
            result["AnimationV1_291_03_06PC"] = from_union(
                [lambda x: to_class(AnimationV1291_03_06_PC, x), from_none],
                self.animation_v1_291_03_06_pc,
            )
        if self.animation_v1_381_67_09_pc is not None:
            result["AnimationV1_381_67_09PC"] = from_union(
                [lambda x: to_class(AnimationV1381_67_09_PC, x), from_none],
                self.animation_v1_381_67_09_pc,
            )
        return result


class AltitudeElement:
    def __init__(self, value):
        self.value = value

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        value = from_int(obj.get("value"))
        return AltitudeElement(value)

    def to_dict(self):
        result = {}
        result["value"] = from_int(self.value)
        return result


class AltitudesPackedElement:
    def __init__(self, altitudes):
        self.altitudes = altitudes

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        altitudes = from_list(AltitudeElement.from_dict, obj.get("altitudes"))
        return AltitudesPackedElement(altitudes)

    def to_dict(self):
        result = {}
        result["altitudes"] = from_list(
            lambda x: to_class(AltitudeElement, x), self.altitudes
        )
        return result


class AltitudesUnpackedElement:
    def __init__(self, altitudes):
        self.altitudes = altitudes

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        altitudes = from_list(from_int, obj.get("altitudes"))
        return AltitudesUnpackedElement(altitudes)

    def to_dict(self):
        result = {}
        result["altitudes"] = from_list(from_int, self.altitudes)
        return result


class LookupElement:
    def __init__(self, value):
        self.value = value

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        value = from_int(obj.get("value"))
        return LookupElement(value)

    def to_dict(self):
        result = {}
        result["value"] = from_int(self.value)
        return result


class Data:
    def __init__(
        self,
        altitudes_packed,
        altitudes_packed_size,
        altitudes_total_size,
        altitudes_unpacked,
        denominator,
        height,
        lookup,
        negative_one,
        two,
        width,
    ):
        self.altitudes_packed = altitudes_packed
        self.altitudes_packed_size = altitudes_packed_size
        self.altitudes_total_size = altitudes_total_size
        self.altitudes_unpacked = altitudes_unpacked
        self.denominator = denominator
        self.height = height
        self.lookup = lookup
        self.negative_one = negative_one
        self.two = two
        self.width = width

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        altitudes_packed = from_list(
            AltitudesPackedElement.from_dict, obj.get("altitudes_packed")
        )
        altitudes_packed_size = from_int(obj.get("altitudes_packed_size"))
        altitudes_total_size = from_int(obj.get("altitudes_total_size"))
        altitudes_unpacked = from_list(
            AltitudesUnpackedElement.from_dict, obj.get("altitudes_unpacked")
        )
        denominator = from_float(obj.get("denominator"))
        height = from_int(obj.get("height"))
        lookup = from_list(LookupElement.from_dict, obj.get("lookup"))
        negative_one = from_int(obj.get("negative_one"))
        two = from_float(obj.get("two"))
        width = from_int(obj.get("width"))
        return Data(
            altitudes_packed,
            altitudes_packed_size,
            altitudes_total_size,
            altitudes_unpacked,
            denominator,
            height,
            lookup,
            negative_one,
            two,
            width,
        )

    def to_dict(self):
        result = {}
        result["altitudes_packed"] = from_list(
            lambda x: to_class(AltitudesPackedElement, x), self.altitudes_packed
        )
        result["altitudes_packed_size"] = from_int(self.altitudes_packed_size)
        result["altitudes_total_size"] = from_int(self.altitudes_total_size)
        result["altitudes_unpacked"] = from_list(
            lambda x: to_class(AltitudesUnpackedElement, x), self.altitudes_unpacked
        )
        result["denominator"] = to_float(self.denominator)
        result["height"] = from_int(self.height)
        result["lookup"] = from_list(lambda x: to_class(LookupElement, x), self.lookup)
        result["negative_one"] = from_int(self.negative_one)
        result["two"] = to_float(self.two)
        result["width"] = from_int(self.width)
        return result


class BinaryV1381_67_09PCBody:
    def __init__(self, data, data_size):
        self.data = data
        self.data_size = data_size

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        data = Data.from_dict(obj.get("data"))
        data_size = from_int(obj.get("data_size"))
        return BinaryV1381_67_09PCBody(data, data_size)

    def to_dict(self):
        result = {}
        result["data"] = to_class(Data, self.data)
        result["data_size"] = from_int(self.data_size)
        return result


class BinaryV1381_67_09_PC:
    def __init__(self, body, class_name, link_header, link_name, name):
        self.body = body
        self.class_name = class_name
        self.link_header = link_header
        self.link_name = link_name
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        body = BinaryV1381_67_09PCBody.from_dict(obj.get("body"))
        class_name = from_union([from_int, from_str], obj.get("class_name"))
        link_header = AnimationV1381_67_09PCLinkHeader.from_dict(obj.get("link_header"))
        link_name = from_union([from_none, from_int, from_str], obj.get("link_name"))
        name = from_union([from_int, from_str], obj.get("name"))
        return BinaryV1381_67_09_PC(body, class_name, link_header, link_name, name)

    def to_dict(self):
        result = {}
        result["body"] = to_class(BinaryV1381_67_09PCBody, self.body)
        result["class_name"] = from_union([from_int, from_str], self.class_name)
        result["link_header"] = to_class(
            AnimationV1381_67_09PCLinkHeader, self.link_header
        )
        if self.link_name is not None:
            result["link_name"] = from_union(
                [from_none, from_int, from_str], self.link_name
            )
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class Binary:
    def __init__(self, binary_v1_381_67_09_pc):
        self.binary_v1_381_67_09_pc = binary_v1_381_67_09_pc

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        binary_v1_381_67_09_pc = BinaryV1381_67_09_PC.from_dict(
            obj.get("BinaryV1_381_67_09PC")
        )
        return Binary(binary_v1_381_67_09_pc)

    def to_dict(self):
        result = {}
        result["BinaryV1_381_67_09PC"] = to_class(
            BinaryV1381_67_09_PC, self.binary_v1_381_67_09_pc
        )
        return result


class BitmapV106_63_02PCBody:
    def __init__(
        self,
        flag,
        format,
        format_copy,
        four,
        height,
        mipmap_count,
        palette_format,
        precalculated_size,
        transp_format,
        width,
    ):
        self.flag = flag
        self.format = format
        self.format_copy = format_copy
        self.four = four
        self.height = height
        self.mipmap_count = mipmap_count
        self.palette_format = palette_format
        self.precalculated_size = precalculated_size
        self.transp_format = transp_format
        self.width = width

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        flag = from_int(obj.get("flag"))
        format = from_int(obj.get("format"))
        format_copy = from_int(obj.get("format_copy"))
        four = from_int(obj.get("four"))
        height = from_int(obj.get("height"))
        mipmap_count = from_int(obj.get("mipmap_count"))
        palette_format = from_int(obj.get("palette_format"))
        precalculated_size = from_int(obj.get("precalculated_size"))
        transp_format = from_int(obj.get("transp_format"))
        width = from_int(obj.get("width"))
        return BitmapV106_63_02PCBody(
            flag,
            format,
            format_copy,
            four,
            height,
            mipmap_count,
            palette_format,
            precalculated_size,
            transp_format,
            width,
        )

    def to_dict(self):
        result = {}
        result["flag"] = from_int(self.flag)
        result["format"] = from_int(self.format)
        result["format_copy"] = from_int(self.format_copy)
        result["four"] = from_int(self.four)
        result["height"] = from_int(self.height)
        result["mipmap_count"] = from_int(self.mipmap_count)
        result["palette_format"] = from_int(self.palette_format)
        result["precalculated_size"] = from_int(self.precalculated_size)
        result["transp_format"] = from_int(self.transp_format)
        result["width"] = from_int(self.width)
        return result


class BitmapV106_63_02_PC:
    def __init__(self, body, class_name, link_header, link_name, name):
        self.body = body
        self.class_name = class_name
        self.link_header = link_header
        self.link_name = link_name
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        body = BitmapV106_63_02PCBody.from_dict(obj.get("body"))
        class_name = from_union([from_int, from_str], obj.get("class_name"))
        link_header = AnimationV1291_03_06PCLinkHeader.from_dict(obj.get("link_header"))
        link_name = from_union([from_none, from_int, from_str], obj.get("link_name"))
        name = from_union([from_int, from_str], obj.get("name"))
        return BitmapV106_63_02_PC(body, class_name, link_header, link_name, name)

    def to_dict(self):
        result = {}
        result["body"] = to_class(BitmapV106_63_02PCBody, self.body)
        result["class_name"] = from_union([from_int, from_str], self.class_name)
        result["link_header"] = to_class(
            AnimationV1291_03_06PCLinkHeader, self.link_header
        )
        if self.link_name is not None:
            result["link_name"] = from_union(
                [from_none, from_int, from_str], self.link_name
            )
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class BodyHeader:
    def __init__(
        self, flag, format, height, mipmap_count, precalculated_size, unknown, width
    ):
        self.flag = flag
        self.format = format
        self.height = height
        self.mipmap_count = mipmap_count
        self.precalculated_size = precalculated_size
        self.unknown = unknown
        self.width = width

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        flag = from_int(obj.get("flag"))
        format = from_int(obj.get("format"))
        height = from_int(obj.get("height"))
        mipmap_count = from_int(obj.get("mipmap_count"))
        precalculated_size = from_int(obj.get("precalculated_size"))
        unknown = from_int(obj.get("unknown"))
        width = from_int(obj.get("width"))
        return BodyHeader(
            flag, format, height, mipmap_count, precalculated_size, unknown, width
        )

    def to_dict(self):
        result = {}
        result["flag"] = from_int(self.flag)
        result["format"] = from_int(self.format)
        result["height"] = from_int(self.height)
        result["mipmap_count"] = from_int(self.mipmap_count)
        result["precalculated_size"] = from_int(self.precalculated_size)
        result["unknown"] = from_int(self.unknown)
        result["width"] = from_int(self.width)
        return result


class BitmapV1291_03_06PCBody:
    def __init__(self, header):
        self.header = header

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        header = BodyHeader.from_dict(obj.get("header"))
        return BitmapV1291_03_06PCBody(header)

    def to_dict(self):
        result = {}
        result["header"] = to_class(BodyHeader, self.header)
        return result


class BitmapV1291_03_06_PC:
    def __init__(self, body, class_name, link_header, link_name, name):
        self.body = body
        self.class_name = class_name
        self.link_header = link_header
        self.link_name = link_name
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        body = BitmapV1291_03_06PCBody.from_dict(obj.get("body"))
        class_name = from_union([from_int, from_str], obj.get("class_name"))
        link_header = AnimationV1291_03_06PCLinkHeader.from_dict(obj.get("link_header"))
        link_name = from_union([from_none, from_int, from_str], obj.get("link_name"))
        name = from_union([from_int, from_str], obj.get("name"))
        return BitmapV1291_03_06_PC(body, class_name, link_header, link_name, name)

    def to_dict(self):
        result = {}
        result["body"] = to_class(BitmapV1291_03_06PCBody, self.body)
        result["class_name"] = from_union([from_int, from_str], self.class_name)
        result["link_header"] = to_class(
            AnimationV1291_03_06PCLinkHeader, self.link_header
        )
        if self.link_name is not None:
            result["link_name"] = from_union(
                [from_none, from_int, from_str], self.link_name
            )
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class BitmapClass(Enum):
    CUBEMAP = "Cubemap"
    SINGLE = "Single"


class BitmapClass2(Enum):
    CUBEMAP2 = "Cubemap2"
    SINGLE2 = "Single2"


class Transparency(Enum):
    CUBEMAP = "Cubemap"
    NO_TRANSP = "NoTransp"
    TRANSP = "Transp"
    TRANSP_ONE = "TranspOne"


class BitmapV1381_67_09PCLinkHeader:
    def __init__(
        self,
        bitmap_class,
        bitmap_class2,
        bitmap_type,
        flags,
        four,
        layer,
        link_name,
        pad,
        transparency,
    ):
        self.bitmap_class = bitmap_class
        self.bitmap_class2 = bitmap_class2
        self.bitmap_type = bitmap_type
        self.flags = flags
        self.four = four
        self.layer = layer
        self.link_name = link_name
        self.pad = pad
        self.transparency = transparency

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        bitmap_class = BitmapClass(obj.get("bitmap_class"))
        bitmap_class2 = BitmapClass2(obj.get("bitmap_class2"))
        bitmap_type = from_int(obj.get("bitmap_type"))
        flags = from_int(obj.get("flags"))
        four = from_int(obj.get("four"))
        layer = from_float(obj.get("layer"))
        link_name = from_union([from_int, from_str], obj.get("link_name"))
        pad = from_int(obj.get("pad"))
        transparency = Transparency(obj.get("transparency"))
        return BitmapV1381_67_09PCLinkHeader(
            bitmap_class,
            bitmap_class2,
            bitmap_type,
            flags,
            four,
            layer,
            link_name,
            pad,
            transparency,
        )

    def to_dict(self):
        result = {}
        result["bitmap_class"] = to_enum(BitmapClass, self.bitmap_class)
        result["bitmap_class2"] = to_enum(BitmapClass2, self.bitmap_class2)
        result["bitmap_type"] = from_int(self.bitmap_type)
        result["flags"] = from_int(self.flags)
        result["four"] = from_int(self.four)
        result["layer"] = to_float(self.layer)
        result["link_name"] = from_union([from_int, from_str], self.link_name)
        result["pad"] = from_int(self.pad)
        result["transparency"] = to_enum(Transparency, self.transparency)
        return result


class BitmapV1381_67_09_PC:
    def __init__(self, body, class_name, link_header, link_name, name):
        self.body = body
        self.class_name = class_name
        self.link_header = link_header
        self.link_name = link_name
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        body = from_dict(lambda x: x, obj.get("body"))
        class_name = from_union([from_int, from_str], obj.get("class_name"))
        link_header = BitmapV1381_67_09PCLinkHeader.from_dict(obj.get("link_header"))
        link_name = from_union([from_none, from_int, from_str], obj.get("link_name"))
        name = from_union([from_int, from_str], obj.get("name"))
        return BitmapV1381_67_09_PC(body, class_name, link_header, link_name, name)

    def to_dict(self):
        result = {}
        result["body"] = from_dict(lambda x: x, self.body)
        result["class_name"] = from_union([from_int, from_str], self.class_name)
        result["link_header"] = to_class(
            BitmapV1381_67_09PCLinkHeader, self.link_header
        )
        if self.link_name is not None:
            result["link_name"] = from_union(
                [from_none, from_int, from_str], self.link_name
            )
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class Bitmap:
    def __init__(
        self, bitmap_v1_06_63_02_pc, bitmap_v1_291_03_06_pc, bitmap_v1_381_67_09_pc
    ):
        self.bitmap_v1_06_63_02_pc = bitmap_v1_06_63_02_pc
        self.bitmap_v1_291_03_06_pc = bitmap_v1_291_03_06_pc
        self.bitmap_v1_381_67_09_pc = bitmap_v1_381_67_09_pc

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        bitmap_v1_06_63_02_pc = from_union(
            [BitmapV106_63_02_PC.from_dict, from_none], obj.get("BitmapV1_06_63_02PC")
        )
        bitmap_v1_291_03_06_pc = from_union(
            [BitmapV1291_03_06_PC.from_dict, from_none], obj.get("BitmapV1_291_03_06PC")
        )
        bitmap_v1_381_67_09_pc = from_union(
            [BitmapV1381_67_09_PC.from_dict, from_none], obj.get("BitmapV1_381_67_09PC")
        )
        return Bitmap(
            bitmap_v1_06_63_02_pc, bitmap_v1_291_03_06_pc, bitmap_v1_381_67_09_pc
        )

    def to_dict(self):
        result = {}
        if self.bitmap_v1_06_63_02_pc is not None:
            result["BitmapV1_06_63_02PC"] = from_union(
                [lambda x: to_class(BitmapV106_63_02_PC, x), from_none],
                self.bitmap_v1_06_63_02_pc,
            )
        if self.bitmap_v1_291_03_06_pc is not None:
            result["BitmapV1_291_03_06PC"] = from_union(
                [lambda x: to_class(BitmapV1291_03_06_PC, x), from_none],
                self.bitmap_v1_291_03_06_pc,
            )
        if self.bitmap_v1_381_67_09_pc is not None:
            result["BitmapV1_381_67_09PC"] = from_union(
                [lambda x: to_class(BitmapV1381_67_09_PC, x), from_none],
                self.bitmap_v1_381_67_09_pc,
            )
        return result


class CameraV1381_67_09PCBody:
    def __init__(self, angle_of_view, node_name, zero):
        self.angle_of_view = angle_of_view
        self.node_name = node_name
        self.zero = zero

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        angle_of_view = from_float(obj.get("angle_of_view"))
        node_name = from_union([from_int, from_str], obj.get("node_name"))
        zero = from_float(obj.get("zero"))
        return CameraV1381_67_09PCBody(angle_of_view, node_name, zero)

    def to_dict(self):
        result = {}
        result["angle_of_view"] = to_float(self.angle_of_view)
        result["node_name"] = from_union([from_int, from_str], self.node_name)
        result["zero"] = to_float(self.zero)
        return result


class Box:
    def __init__(self, matrix, scale, vec):
        self.matrix = matrix
        self.scale = scale
        self.vec = vec

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        matrix = from_list(lambda x: from_list(from_float, x), obj.get("matrix"))
        scale = from_float(obj.get("scale"))
        vec = from_list(from_float, obj.get("vec"))
        return Box(matrix, scale, vec)

    def to_dict(self):
        result = {}
        result["matrix"] = from_list(lambda x: from_list(to_float, x), self.matrix)
        result["scale"] = to_float(self.scale)
        result["vec"] = from_list(to_float, self.vec)
        return result


class Sphere:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        center = from_list(from_float, obj.get("center"))
        radius = from_float(obj.get("radius"))
        return Sphere(center, radius)

    def to_dict(self):
        result = {}
        result["center"] = from_list(to_float, self.center)
        result["radius"] = to_float(self.radius)
        return result


class ResourceLinkHeaderFlags:
    def __init__(self, value):
        self.value = value

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        value = from_int(obj.get("value"))
        return ResourceLinkHeaderFlags(value)

    def to_dict(self):
        result = {}
        result["value"] = from_int(self.value)
        return result


class TypeEnum(Enum):
    CAMERA = "Camera"
    CAMERA_ZONE = "CameraZone"
    COLLISION_VOL = "CollisionVol"
    EMITER = "Emiter"
    FLARE = "Flare"
    GEN_WORLD = "GenWorld"
    GEN_WORLD_SURFACE = "GenWorldSurface"
    GRAPH = "Graph"
    H_FIELD = "HField"
    H_FOG = "HFog"
    LIGHT = "Light"
    LOD = "Lod"
    MESH = "Mesh"
    OCCLUDER = "Occluder"
    OMNI = "Omni"
    PARTICLES = "Particles"
    POINTS = "Points"
    ROAD = "Road"
    ROT_SHAPE = "RotShape"
    SKIN = "Skin"
    SPLINE = "Spline"
    SPLINE_GRAPH = "SplineGraph"
    SPLINE_ZONE = "SplineZone"
    SURFACE = "Surface"
    TREE = "Tree"
    WORLD_REF = "WorldRef"


class CameraV1381_67_09PCLinkHeader:
    def __init__(
        self, b_box, b_sphere, data_name, fade_out_dist, flags, link_name, type
    ):
        self.b_box = b_box
        self.b_sphere = b_sphere
        self.data_name = data_name
        self.fade_out_dist = fade_out_dist
        self.flags = flags
        self.link_name = link_name
        self.type = type

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        b_box = Box.from_dict(obj.get("b_box"))
        b_sphere = Sphere.from_dict(obj.get("b_sphere"))
        data_name = from_union([from_int, from_str], obj.get("data_name"))
        fade_out_dist = from_float(obj.get("fade_out_dist"))
        flags = ResourceLinkHeaderFlags.from_dict(obj.get("flags"))
        link_name = from_union([from_int, from_str], obj.get("link_name"))
        type = TypeEnum(obj.get("type"))
        return CameraV1381_67_09PCLinkHeader(
            b_box, b_sphere, data_name, fade_out_dist, flags, link_name, type
        )

    def to_dict(self):
        result = {}
        result["b_box"] = to_class(Box, self.b_box)
        result["b_sphere"] = to_class(Sphere, self.b_sphere)
        result["data_name"] = from_union([from_int, from_str], self.data_name)
        result["fade_out_dist"] = to_float(self.fade_out_dist)
        result["flags"] = to_class(ResourceLinkHeaderFlags, self.flags)
        result["link_name"] = from_union([from_int, from_str], self.link_name)
        result["type"] = to_enum(TypeEnum, self.type)
        return result


class CameraV1381_67_09_PC:
    def __init__(self, body, class_name, link_header, link_name, name):
        self.body = body
        self.class_name = class_name
        self.link_header = link_header
        self.link_name = link_name
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        body = CameraV1381_67_09PCBody.from_dict(obj.get("body"))
        class_name = from_union([from_int, from_str], obj.get("class_name"))
        link_header = CameraV1381_67_09PCLinkHeader.from_dict(obj.get("link_header"))
        link_name = from_union([from_none, from_int, from_str], obj.get("link_name"))
        name = from_union([from_int, from_str], obj.get("name"))
        return CameraV1381_67_09_PC(body, class_name, link_header, link_name, name)

    def to_dict(self):
        result = {}
        result["body"] = to_class(CameraV1381_67_09PCBody, self.body)
        result["class_name"] = from_union([from_int, from_str], self.class_name)
        result["link_header"] = to_class(
            CameraV1381_67_09PCLinkHeader, self.link_header
        )
        if self.link_name is not None:
            result["link_name"] = from_union(
                [from_none, from_int, from_str], self.link_name
            )
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class Camera:
    def __init__(self, camera_v1_381_67_09_pc):
        self.camera_v1_381_67_09_pc = camera_v1_381_67_09_pc

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        camera_v1_381_67_09_pc = CameraV1381_67_09_PC.from_dict(
            obj.get("CameraV1_381_67_09PC")
        )
        return Camera(camera_v1_381_67_09_pc)

    def to_dict(self):
        result = {}
        result["CameraV1_381_67_09PC"] = to_class(
            CameraV1381_67_09_PC, self.camera_v1_381_67_09_pc
        )
        return result


class TriggerIDSRefElement:
    def __init__(self, offset, size):
        self.offset = offset
        self.size = size

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        offset = from_int(obj.get("offset"))
        size = from_int(obj.get("size"))
        return TriggerIDSRefElement(offset, size)

    def to_dict(self):
        result = {}
        result["offset"] = from_int(self.offset)
        result["size"] = from_int(self.size)
        return result


class SplineZoneSead:
    def __init__(
        self,
        grid_da,
        inv_diag,
        max_zone_index,
        p_max,
        p_min,
        size_x,
        size_y,
        zone_indices,
    ):
        self.grid_da = grid_da
        self.inv_diag = inv_diag
        self.max_zone_index = max_zone_index
        self.p_max = p_max
        self.p_min = p_min
        self.size_x = size_x
        self.size_y = size_y
        self.zone_indices = zone_indices

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        grid_da = from_list(TriggerIDSRefElement.from_dict, obj.get("grid_da"))
        inv_diag = from_list(from_float, obj.get("inv_diag"))
        max_zone_index = from_int(obj.get("max_zone_index"))
        p_max = from_list(from_float, obj.get("p_max"))
        p_min = from_list(from_float, obj.get("p_min"))
        size_x = from_int(obj.get("size_x"))
        size_y = from_int(obj.get("size_y"))
        zone_indices = from_list(from_int, obj.get("zone_indices"))
        return SplineZoneSead(
            grid_da,
            inv_diag,
            max_zone_index,
            p_max,
            p_min,
            size_x,
            size_y,
            zone_indices,
        )

    def to_dict(self):
        result = {}
        result["grid_da"] = from_list(
            lambda x: to_class(TriggerIDSRefElement, x), self.grid_da
        )
        result["inv_diag"] = from_list(to_float, self.inv_diag)
        result["max_zone_index"] = from_int(self.max_zone_index)
        result["p_max"] = from_list(to_float, self.p_max)
        result["p_min"] = from_list(to_float, self.p_min)
        result["size_x"] = from_int(self.size_x)
        result["size_y"] = from_int(self.size_y)
        result["zone_indices"] = from_list(from_int, self.zone_indices)
        return result


class SplineZoneElement:
    def __init__(self, point_flag, spline_ids_ref, unknown0, unknown1, y):
        self.point_flag = point_flag
        self.spline_ids_ref = spline_ids_ref
        self.unknown0 = unknown0
        self.unknown1 = unknown1
        self.y = y

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        point_flag = from_int(obj.get("point_flag"))
        spline_ids_ref = TriggerIDSRefElement.from_dict(obj.get("spline_ids_ref"))
        unknown0 = from_int(obj.get("unknown0"))
        unknown1 = from_int(obj.get("unknown1"))
        y = from_float(obj.get("y"))
        return SplineZoneElement(point_flag, spline_ids_ref, unknown0, unknown1, y)

    def to_dict(self):
        result = {}
        result["point_flag"] = from_int(self.point_flag)
        result["spline_ids_ref"] = to_class(TriggerIDSRefElement, self.spline_ids_ref)
        result["unknown0"] = from_int(self.unknown0)
        result["unknown1"] = from_int(self.unknown1)
        result["y"] = to_float(self.y)
        return result


class SplineZoneSpline:
    def __init__(self, pt_0__id, pt_1__id):
        self.pt_0__id = pt_0__id
        self.pt_1__id = pt_1__id

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        pt_0__id = from_int(obj.get("pt_0_id"))
        pt_1__id = from_int(obj.get("pt_1_id"))
        return SplineZoneSpline(pt_0__id, pt_1__id)

    def to_dict(self):
        result = {}
        result["pt_0_id"] = from_int(self.pt_0__id)
        result["pt_1_id"] = from_int(self.pt_1__id)
        return result


class SplineZone:
    def __init__(
        self,
        points,
        spline_ids,
        spline_zone_sead,
        spline_zones,
        splines,
        unknown,
        unknowns,
    ):
        self.points = points
        self.spline_ids = spline_ids
        self.spline_zone_sead = spline_zone_sead
        self.spline_zones = spline_zones
        self.splines = splines
        self.unknown = unknown
        self.unknowns = unknowns

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        points = from_list(lambda x: from_list(from_float, x), obj.get("points"))
        spline_ids = from_list(from_int, obj.get("spline_ids"))
        spline_zone_sead = SplineZoneSead.from_dict(obj.get("spline_zone_sead"))
        spline_zones = from_list(SplineZoneElement.from_dict, obj.get("spline_zones"))
        splines = from_list(SplineZoneSpline.from_dict, obj.get("splines"))
        unknown = from_list(from_float, obj.get("unknown"))
        unknowns = from_list(lambda x: from_list(from_float, x), obj.get("unknowns"))
        return SplineZone(
            points,
            spline_ids,
            spline_zone_sead,
            spline_zones,
            splines,
            unknown,
            unknowns,
        )

    def to_dict(self):
        result = {}
        result["points"] = from_list(lambda x: from_list(to_float, x), self.points)
        result["spline_ids"] = from_list(from_int, self.spline_ids)
        result["spline_zone_sead"] = to_class(SplineZoneSead, self.spline_zone_sead)
        result["spline_zones"] = from_list(
            lambda x: to_class(SplineZoneElement, x), self.spline_zones
        )
        result["splines"] = from_list(
            lambda x: to_class(SplineZoneSpline, x), self.splines
        )
        result["unknown"] = from_list(to_float, self.unknown)
        result["unknowns"] = from_list(lambda x: from_list(to_float, x), self.unknowns)
        return result


class TriggerElement:
    def __init__(
        self,
        at_point_id,
        color,
        dist,
        far,
        flag,
        fog,
        fov,
        height,
        point_id,
        rot,
        smooth,
        spline_id,
        spline_length,
        unknown,
    ):
        self.at_point_id = at_point_id
        self.color = color
        self.dist = dist
        self.far = far
        self.flag = flag
        self.fog = fog
        self.fov = fov
        self.height = height
        self.point_id = point_id
        self.rot = rot
        self.smooth = smooth
        self.spline_id = spline_id
        self.spline_length = spline_length
        self.unknown = unknown

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        at_point_id = from_int(obj.get("at_point_id"))
        color = from_list(from_float, obj.get("color"))
        dist = from_float(obj.get("dist"))
        far = from_float(obj.get("far"))
        flag = from_int(obj.get("flag"))
        fog = from_float(obj.get("fog"))
        fov = from_float(obj.get("fov"))
        height = from_float(obj.get("height"))
        point_id = from_int(obj.get("point_id"))
        rot = from_float(obj.get("rot"))
        smooth = from_float(obj.get("smooth"))
        spline_id = from_int(obj.get("spline_id"))
        spline_length = from_float(obj.get("spline_length"))
        unknown = from_list(from_float, obj.get("unknown"))
        return TriggerElement(
            at_point_id,
            color,
            dist,
            far,
            flag,
            fog,
            fov,
            height,
            point_id,
            rot,
            smooth,
            spline_id,
            spline_length,
            unknown,
        )

    def to_dict(self):
        result = {}
        result["at_point_id"] = from_int(self.at_point_id)
        result["color"] = from_list(to_float, self.color)
        result["dist"] = to_float(self.dist)
        result["far"] = to_float(self.far)
        result["flag"] = from_int(self.flag)
        result["fog"] = to_float(self.fog)
        result["fov"] = to_float(self.fov)
        result["height"] = to_float(self.height)
        result["point_id"] = from_int(self.point_id)
        result["rot"] = to_float(self.rot)
        result["smooth"] = to_float(self.smooth)
        result["spline_id"] = from_int(self.spline_id)
        result["spline_length"] = to_float(self.spline_length)
        result["unknown"] = from_list(to_float, self.unknown)
        return result


class ZoneTriggerElement:
    def __init__(self, trigger_ids_ref):
        self.trigger_ids_ref = trigger_ids_ref

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        trigger_ids_ref = TriggerIDSRefElement.from_dict(obj.get("trigger_ids_ref"))
        return ZoneTriggerElement(trigger_ids_ref)

    def to_dict(self):
        result = {}
        result["trigger_ids_ref"] = to_class(TriggerIDSRefElement, self.trigger_ids_ref)
        return result


class CameraZoneV106_63_02PCBody:
    def __init__(self, spline_zone, trigger_ids, triggers, zone_triggers):
        self.spline_zone = spline_zone
        self.trigger_ids = trigger_ids
        self.triggers = triggers
        self.zone_triggers = zone_triggers

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        spline_zone = SplineZone.from_dict(obj.get("spline_zone"))
        trigger_ids = from_list(from_int, obj.get("trigger_ids"))
        triggers = from_list(TriggerElement.from_dict, obj.get("triggers"))
        zone_triggers = from_list(
            ZoneTriggerElement.from_dict, obj.get("zone_triggers")
        )
        return CameraZoneV106_63_02PCBody(
            spline_zone, trigger_ids, triggers, zone_triggers
        )

    def to_dict(self):
        result = {}
        result["spline_zone"] = to_class(SplineZone, self.spline_zone)
        result["trigger_ids"] = from_list(from_int, self.trigger_ids)
        result["triggers"] = from_list(
            lambda x: to_class(TriggerElement, x), self.triggers
        )
        result["zone_triggers"] = from_list(
            lambda x: to_class(ZoneTriggerElement, x), self.zone_triggers
        )
        return result


class CameraZoneV106_63_02PCLinkHeader:
    def __init__(
        self, b_box, b_sphere, data_name, fade_out_dist, flags, link_name, names, type
    ):
        self.b_box = b_box
        self.b_sphere = b_sphere
        self.data_name = data_name
        self.fade_out_dist = fade_out_dist
        self.flags = flags
        self.link_name = link_name
        self.names = names
        self.type = type

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        b_box = Box.from_dict(obj.get("b_box"))
        b_sphere = Sphere.from_dict(obj.get("b_sphere"))
        data_name = from_union([from_int, from_str], obj.get("data_name"))
        fade_out_dist = from_float(obj.get("fade_out_dist"))
        flags = from_int(obj.get("flags"))
        link_name = from_union([from_int, from_str], obj.get("link_name"))
        names = from_list(
            lambda x: from_union([from_int, from_str], x), obj.get("names")
        )
        type = TypeEnum(obj.get("type"))
        return CameraZoneV106_63_02PCLinkHeader(
            b_box, b_sphere, data_name, fade_out_dist, flags, link_name, names, type
        )

    def to_dict(self):
        result = {}
        result["b_box"] = to_class(Box, self.b_box)
        result["b_sphere"] = to_class(Sphere, self.b_sphere)
        result["data_name"] = from_union([from_int, from_str], self.data_name)
        result["fade_out_dist"] = to_float(self.fade_out_dist)
        result["flags"] = from_int(self.flags)
        result["link_name"] = from_union([from_int, from_str], self.link_name)
        result["names"] = from_list(
            lambda x: from_union([from_int, from_str], x), self.names
        )
        result["type"] = to_enum(TypeEnum, self.type)
        return result


class CameraZoneV106_63_02_PC:
    def __init__(self, body, class_name, link_header, link_name, name):
        self.body = body
        self.class_name = class_name
        self.link_header = link_header
        self.link_name = link_name
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        body = CameraZoneV106_63_02PCBody.from_dict(obj.get("body"))
        class_name = from_union([from_int, from_str], obj.get("class_name"))
        link_header = CameraZoneV106_63_02PCLinkHeader.from_dict(obj.get("link_header"))
        link_name = from_union([from_none, from_int, from_str], obj.get("link_name"))
        name = from_union([from_int, from_str], obj.get("name"))
        return CameraZoneV106_63_02_PC(body, class_name, link_header, link_name, name)

    def to_dict(self):
        result = {}
        result["body"] = to_class(CameraZoneV106_63_02PCBody, self.body)
        result["class_name"] = from_union([from_int, from_str], self.class_name)
        result["link_header"] = to_class(
            CameraZoneV106_63_02PCLinkHeader, self.link_header
        )
        if self.link_name is not None:
            result["link_name"] = from_union(
                [from_none, from_int, from_str], self.link_name
            )
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class CameraZone:
    def __init__(self, camera_zone_v1_06_63_02_pc):
        self.camera_zone_v1_06_63_02_pc = camera_zone_v1_06_63_02_pc

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        camera_zone_v1_06_63_02_pc = CameraZoneV106_63_02_PC.from_dict(
            obj.get("CameraZoneV1_06_63_02PC")
        )
        return CameraZone(camera_zone_v1_06_63_02_pc)

    def to_dict(self):
        result = {}
        result["CameraZoneV1_06_63_02PC"] = to_class(
            CameraZoneV106_63_02_PC, self.camera_zone_v1_06_63_02_pc
        )
        return result


class PurpleSchema:
    def __init__(self, inv_local_transform, local_transform):
        self.inv_local_transform = inv_local_transform
        self.local_transform = local_transform

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        inv_local_transform = from_list(
            lambda x: from_list(from_float, x), obj.get("inv_local_transform")
        )
        local_transform = from_list(
            lambda x: from_list(from_float, x), obj.get("local_transform")
        )
        return PurpleSchema(inv_local_transform, local_transform)

    def to_dict(self):
        result = {}
        result["inv_local_transform"] = from_list(
            lambda x: from_list(to_float, x), self.inv_local_transform
        )
        result["local_transform"] = from_list(
            lambda x: from_list(to_float, x), self.local_transform
        )
        return result


class CollisionVolV1291_03_06PCBody:
    def __init__(
        self,
        anim_frame_names,
        anim_start_time,
        collision_vol_agent_name,
        collision_vol_infos,
        float_param_names,
        in_message_id,
        node_param_names,
        out_message_id,
    ):
        self.anim_frame_names = anim_frame_names
        self.anim_start_time = anim_start_time
        self.collision_vol_agent_name = collision_vol_agent_name
        self.collision_vol_infos = collision_vol_infos
        self.float_param_names = float_param_names
        self.in_message_id = in_message_id
        self.node_param_names = node_param_names
        self.out_message_id = out_message_id

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        anim_frame_names = from_list(
            lambda x: from_union([from_int, from_str], x), obj.get("anim_frame_names")
        )
        anim_start_time = from_float(obj.get("anim_start_time"))
        collision_vol_agent_name = from_union(
            [from_int, from_str], obj.get("collision_vol_agent_name")
        )
        collision_vol_infos = from_list(
            PurpleSchema.from_dict, obj.get("collision_vol_infos")
        )
        float_param_names = from_list(from_int, obj.get("float_param_names"))
        in_message_id = from_int(obj.get("in_message_id"))
        node_param_names = from_list(from_int, obj.get("node_param_names"))
        out_message_id = from_int(obj.get("out_message_id"))
        return CollisionVolV1291_03_06PCBody(
            anim_frame_names,
            anim_start_time,
            collision_vol_agent_name,
            collision_vol_infos,
            float_param_names,
            in_message_id,
            node_param_names,
            out_message_id,
        )

    def to_dict(self):
        result = {}
        result["anim_frame_names"] = from_list(
            lambda x: from_union([from_int, from_str], x), self.anim_frame_names
        )
        result["anim_start_time"] = to_float(self.anim_start_time)
        result["collision_vol_agent_name"] = from_union(
            [from_int, from_str], self.collision_vol_agent_name
        )
        result["collision_vol_infos"] = from_list(
            lambda x: to_class(PurpleSchema, x), self.collision_vol_infos
        )
        result["float_param_names"] = from_list(from_int, self.float_param_names)
        result["in_message_id"] = from_int(self.in_message_id)
        result["node_param_names"] = from_list(from_int, self.node_param_names)
        result["out_message_id"] = from_int(self.out_message_id)
        return result


class CollisionVolV1291_03_06_PC:
    def __init__(self, body, class_name, link_header, link_name, name):
        self.body = body
        self.class_name = class_name
        self.link_header = link_header
        self.link_name = link_name
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        body = CollisionVolV1291_03_06PCBody.from_dict(obj.get("body"))
        class_name = from_union([from_int, from_str], obj.get("class_name"))
        link_header = CameraZoneV106_63_02PCLinkHeader.from_dict(obj.get("link_header"))
        link_name = from_union([from_none, from_int, from_str], obj.get("link_name"))
        name = from_union([from_int, from_str], obj.get("name"))
        return CollisionVolV1291_03_06_PC(
            body, class_name, link_header, link_name, name
        )

    def to_dict(self):
        result = {}
        result["body"] = to_class(CollisionVolV1291_03_06PCBody, self.body)
        result["class_name"] = from_union([from_int, from_str], self.class_name)
        result["link_header"] = to_class(
            CameraZoneV106_63_02PCLinkHeader, self.link_header
        )
        if self.link_name is not None:
            result["link_name"] = from_union(
                [from_none, from_int, from_str], self.link_name
            )
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class FluffySchema:
    def __init__(self, local_transform, local_transform_inverse):
        self.local_transform = local_transform
        self.local_transform_inverse = local_transform_inverse

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        local_transform = from_list(
            lambda x: from_list(from_float, x), obj.get("local_transform")
        )
        local_transform_inverse = from_list(
            lambda x: from_list(from_float, x), obj.get("local_transform_inverse")
        )
        return FluffySchema(local_transform, local_transform_inverse)

    def to_dict(self):
        result = {}
        result["local_transform"] = from_list(
            lambda x: from_list(to_float, x), self.local_transform
        )
        result["local_transform_inverse"] = from_list(
            lambda x: from_list(to_float, x), self.local_transform_inverse
        )
        return result


class CollisionVolV1381_67_09PCBody:
    def __init__(
        self,
        anim_frame_names,
        collision_vol_info,
        delay,
        float_params,
        in_message_id,
        material_anim_names,
        node_name_params,
        out_message_id,
        volume_type,
    ):
        self.anim_frame_names = anim_frame_names
        self.collision_vol_info = collision_vol_info
        self.delay = delay
        self.float_params = float_params
        self.in_message_id = in_message_id
        self.material_anim_names = material_anim_names
        self.node_name_params = node_name_params
        self.out_message_id = out_message_id
        self.volume_type = volume_type

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        anim_frame_names = from_list(
            lambda x: from_union([from_int, from_str], x), obj.get("anim_frame_names")
        )
        collision_vol_info = from_list(
            FluffySchema.from_dict, obj.get("collision_vol_info")
        )
        delay = from_float(obj.get("delay"))
        float_params = from_list(from_float, obj.get("float_params"))
        in_message_id = from_union([from_int, from_str], obj.get("in_message_id"))
        material_anim_names = from_list(
            lambda x: from_union([from_int, from_str], x),
            obj.get("material_anim_names"),
        )
        node_name_params = from_list(
            lambda x: from_union([from_int, from_str], x), obj.get("node_name_params")
        )
        out_message_id = from_union([from_int, from_str], obj.get("out_message_id"))
        volume_type = from_union([from_int, from_str], obj.get("volume_type"))
        return CollisionVolV1381_67_09PCBody(
            anim_frame_names,
            collision_vol_info,
            delay,
            float_params,
            in_message_id,
            material_anim_names,
            node_name_params,
            out_message_id,
            volume_type,
        )

    def to_dict(self):
        result = {}
        result["anim_frame_names"] = from_list(
            lambda x: from_union([from_int, from_str], x), self.anim_frame_names
        )
        result["collision_vol_info"] = from_list(
            lambda x: to_class(FluffySchema, x), self.collision_vol_info
        )
        result["delay"] = to_float(self.delay)
        result["float_params"] = from_list(to_float, self.float_params)
        result["in_message_id"] = from_union([from_int, from_str], self.in_message_id)
        result["material_anim_names"] = from_list(
            lambda x: from_union([from_int, from_str], x), self.material_anim_names
        )
        result["node_name_params"] = from_list(
            lambda x: from_union([from_int, from_str], x), self.node_name_params
        )
        result["out_message_id"] = from_union([from_int, from_str], self.out_message_id)
        result["volume_type"] = from_union([from_int, from_str], self.volume_type)
        return result


class CollisionVolV1381_67_09_PC:
    def __init__(self, body, class_name, link_header, link_name, name):
        self.body = body
        self.class_name = class_name
        self.link_header = link_header
        self.link_name = link_name
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        body = CollisionVolV1381_67_09PCBody.from_dict(obj.get("body"))
        class_name = from_union([from_int, from_str], obj.get("class_name"))
        link_header = CameraV1381_67_09PCLinkHeader.from_dict(obj.get("link_header"))
        link_name = from_union([from_none, from_int, from_str], obj.get("link_name"))
        name = from_union([from_int, from_str], obj.get("name"))
        return CollisionVolV1381_67_09_PC(
            body, class_name, link_header, link_name, name
        )

    def to_dict(self):
        result = {}
        result["body"] = to_class(CollisionVolV1381_67_09PCBody, self.body)
        result["class_name"] = from_union([from_int, from_str], self.class_name)
        result["link_header"] = to_class(
            CameraV1381_67_09PCLinkHeader, self.link_header
        )
        if self.link_name is not None:
            result["link_name"] = from_union(
                [from_none, from_int, from_str], self.link_name
            )
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class CollisionVol:
    def __init__(self, collision_vol_v1_291_03_06_pc, collision_vol_v1_381_67_09_pc):
        self.collision_vol_v1_291_03_06_pc = collision_vol_v1_291_03_06_pc
        self.collision_vol_v1_381_67_09_pc = collision_vol_v1_381_67_09_pc

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        collision_vol_v1_291_03_06_pc = from_union(
            [CollisionVolV1291_03_06_PC.from_dict, from_none],
            obj.get("CollisionVolV1_291_03_06PC"),
        )
        collision_vol_v1_381_67_09_pc = from_union(
            [CollisionVolV1381_67_09_PC.from_dict, from_none],
            obj.get("CollisionVolV1_381_67_09PC"),
        )
        return CollisionVol(
            collision_vol_v1_291_03_06_pc, collision_vol_v1_381_67_09_pc
        )

    def to_dict(self):
        result = {}
        if self.collision_vol_v1_291_03_06_pc is not None:
            result["CollisionVolV1_291_03_06PC"] = from_union(
                [lambda x: to_class(CollisionVolV1291_03_06_PC, x), from_none],
                self.collision_vol_v1_291_03_06_pc,
            )
        if self.collision_vol_v1_381_67_09_pc is not None:
            result["CollisionVolV1_381_67_09PC"] = from_union(
                [lambda x: to_class(CollisionVolV1381_67_09_PC, x), from_none],
                self.collision_vol_v1_381_67_09_pc,
            )
        return result


class CharacterValue:
    def __init__(self, bottom_right_corner, descent, material_index, top_left_corner):
        self.bottom_right_corner = bottom_right_corner
        self.descent = descent
        self.material_index = material_index
        self.top_left_corner = top_left_corner

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        bottom_right_corner = from_list(from_float, obj.get("bottom_right_corner"))
        descent = from_float(obj.get("descent"))
        material_index = from_int(obj.get("material_index"))
        top_left_corner = from_list(from_float, obj.get("top_left_corner"))
        return CharacterValue(
            bottom_right_corner, descent, material_index, top_left_corner
        )

    def to_dict(self):
        result = {}
        result["bottom_right_corner"] = from_list(to_float, self.bottom_right_corner)
        result["descent"] = to_float(self.descent)
        result["material_index"] = from_int(self.material_index)
        result["top_left_corner"] = from_list(to_float, self.top_left_corner)
        return result


class FontsV106_63_02PCBody:
    def __init__(self, characters, material_names):
        self.characters = characters
        self.material_names = material_names

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        characters = from_dict(CharacterValue.from_dict, obj.get("characters"))
        material_names = from_list(
            lambda x: from_union([from_int, from_str], x), obj.get("material_names")
        )
        return FontsV106_63_02PCBody(characters, material_names)

    def to_dict(self):
        result = {}
        result["characters"] = from_dict(
            lambda x: to_class(CharacterValue, x), self.characters
        )
        result["material_names"] = from_list(
            lambda x: from_union([from_int, from_str], x), self.material_names
        )
        return result


class FontsV106_63_02_PC:
    def __init__(self, body, class_name, link_header, link_name, name):
        self.body = body
        self.class_name = class_name
        self.link_header = link_header
        self.link_name = link_name
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        body = FontsV106_63_02PCBody.from_dict(obj.get("body"))
        class_name = from_union([from_int, from_str], obj.get("class_name"))
        link_header = AnimationV1291_03_06PCLinkHeader.from_dict(obj.get("link_header"))
        link_name = from_union([from_none, from_int, from_str], obj.get("link_name"))
        name = from_union([from_int, from_str], obj.get("name"))
        return FontsV106_63_02_PC(body, class_name, link_header, link_name, name)

    def to_dict(self):
        result = {}
        result["body"] = to_class(FontsV106_63_02PCBody, self.body)
        result["class_name"] = from_union([from_int, from_str], self.class_name)
        result["link_header"] = to_class(
            AnimationV1291_03_06PCLinkHeader, self.link_header
        )
        if self.link_name is not None:
            result["link_name"] = from_union(
                [from_none, from_int, from_str], self.link_name
            )
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class FontsV1381_67_09PCBody:
    def __init__(self, characters, material_names):
        self.characters = characters
        self.material_names = material_names

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        characters = from_dict(CharacterValue.from_dict, obj.get("characters"))
        material_names = from_list(
            lambda x: from_union([from_int, from_str], x), obj.get("material_names")
        )
        return FontsV1381_67_09PCBody(characters, material_names)

    def to_dict(self):
        result = {}
        result["characters"] = from_dict(
            lambda x: to_class(CharacterValue, x), self.characters
        )
        result["material_names"] = from_list(
            lambda x: from_union([from_int, from_str], x), self.material_names
        )
        return result


class FontsV1381_67_09_PC:
    def __init__(self, body, class_name, link_header, link_name, name):
        self.body = body
        self.class_name = class_name
        self.link_header = link_header
        self.link_name = link_name
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        body = FontsV1381_67_09PCBody.from_dict(obj.get("body"))
        class_name = from_union([from_int, from_str], obj.get("class_name"))
        link_header = AnimationV1381_67_09PCLinkHeader.from_dict(obj.get("link_header"))
        link_name = from_union([from_none, from_int, from_str], obj.get("link_name"))
        name = from_union([from_int, from_str], obj.get("name"))
        return FontsV1381_67_09_PC(body, class_name, link_header, link_name, name)

    def to_dict(self):
        result = {}
        result["body"] = to_class(FontsV1381_67_09PCBody, self.body)
        result["class_name"] = from_union([from_int, from_str], self.class_name)
        result["link_header"] = to_class(
            AnimationV1381_67_09PCLinkHeader, self.link_header
        )
        if self.link_name is not None:
            result["link_name"] = from_union(
                [from_none, from_int, from_str], self.link_name
            )
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class Fonts:
    def __init__(self, fonts_v1_06_63_02_pc, fonts_v1_381_67_09_pc):
        self.fonts_v1_06_63_02_pc = fonts_v1_06_63_02_pc
        self.fonts_v1_381_67_09_pc = fonts_v1_381_67_09_pc

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        fonts_v1_06_63_02_pc = from_union(
            [FontsV106_63_02_PC.from_dict, from_none], obj.get("FontsV1_06_63_02PC")
        )
        fonts_v1_381_67_09_pc = from_union(
            [FontsV1381_67_09_PC.from_dict, from_none], obj.get("FontsV1_381_67_09PC")
        )
        return Fonts(fonts_v1_06_63_02_pc, fonts_v1_381_67_09_pc)

    def to_dict(self):
        result = {}
        if self.fonts_v1_06_63_02_pc is not None:
            result["FontsV1_06_63_02PC"] = from_union(
                [lambda x: to_class(FontsV106_63_02_PC, x), from_none],
                self.fonts_v1_06_63_02_pc,
            )
        if self.fonts_v1_381_67_09_pc is not None:
            result["FontsV1_381_67_09PC"] = from_union(
                [lambda x: to_class(FontsV1381_67_09_PC, x), from_none],
                self.fonts_v1_381_67_09_pc,
            )
        return result


class GameObjV1291_03_06PCBody:
    def __init__(self, node_names):
        self.node_names = node_names

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        node_names = from_list(
            lambda x: from_union([from_int, from_str], x), obj.get("node_names")
        )
        return GameObjV1291_03_06PCBody(node_names)

    def to_dict(self):
        result = {}
        result["node_names"] = from_list(
            lambda x: from_union([from_int, from_str], x), self.node_names
        )
        return result


class GameObjV1291_03_06_PC:
    def __init__(self, body, class_name, link_header, link_name, name):
        self.body = body
        self.class_name = class_name
        self.link_header = link_header
        self.link_name = link_name
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        body = GameObjV1291_03_06PCBody.from_dict(obj.get("body"))
        class_name = from_union([from_int, from_str], obj.get("class_name"))
        link_header = AnimationV1291_03_06PCLinkHeader.from_dict(obj.get("link_header"))
        link_name = from_union([from_none, from_int, from_str], obj.get("link_name"))
        name = from_union([from_int, from_str], obj.get("name"))
        return GameObjV1291_03_06_PC(body, class_name, link_header, link_name, name)

    def to_dict(self):
        result = {}
        result["body"] = to_class(GameObjV1291_03_06PCBody, self.body)
        result["class_name"] = from_union([from_int, from_str], self.class_name)
        result["link_header"] = to_class(
            AnimationV1291_03_06PCLinkHeader, self.link_header
        )
        if self.link_name is not None:
            result["link_name"] = from_union(
                [from_none, from_int, from_str], self.link_name
            )
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class PrefabElement:
    def __init__(self, in_world, names, string):
        self.in_world = in_world
        self.names = names
        self.string = string

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        in_world = from_int(obj.get("in_world"))
        names = from_list(
            lambda x: from_union([from_int, from_str], x), obj.get("names")
        )
        string = from_str(obj.get("string"))
        return PrefabElement(in_world, names, string)

    def to_dict(self):
        result = {}
        result["in_world"] = from_int(self.in_world)
        result["names"] = from_list(
            lambda x: from_union([from_int, from_str], x), self.names
        )
        result["string"] = from_str(self.string)
        return result


class GameObjV1381_67_09PCBody:
    def __init__(self, prefabs):
        self.prefabs = prefabs

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        prefabs = from_list(PrefabElement.from_dict, obj.get("prefabs"))
        return GameObjV1381_67_09PCBody(prefabs)

    def to_dict(self):
        result = {}
        result["prefabs"] = from_list(
            lambda x: to_class(PrefabElement, x), self.prefabs
        )
        return result


class GameObjV1381_67_09_PC:
    def __init__(self, body, class_name, link_header, link_name, name):
        self.body = body
        self.class_name = class_name
        self.link_header = link_header
        self.link_name = link_name
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        body = GameObjV1381_67_09PCBody.from_dict(obj.get("body"))
        class_name = from_union([from_int, from_str], obj.get("class_name"))
        link_header = AnimationV1381_67_09PCLinkHeader.from_dict(obj.get("link_header"))
        link_name = from_union([from_none, from_int, from_str], obj.get("link_name"))
        name = from_union([from_int, from_str], obj.get("name"))
        return GameObjV1381_67_09_PC(body, class_name, link_header, link_name, name)

    def to_dict(self):
        result = {}
        result["body"] = to_class(GameObjV1381_67_09PCBody, self.body)
        result["class_name"] = from_union([from_int, from_str], self.class_name)
        result["link_header"] = to_class(
            AnimationV1381_67_09PCLinkHeader, self.link_header
        )
        if self.link_name is not None:
            result["link_name"] = from_union(
                [from_none, from_int, from_str], self.link_name
            )
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class GameObj:
    def __init__(self, game_obj_v1_291_03_06_pc, game_obj_v1_381_67_09_pc):
        self.game_obj_v1_291_03_06_pc = game_obj_v1_291_03_06_pc
        self.game_obj_v1_381_67_09_pc = game_obj_v1_381_67_09_pc

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        game_obj_v1_291_03_06_pc = from_union(
            [GameObjV1291_03_06_PC.from_dict, from_none],
            obj.get("GameObjV1_291_03_06PC"),
        )
        game_obj_v1_381_67_09_pc = from_union(
            [GameObjV1381_67_09_PC.from_dict, from_none],
            obj.get("GameObjV1_381_67_09PC"),
        )
        return GameObj(game_obj_v1_291_03_06_pc, game_obj_v1_381_67_09_pc)

    def to_dict(self):
        result = {}
        if self.game_obj_v1_291_03_06_pc is not None:
            result["GameObjV1_291_03_06PC"] = from_union(
                [lambda x: to_class(GameObjV1291_03_06_PC, x), from_none],
                self.game_obj_v1_291_03_06_pc,
            )
        if self.game_obj_v1_381_67_09_pc is not None:
            result["GameObjV1_381_67_09PC"] = from_union(
                [lambda x: to_class(GameObjV1381_67_09_PC, x), from_none],
                self.game_obj_v1_381_67_09_pc,
            )
        return result


class CAFlatSurfaceElement:
    def __init__(
        self,
        a,
        b,
        c,
        mat,
        reciprocal,
        unknown1,
        unknown2,
        unknown20,
        unknown21,
        unknown22,
        unknown23,
        unknown24,
        unknown3,
        unknown4,
        unknown9,
        vec,
        zero0,
        zero1,
        zero2,
        zero3,
        zero4,
    ):
        self.a = a
        self.b = b
        self.c = c
        self.mat = mat
        self.reciprocal = reciprocal
        self.unknown1 = unknown1
        self.unknown2 = unknown2
        self.unknown20 = unknown20
        self.unknown21 = unknown21
        self.unknown22 = unknown22
        self.unknown23 = unknown23
        self.unknown24 = unknown24
        self.unknown3 = unknown3
        self.unknown4 = unknown4
        self.unknown9 = unknown9
        self.vec = vec
        self.zero0 = zero0
        self.zero1 = zero1
        self.zero2 = zero2
        self.zero3 = zero3
        self.zero4 = zero4

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        a = from_float(obj.get("a"))
        b = from_float(obj.get("b"))
        c = from_float(obj.get("c"))
        mat = from_list(lambda x: from_list(from_float, x), obj.get("mat"))
        reciprocal = from_float(obj.get("reciprocal"))
        unknown1 = from_float(obj.get("unknown1"))
        unknown2 = from_int(obj.get("unknown2"))
        unknown20 = from_int(obj.get("unknown20"))
        unknown21 = from_int(obj.get("unknown21"))
        unknown22 = from_int(obj.get("unknown22"))
        unknown23 = from_int(obj.get("unknown23"))
        unknown24 = from_int(obj.get("unknown24"))
        unknown3 = from_float(obj.get("unknown3"))
        unknown4 = from_int(obj.get("unknown4"))
        unknown9 = from_int(obj.get("unknown9"))
        vec = from_list(from_float, obj.get("vec"))
        zero0 = from_int(obj.get("zero0"))
        zero1 = from_int(obj.get("zero1"))
        zero2 = from_int(obj.get("zero2"))
        zero3 = from_int(obj.get("zero3"))
        zero4 = from_int(obj.get("zero4"))
        return CAFlatSurfaceElement(
            a,
            b,
            c,
            mat,
            reciprocal,
            unknown1,
            unknown2,
            unknown20,
            unknown21,
            unknown22,
            unknown23,
            unknown24,
            unknown3,
            unknown4,
            unknown9,
            vec,
            zero0,
            zero1,
            zero2,
            zero3,
            zero4,
        )

    def to_dict(self):
        result = {}
        result["a"] = to_float(self.a)
        result["b"] = to_float(self.b)
        result["c"] = to_float(self.c)
        result["mat"] = from_list(lambda x: from_list(to_float, x), self.mat)
        result["reciprocal"] = to_float(self.reciprocal)
        result["unknown1"] = to_float(self.unknown1)
        result["unknown2"] = from_int(self.unknown2)
        result["unknown20"] = from_int(self.unknown20)
        result["unknown21"] = from_int(self.unknown21)
        result["unknown22"] = from_int(self.unknown22)
        result["unknown23"] = from_int(self.unknown23)
        result["unknown24"] = from_int(self.unknown24)
        result["unknown3"] = to_float(self.unknown3)
        result["unknown4"] = from_int(self.unknown4)
        result["unknown9"] = from_int(self.unknown9)
        result["vec"] = from_list(to_float, self.vec)
        result["zero0"] = from_int(self.zero0)
        result["zero1"] = from_int(self.zero1)
        result["zero2"] = from_int(self.zero2)
        result["zero3"] = from_int(self.zero3)
        result["zero4"] = from_int(self.zero4)
        return result


class CategoryValue:
    def __init__(self, node_name_arrays, one):
        self.node_name_arrays = node_name_arrays
        self.one = one

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        node_name_arrays = from_list(
            lambda x: from_union([from_int, from_str], x), obj.get("node_name_arrays")
        )
        one = from_int(obj.get("one"))
        return CategoryValue(node_name_arrays, one)

    def to_dict(self):
        result = {}
        result["node_name_arrays"] = from_list(
            lambda x: from_union([from_int, from_str], x), self.node_name_arrays
        )
        result["one"] = from_int(self.one)
        return result


class RegionEdgeElement:
    def __init__(self, region_vertices_index_a, region_vertices_index_b):
        self.region_vertices_index_a = region_vertices_index_a
        self.region_vertices_index_b = region_vertices_index_b

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        region_vertices_index_a = from_int(obj.get("region_vertices_index_a"))
        region_vertices_index_b = from_int(obj.get("region_vertices_index_b"))
        return RegionEdgeElement(region_vertices_index_a, region_vertices_index_b)

    def to_dict(self):
        result = {}
        result["region_vertices_index_a"] = from_int(self.region_vertices_index_a)
        result["region_vertices_index_b"] = from_int(self.region_vertices_index_b)
        return result


class RegionValue:
    def __init__(self, region_edges_indices, unknown):
        self.region_edges_indices = region_edges_indices
        self.unknown = unknown

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        region_edges_indices = from_list(from_int, obj.get("region_edges_indices"))
        unknown = from_int(obj.get("unknown"))
        return RegionValue(region_edges_indices, unknown)

    def to_dict(self):
        result = {}
        result["region_edges_indices"] = from_list(from_int, self.region_edges_indices)
        result["unknown"] = from_int(self.unknown)
        return result


class Unused10Element:
    def __init__(self, unused0, unused1_s, unused2, unused3, unused4):
        self.unused0 = unused0
        self.unused1_s = unused1_s
        self.unused2 = unused2
        self.unused3 = unused3
        self.unused4 = unused4

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        unused0 = from_int(obj.get("unused0"))
        unused1_s = from_list(from_int, obj.get("unused1s"))
        unused2 = from_int(obj.get("unused2"))
        unused3 = from_int(obj.get("unused3"))
        unused4 = from_int(obj.get("unused4"))
        return Unused10Element(unused0, unused1_s, unused2, unused3, unused4)

    def to_dict(self):
        result = {}
        result["unused0"] = from_int(self.unused0)
        result["unused1s"] = from_list(from_int, self.unused1_s)
        result["unused2"] = from_int(self.unused2)
        result["unused3"] = from_int(self.unused3)
        result["unused4"] = from_int(self.unused4)
        return result


class GenWorldV1381_67_09PCBody:
    def __init__(
        self,
        binary_names,
        bitmap_names,
        ca_flat_surfaces,
        cancel_auto_mesh_placement,
        categories,
        equals41,
        gw_road_name,
        material_names,
        node_name,
        region_edges,
        region_vertices,
        regions,
        unused10_s,
        user_define_name,
    ):
        self.binary_names = binary_names
        self.bitmap_names = bitmap_names
        self.ca_flat_surfaces = ca_flat_surfaces
        self.cancel_auto_mesh_placement = cancel_auto_mesh_placement
        self.categories = categories
        self.equals41 = equals41
        self.gw_road_name = gw_road_name
        self.material_names = material_names
        self.node_name = node_name
        self.region_edges = region_edges
        self.region_vertices = region_vertices
        self.regions = regions
        self.unused10_s = unused10_s
        self.user_define_name = user_define_name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        binary_names = from_list(
            lambda x: from_union([from_int, from_str], x), obj.get("binary_names")
        )
        bitmap_names = from_list(
            lambda x: from_union([from_int, from_str], x), obj.get("bitmap_names")
        )
        ca_flat_surfaces = from_list(
            CAFlatSurfaceElement.from_dict, obj.get("ca_flat_surfaces")
        )
        cancel_auto_mesh_placement = from_list(
            lambda x: from_list(lambda x: from_list(from_float, x), x),
            obj.get("cancel_auto_mesh_placement"),
        )
        categories = from_dict(CategoryValue.from_dict, obj.get("categories"))
        equals41 = from_int(obj.get("equals41"))
        gw_road_name = from_union([from_int, from_str], obj.get("gw_road_name"))
        material_names = from_list(
            lambda x: from_union([from_int, from_str], x), obj.get("material_names")
        )
        node_name = from_union([from_int, from_str], obj.get("node_name"))
        region_edges = from_list(RegionEdgeElement.from_dict, obj.get("region_edges"))
        region_vertices = from_list(
            lambda x: from_list(from_float, x), obj.get("region_vertices")
        )
        regions = from_dict(RegionValue.from_dict, obj.get("regions"))
        unused10_s = from_list(Unused10Element.from_dict, obj.get("unused10s"))
        user_define_name = from_union([from_int, from_str], obj.get("user_define_name"))
        return GenWorldV1381_67_09PCBody(
            binary_names,
            bitmap_names,
            ca_flat_surfaces,
            cancel_auto_mesh_placement,
            categories,
            equals41,
            gw_road_name,
            material_names,
            node_name,
            region_edges,
            region_vertices,
            regions,
            unused10_s,
            user_define_name,
        )

    def to_dict(self):
        result = {}
        result["binary_names"] = from_list(
            lambda x: from_union([from_int, from_str], x), self.binary_names
        )
        result["bitmap_names"] = from_list(
            lambda x: from_union([from_int, from_str], x), self.bitmap_names
        )
        result["ca_flat_surfaces"] = from_list(
            lambda x: to_class(CAFlatSurfaceElement, x), self.ca_flat_surfaces
        )
        result["cancel_auto_mesh_placement"] = from_list(
            lambda x: from_list(lambda x: from_list(to_float, x), x),
            self.cancel_auto_mesh_placement,
        )
        result["categories"] = from_dict(
            lambda x: to_class(CategoryValue, x), self.categories
        )
        result["equals41"] = from_int(self.equals41)
        result["gw_road_name"] = from_union([from_int, from_str], self.gw_road_name)
        result["material_names"] = from_list(
            lambda x: from_union([from_int, from_str], x), self.material_names
        )
        result["node_name"] = from_union([from_int, from_str], self.node_name)
        result["region_edges"] = from_list(
            lambda x: to_class(RegionEdgeElement, x), self.region_edges
        )
        result["region_vertices"] = from_list(
            lambda x: from_list(to_float, x), self.region_vertices
        )
        result["regions"] = from_dict(lambda x: to_class(RegionValue, x), self.regions)
        result["unused10s"] = from_list(
            lambda x: to_class(Unused10Element, x), self.unused10_s
        )
        result["user_define_name"] = from_union(
            [from_int, from_str], self.user_define_name
        )
        return result


class GenWorldV1381_67_09_PC:
    def __init__(self, body, class_name, link_header, link_name, name):
        self.body = body
        self.class_name = class_name
        self.link_header = link_header
        self.link_name = link_name
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        body = GenWorldV1381_67_09PCBody.from_dict(obj.get("body"))
        class_name = from_union([from_int, from_str], obj.get("class_name"))
        link_header = CameraV1381_67_09PCLinkHeader.from_dict(obj.get("link_header"))
        link_name = from_union([from_none, from_int, from_str], obj.get("link_name"))
        name = from_union([from_int, from_str], obj.get("name"))
        return GenWorldV1381_67_09_PC(body, class_name, link_header, link_name, name)

    def to_dict(self):
        result = {}
        result["body"] = to_class(GenWorldV1381_67_09PCBody, self.body)
        result["class_name"] = from_union([from_int, from_str], self.class_name)
        result["link_header"] = to_class(
            CameraV1381_67_09PCLinkHeader, self.link_header
        )
        if self.link_name is not None:
            result["link_name"] = from_union(
                [from_none, from_int, from_str], self.link_name
            )
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class GenWorld:
    def __init__(self, gen_world_v1_381_67_09_pc):
        self.gen_world_v1_381_67_09_pc = gen_world_v1_381_67_09_pc

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        gen_world_v1_381_67_09_pc = GenWorldV1381_67_09_PC.from_dict(
            obj.get("GenWorldV1_381_67_09PC")
        )
        return GenWorld(gen_world_v1_381_67_09_pc)

    def to_dict(self):
        result = {}
        result["GenWorldV1_381_67_09PC"] = to_class(
            GenWorldV1381_67_09_PC, self.gen_world_v1_381_67_09_pc
        )
        return result


class TypeClass:
    def __init__(self, value):
        self.value = value

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        value = from_int(obj.get("value"))
        return TypeClass(value)

    def to_dict(self):
        result = {}
        result["value"] = from_int(self.value)
        return result


class RoadElement:
    def __init__(self, points, type):
        self.points = points
        self.type = type

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        points = from_list(lambda x: from_list(from_float, x), obj.get("points"))
        type = TypeClass.from_dict(obj.get("type"))
        return RoadElement(points, type)

    def to_dict(self):
        result = {}
        result["points"] = from_list(lambda x: from_list(to_float, x), self.points)
        result["type"] = to_class(TypeClass, self.type)
        return result


class Unused5Element:
    def __init__(
        self,
        unused0,
        unused1,
        unused2,
        unused3,
        unused4,
        unused5,
        unused6,
        unused7,
        unused8_s,
    ):
        self.unused0 = unused0
        self.unused1 = unused1
        self.unused2 = unused2
        self.unused3 = unused3
        self.unused4 = unused4
        self.unused5 = unused5
        self.unused6 = unused6
        self.unused7 = unused7
        self.unused8_s = unused8_s

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        unused0 = from_int(obj.get("unused0"))
        unused1 = from_int(obj.get("unused1"))
        unused2 = from_int(obj.get("unused2"))
        unused3 = from_int(obj.get("unused3"))
        unused4 = from_int(obj.get("unused4"))
        unused5 = from_int(obj.get("unused5"))
        unused6 = from_int(obj.get("unused6"))
        unused7 = from_int(obj.get("unused7"))
        unused8_s = from_list(from_int, obj.get("unused8s"))
        return Unused5Element(
            unused0,
            unused1,
            unused2,
            unused3,
            unused4,
            unused5,
            unused6,
            unused7,
            unused8_s,
        )

    def to_dict(self):
        result = {}
        result["unused0"] = from_int(self.unused0)
        result["unused1"] = from_int(self.unused1)
        result["unused2"] = from_int(self.unused2)
        result["unused3"] = from_int(self.unused3)
        result["unused4"] = from_int(self.unused4)
        result["unused5"] = from_int(self.unused5)
        result["unused6"] = from_int(self.unused6)
        result["unused7"] = from_int(self.unused7)
        result["unused8s"] = from_list(from_int, self.unused8_s)
        return result


class GwRoadV1381_67_09PCBody:
    def __init__(
        self,
        gen_road_max,
        gen_road_min,
        gen_world_name,
        road_count,
        roads,
        unused5_count,
        unused5_max,
        unused5_min,
        unused5_s,
    ):
        self.gen_road_max = gen_road_max
        self.gen_road_min = gen_road_min
        self.gen_world_name = gen_world_name
        self.road_count = road_count
        self.roads = roads
        self.unused5_count = unused5_count
        self.unused5_max = unused5_max
        self.unused5_min = unused5_min
        self.unused5_s = unused5_s

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        gen_road_max = from_list(from_float, obj.get("gen_road_max"))
        gen_road_min = from_list(from_float, obj.get("gen_road_min"))
        gen_world_name = from_union([from_int, from_str], obj.get("gen_world_name"))
        road_count = from_int(obj.get("road_count"))
        roads = from_list(RoadElement.from_dict, obj.get("roads"))
        unused5_count = from_int(obj.get("unused5_count"))
        unused5_max = from_list(from_float, obj.get("unused5_max"))
        unused5_min = from_list(from_float, obj.get("unused5_min"))
        unused5_s = from_list(Unused5Element.from_dict, obj.get("unused5s"))
        return GwRoadV1381_67_09PCBody(
            gen_road_max,
            gen_road_min,
            gen_world_name,
            road_count,
            roads,
            unused5_count,
            unused5_max,
            unused5_min,
            unused5_s,
        )

    def to_dict(self):
        result = {}
        result["gen_road_max"] = from_list(to_float, self.gen_road_max)
        result["gen_road_min"] = from_list(to_float, self.gen_road_min)
        result["gen_world_name"] = from_union([from_int, from_str], self.gen_world_name)
        result["road_count"] = from_int(self.road_count)
        result["roads"] = from_list(lambda x: to_class(RoadElement, x), self.roads)
        result["unused5_count"] = from_int(self.unused5_count)
        result["unused5_max"] = from_list(to_float, self.unused5_max)
        result["unused5_min"] = from_list(to_float, self.unused5_min)
        result["unused5s"] = from_list(
            lambda x: to_class(Unused5Element, x), self.unused5_s
        )
        return result


class GwRoadV1381_67_09_PC:
    def __init__(self, body, class_name, link_header, link_name, name):
        self.body = body
        self.class_name = class_name
        self.link_header = link_header
        self.link_name = link_name
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        body = GwRoadV1381_67_09PCBody.from_dict(obj.get("body"))
        class_name = from_union([from_int, from_str], obj.get("class_name"))
        link_header = AnimationV1381_67_09PCLinkHeader.from_dict(obj.get("link_header"))
        link_name = from_union([from_none, from_int, from_str], obj.get("link_name"))
        name = from_union([from_int, from_str], obj.get("name"))
        return GwRoadV1381_67_09_PC(body, class_name, link_header, link_name, name)

    def to_dict(self):
        result = {}
        result["body"] = to_class(GwRoadV1381_67_09PCBody, self.body)
        result["class_name"] = from_union([from_int, from_str], self.class_name)
        result["link_header"] = to_class(
            AnimationV1381_67_09PCLinkHeader, self.link_header
        )
        if self.link_name is not None:
            result["link_name"] = from_union(
                [from_none, from_int, from_str], self.link_name
            )
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class GwRoad:
    def __init__(self, gw_road_v1_381_67_09_pc):
        self.gw_road_v1_381_67_09_pc = gw_road_v1_381_67_09_pc

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        gw_road_v1_381_67_09_pc = GwRoadV1381_67_09_PC.from_dict(
            obj.get("GwRoadV1_381_67_09PC")
        )
        return GwRoad(gw_road_v1_381_67_09_pc)

    def to_dict(self):
        result = {}
        result["GwRoadV1_381_67_09PC"] = to_class(
            GwRoadV1381_67_09_PC, self.gw_road_v1_381_67_09_pc
        )
        return result


class LightV1291_03_06PCBody:
    def __init__(self, ambient, color, direction, position, rotation):
        self.ambient = ambient
        self.color = color
        self.direction = direction
        self.position = position
        self.rotation = rotation

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        ambient = from_list(from_float, obj.get("ambient"))
        color = from_list(from_float, obj.get("color"))
        direction = from_list(from_float, obj.get("direction"))
        position = from_list(from_float, obj.get("position"))
        rotation = from_list(from_float, obj.get("rotation"))
        return LightV1291_03_06PCBody(ambient, color, direction, position, rotation)

    def to_dict(self):
        result = {}
        result["ambient"] = from_list(to_float, self.ambient)
        result["color"] = from_list(to_float, self.color)
        result["direction"] = from_list(to_float, self.direction)
        result["position"] = from_list(to_float, self.position)
        result["rotation"] = from_list(to_float, self.rotation)
        return result


class LightV1291_03_06_PC:
    def __init__(self, body, class_name, link_header, link_name, name):
        self.body = body
        self.class_name = class_name
        self.link_header = link_header
        self.link_name = link_name
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        body = LightV1291_03_06PCBody.from_dict(obj.get("body"))
        class_name = from_union([from_int, from_str], obj.get("class_name"))
        link_header = CameraZoneV106_63_02PCLinkHeader.from_dict(obj.get("link_header"))
        link_name = from_union([from_none, from_int, from_str], obj.get("link_name"))
        name = from_union([from_int, from_str], obj.get("name"))
        return LightV1291_03_06_PC(body, class_name, link_header, link_name, name)

    def to_dict(self):
        result = {}
        result["body"] = to_class(LightV1291_03_06PCBody, self.body)
        result["class_name"] = from_union([from_int, from_str], self.class_name)
        result["link_header"] = to_class(
            CameraZoneV106_63_02PCLinkHeader, self.link_header
        )
        if self.link_name is not None:
            result["link_name"] = from_union(
                [from_none, from_int, from_str], self.link_name
            )
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class LightV1381_67_09PCBody:
    def __init__(self, ambient, color, direction, position, rotation):
        self.ambient = ambient
        self.color = color
        self.direction = direction
        self.position = position
        self.rotation = rotation

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        ambient = from_list(from_float, obj.get("ambient"))
        color = from_list(from_float, obj.get("color"))
        direction = from_list(from_float, obj.get("direction"))
        position = from_list(from_float, obj.get("position"))
        rotation = from_list(from_float, obj.get("rotation"))
        return LightV1381_67_09PCBody(ambient, color, direction, position, rotation)

    def to_dict(self):
        result = {}
        result["ambient"] = from_list(to_float, self.ambient)
        result["color"] = from_list(to_float, self.color)
        result["direction"] = from_list(to_float, self.direction)
        result["position"] = from_list(to_float, self.position)
        result["rotation"] = from_list(to_float, self.rotation)
        return result


class LightV1381_67_09_PC:
    def __init__(self, body, class_name, link_header, link_name, name):
        self.body = body
        self.class_name = class_name
        self.link_header = link_header
        self.link_name = link_name
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        body = LightV1381_67_09PCBody.from_dict(obj.get("body"))
        class_name = from_union([from_int, from_str], obj.get("class_name"))
        link_header = CameraV1381_67_09PCLinkHeader.from_dict(obj.get("link_header"))
        link_name = from_union([from_none, from_int, from_str], obj.get("link_name"))
        name = from_union([from_int, from_str], obj.get("name"))
        return LightV1381_67_09_PC(body, class_name, link_header, link_name, name)

    def to_dict(self):
        result = {}
        result["body"] = to_class(LightV1381_67_09PCBody, self.body)
        result["class_name"] = from_union([from_int, from_str], self.class_name)
        result["link_header"] = to_class(
            CameraV1381_67_09PCLinkHeader, self.link_header
        )
        if self.link_name is not None:
            result["link_name"] = from_union(
                [from_none, from_int, from_str], self.link_name
            )
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class Light:
    def __init__(self, light_v1_291_03_06_pc, light_v1_381_67_09_pc):
        self.light_v1_291_03_06_pc = light_v1_291_03_06_pc
        self.light_v1_381_67_09_pc = light_v1_381_67_09_pc

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        light_v1_291_03_06_pc = from_union(
            [LightV1291_03_06_PC.from_dict, from_none], obj.get("LightV1_291_03_06PC")
        )
        light_v1_381_67_09_pc = from_union(
            [LightV1381_67_09_PC.from_dict, from_none], obj.get("LightV1_381_67_09PC")
        )
        return Light(light_v1_291_03_06_pc, light_v1_381_67_09_pc)

    def to_dict(self):
        result = {}
        if self.light_v1_291_03_06_pc is not None:
            result["LightV1_291_03_06PC"] = from_union(
                [lambda x: to_class(LightV1291_03_06_PC, x), from_none],
                self.light_v1_291_03_06_pc,
            )
        if self.light_v1_381_67_09_pc is not None:
            result["LightV1_381_67_09PC"] = from_union(
                [lambda x: to_class(LightV1381_67_09_PC, x), from_none],
                self.light_v1_381_67_09_pc,
            )
        return result


class PurpleObjectDatas:
    def __init__(self, color, unknown):
        self.color = color
        self.unknown = unknown

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        color = from_list(from_float, obj.get("color"))
        unknown = from_float(obj.get("unknown"))
        return PurpleObjectDatas(color, unknown)

    def to_dict(self):
        result = {}
        result["color"] = from_list(to_float, self.color)
        result["unknown"] = to_float(self.unknown)
        return result


class LightDataV106_63_02PCBody:
    def __init__(self, ambient, color, direction, flag, object_datas, padding):
        self.ambient = ambient
        self.color = color
        self.direction = direction
        self.flag = flag
        self.object_datas = object_datas
        self.padding = padding

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        ambient = from_list(from_float, obj.get("ambient"))
        color = from_list(from_float, obj.get("color"))
        direction = from_list(from_float, obj.get("direction"))
        flag = from_int(obj.get("flag"))
        object_datas = PurpleObjectDatas.from_dict(obj.get("object_datas"))
        padding = from_list(from_int, obj.get("padding"))
        return LightDataV106_63_02PCBody(
            ambient, color, direction, flag, object_datas, padding
        )

    def to_dict(self):
        result = {}
        result["ambient"] = from_list(to_float, self.ambient)
        result["color"] = from_list(to_float, self.color)
        result["direction"] = from_list(to_float, self.direction)
        result["flag"] = from_int(self.flag)
        result["object_datas"] = to_class(PurpleObjectDatas, self.object_datas)
        result["padding"] = from_list(from_int, self.padding)
        return result


class LightDataV106_63_02_PC:
    def __init__(self, body, class_name, link_header, link_name, name):
        self.body = body
        self.class_name = class_name
        self.link_header = link_header
        self.link_name = link_name
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        body = LightDataV106_63_02PCBody.from_dict(obj.get("body"))
        class_name = from_union([from_int, from_str], obj.get("class_name"))
        link_header = AnimationV1291_03_06PCLinkHeader.from_dict(obj.get("link_header"))
        link_name = from_union([from_none, from_int, from_str], obj.get("link_name"))
        name = from_union([from_int, from_str], obj.get("name"))
        return LightDataV106_63_02_PC(body, class_name, link_header, link_name, name)

    def to_dict(self):
        result = {}
        result["body"] = to_class(LightDataV106_63_02PCBody, self.body)
        result["class_name"] = from_union([from_int, from_str], self.class_name)
        result["link_header"] = to_class(
            AnimationV1291_03_06PCLinkHeader, self.link_header
        )
        if self.link_name is not None:
            result["link_name"] = from_union(
                [from_none, from_int, from_str], self.link_name
            )
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class FluffyObjectDatas:
    def __init__(self, color):
        self.color = color

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        color = from_list(from_float, obj.get("color"))
        return FluffyObjectDatas(color)

    def to_dict(self):
        result = {}
        result["color"] = from_list(to_float, self.color)
        return result


class LightDataV1291_03_06PCBody:
    def __init__(self, ambient, color, flag, object_datas, padding):
        self.ambient = ambient
        self.color = color
        self.flag = flag
        self.object_datas = object_datas
        self.padding = padding

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        ambient = from_list(from_float, obj.get("ambient"))
        color = from_list(from_float, obj.get("color"))
        flag = from_int(obj.get("flag"))
        object_datas = FluffyObjectDatas.from_dict(obj.get("object_datas"))
        padding = from_list(from_int, obj.get("padding"))
        return LightDataV1291_03_06PCBody(ambient, color, flag, object_datas, padding)

    def to_dict(self):
        result = {}
        result["ambient"] = from_list(to_float, self.ambient)
        result["color"] = from_list(to_float, self.color)
        result["flag"] = from_int(self.flag)
        result["object_datas"] = to_class(FluffyObjectDatas, self.object_datas)
        result["padding"] = from_list(from_int, self.padding)
        return result


class LightDataV1291_03_06_PC:
    def __init__(self, body, class_name, link_header, link_name, name):
        self.body = body
        self.class_name = class_name
        self.link_header = link_header
        self.link_name = link_name
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        body = LightDataV1291_03_06PCBody.from_dict(obj.get("body"))
        class_name = from_union([from_int, from_str], obj.get("class_name"))
        link_header = AnimationV1291_03_06PCLinkHeader.from_dict(obj.get("link_header"))
        link_name = from_union([from_none, from_int, from_str], obj.get("link_name"))
        name = from_union([from_int, from_str], obj.get("name"))
        return LightDataV1291_03_06_PC(body, class_name, link_header, link_name, name)

    def to_dict(self):
        result = {}
        result["body"] = to_class(LightDataV1291_03_06PCBody, self.body)
        result["class_name"] = from_union([from_int, from_str], self.class_name)
        result["link_header"] = to_class(
            AnimationV1291_03_06PCLinkHeader, self.link_header
        )
        if self.link_name is not None:
            result["link_name"] = from_union(
                [from_none, from_int, from_str], self.link_name
            )
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class ResourceDatasFlags:
    def __init__(self, value):
        self.value = value

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        value = from_int(obj.get("value"))
        return ResourceDatasFlags(value)

    def to_dict(self):
        result = {}
        result["value"] = from_int(self.value)
        return result


class LightDataV1381_67_09PCBody:
    def __init__(
        self,
        facing,
        flags,
        local_collision_sphere,
        local_collision_sphere_facing,
        resource_datas_flags,
        unused_vec,
    ):
        self.facing = facing
        self.flags = flags
        self.local_collision_sphere = local_collision_sphere
        self.local_collision_sphere_facing = local_collision_sphere_facing
        self.resource_datas_flags = resource_datas_flags
        self.unused_vec = unused_vec

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        facing = from_list(from_float, obj.get("facing"))
        flags = from_int(obj.get("flags"))
        local_collision_sphere = from_list(
            from_float, obj.get("local_collision_sphere")
        )
        local_collision_sphere_facing = from_list(
            from_float, obj.get("local_collision_sphere_facing")
        )
        resource_datas_flags = ResourceDatasFlags.from_dict(
            obj.get("resource_datas_flags")
        )
        unused_vec = from_list(from_int, obj.get("unused_vec"))
        return LightDataV1381_67_09PCBody(
            facing,
            flags,
            local_collision_sphere,
            local_collision_sphere_facing,
            resource_datas_flags,
            unused_vec,
        )

    def to_dict(self):
        result = {}
        result["facing"] = from_list(to_float, self.facing)
        result["flags"] = from_int(self.flags)
        result["local_collision_sphere"] = from_list(
            to_float, self.local_collision_sphere
        )
        result["local_collision_sphere_facing"] = from_list(
            to_float, self.local_collision_sphere_facing
        )
        result["resource_datas_flags"] = to_class(
            ResourceDatasFlags, self.resource_datas_flags
        )
        result["unused_vec"] = from_list(from_int, self.unused_vec)
        return result


class LightDataV1381_67_09_PC:
    def __init__(self, body, class_name, link_header, link_name, name):
        self.body = body
        self.class_name = class_name
        self.link_header = link_header
        self.link_name = link_name
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        body = LightDataV1381_67_09PCBody.from_dict(obj.get("body"))
        class_name = from_union([from_int, from_str], obj.get("class_name"))
        link_header = AnimationV1381_67_09PCLinkHeader.from_dict(obj.get("link_header"))
        link_name = from_union([from_none, from_int, from_str], obj.get("link_name"))
        name = from_union([from_int, from_str], obj.get("name"))
        return LightDataV1381_67_09_PC(body, class_name, link_header, link_name, name)

    def to_dict(self):
        result = {}
        result["body"] = to_class(LightDataV1381_67_09PCBody, self.body)
        result["class_name"] = from_union([from_int, from_str], self.class_name)
        result["link_header"] = to_class(
            AnimationV1381_67_09PCLinkHeader, self.link_header
        )
        if self.link_name is not None:
            result["link_name"] = from_union(
                [from_none, from_int, from_str], self.link_name
            )
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class LightData:
    def __init__(
        self,
        light_data_v1_06_63_02_pc,
        light_data_v1_291_03_06_pc,
        light_data_v1_381_67_09_pc,
    ):
        self.light_data_v1_06_63_02_pc = light_data_v1_06_63_02_pc
        self.light_data_v1_291_03_06_pc = light_data_v1_291_03_06_pc
        self.light_data_v1_381_67_09_pc = light_data_v1_381_67_09_pc

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        light_data_v1_06_63_02_pc = from_union(
            [LightDataV106_63_02_PC.from_dict, from_none],
            obj.get("LightDataV1_06_63_02PC"),
        )
        light_data_v1_291_03_06_pc = from_union(
            [LightDataV1291_03_06_PC.from_dict, from_none],
            obj.get("LightDataV1_291_03_06PC"),
        )
        light_data_v1_381_67_09_pc = from_union(
            [LightDataV1381_67_09_PC.from_dict, from_none],
            obj.get("LightDataV1_381_67_09PC"),
        )
        return LightData(
            light_data_v1_06_63_02_pc,
            light_data_v1_291_03_06_pc,
            light_data_v1_381_67_09_pc,
        )

    def to_dict(self):
        result = {}
        if self.light_data_v1_06_63_02_pc is not None:
            result["LightDataV1_06_63_02PC"] = from_union(
                [lambda x: to_class(LightDataV106_63_02_PC, x), from_none],
                self.light_data_v1_06_63_02_pc,
            )
        if self.light_data_v1_291_03_06_pc is not None:
            result["LightDataV1_291_03_06PC"] = from_union(
                [lambda x: to_class(LightDataV1291_03_06_PC, x), from_none],
                self.light_data_v1_291_03_06_pc,
            )
        if self.light_data_v1_381_67_09_pc is not None:
            result["LightDataV1_381_67_09PC"] = from_union(
                [lambda x: to_class(LightDataV1381_67_09_PC, x), from_none],
                self.light_data_v1_381_67_09_pc,
            )
        return result


class AnimElement:
    def __init__(self, crc32, id):
        self.crc32 = crc32
        self.id = id

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        crc32 = from_union([from_int, from_str], obj.get("crc32"))
        id = from_int(obj.get("id"))
        return AnimElement(crc32, id)

    def to_dict(self):
        result = {}
        result["crc32"] = from_union([from_int, from_str], self.crc32)
        result["id"] = from_int(self.id)
        return result


class CollisionBoxElement:
    def __init__(self, flags, matrix, name):
        self.flags = flags
        self.matrix = matrix
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        flags = from_int(obj.get("flags"))
        matrix = from_list(lambda x: from_list(from_float, x), obj.get("matrix"))
        name = from_union([from_int, from_str], obj.get("name"))
        return CollisionBoxElement(flags, matrix, name)

    def to_dict(self):
        result = {}
        result["flags"] = from_int(self.flags)
        result["matrix"] = from_list(lambda x: from_list(to_float, x), self.matrix)
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class Segment:
    def __init__(self, direction, length, origin, pad):
        self.direction = direction
        self.length = length
        self.origin = origin
        self.pad = pad

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        direction = from_list(from_float, obj.get("direction"))
        length = from_float(obj.get("length"))
        origin = from_list(from_float, obj.get("origin"))
        pad = from_float(obj.get("pad"))
        return Segment(direction, length, origin, pad)

    def to_dict(self):
        result = {}
        result["direction"] = from_list(to_float, self.direction)
        result["length"] = to_float(self.length)
        result["origin"] = from_list(to_float, self.origin)
        result["pad"] = to_float(self.pad)
        return result


class Cylindre:
    def __init__(self, radius, seg):
        self.radius = radius
        self.seg = seg

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        radius = from_float(obj.get("radius"))
        seg = Segment.from_dict(obj.get("seg"))
        return Cylindre(radius, seg)

    def to_dict(self):
        result = {}
        result["radius"] = to_float(self.radius)
        result["seg"] = to_class(Segment, self.seg)
        return result


class TentacledSchema:
    def __init__(self, cylindre, flag, name):
        self.cylindre = cylindre
        self.flag = flag
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        cylindre = Cylindre.from_dict(obj.get("cylindre"))
        flag = from_int(obj.get("flag"))
        name = from_union([from_int, from_str], obj.get("name"))
        return TentacledSchema(cylindre, flag, name)

    def to_dict(self):
        result = {}
        result["cylindre"] = to_class(Cylindre, self.cylindre)
        result["flag"] = from_int(self.flag)
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class StickySchema:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        data = from_list(from_int, obj.get("data"))
        return StickySchema(data)

    def to_dict(self):
        result = {}
        result["data"] = from_list(from_int, self.data)
        return result


class SpheresColElement:
    def __init__(self, flags, name, sphere):
        self.flags = flags
        self.name = name
        self.sphere = sphere

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        flags = from_int(obj.get("flags"))
        name = from_union([from_int, from_str], obj.get("name"))
        sphere = Sphere.from_dict(obj.get("sphere"))
        return SpheresColElement(flags, name, sphere)

    def to_dict(self):
        result = {}
        result["flags"] = from_int(self.flags)
        result["name"] = from_union([from_int, from_str], self.name)
        result["sphere"] = to_class(Sphere, self.sphere)
        return result


class LodV106_63_02PCBody:
    def __init__(
        self,
        anims,
        b_sphere_col_node,
        box_cols,
        close,
        component_names,
        cylindre_cols,
        shadow_name,
        sounds,
        sphere_col_node,
        spheres_cols,
        user_define_name,
    ):
        self.anims = anims
        self.b_sphere_col_node = b_sphere_col_node
        self.box_cols = box_cols
        self.close = close
        self.component_names = component_names
        self.cylindre_cols = cylindre_cols
        self.shadow_name = shadow_name
        self.sounds = sounds
        self.sphere_col_node = sphere_col_node
        self.spheres_cols = spheres_cols
        self.user_define_name = user_define_name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        anims = from_list(AnimElement.from_dict, obj.get("anims"))
        b_sphere_col_node = from_union(
            [from_int, from_str], obj.get("b_sphere_col_node")
        )
        box_cols = from_list(CollisionBoxElement.from_dict, obj.get("box_cols"))
        close = from_list(from_float, obj.get("close"))
        component_names = from_list(
            lambda x: from_union([from_int, from_str], x), obj.get("component_names")
        )
        cylindre_cols = from_list(TentacledSchema.from_dict, obj.get("cylindre_cols"))
        shadow_name = from_union([from_int, from_str], obj.get("shadow_name"))
        sounds = from_union(
            [from_none, lambda x: from_list(AnimElement.from_dict, x)],
            obj.get("sounds"),
        )
        sphere_col_node = from_union(
            [StickySchema.from_dict, from_none], obj.get("sphere_col_node")
        )
        spheres_cols = from_list(SpheresColElement.from_dict, obj.get("spheres_cols"))
        user_define_name = from_union([from_int, from_str], obj.get("user_define_name"))
        return LodV106_63_02PCBody(
            anims,
            b_sphere_col_node,
            box_cols,
            close,
            component_names,
            cylindre_cols,
            shadow_name,
            sounds,
            sphere_col_node,
            spheres_cols,
            user_define_name,
        )

    def to_dict(self):
        result = {}
        result["anims"] = from_list(lambda x: to_class(AnimElement, x), self.anims)
        result["b_sphere_col_node"] = from_union(
            [from_int, from_str], self.b_sphere_col_node
        )
        result["box_cols"] = from_list(
            lambda x: to_class(CollisionBoxElement, x), self.box_cols
        )
        result["close"] = from_list(to_float, self.close)
        result["component_names"] = from_list(
            lambda x: from_union([from_int, from_str], x), self.component_names
        )
        result["cylindre_cols"] = from_list(
            lambda x: to_class(TentacledSchema, x), self.cylindre_cols
        )
        result["shadow_name"] = from_union([from_int, from_str], self.shadow_name)
        if self.sounds is not None:
            result["sounds"] = from_union(
                [from_none, lambda x: from_list(lambda x: to_class(AnimElement, x), x)],
                self.sounds,
            )
        if self.sphere_col_node is not None:
            result["sphere_col_node"] = from_union(
                [lambda x: to_class(StickySchema, x), from_none], self.sphere_col_node
            )
        result["spheres_cols"] = from_list(
            lambda x: to_class(SpheresColElement, x), self.spheres_cols
        )
        result["user_define_name"] = from_union(
            [from_int, from_str], self.user_define_name
        )
        return result


class LodV106_63_02_PC:
    def __init__(self, body, class_name, link_header, link_name, name):
        self.body = body
        self.class_name = class_name
        self.link_header = link_header
        self.link_name = link_name
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        body = LodV106_63_02PCBody.from_dict(obj.get("body"))
        class_name = from_union([from_int, from_str], obj.get("class_name"))
        link_header = CameraZoneV106_63_02PCLinkHeader.from_dict(obj.get("link_header"))
        link_name = from_union([from_none, from_int, from_str], obj.get("link_name"))
        name = from_union([from_int, from_str], obj.get("name"))
        return LodV106_63_02_PC(body, class_name, link_header, link_name, name)

    def to_dict(self):
        result = {}
        result["body"] = to_class(LodV106_63_02PCBody, self.body)
        result["class_name"] = from_union([from_int, from_str], self.class_name)
        result["link_header"] = to_class(
            CameraZoneV106_63_02PCLinkHeader, self.link_header
        )
        if self.link_name is not None:
            result["link_name"] = from_union(
                [from_none, from_int, from_str], self.link_name
            )
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class InnerElement:
    def __init__(self, crc32, id):
        self.crc32 = crc32
        self.id = id

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        crc32 = from_union([from_int, from_str], obj.get("crc32"))
        id = from_int(obj.get("id"))
        return InnerElement(crc32, id)

    def to_dict(self):
        result = {}
        result["crc32"] = from_union([from_int, from_str], self.crc32)
        result["id"] = from_int(self.id)
        return result


class Anims:
    def __init__(self, inner):
        self.inner = inner

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        inner = from_union(
            [from_none, lambda x: from_list(InnerElement.from_dict, x)],
            obj.get("inner"),
        )
        return Anims(inner)

    def to_dict(self):
        result = {}
        if self.inner is not None:
            result["inner"] = from_union(
                [
                    from_none,
                    lambda x: from_list(lambda x: to_class(InnerElement, x), x),
                ],
                self.inner,
            )
        return result


class CylinderColElement:
    def __init__(self, cylindre, flag, name):
        self.cylindre = cylindre
        self.flag = flag
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        cylindre = Cylindre.from_dict(obj.get("cylindre"))
        flag = from_int(obj.get("flag"))
        name = from_union([from_int, from_str], obj.get("name"))
        return CylinderColElement(cylindre, flag, name)

    def to_dict(self):
        result = {}
        result["cylindre"] = to_class(Cylindre, self.cylindre)
        result["flag"] = from_int(self.flag)
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class IndigoSchema:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        data = from_list(from_int, obj.get("data"))
        return IndigoSchema(data)

    def to_dict(self):
        result = {}
        result["data"] = from_list(from_int, self.data)
        return result


class LodV1291_03_06PCBody:
    def __init__(
        self,
        anims,
        b_sphere_col_node,
        box_cols,
        close,
        component_names,
        cylinder_cols,
        shadow_name,
        sounds,
        sphere_col_node,
        sphere_cols,
        user_define_name,
    ):
        self.anims = anims
        self.b_sphere_col_node = b_sphere_col_node
        self.box_cols = box_cols
        self.close = close
        self.component_names = component_names
        self.cylinder_cols = cylinder_cols
        self.shadow_name = shadow_name
        self.sounds = sounds
        self.sphere_col_node = sphere_col_node
        self.sphere_cols = sphere_cols
        self.user_define_name = user_define_name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        anims = from_union([Anims.from_dict, from_none], obj.get("anims"))
        b_sphere_col_node = from_union(
            [from_int, from_str], obj.get("b_sphere_col_node")
        )
        box_cols = from_list(CollisionBoxElement.from_dict, obj.get("box_cols"))
        close = from_list(from_float, obj.get("close"))
        component_names = from_list(
            lambda x: from_union([from_int, from_str], x), obj.get("component_names")
        )
        cylinder_cols = from_list(
            CylinderColElement.from_dict, obj.get("cylinder_cols")
        )
        shadow_name = from_union([from_int, from_str], obj.get("shadow_name"))
        sounds = from_union([Anims.from_dict, from_none], obj.get("sounds"))
        sphere_col_node = from_union(
            [IndigoSchema.from_dict, from_none], obj.get("sphere_col_node")
        )
        sphere_cols = from_list(SpheresColElement.from_dict, obj.get("sphere_cols"))
        user_define_name = from_union([from_int, from_str], obj.get("user_define_name"))
        return LodV1291_03_06PCBody(
            anims,
            b_sphere_col_node,
            box_cols,
            close,
            component_names,
            cylinder_cols,
            shadow_name,
            sounds,
            sphere_col_node,
            sphere_cols,
            user_define_name,
        )

    def to_dict(self):
        result = {}
        if self.anims is not None:
            result["anims"] = from_union(
                [lambda x: to_class(Anims, x), from_none], self.anims
            )
        result["b_sphere_col_node"] = from_union(
            [from_int, from_str], self.b_sphere_col_node
        )
        result["box_cols"] = from_list(
            lambda x: to_class(CollisionBoxElement, x), self.box_cols
        )
        result["close"] = from_list(to_float, self.close)
        result["component_names"] = from_list(
            lambda x: from_union([from_int, from_str], x), self.component_names
        )
        result["cylinder_cols"] = from_list(
            lambda x: to_class(CylinderColElement, x), self.cylinder_cols
        )
        result["shadow_name"] = from_union([from_int, from_str], self.shadow_name)
        if self.sounds is not None:
            result["sounds"] = from_union(
                [lambda x: to_class(Anims, x), from_none], self.sounds
            )
        if self.sphere_col_node is not None:
            result["sphere_col_node"] = from_union(
                [lambda x: to_class(IndigoSchema, x), from_none], self.sphere_col_node
            )
        result["sphere_cols"] = from_list(
            lambda x: to_class(SpheresColElement, x), self.sphere_cols
        )
        result["user_define_name"] = from_union(
            [from_int, from_str], self.user_define_name
        )
        return result


class LodV1291_03_06_PC:
    def __init__(self, body, class_name, link_header, link_name, name):
        self.body = body
        self.class_name = class_name
        self.link_header = link_header
        self.link_name = link_name
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        body = LodV1291_03_06PCBody.from_dict(obj.get("body"))
        class_name = from_union([from_int, from_str], obj.get("class_name"))
        link_header = CameraZoneV106_63_02PCLinkHeader.from_dict(obj.get("link_header"))
        link_name = from_union([from_none, from_int, from_str], obj.get("link_name"))
        name = from_union([from_int, from_str], obj.get("name"))
        return LodV1291_03_06_PC(body, class_name, link_header, link_name, name)

    def to_dict(self):
        result = {}
        result["body"] = to_class(LodV1291_03_06PCBody, self.body)
        result["class_name"] = from_union([from_int, from_str], self.class_name)
        result["link_header"] = to_class(
            CameraZoneV106_63_02PCLinkHeader, self.link_header
        )
        if self.link_name is not None:
            result["link_name"] = from_union(
                [from_none, from_int, from_str], self.link_name
            )
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class AnimationEntriesInner:
    def __init__(
        self,
    ):
        pass

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        return AnimationEntriesInner()

    def to_dict(self):
        result = {}
        return result


class AnimationEntries:
    def __init__(self, inner):
        self.inner = inner

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        inner = from_union(
            [from_none, AnimationEntriesInner.from_dict], obj.get("inner")
        )
        return AnimationEntries(inner)

    def to_dict(self):
        result = {}
        if self.inner is not None:
            result["inner"] = from_union(
                [from_none, lambda x: to_class(AnimationEntriesInner, x)], self.inner
            )
        return result


class PurpleFade:
    def __init__(self, fade_close, x, y):
        self.fade_close = fade_close
        self.x = x
        self.y = y

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        fade_close = from_float(obj.get("fade_close"))
        x = from_float(obj.get("x"))
        y = from_float(obj.get("y"))
        return PurpleFade(fade_close, x, y)

    def to_dict(self):
        result = {}
        result["fade_close"] = to_float(self.fade_close)
        result["x"] = to_float(self.x)
        result["y"] = to_float(self.y)
        return result


class LodV1381_67_09PCBody:
    def __init__(
        self,
        animation_entries,
        collision_boxes,
        collision_spheres,
        fade,
        skin_or_mesh_or_particles_names,
        sound_entries,
        user_define_name,
        zero,
    ):
        self.animation_entries = animation_entries
        self.collision_boxes = collision_boxes
        self.collision_spheres = collision_spheres
        self.fade = fade
        self.skin_or_mesh_or_particles_names = skin_or_mesh_or_particles_names
        self.sound_entries = sound_entries
        self.user_define_name = user_define_name
        self.zero = zero

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        animation_entries = from_union(
            [AnimationEntries.from_dict, from_none], obj.get("animation_entries")
        )
        collision_boxes = from_list(
            CollisionBoxElement.from_dict, obj.get("collision_boxes")
        )
        collision_spheres = from_list(
            SpheresColElement.from_dict, obj.get("collision_spheres")
        )
        fade = PurpleFade.from_dict(obj.get("fade"))
        skin_or_mesh_or_particles_names = from_list(
            lambda x: from_union([from_int, from_str], x),
            obj.get("skin_or_mesh_or_particles_names"),
        )
        sound_entries = from_union(
            [AnimationEntries.from_dict, from_none], obj.get("sound_entries")
        )
        user_define_name = from_union([from_int, from_str], obj.get("user_define_name"))
        zero = from_int(obj.get("zero"))
        return LodV1381_67_09PCBody(
            animation_entries,
            collision_boxes,
            collision_spheres,
            fade,
            skin_or_mesh_or_particles_names,
            sound_entries,
            user_define_name,
            zero,
        )

    def to_dict(self):
        result = {}
        if self.animation_entries is not None:
            result["animation_entries"] = from_union(
                [lambda x: to_class(AnimationEntries, x), from_none],
                self.animation_entries,
            )
        result["collision_boxes"] = from_list(
            lambda x: to_class(CollisionBoxElement, x), self.collision_boxes
        )
        result["collision_spheres"] = from_list(
            lambda x: to_class(SpheresColElement, x), self.collision_spheres
        )
        result["fade"] = to_class(PurpleFade, self.fade)
        result["skin_or_mesh_or_particles_names"] = from_list(
            lambda x: from_union([from_int, from_str], x),
            self.skin_or_mesh_or_particles_names,
        )
        if self.sound_entries is not None:
            result["sound_entries"] = from_union(
                [lambda x: to_class(AnimationEntries, x), from_none], self.sound_entries
            )
        result["user_define_name"] = from_union(
            [from_int, from_str], self.user_define_name
        )
        result["zero"] = from_int(self.zero)
        return result


class LodV1381_67_09_PC:
    def __init__(self, body, class_name, link_header, link_name, name):
        self.body = body
        self.class_name = class_name
        self.link_header = link_header
        self.link_name = link_name
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        body = LodV1381_67_09PCBody.from_dict(obj.get("body"))
        class_name = from_union([from_int, from_str], obj.get("class_name"))
        link_header = CameraV1381_67_09PCLinkHeader.from_dict(obj.get("link_header"))
        link_name = from_union([from_none, from_int, from_str], obj.get("link_name"))
        name = from_union([from_int, from_str], obj.get("name"))
        return LodV1381_67_09_PC(body, class_name, link_header, link_name, name)

    def to_dict(self):
        result = {}
        result["body"] = to_class(LodV1381_67_09PCBody, self.body)
        result["class_name"] = from_union([from_int, from_str], self.class_name)
        result["link_header"] = to_class(
            CameraV1381_67_09PCLinkHeader, self.link_header
        )
        if self.link_name is not None:
            result["link_name"] = from_union(
                [from_none, from_int, from_str], self.link_name
            )
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class Lod:
    def __init__(self, lod_v1_06_63_02_pc, lod_v1_291_03_06_pc, lod_v1_381_67_09_pc):
        self.lod_v1_06_63_02_pc = lod_v1_06_63_02_pc
        self.lod_v1_291_03_06_pc = lod_v1_291_03_06_pc
        self.lod_v1_381_67_09_pc = lod_v1_381_67_09_pc

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        lod_v1_06_63_02_pc = from_union(
            [LodV106_63_02_PC.from_dict, from_none], obj.get("LodV1_06_63_02PC")
        )
        lod_v1_291_03_06_pc = from_union(
            [LodV1291_03_06_PC.from_dict, from_none], obj.get("LodV1_291_03_06PC")
        )
        lod_v1_381_67_09_pc = from_union(
            [LodV1381_67_09_PC.from_dict, from_none], obj.get("LodV1_381_67_09PC")
        )
        return Lod(lod_v1_06_63_02_pc, lod_v1_291_03_06_pc, lod_v1_381_67_09_pc)

    def to_dict(self):
        result = {}
        if self.lod_v1_06_63_02_pc is not None:
            result["LodV1_06_63_02PC"] = from_union(
                [lambda x: to_class(LodV106_63_02_PC, x), from_none],
                self.lod_v1_06_63_02_pc,
            )
        if self.lod_v1_291_03_06_pc is not None:
            result["LodV1_291_03_06PC"] = from_union(
                [lambda x: to_class(LodV1291_03_06_PC, x), from_none],
                self.lod_v1_291_03_06_pc,
            )
        if self.lod_v1_381_67_09_pc is not None:
            result["LodV1_381_67_09PC"] = from_union(
                [lambda x: to_class(LodV1381_67_09_PC, x), from_none],
                self.lod_v1_381_67_09_pc,
            )
        return result


class UnkStructElement:
    def __init__(self, unk1_name, unk2_name, unk3_name, unks):
        self.unk1_name = unk1_name
        self.unk2_name = unk2_name
        self.unk3_name = unk3_name
        self.unks = unks

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        unk1_name = from_union([from_int, from_str], obj.get("unk1_name"))
        unk2_name = from_union([from_int, from_str], obj.get("unk2_name"))
        unk3_name = from_union([from_int, from_str], obj.get("unk3_name"))
        unks = from_list(from_int, obj.get("unks"))
        return UnkStructElement(unk1_name, unk2_name, unk3_name, unks)

    def to_dict(self):
        result = {}
        result["unk1_name"] = from_union([from_int, from_str], self.unk1_name)
        result["unk2_name"] = from_union([from_int, from_str], self.unk2_name)
        result["unk3_name"] = from_union([from_int, from_str], self.unk3_name)
        result["unks"] = from_list(from_int, self.unks)
        return result


class ActorDataInner:
    def __init__(
        self,
        flag,
        placeholder1,
        placeholder2,
        placeholder3,
        placeholder4,
        unk_bytes1,
        unk_floats1,
        unk_name,
        unk_structs,
        unk_uints1,
        zero1,
    ):
        self.flag = flag
        self.placeholder1 = placeholder1
        self.placeholder2 = placeholder2
        self.placeholder3 = placeholder3
        self.placeholder4 = placeholder4
        self.unk_bytes1 = unk_bytes1
        self.unk_floats1 = unk_floats1
        self.unk_name = unk_name
        self.unk_structs = unk_structs
        self.unk_uints1 = unk_uints1
        self.zero1 = zero1

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        flag = from_int(obj.get("flag"))
        placeholder1 = from_list(from_int, obj.get("placeholder1"))
        placeholder2 = from_list(from_int, obj.get("placeholder2"))
        placeholder3 = from_list(from_int, obj.get("placeholder3"))
        placeholder4 = from_list(from_int, obj.get("placeholder4"))
        unk_bytes1 = from_list(from_int, obj.get("unk_bytes1"))
        unk_floats1 = from_list(from_float, obj.get("unk_floats1"))
        unk_name = from_union([from_int, from_str], obj.get("unk_name"))
        unk_structs = from_list(UnkStructElement.from_dict, obj.get("unk_structs"))
        unk_uints1 = from_list(from_int, obj.get("unk_uints1"))
        zero1 = from_int(obj.get("zero1"))
        return ActorDataInner(
            flag,
            placeholder1,
            placeholder2,
            placeholder3,
            placeholder4,
            unk_bytes1,
            unk_floats1,
            unk_name,
            unk_structs,
            unk_uints1,
            zero1,
        )

    def to_dict(self):
        result = {}
        result["flag"] = from_int(self.flag)
        result["placeholder1"] = from_list(from_int, self.placeholder1)
        result["placeholder2"] = from_list(from_int, self.placeholder2)
        result["placeholder3"] = from_list(from_int, self.placeholder3)
        result["placeholder4"] = from_list(from_int, self.placeholder4)
        result["unk_bytes1"] = from_list(from_int, self.unk_bytes1)
        result["unk_floats1"] = from_list(to_float, self.unk_floats1)
        result["unk_name"] = from_union([from_int, from_str], self.unk_name)
        result["unk_structs"] = from_list(
            lambda x: to_class(UnkStructElement, x), self.unk_structs
        )
        result["unk_uints1"] = from_list(from_int, self.unk_uints1)
        result["zero1"] = from_int(self.zero1)
        return result


class ActorData:
    def __init__(self, inner):
        self.inner = inner

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        inner = from_union([ActorDataInner.from_dict, from_none], obj.get("inner"))
        return ActorData(inner)

    def to_dict(self):
        result = {}
        if self.inner is not None:
            result["inner"] = from_union(
                [lambda x: to_class(ActorDataInner, x), from_none], self.inner
            )
        return result


class TentacledObjectDatas:
    def __init__(self, color, flags):
        self.color = color
        self.flags = flags

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        color = from_list(from_float, obj.get("color"))
        flags = from_int(obj.get("flags"))
        return TentacledObjectDatas(color, flags)

    def to_dict(self):
        result = {}
        result["color"] = from_list(to_float, self.color)
        result["flags"] = from_int(self.flags)
        return result


class LodDataV106_63_02PCBody:
    def __init__(
        self, actor_data, final_skel_name, mesh_data_or_skelcrc32_s, object_datas
    ):
        self.actor_data = actor_data
        self.final_skel_name = final_skel_name
        self.mesh_data_or_skelcrc32_s = mesh_data_or_skelcrc32_s
        self.object_datas = object_datas

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        actor_data = from_union([ActorData.from_dict, from_none], obj.get("actor_data"))
        final_skel_name = from_union([from_int, from_str], obj.get("final_skel_name"))
        mesh_data_or_skelcrc32_s = from_list(
            lambda x: from_union([from_int, from_str], x),
            obj.get("mesh_data_or_skelcrc32s"),
        )
        object_datas = TentacledObjectDatas.from_dict(obj.get("object_datas"))
        return LodDataV106_63_02PCBody(
            actor_data, final_skel_name, mesh_data_or_skelcrc32_s, object_datas
        )

    def to_dict(self):
        result = {}
        if self.actor_data is not None:
            result["actor_data"] = from_union(
                [lambda x: to_class(ActorData, x), from_none], self.actor_data
            )
        result["final_skel_name"] = from_union(
            [from_int, from_str], self.final_skel_name
        )
        result["mesh_data_or_skelcrc32s"] = from_list(
            lambda x: from_union([from_int, from_str], x), self.mesh_data_or_skelcrc32_s
        )
        result["object_datas"] = to_class(TentacledObjectDatas, self.object_datas)
        return result


class LodDataV106_63_02_PC:
    def __init__(self, body, class_name, link_header, link_name, name):
        self.body = body
        self.class_name = class_name
        self.link_header = link_header
        self.link_name = link_name
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        body = LodDataV106_63_02PCBody.from_dict(obj.get("body"))
        class_name = from_union([from_int, from_str], obj.get("class_name"))
        link_header = AnimationV1291_03_06PCLinkHeader.from_dict(obj.get("link_header"))
        link_name = from_union([from_none, from_int, from_str], obj.get("link_name"))
        name = from_union([from_int, from_str], obj.get("name"))
        return LodDataV106_63_02_PC(body, class_name, link_header, link_name, name)

    def to_dict(self):
        result = {}
        result["body"] = to_class(LodDataV106_63_02PCBody, self.body)
        result["class_name"] = from_union([from_int, from_str], self.class_name)
        result["link_header"] = to_class(
            AnimationV1291_03_06PCLinkHeader, self.link_header
        )
        if self.link_name is not None:
            result["link_name"] = from_union(
                [from_none, from_int, from_str], self.link_name
            )
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class IndecentSchema:
    def __init__(
        self,
        flags,
        padding,
        scale,
        unknown0,
        unknown1,
        zero0,
        zero1_s,
        zero2_s,
        zero3_s,
    ):
        self.flags = flags
        self.padding = padding
        self.scale = scale
        self.unknown0 = unknown0
        self.unknown1 = unknown1
        self.zero0 = zero0
        self.zero1_s = zero1_s
        self.zero2_s = zero2_s
        self.zero3_s = zero3_s

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        flags = from_int(obj.get("flags"))
        padding = from_list(from_int, obj.get("padding"))
        scale = from_list(from_float, obj.get("scale"))
        unknown0 = from_int(obj.get("unknown0"))
        unknown1 = from_int(obj.get("unknown1"))
        zero0 = from_int(obj.get("zero0"))
        zero1_s = from_list(from_int, obj.get("zero1s"))
        zero2_s = from_list(from_int, obj.get("zero2s"))
        zero3_s = from_list(from_int, obj.get("zero3s"))
        return IndecentSchema(
            flags, padding, scale, unknown0, unknown1, zero0, zero1_s, zero2_s, zero3_s
        )

    def to_dict(self):
        result = {}
        result["flags"] = from_int(self.flags)
        result["padding"] = from_list(from_int, self.padding)
        result["scale"] = from_list(to_float, self.scale)
        result["unknown0"] = from_int(self.unknown0)
        result["unknown1"] = from_int(self.unknown1)
        result["zero0"] = from_int(self.zero0)
        result["zero1s"] = from_list(from_int, self.zero1_s)
        result["zero2s"] = from_list(from_int, self.zero2_s)
        result["zero3s"] = from_list(from_int, self.zero3_s)
        return result


class PurpleExtended:
    def __init__(self, inner):
        self.inner = inner

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        inner = from_union([IndecentSchema.from_dict, from_none], obj.get("inner"))
        return PurpleExtended(inner)

    def to_dict(self):
        result = {}
        if self.inner is not None:
            result["inner"] = from_union(
                [lambda x: to_class(IndecentSchema, x), from_none], self.inner
            )
        return result


class LodDataV1291_03_06PCBody:
    def __init__(self, extended, flags, mesh_data_names, zero):
        self.extended = extended
        self.flags = flags
        self.mesh_data_names = mesh_data_names
        self.zero = zero

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        extended = from_union(
            [PurpleExtended.from_dict, from_none], obj.get("extended")
        )
        flags = from_int(obj.get("flags"))
        mesh_data_names = from_list(
            lambda x: from_union([from_int, from_str], x), obj.get("mesh_data_names")
        )
        zero = from_int(obj.get("zero"))
        return LodDataV1291_03_06PCBody(extended, flags, mesh_data_names, zero)

    def to_dict(self):
        result = {}
        if self.extended is not None:
            result["extended"] = from_union(
                [lambda x: to_class(PurpleExtended, x), from_none], self.extended
            )
        result["flags"] = from_int(self.flags)
        result["mesh_data_names"] = from_list(
            lambda x: from_union([from_int, from_str], x), self.mesh_data_names
        )
        result["zero"] = from_int(self.zero)
        return result


class LodDataV1291_03_06_PC:
    def __init__(self, body, class_name, link_header, link_name, name):
        self.body = body
        self.class_name = class_name
        self.link_header = link_header
        self.link_name = link_name
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        body = LodDataV1291_03_06PCBody.from_dict(obj.get("body"))
        class_name = from_union([from_int, from_str], obj.get("class_name"))
        link_header = AnimationV1291_03_06PCLinkHeader.from_dict(obj.get("link_header"))
        link_name = from_union([from_none, from_int, from_str], obj.get("link_name"))
        name = from_union([from_int, from_str], obj.get("name"))
        return LodDataV1291_03_06_PC(body, class_name, link_header, link_name, name)

    def to_dict(self):
        result = {}
        result["body"] = to_class(LodDataV1291_03_06PCBody, self.body)
        result["class_name"] = from_union([from_int, from_str], self.class_name)
        result["link_header"] = to_class(
            AnimationV1291_03_06PCLinkHeader, self.link_header
        )
        if self.link_name is not None:
            result["link_name"] = from_union(
                [from_none, from_int, from_str], self.link_name
            )
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class HilariousSchema:
    def __init__(
        self,
        equals0_x004000000,
        equals0_x004000001,
        flags1,
        pad,
        scale,
        zero1,
        zero10,
        zero11,
        zero2,
        zero3,
        zero4,
        zero5,
        zero6,
        zero7,
        zero8,
        zero9,
    ):
        self.equals0_x004000000 = equals0_x004000000
        self.equals0_x004000001 = equals0_x004000001
        self.flags1 = flags1
        self.pad = pad
        self.scale = scale
        self.zero1 = zero1
        self.zero10 = zero10
        self.zero11 = zero11
        self.zero2 = zero2
        self.zero3 = zero3
        self.zero4 = zero4
        self.zero5 = zero5
        self.zero6 = zero6
        self.zero7 = zero7
        self.zero8 = zero8
        self.zero9 = zero9

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        equals0_x004000000 = from_int(obj.get("equals0x004000000"))
        equals0_x004000001 = from_int(obj.get("equals0x004000001"))
        flags1 = from_int(obj.get("flags1"))
        pad = from_list(from_int, obj.get("pad"))
        scale = from_list(from_float, obj.get("scale"))
        zero1 = from_int(obj.get("zero1"))
        zero10 = from_int(obj.get("zero10"))
        zero11 = from_int(obj.get("zero11"))
        zero2 = from_int(obj.get("zero2"))
        zero3 = from_int(obj.get("zero3"))
        zero4 = from_int(obj.get("zero4"))
        zero5 = from_int(obj.get("zero5"))
        zero6 = from_int(obj.get("zero6"))
        zero7 = from_int(obj.get("zero7"))
        zero8 = from_int(obj.get("zero8"))
        zero9 = from_int(obj.get("zero9"))
        return HilariousSchema(
            equals0_x004000000,
            equals0_x004000001,
            flags1,
            pad,
            scale,
            zero1,
            zero10,
            zero11,
            zero2,
            zero3,
            zero4,
            zero5,
            zero6,
            zero7,
            zero8,
            zero9,
        )

    def to_dict(self):
        result = {}
        result["equals0x004000000"] = from_int(self.equals0_x004000000)
        result["equals0x004000001"] = from_int(self.equals0_x004000001)
        result["flags1"] = from_int(self.flags1)
        result["pad"] = from_list(from_int, self.pad)
        result["scale"] = from_list(to_float, self.scale)
        result["zero1"] = from_int(self.zero1)
        result["zero10"] = from_int(self.zero10)
        result["zero11"] = from_int(self.zero11)
        result["zero2"] = from_int(self.zero2)
        result["zero3"] = from_int(self.zero3)
        result["zero4"] = from_int(self.zero4)
        result["zero5"] = from_int(self.zero5)
        result["zero6"] = from_int(self.zero6)
        result["zero7"] = from_int(self.zero7)
        result["zero8"] = from_int(self.zero8)
        result["zero9"] = from_int(self.zero9)
        return result


class FluffyExtended:
    def __init__(self, inner):
        self.inner = inner

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        inner = from_union([HilariousSchema.from_dict, from_none], obj.get("inner"))
        return FluffyExtended(inner)

    def to_dict(self):
        result = {}
        if self.inner is not None:
            result["inner"] = from_union(
                [lambda x: to_class(HilariousSchema, x), from_none], self.inner
            )
        return result


class LodDataV1381_67_09PCBody:
    def __init__(self, extended, flags, mesh_data_names, zero):
        self.extended = extended
        self.flags = flags
        self.mesh_data_names = mesh_data_names
        self.zero = zero

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        extended = from_union(
            [FluffyExtended.from_dict, from_none], obj.get("extended")
        )
        flags = ResourceDatasFlags.from_dict(obj.get("flags"))
        mesh_data_names = from_list(
            lambda x: from_union([from_int, from_str], x), obj.get("mesh_data_names")
        )
        zero = from_int(obj.get("zero"))
        return LodDataV1381_67_09PCBody(extended, flags, mesh_data_names, zero)

    def to_dict(self):
        result = {}
        if self.extended is not None:
            result["extended"] = from_union(
                [lambda x: to_class(FluffyExtended, x), from_none], self.extended
            )
        result["flags"] = to_class(ResourceDatasFlags, self.flags)
        result["mesh_data_names"] = from_list(
            lambda x: from_union([from_int, from_str], x), self.mesh_data_names
        )
        result["zero"] = from_int(self.zero)
        return result


class LodDataV1381_67_09_PC:
    def __init__(self, body, class_name, link_header, link_name, name):
        self.body = body
        self.class_name = class_name
        self.link_header = link_header
        self.link_name = link_name
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        body = LodDataV1381_67_09PCBody.from_dict(obj.get("body"))
        class_name = from_union([from_int, from_str], obj.get("class_name"))
        link_header = AnimationV1381_67_09PCLinkHeader.from_dict(obj.get("link_header"))
        link_name = from_union([from_none, from_int, from_str], obj.get("link_name"))
        name = from_union([from_int, from_str], obj.get("name"))
        return LodDataV1381_67_09_PC(body, class_name, link_header, link_name, name)

    def to_dict(self):
        result = {}
        result["body"] = to_class(LodDataV1381_67_09PCBody, self.body)
        result["class_name"] = from_union([from_int, from_str], self.class_name)
        result["link_header"] = to_class(
            AnimationV1381_67_09PCLinkHeader, self.link_header
        )
        if self.link_name is not None:
            result["link_name"] = from_union(
                [from_none, from_int, from_str], self.link_name
            )
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class LodData:
    def __init__(
        self,
        lod_data_v1_06_63_02_pc,
        lod_data_v1_291_03_06_pc,
        lod_data_v1_381_67_09_pc,
    ):
        self.lod_data_v1_06_63_02_pc = lod_data_v1_06_63_02_pc
        self.lod_data_v1_291_03_06_pc = lod_data_v1_291_03_06_pc
        self.lod_data_v1_381_67_09_pc = lod_data_v1_381_67_09_pc

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        lod_data_v1_06_63_02_pc = from_union(
            [LodDataV106_63_02_PC.from_dict, from_none], obj.get("LodDataV1_06_63_02PC")
        )
        lod_data_v1_291_03_06_pc = from_union(
            [LodDataV1291_03_06_PC.from_dict, from_none],
            obj.get("LodDataV1_291_03_06PC"),
        )
        lod_data_v1_381_67_09_pc = from_union(
            [LodDataV1381_67_09_PC.from_dict, from_none],
            obj.get("LodDataV1_381_67_09PC"),
        )
        return LodData(
            lod_data_v1_06_63_02_pc, lod_data_v1_291_03_06_pc, lod_data_v1_381_67_09_pc
        )

    def to_dict(self):
        result = {}
        if self.lod_data_v1_06_63_02_pc is not None:
            result["LodDataV1_06_63_02PC"] = from_union(
                [lambda x: to_class(LodDataV106_63_02_PC, x), from_none],
                self.lod_data_v1_06_63_02_pc,
            )
        if self.lod_data_v1_291_03_06_pc is not None:
            result["LodDataV1_291_03_06PC"] = from_union(
                [lambda x: to_class(LodDataV1291_03_06_PC, x), from_none],
                self.lod_data_v1_291_03_06_pc,
            )
        if self.lod_data_v1_381_67_09_pc is not None:
            result["LodDataV1_381_67_09PC"] = from_union(
                [lambda x: to_class(LodDataV1381_67_09_PC, x), from_none],
                self.lod_data_v1_381_67_09_pc,
            )
        return result


class MaterialV106_63_02PCBody:
    def __init__(
        self,
        cdcdcdcd,
        collision_flag,
        diffuse,
        emission,
        general_flag,
        object_flag,
        params,
        render_flag,
        rotation,
        scale,
        specular,
        specular_pow,
        textures,
        translation,
        uv_transform_matrix,
    ):
        self.cdcdcdcd = cdcdcdcd
        self.collision_flag = collision_flag
        self.diffuse = diffuse
        self.emission = emission
        self.general_flag = general_flag
        self.object_flag = object_flag
        self.params = params
        self.render_flag = render_flag
        self.rotation = rotation
        self.scale = scale
        self.specular = specular
        self.specular_pow = specular_pow
        self.textures = textures
        self.translation = translation
        self.uv_transform_matrix = uv_transform_matrix

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        cdcdcdcd = from_int(obj.get("cdcdcdcd"))
        collision_flag = from_int(obj.get("collision_flag"))
        diffuse = from_list(from_float, obj.get("diffuse"))
        emission = from_list(from_float, obj.get("emission"))
        general_flag = from_int(obj.get("general_flag"))
        object_flag = from_int(obj.get("object_flag"))
        params = from_list(from_float, obj.get("params"))
        render_flag = from_int(obj.get("render_flag"))
        rotation = from_float(obj.get("rotation"))
        scale = from_list(from_float, obj.get("scale"))
        specular = from_list(from_float, obj.get("specular"))
        specular_pow = from_float(obj.get("specular_pow"))
        textures = from_list(
            lambda x: from_union([from_int, from_str], x), obj.get("textures")
        )
        translation = from_list(from_float, obj.get("translation"))
        uv_transform_matrix = from_list(
            lambda x: from_list(from_float, x), obj.get("uv_transform_matrix")
        )
        return MaterialV106_63_02PCBody(
            cdcdcdcd,
            collision_flag,
            diffuse,
            emission,
            general_flag,
            object_flag,
            params,
            render_flag,
            rotation,
            scale,
            specular,
            specular_pow,
            textures,
            translation,
            uv_transform_matrix,
        )

    def to_dict(self):
        result = {}
        result["cdcdcdcd"] = from_int(self.cdcdcdcd)
        result["collision_flag"] = from_int(self.collision_flag)
        result["diffuse"] = from_list(to_float, self.diffuse)
        result["emission"] = from_list(to_float, self.emission)
        result["general_flag"] = from_int(self.general_flag)
        result["object_flag"] = from_int(self.object_flag)
        result["params"] = from_list(to_float, self.params)
        result["render_flag"] = from_int(self.render_flag)
        result["rotation"] = to_float(self.rotation)
        result["scale"] = from_list(to_float, self.scale)
        result["specular"] = from_list(to_float, self.specular)
        result["specular_pow"] = to_float(self.specular_pow)
        result["textures"] = from_list(
            lambda x: from_union([from_int, from_str], x), self.textures
        )
        result["translation"] = from_list(to_float, self.translation)
        result["uv_transform_matrix"] = from_list(
            lambda x: from_list(to_float, x), self.uv_transform_matrix
        )
        return result


class MaterialV106_63_02_PC:
    def __init__(self, body, class_name, link_header, link_name, name):
        self.body = body
        self.class_name = class_name
        self.link_header = link_header
        self.link_name = link_name
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        body = MaterialV106_63_02PCBody.from_dict(obj.get("body"))
        class_name = from_union([from_int, from_str], obj.get("class_name"))
        link_header = AnimationV1291_03_06PCLinkHeader.from_dict(obj.get("link_header"))
        link_name = from_union([from_none, from_int, from_str], obj.get("link_name"))
        name = from_union([from_int, from_str], obj.get("name"))
        return MaterialV106_63_02_PC(body, class_name, link_header, link_name, name)

    def to_dict(self):
        result = {}
        result["body"] = to_class(MaterialV106_63_02PCBody, self.body)
        result["class_name"] = from_union([from_int, from_str], self.class_name)
        result["link_header"] = to_class(
            AnimationV1291_03_06PCLinkHeader, self.link_header
        )
        if self.link_name is not None:
            result["link_name"] = from_union(
                [from_none, from_int, from_str], self.link_name
            )
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class MaterialV1291_03_06PCBody:
    def __init__(
        self,
        cdcdcdcd,
        diffuse,
        diffuse_rotation,
        diffuse_scale,
        diffuse_translation,
        emission,
        flags,
        texture_flag,
        textures,
        unknown1_s,
        unknown2_s,
        uv_transform_matrix,
    ):
        self.cdcdcdcd = cdcdcdcd
        self.diffuse = diffuse
        self.diffuse_rotation = diffuse_rotation
        self.diffuse_scale = diffuse_scale
        self.diffuse_translation = diffuse_translation
        self.emission = emission
        self.flags = flags
        self.texture_flag = texture_flag
        self.textures = textures
        self.unknown1_s = unknown1_s
        self.unknown2_s = unknown2_s
        self.uv_transform_matrix = uv_transform_matrix

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        cdcdcdcd = from_int(obj.get("cdcdcdcd"))
        diffuse = from_list(from_float, obj.get("diffuse"))
        diffuse_rotation = from_float(obj.get("diffuse_rotation"))
        diffuse_scale = from_list(from_float, obj.get("diffuse_scale"))
        diffuse_translation = from_list(from_float, obj.get("diffuse_translation"))
        emission = from_list(from_float, obj.get("emission"))
        flags = from_list(from_int, obj.get("flags"))
        texture_flag = from_int(obj.get("texture_flag"))
        textures = from_list(
            lambda x: from_union([from_int, from_str], x), obj.get("textures")
        )
        unknown1_s = from_list(from_float, obj.get("unknown1s"))
        unknown2_s = from_list(from_int, obj.get("unknown2s"))
        uv_transform_matrix = from_list(
            lambda x: from_list(from_float, x), obj.get("uv_transform_matrix")
        )
        return MaterialV1291_03_06PCBody(
            cdcdcdcd,
            diffuse,
            diffuse_rotation,
            diffuse_scale,
            diffuse_translation,
            emission,
            flags,
            texture_flag,
            textures,
            unknown1_s,
            unknown2_s,
            uv_transform_matrix,
        )

    def to_dict(self):
        result = {}
        result["cdcdcdcd"] = from_int(self.cdcdcdcd)
        result["diffuse"] = from_list(to_float, self.diffuse)
        result["diffuse_rotation"] = to_float(self.diffuse_rotation)
        result["diffuse_scale"] = from_list(to_float, self.diffuse_scale)
        result["diffuse_translation"] = from_list(to_float, self.diffuse_translation)
        result["emission"] = from_list(to_float, self.emission)
        result["flags"] = from_list(from_int, self.flags)
        result["texture_flag"] = from_int(self.texture_flag)
        result["textures"] = from_list(
            lambda x: from_union([from_int, from_str], x), self.textures
        )
        result["unknown1s"] = from_list(to_float, self.unknown1_s)
        result["unknown2s"] = from_list(from_int, self.unknown2_s)
        result["uv_transform_matrix"] = from_list(
            lambda x: from_list(to_float, x), self.uv_transform_matrix
        )
        return result


class MaterialV1291_03_06_PC:
    def __init__(self, body, class_name, link_header, link_name, name):
        self.body = body
        self.class_name = class_name
        self.link_header = link_header
        self.link_name = link_name
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        body = MaterialV1291_03_06PCBody.from_dict(obj.get("body"))
        class_name = from_union([from_int, from_str], obj.get("class_name"))
        link_header = AnimationV1291_03_06PCLinkHeader.from_dict(obj.get("link_header"))
        link_name = from_union([from_none, from_int, from_str], obj.get("link_name"))
        name = from_union([from_int, from_str], obj.get("name"))
        return MaterialV1291_03_06_PC(body, class_name, link_header, link_name, name)

    def to_dict(self):
        result = {}
        result["body"] = to_class(MaterialV1291_03_06PCBody, self.body)
        result["class_name"] = from_union([from_int, from_str], self.class_name)
        result["link_header"] = to_class(
            AnimationV1291_03_06PCLinkHeader, self.link_header
        )
        if self.link_name is not None:
            result["link_name"] = from_union(
                [from_none, from_int, from_str], self.link_name
            )
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class EnabledBitmaps:
    def __init__(self, value):
        self.value = value

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        value = from_int(obj.get("value"))
        return EnabledBitmaps(value)

    def to_dict(self):
        result = {}
        result["value"] = from_int(self.value)
        return result


class RdrFlag:
    def __init__(self, value):
        self.value = value

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        value = from_int(obj.get("value"))
        return RdrFlag(value)

    def to_dict(self):
        result = {}
        result["value"] = from_int(self.value)
        return result


class MaterialV1381_67_09PCBody:
    def __init__(
        self,
        alpha_ref,
        bump_map_factor,
        diffuse,
        emission,
        enabled_bitmaps,
        env_map_factor,
        flags1,
        param4,
        rdr_flag,
        s_add_normal_local_bitmap_name1,
        s_diffuse_bitmap_name,
        s_dirt_bitmap_name,
        s_normal_bitmap_name,
        s_normal_local_bitmap_name,
        s_occlusion_bitmap_name,
        s_specular_bitmap_name,
        some_number,
        something_bitmap_related,
        spec_map_factor,
        specular,
        t_matrix_bottom_right,
        t_matrix_offset,
        t_matrix_scale,
        t_matrix_top_left,
        t_rotation,
        t_scale,
        t_translation,
        unknown0,
        unused_bitmap_name0,
        unused_bitmap_name1,
    ):
        self.alpha_ref = alpha_ref
        self.bump_map_factor = bump_map_factor
        self.diffuse = diffuse
        self.emission = emission
        self.enabled_bitmaps = enabled_bitmaps
        self.env_map_factor = env_map_factor
        self.flags1 = flags1
        self.param4 = param4
        self.rdr_flag = rdr_flag
        self.s_add_normal_local_bitmap_name1 = s_add_normal_local_bitmap_name1
        self.s_diffuse_bitmap_name = s_diffuse_bitmap_name
        self.s_dirt_bitmap_name = s_dirt_bitmap_name
        self.s_normal_bitmap_name = s_normal_bitmap_name
        self.s_normal_local_bitmap_name = s_normal_local_bitmap_name
        self.s_occlusion_bitmap_name = s_occlusion_bitmap_name
        self.s_specular_bitmap_name = s_specular_bitmap_name
        self.some_number = some_number
        self.something_bitmap_related = something_bitmap_related
        self.spec_map_factor = spec_map_factor
        self.specular = specular
        self.t_matrix_bottom_right = t_matrix_bottom_right
        self.t_matrix_offset = t_matrix_offset
        self.t_matrix_scale = t_matrix_scale
        self.t_matrix_top_left = t_matrix_top_left
        self.t_rotation = t_rotation
        self.t_scale = t_scale
        self.t_translation = t_translation
        self.unknown0 = unknown0
        self.unused_bitmap_name0 = unused_bitmap_name0
        self.unused_bitmap_name1 = unused_bitmap_name1

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        alpha_ref = from_float(obj.get("alpha_ref"))
        bump_map_factor = from_float(obj.get("bump_map_factor"))
        diffuse = from_list(from_float, obj.get("diffuse"))
        emission = from_list(from_float, obj.get("emission"))
        enabled_bitmaps = EnabledBitmaps.from_dict(obj.get("enabled_bitmaps"))
        env_map_factor = from_float(obj.get("env_map_factor"))
        flags1 = from_int(obj.get("flags1"))
        param4 = from_float(obj.get("param4"))
        rdr_flag = RdrFlag.from_dict(obj.get("rdr_flag"))
        s_add_normal_local_bitmap_name1 = from_union(
            [from_int, from_str], obj.get("s_add_normal_local_bitmap_name1")
        )
        s_diffuse_bitmap_name = from_union(
            [from_int, from_str], obj.get("s_diffuse_bitmap_name")
        )
        s_dirt_bitmap_name = from_union(
            [from_int, from_str], obj.get("s_dirt_bitmap_name")
        )
        s_normal_bitmap_name = from_union(
            [from_int, from_str], obj.get("s_normal_bitmap_name")
        )
        s_normal_local_bitmap_name = from_union(
            [from_int, from_str], obj.get("s_normal_local_bitmap_name")
        )
        s_occlusion_bitmap_name = from_union(
            [from_int, from_str], obj.get("s_occlusion_bitmap_name")
        )
        s_specular_bitmap_name = from_union(
            [from_int, from_str], obj.get("s_specular_bitmap_name")
        )
        some_number = from_int(obj.get("some_number"))
        something_bitmap_related = from_list(
            from_float, obj.get("something_bitmap_related")
        )
        spec_map_factor = from_float(obj.get("spec_map_factor"))
        specular = from_list(from_float, obj.get("specular"))
        t_matrix_bottom_right = from_list(from_float, obj.get("t_matrix_bottom_right"))
        t_matrix_offset = from_list(from_float, obj.get("t_matrix_offset"))
        t_matrix_scale = from_float(obj.get("t_matrix_scale"))
        t_matrix_top_left = from_list(from_float, obj.get("t_matrix_top_left"))
        t_rotation = from_float(obj.get("t_rotation"))
        t_scale = from_list(from_float, obj.get("t_scale"))
        t_translation = from_list(from_float, obj.get("t_translation"))
        unknown0 = from_int(obj.get("unknown0"))
        unused_bitmap_name0 = from_union(
            [from_int, from_str], obj.get("unused_bitmap_name0")
        )
        unused_bitmap_name1 = from_union(
            [from_int, from_str], obj.get("unused_bitmap_name1")
        )
        return MaterialV1381_67_09PCBody(
            alpha_ref,
            bump_map_factor,
            diffuse,
            emission,
            enabled_bitmaps,
            env_map_factor,
            flags1,
            param4,
            rdr_flag,
            s_add_normal_local_bitmap_name1,
            s_diffuse_bitmap_name,
            s_dirt_bitmap_name,
            s_normal_bitmap_name,
            s_normal_local_bitmap_name,
            s_occlusion_bitmap_name,
            s_specular_bitmap_name,
            some_number,
            something_bitmap_related,
            spec_map_factor,
            specular,
            t_matrix_bottom_right,
            t_matrix_offset,
            t_matrix_scale,
            t_matrix_top_left,
            t_rotation,
            t_scale,
            t_translation,
            unknown0,
            unused_bitmap_name0,
            unused_bitmap_name1,
        )

    def to_dict(self):
        result = {}
        result["alpha_ref"] = to_float(self.alpha_ref)
        result["bump_map_factor"] = to_float(self.bump_map_factor)
        result["diffuse"] = from_list(to_float, self.diffuse)
        result["emission"] = from_list(to_float, self.emission)
        result["enabled_bitmaps"] = to_class(EnabledBitmaps, self.enabled_bitmaps)
        result["env_map_factor"] = to_float(self.env_map_factor)
        result["flags1"] = from_int(self.flags1)
        result["param4"] = to_float(self.param4)
        result["rdr_flag"] = to_class(RdrFlag, self.rdr_flag)
        result["s_add_normal_local_bitmap_name1"] = from_union(
            [from_int, from_str], self.s_add_normal_local_bitmap_name1
        )
        result["s_diffuse_bitmap_name"] = from_union(
            [from_int, from_str], self.s_diffuse_bitmap_name
        )
        result["s_dirt_bitmap_name"] = from_union(
            [from_int, from_str], self.s_dirt_bitmap_name
        )
        result["s_normal_bitmap_name"] = from_union(
            [from_int, from_str], self.s_normal_bitmap_name
        )
        result["s_normal_local_bitmap_name"] = from_union(
            [from_int, from_str], self.s_normal_local_bitmap_name
        )
        result["s_occlusion_bitmap_name"] = from_union(
            [from_int, from_str], self.s_occlusion_bitmap_name
        )
        result["s_specular_bitmap_name"] = from_union(
            [from_int, from_str], self.s_specular_bitmap_name
        )
        result["some_number"] = from_int(self.some_number)
        result["something_bitmap_related"] = from_list(
            to_float, self.something_bitmap_related
        )
        result["spec_map_factor"] = to_float(self.spec_map_factor)
        result["specular"] = from_list(to_float, self.specular)
        result["t_matrix_bottom_right"] = from_list(
            to_float, self.t_matrix_bottom_right
        )
        result["t_matrix_offset"] = from_list(to_float, self.t_matrix_offset)
        result["t_matrix_scale"] = to_float(self.t_matrix_scale)
        result["t_matrix_top_left"] = from_list(to_float, self.t_matrix_top_left)
        result["t_rotation"] = to_float(self.t_rotation)
        result["t_scale"] = from_list(to_float, self.t_scale)
        result["t_translation"] = from_list(to_float, self.t_translation)
        result["unknown0"] = from_int(self.unknown0)
        result["unused_bitmap_name0"] = from_union(
            [from_int, from_str], self.unused_bitmap_name0
        )
        result["unused_bitmap_name1"] = from_union(
            [from_int, from_str], self.unused_bitmap_name1
        )
        return result


class MaterialV1381_67_09_PC:
    def __init__(self, body, class_name, link_header, link_name, name):
        self.body = body
        self.class_name = class_name
        self.link_header = link_header
        self.link_name = link_name
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        body = MaterialV1381_67_09PCBody.from_dict(obj.get("body"))
        class_name = from_union([from_int, from_str], obj.get("class_name"))
        link_header = AnimationV1381_67_09PCLinkHeader.from_dict(obj.get("link_header"))
        link_name = from_union([from_none, from_int, from_str], obj.get("link_name"))
        name = from_union([from_int, from_str], obj.get("name"))
        return MaterialV1381_67_09_PC(body, class_name, link_header, link_name, name)

    def to_dict(self):
        result = {}
        result["body"] = to_class(MaterialV1381_67_09PCBody, self.body)
        result["class_name"] = from_union([from_int, from_str], self.class_name)
        result["link_header"] = to_class(
            AnimationV1381_67_09PCLinkHeader, self.link_header
        )
        if self.link_name is not None:
            result["link_name"] = from_union(
                [from_none, from_int, from_str], self.link_name
            )
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class Material:
    def __init__(
        self,
        material_v1_06_63_02_pc,
        material_v1_291_03_06_pc,
        material_v1_381_67_09_pc,
    ):
        self.material_v1_06_63_02_pc = material_v1_06_63_02_pc
        self.material_v1_291_03_06_pc = material_v1_291_03_06_pc
        self.material_v1_381_67_09_pc = material_v1_381_67_09_pc

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        material_v1_06_63_02_pc = from_union(
            [MaterialV106_63_02_PC.from_dict, from_none],
            obj.get("MaterialV1_06_63_02PC"),
        )
        material_v1_291_03_06_pc = from_union(
            [MaterialV1291_03_06_PC.from_dict, from_none],
            obj.get("MaterialV1_291_03_06PC"),
        )
        material_v1_381_67_09_pc = from_union(
            [MaterialV1381_67_09_PC.from_dict, from_none],
            obj.get("MaterialV1_381_67_09PC"),
        )
        return Material(
            material_v1_06_63_02_pc, material_v1_291_03_06_pc, material_v1_381_67_09_pc
        )

    def to_dict(self):
        result = {}
        if self.material_v1_06_63_02_pc is not None:
            result["MaterialV1_06_63_02PC"] = from_union(
                [lambda x: to_class(MaterialV106_63_02_PC, x), from_none],
                self.material_v1_06_63_02_pc,
            )
        if self.material_v1_291_03_06_pc is not None:
            result["MaterialV1_291_03_06PC"] = from_union(
                [lambda x: to_class(MaterialV1291_03_06_PC, x), from_none],
                self.material_v1_291_03_06_pc,
            )
        if self.material_v1_381_67_09_pc is not None:
            result["MaterialV1_381_67_09PC"] = from_union(
                [lambda x: to_class(MaterialV1381_67_09_PC, x), from_none],
                self.material_v1_381_67_09_pc,
            )
        return result


class AlphaKeyframerKeyframe:
    def __init__(self, time, value):
        self.time = time
        self.value = value

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        time = from_float(obj.get("time"))
        value = from_int(obj.get("value"))
        return AlphaKeyframerKeyframe(time, value)

    def to_dict(self):
        result = {}
        result["time"] = to_float(self.time)
        result["value"] = from_int(self.value)
        return result


class AlphaKeyframer:
    def __init__(self, interpolation_type, keyframes):
        self.interpolation_type = interpolation_type
        self.keyframes = keyframes

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        interpolation_type = InterpolationType(obj.get("interpolation_type"))
        keyframes = from_list(AlphaKeyframerKeyframe.from_dict, obj.get("keyframes"))
        return AlphaKeyframer(interpolation_type, keyframes)

    def to_dict(self):
        result = {}
        result["interpolation_type"] = to_enum(
            InterpolationType, self.interpolation_type
        )
        result["keyframes"] = from_list(
            lambda x: to_class(AlphaKeyframerKeyframe, x), self.keyframes
        )
        return result


class BitmapNameKeyframerKeyframe:
    def __init__(self, time, value):
        self.time = time
        self.value = value

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        time = from_float(obj.get("time"))
        value = from_union([from_int, from_str], obj.get("value"))
        return BitmapNameKeyframerKeyframe(time, value)

    def to_dict(self):
        result = {}
        result["time"] = to_float(self.time)
        result["value"] = from_union([from_int, from_str], self.value)
        return result


class BitmapNameKeyframer:
    def __init__(self, keyframes):
        self.keyframes = keyframes

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        keyframes = from_list(
            BitmapNameKeyframerKeyframe.from_dict, obj.get("keyframes")
        )
        return BitmapNameKeyframer(keyframes)

    def to_dict(self):
        result = {}
        result["keyframes"] = from_list(
            lambda x: to_class(BitmapNameKeyframerKeyframe, x), self.keyframes
        )
        return result


class DiffuseKeyframerKeyframe:
    def __init__(self, time, value):
        self.time = time
        self.value = value

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        time = from_float(obj.get("time"))
        value = from_list(from_float, obj.get("value"))
        return DiffuseKeyframerKeyframe(time, value)

    def to_dict(self):
        result = {}
        result["time"] = to_float(self.time)
        result["value"] = from_list(to_float, self.value)
        return result


class DiffuseKeyframer:
    def __init__(self, interpolation_type, keyframes):
        self.interpolation_type = interpolation_type
        self.keyframes = keyframes

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        interpolation_type = InterpolationType(obj.get("interpolation_type"))
        keyframes = from_list(DiffuseKeyframerKeyframe.from_dict, obj.get("keyframes"))
        return DiffuseKeyframer(interpolation_type, keyframes)

    def to_dict(self):
        result = {}
        result["interpolation_type"] = to_enum(
            InterpolationType, self.interpolation_type
        )
        result["keyframes"] = from_list(
            lambda x: to_class(DiffuseKeyframerKeyframe, x), self.keyframes
        )
        return result


class BodyFlags:
    def __init__(self, value):
        self.value = value

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        value = from_int(obj.get("value"))
        return BodyFlags(value)

    def to_dict(self):
        result = {}
        result["value"] = from_int(self.value)
        return result


class ParamsKeyframer:
    def __init__(self, interpolation_type, keyframes):
        self.interpolation_type = interpolation_type
        self.keyframes = keyframes

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        interpolation_type = InterpolationType(obj.get("interpolation_type"))
        keyframes = from_list(KeyframerRotKeyframe.from_dict, obj.get("keyframes"))
        return ParamsKeyframer(interpolation_type, keyframes)

    def to_dict(self):
        result = {}
        result["interpolation_type"] = to_enum(
            InterpolationType, self.interpolation_type
        )
        result["keyframes"] = from_list(
            lambda x: to_class(KeyframerRotKeyframe, x), self.keyframes
        )
        return result


class RenderFlagKeyframerKeyframe:
    def __init__(self, time, value):
        self.time = time
        self.value = value

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        time = from_float(obj.get("time"))
        value = from_int(obj.get("value"))
        return RenderFlagKeyframerKeyframe(time, value)

    def to_dict(self):
        result = {}
        result["time"] = to_float(self.time)
        result["value"] = from_int(self.value)
        return result


class RenderFlagKeyframer:
    def __init__(self, keyframes):
        self.keyframes = keyframes

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        keyframes = from_list(
            RenderFlagKeyframerKeyframe.from_dict, obj.get("keyframes")
        )
        return RenderFlagKeyframer(keyframes)

    def to_dict(self):
        result = {}
        result["keyframes"] = from_list(
            lambda x: to_class(RenderFlagKeyframerKeyframe, x), self.keyframes
        )
        return result


class ScaleKeyframerKeyframe:
    def __init__(self, time, value):
        self.time = time
        self.value = value

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        time = from_float(obj.get("time"))
        value = from_list(from_float, obj.get("value"))
        return ScaleKeyframerKeyframe(time, value)

    def to_dict(self):
        result = {}
        result["time"] = to_float(self.time)
        result["value"] = from_list(to_float, self.value)
        return result


class ScaleKeyframer:
    def __init__(self, interpolation_type, keyframes):
        self.interpolation_type = interpolation_type
        self.keyframes = keyframes

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        interpolation_type = InterpolationType(obj.get("interpolation_type"))
        keyframes = from_list(ScaleKeyframerKeyframe.from_dict, obj.get("keyframes"))
        return ScaleKeyframer(interpolation_type, keyframes)

    def to_dict(self):
        result = {}
        result["interpolation_type"] = to_enum(
            InterpolationType, self.interpolation_type
        )
        result["keyframes"] = from_list(
            lambda x: to_class(ScaleKeyframerKeyframe, x), self.keyframes
        )
        return result


class MaterialAnimV1381_67_09PCBody:
    def __init__(
        self,
        alpha_keyframer,
        base_material_name,
        bitmap_name_keyframer,
        diffuse_keyframer,
        duration,
        emission_keyframer,
        flags,
        params_keyframer,
        render_flag_keyframer,
        resource_flag_keyframer,
        rotation_keyframer,
        scale_keyframer,
        scroll_keyframer,
        vec4_f_keyframer0,
    ):
        self.alpha_keyframer = alpha_keyframer
        self.base_material_name = base_material_name
        self.bitmap_name_keyframer = bitmap_name_keyframer
        self.diffuse_keyframer = diffuse_keyframer
        self.duration = duration
        self.emission_keyframer = emission_keyframer
        self.flags = flags
        self.params_keyframer = params_keyframer
        self.render_flag_keyframer = render_flag_keyframer
        self.resource_flag_keyframer = resource_flag_keyframer
        self.rotation_keyframer = rotation_keyframer
        self.scale_keyframer = scale_keyframer
        self.scroll_keyframer = scroll_keyframer
        self.vec4_f_keyframer0 = vec4_f_keyframer0

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        alpha_keyframer = AlphaKeyframer.from_dict(obj.get("alpha_keyframer"))
        base_material_name = from_union(
            [from_int, from_str], obj.get("base_material_name")
        )
        bitmap_name_keyframer = BitmapNameKeyframer.from_dict(
            obj.get("bitmap_name_keyframer")
        )
        diffuse_keyframer = DiffuseKeyframer.from_dict(obj.get("diffuse_keyframer"))
        duration = from_float(obj.get("duration"))
        emission_keyframer = DiffuseKeyframer.from_dict(obj.get("emission_keyframer"))
        flags = BodyFlags.from_dict(obj.get("flags"))
        params_keyframer = ParamsKeyframer.from_dict(obj.get("params_keyframer"))
        render_flag_keyframer = RenderFlagKeyframer.from_dict(
            obj.get("render_flag_keyframer")
        )
        resource_flag_keyframer = RenderFlagKeyframer.from_dict(
            obj.get("resource_flag_keyframer")
        )
        rotation_keyframer = AlphaKeyframer.from_dict(obj.get("rotation_keyframer"))
        scale_keyframer = ScaleKeyframer.from_dict(obj.get("scale_keyframer"))
        scroll_keyframer = ScaleKeyframer.from_dict(obj.get("scroll_keyframer"))
        vec4_f_keyframer0 = ParamsKeyframer.from_dict(obj.get("vec4f_keyframer0"))
        return MaterialAnimV1381_67_09PCBody(
            alpha_keyframer,
            base_material_name,
            bitmap_name_keyframer,
            diffuse_keyframer,
            duration,
            emission_keyframer,
            flags,
            params_keyframer,
            render_flag_keyframer,
            resource_flag_keyframer,
            rotation_keyframer,
            scale_keyframer,
            scroll_keyframer,
            vec4_f_keyframer0,
        )

    def to_dict(self):
        result = {}
        result["alpha_keyframer"] = to_class(AlphaKeyframer, self.alpha_keyframer)
        result["base_material_name"] = from_union(
            [from_int, from_str], self.base_material_name
        )
        result["bitmap_name_keyframer"] = to_class(
            BitmapNameKeyframer, self.bitmap_name_keyframer
        )
        result["diffuse_keyframer"] = to_class(DiffuseKeyframer, self.diffuse_keyframer)
        result["duration"] = to_float(self.duration)
        result["emission_keyframer"] = to_class(
            DiffuseKeyframer, self.emission_keyframer
        )
        result["flags"] = to_class(BodyFlags, self.flags)
        result["params_keyframer"] = to_class(ParamsKeyframer, self.params_keyframer)
        result["render_flag_keyframer"] = to_class(
            RenderFlagKeyframer, self.render_flag_keyframer
        )
        result["resource_flag_keyframer"] = to_class(
            RenderFlagKeyframer, self.resource_flag_keyframer
        )
        result["rotation_keyframer"] = to_class(AlphaKeyframer, self.rotation_keyframer)
        result["scale_keyframer"] = to_class(ScaleKeyframer, self.scale_keyframer)
        result["scroll_keyframer"] = to_class(ScaleKeyframer, self.scroll_keyframer)
        result["vec4f_keyframer0"] = to_class(ParamsKeyframer, self.vec4_f_keyframer0)
        return result


class MaterialAnimV1381_67_09_PC:
    def __init__(self, body, class_name, link_header, link_name, name):
        self.body = body
        self.class_name = class_name
        self.link_header = link_header
        self.link_name = link_name
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        body = MaterialAnimV1381_67_09PCBody.from_dict(obj.get("body"))
        class_name = from_union([from_int, from_str], obj.get("class_name"))
        link_header = AnimationV1381_67_09PCLinkHeader.from_dict(obj.get("link_header"))
        link_name = from_union([from_none, from_int, from_str], obj.get("link_name"))
        name = from_union([from_int, from_str], obj.get("name"))
        return MaterialAnimV1381_67_09_PC(
            body, class_name, link_header, link_name, name
        )

    def to_dict(self):
        result = {}
        result["body"] = to_class(MaterialAnimV1381_67_09PCBody, self.body)
        result["class_name"] = from_union([from_int, from_str], self.class_name)
        result["link_header"] = to_class(
            AnimationV1381_67_09PCLinkHeader, self.link_header
        )
        if self.link_name is not None:
            result["link_name"] = from_union(
                [from_none, from_int, from_str], self.link_name
            )
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class MaterialAnim:
    def __init__(self, material_anim_v1_381_67_09_pc):
        self.material_anim_v1_381_67_09_pc = material_anim_v1_381_67_09_pc

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        material_anim_v1_381_67_09_pc = MaterialAnimV1381_67_09_PC.from_dict(
            obj.get("MaterialAnimV1_381_67_09PC")
        )
        return MaterialAnim(material_anim_v1_381_67_09_pc)

    def to_dict(self):
        result = {}
        result["MaterialAnimV1_381_67_09PC"] = to_class(
            MaterialAnimV1381_67_09_PC, self.material_anim_v1_381_67_09_pc
        )
        return result


class MaterialObjV1381_67_09PCBody:
    def __init__(self, entries):
        self.entries = entries

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        entries = from_dict(
            lambda x: from_list(lambda x: from_union([from_int, from_str], x), x),
            obj.get("entries"),
        )
        return MaterialObjV1381_67_09PCBody(entries)

    def to_dict(self):
        result = {}
        result["entries"] = from_dict(
            lambda x: from_list(lambda x: from_union([from_int, from_str], x), x),
            self.entries,
        )
        return result


class MaterialObjV1381_67_09_PC:
    def __init__(self, body, class_name, link_header, link_name, name):
        self.body = body
        self.class_name = class_name
        self.link_header = link_header
        self.link_name = link_name
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        body = MaterialObjV1381_67_09PCBody.from_dict(obj.get("body"))
        class_name = from_union([from_int, from_str], obj.get("class_name"))
        link_header = AnimationV1381_67_09PCLinkHeader.from_dict(obj.get("link_header"))
        link_name = from_union([from_none, from_int, from_str], obj.get("link_name"))
        name = from_union([from_int, from_str], obj.get("name"))
        return MaterialObjV1381_67_09_PC(body, class_name, link_header, link_name, name)

    def to_dict(self):
        result = {}
        result["body"] = to_class(MaterialObjV1381_67_09PCBody, self.body)
        result["class_name"] = from_union([from_int, from_str], self.class_name)
        result["link_header"] = to_class(
            AnimationV1381_67_09PCLinkHeader, self.link_header
        )
        if self.link_name is not None:
            result["link_name"] = from_union(
                [from_none, from_int, from_str], self.link_name
            )
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class MaterialObj:
    def __init__(self, material_obj_v1_381_67_09_pc):
        self.material_obj_v1_381_67_09_pc = material_obj_v1_381_67_09_pc

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        material_obj_v1_381_67_09_pc = MaterialObjV1381_67_09_PC.from_dict(
            obj.get("MaterialObjV1_381_67_09PC")
        )
        return MaterialObj(material_obj_v1_381_67_09_pc)

    def to_dict(self):
        result = {}
        result["MaterialObjV1_381_67_09PC"] = to_class(
            MaterialObjV1381_67_09_PC, self.material_obj_v1_381_67_09_pc
        )
        return result


class RangeInner:
    def __init__(self, end, start):
        self.end = end
        self.start = start

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        end = from_int(obj.get("end"))
        start = from_int(obj.get("start"))
        return RangeInner(end, start)

    def to_dict(self):
        result = {}
        result["end"] = from_int(self.end)
        result["start"] = from_int(self.start)
        return result


class Range:
    def __init__(self, inner):
        self.inner = inner

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        inner = RangeInner.from_dict(obj.get("inner"))
        return Range(inner)

    def to_dict(self):
        result = {}
        result["inner"] = to_class(RangeInner, self.inner)
        return result


class CollisionFacesRange:
    def __init__(self, range, pointer):
        self.range = range
        self.pointer = pointer

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        range = from_union([Range.from_dict, from_none], obj.get("Range"))
        pointer = from_union([from_int, from_none], obj.get("Pointer"))
        return CollisionFacesRange(range, pointer)

    def to_dict(self):
        result = {}
        if self.range is not None:
            result["Range"] = from_union(
                [lambda x: to_class(Range, x), from_none], self.range
            )
        if self.pointer is not None:
            result["Pointer"] = from_union([from_int, from_none], self.pointer)
        return result


class CollisionAABBElement:
    def __init__(self, collision_aabb_children, collision_faces_range, max, min):
        self.collision_aabb_children = collision_aabb_children
        self.collision_faces_range = collision_faces_range
        self.max = max
        self.min = min

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        collision_aabb_children = from_union(
            [from_none, lambda x: from_list(lambda x: x, x)],
            obj.get("collision_aabb_children"),
        )
        collision_faces_range = CollisionFacesRange.from_dict(
            obj.get("collision_faces_range")
        )
        max = from_list(from_float, obj.get("max"))
        min = from_list(from_float, obj.get("min"))
        return CollisionAABBElement(
            collision_aabb_children, collision_faces_range, max, min
        )

    def to_dict(self):
        result = {}
        if self.collision_aabb_children is not None:
            result["collision_aabb_children"] = from_union(
                [from_none, lambda x: from_list(lambda x: x, x)],
                self.collision_aabb_children,
            )
        result["collision_faces_range"] = to_class(
            CollisionFacesRange, self.collision_faces_range
        )
        result["max"] = from_list(to_float, self.max)
        result["min"] = from_list(to_float, self.min)
        return result


class AABBColCollisionFace:
    def __init__(
        self, first_vertex_id, material_index, second_vertex_id, third_vertex_id
    ):
        self.first_vertex_id = first_vertex_id
        self.material_index = material_index
        self.second_vertex_id = second_vertex_id
        self.third_vertex_id = third_vertex_id

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        first_vertex_id = from_int(obj.get("first_vertex_id"))
        material_index = from_int(obj.get("material_index"))
        second_vertex_id = from_int(obj.get("second_vertex_id"))
        third_vertex_id = from_int(obj.get("third_vertex_id"))
        return AABBColCollisionFace(
            first_vertex_id, material_index, second_vertex_id, third_vertex_id
        )

    def to_dict(self):
        result = {}
        result["first_vertex_id"] = from_int(self.first_vertex_id)
        result["material_index"] = from_int(self.material_index)
        result["second_vertex_id"] = from_int(self.second_vertex_id)
        result["third_vertex_id"] = from_int(self.third_vertex_id)
        return result


class AABBCol:
    def __init__(self, collision_aabb_nodes, collision_faces):
        self.collision_aabb_nodes = collision_aabb_nodes
        self.collision_faces = collision_faces

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        collision_aabb_nodes = from_list(
            CollisionAABBElement.from_dict, obj.get("collision_aabb_nodes")
        )
        collision_faces = from_list(
            AABBColCollisionFace.from_dict, obj.get("collision_faces")
        )
        return AABBCol(collision_aabb_nodes, collision_faces)

    def to_dict(self):
        result = {}
        result["collision_aabb_nodes"] = from_list(
            lambda x: to_class(CollisionAABBElement, x), self.collision_aabb_nodes
        )
        result["collision_faces"] = from_list(
            lambda x: to_class(AABBColCollisionFace, x), self.collision_faces
        )
        return result


class BoxCol:
    def __init__(self, col_box, flag, name):
        self.col_box = col_box
        self.flag = flag
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        col_box = Box.from_dict(obj.get("col_box"))
        flag = from_int(obj.get("flag"))
        name = from_union([from_int, from_str], obj.get("name"))
        return BoxCol(col_box, flag, name)

    def to_dict(self):
        result = {}
        result["col_box"] = to_class(Box, self.col_box)
        result["flag"] = from_int(self.flag)
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class CylindreCol:
    def __init__(self, col_cylindre, flag, name):
        self.col_cylindre = col_cylindre
        self.flag = flag
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        col_cylindre = Cylindre.from_dict(obj.get("col_cylindre"))
        flag = from_int(obj.get("flag"))
        name = from_union([from_int, from_str], obj.get("name"))
        return CylindreCol(col_cylindre, flag, name)

    def to_dict(self):
        result = {}
        result["col_cylindre"] = to_class(Cylindre, self.col_cylindre)
        result["flag"] = from_int(self.flag)
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class MagentaSchema:
    def __init__(self, tris):
        self.tris = tris

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        tris = from_list(lambda x: from_list(from_int, x), obj.get("tris"))
        return MagentaSchema(tris)

    def to_dict(self):
        result = {}
        result["tris"] = from_list(lambda x: from_list(from_int, x), self.tris)
        return result


class PrimInfoElement:
    def __init__(
        self,
        face_count,
        index_buffer_offset_in_shorts,
        placeholder_pointers,
        prim_type,
        shader_type,
        unused0,
        unused1,
        vertex_buffer_offset,
        vertex_buffer_range_begin,
        vertex_count,
        vertex_size,
    ):
        self.face_count = face_count
        self.index_buffer_offset_in_shorts = index_buffer_offset_in_shorts
        self.placeholder_pointers = placeholder_pointers
        self.prim_type = prim_type
        self.shader_type = shader_type
        self.unused0 = unused0
        self.unused1 = unused1
        self.vertex_buffer_offset = vertex_buffer_offset
        self.vertex_buffer_range_begin = vertex_buffer_range_begin
        self.vertex_count = vertex_count
        self.vertex_size = vertex_size

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        face_count = from_int(obj.get("face_count"))
        index_buffer_offset_in_shorts = from_int(
            obj.get("index_buffer_offset_in_shorts")
        )
        placeholder_pointers = from_list(from_int, obj.get("placeholder_pointers"))
        prim_type = from_int(obj.get("prim_type"))
        shader_type = from_int(obj.get("shader_type"))
        unused0 = from_int(obj.get("unused0"))
        unused1 = from_int(obj.get("unused1"))
        vertex_buffer_offset = from_int(obj.get("vertex_buffer_offset"))
        vertex_buffer_range_begin = from_int(obj.get("vertex_buffer_range_begin"))
        vertex_count = from_int(obj.get("vertex_count"))
        vertex_size = from_int(obj.get("vertex_size"))
        return PrimInfoElement(
            face_count,
            index_buffer_offset_in_shorts,
            placeholder_pointers,
            prim_type,
            shader_type,
            unused0,
            unused1,
            vertex_buffer_offset,
            vertex_buffer_range_begin,
            vertex_count,
            vertex_size,
        )

    def to_dict(self):
        result = {}
        result["face_count"] = from_int(self.face_count)
        result["index_buffer_offset_in_shorts"] = from_int(
            self.index_buffer_offset_in_shorts
        )
        result["placeholder_pointers"] = from_list(from_int, self.placeholder_pointers)
        result["prim_type"] = from_int(self.prim_type)
        result["shader_type"] = from_int(self.shader_type)
        result["unused0"] = from_int(self.unused0)
        result["unused1"] = from_int(self.unused1)
        result["vertex_buffer_offset"] = from_int(self.vertex_buffer_offset)
        result["vertex_buffer_range_begin"] = from_int(self.vertex_buffer_range_begin)
        result["vertex_count"] = from_int(self.vertex_count)
        result["vertex_size"] = from_int(self.vertex_size)
        return result


class Layout1BlendElement:
    def __init__(
        self,
        blend_index,
        blend_weight,
        normal,
        normal_w,
        pad2,
        position,
        tangent,
        tangent_w,
        uv,
    ):
        self.blend_index = blend_index
        self.blend_weight = blend_weight
        self.normal = normal
        self.normal_w = normal_w
        self.pad2 = pad2
        self.position = position
        self.tangent = tangent
        self.tangent_w = tangent_w
        self.uv = uv

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        blend_index = from_float(obj.get("blend_index"))
        blend_weight = from_float(obj.get("blend_weight"))
        normal = from_list(from_int, obj.get("normal"))
        normal_w = from_int(obj.get("normal_w"))
        pad2 = from_list(from_int, obj.get("pad2"))
        position = from_list(from_float, obj.get("position"))
        tangent = from_list(from_int, obj.get("tangent"))
        tangent_w = from_int(obj.get("tangent_w"))
        uv = from_list(from_float, obj.get("uv"))
        return Layout1BlendElement(
            blend_index,
            blend_weight,
            normal,
            normal_w,
            pad2,
            position,
            tangent,
            tangent_w,
            uv,
        )

    def to_dict(self):
        result = {}
        result["blend_index"] = to_float(self.blend_index)
        result["blend_weight"] = to_float(self.blend_weight)
        result["normal"] = from_list(from_int, self.normal)
        result["normal_w"] = from_int(self.normal_w)
        result["pad2"] = from_list(from_int, self.pad2)
        result["position"] = from_list(to_float, self.position)
        result["tangent"] = from_list(from_int, self.tangent)
        result["tangent_w"] = from_int(self.tangent_w)
        result["uv"] = from_list(to_float, self.uv)
        return result


class Layout4BlendElement:
    def __init__(
        self,
        blend_indices,
        blend_weights,
        normal,
        normal_w,
        position,
        tangent,
        tangent_w,
        uv,
    ):
        self.blend_indices = blend_indices
        self.blend_weights = blend_weights
        self.normal = normal
        self.normal_w = normal_w
        self.position = position
        self.tangent = tangent
        self.tangent_w = tangent_w
        self.uv = uv

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        blend_indices = from_list(from_float, obj.get("blend_indices"))
        blend_weights = from_list(from_float, obj.get("blend_weights"))
        normal = from_list(from_int, obj.get("normal"))
        normal_w = from_int(obj.get("normal_w"))
        position = from_list(from_float, obj.get("position"))
        tangent = from_list(from_int, obj.get("tangent"))
        tangent_w = from_int(obj.get("tangent_w"))
        uv = from_list(from_float, obj.get("uv"))
        return Layout4BlendElement(
            blend_indices,
            blend_weights,
            normal,
            normal_w,
            position,
            tangent,
            tangent_w,
            uv,
        )

    def to_dict(self):
        result = {}
        result["blend_indices"] = from_list(to_float, self.blend_indices)
        result["blend_weights"] = from_list(to_float, self.blend_weights)
        result["normal"] = from_list(from_int, self.normal)
        result["normal_w"] = from_int(self.normal_w)
        result["position"] = from_list(to_float, self.position)
        result["tangent"] = from_list(from_int, self.tangent)
        result["tangent_w"] = from_int(self.tangent_w)
        result["uv"] = from_list(to_float, self.uv)
        return result


class LayoutNoBlendElement:
    def __init__(self, luv, normal, normal_w, position, tangent, tangent_w, uv):
        self.luv = luv
        self.normal = normal
        self.normal_w = normal_w
        self.position = position
        self.tangent = tangent
        self.tangent_w = tangent_w
        self.uv = uv

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        luv = from_list(from_float, obj.get("luv"))
        normal = from_list(from_int, obj.get("normal"))
        normal_w = from_int(obj.get("normal_w"))
        position = from_list(from_float, obj.get("position"))
        tangent = from_list(from_int, obj.get("tangent"))
        tangent_w = from_int(obj.get("tangent_w"))
        uv = from_list(from_float, obj.get("uv"))
        return LayoutNoBlendElement(
            luv, normal, normal_w, position, tangent, tangent_w, uv
        )

    def to_dict(self):
        result = {}
        result["luv"] = from_list(to_float, self.luv)
        result["normal"] = from_list(from_int, self.normal)
        result["normal_w"] = from_int(self.normal_w)
        result["position"] = from_list(to_float, self.position)
        result["tangent"] = from_list(from_int, self.tangent)
        result["tangent_w"] = from_int(self.tangent_w)
        result["uv"] = from_list(to_float, self.uv)
        return result


class LayoutPositionElement:
    def __init__(self, position):
        self.position = position

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        position = from_list(from_float, obj.get("position"))
        return LayoutPositionElement(position)

    def to_dict(self):
        result = {}
        result["position"] = from_list(to_float, self.position)
        return result


class LayoutPositionUVElement:
    def __init__(self, position, unknown, uv):
        self.position = position
        self.unknown = unknown
        self.uv = uv

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        position = from_list(from_float, obj.get("position"))
        unknown = from_float(obj.get("unknown"))
        uv = from_list(from_float, obj.get("uv"))
        return LayoutPositionUVElement(position, unknown, uv)

    def to_dict(self):
        result = {}
        result["position"] = from_list(to_float, self.position)
        result["unknown"] = to_float(self.unknown)
        result["uv"] = from_list(to_float, self.uv)
        return result


class LayoutUnknown:
    def __init__(self, data, layout):
        self.data = data
        self.layout = layout

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        data = from_list(lambda x: from_list(from_int, x), obj.get("data"))
        layout = from_int(obj.get("layout"))
        return LayoutUnknown(data, layout)

    def to_dict(self):
        result = {}
        result["data"] = from_list(lambda x: from_list(from_int, x), self.data)
        result["layout"] = from_int(self.layout)
        return result


class Vertices:
    def __init__(
        self,
        layout_position,
        layout_position_uv,
        layout_no_blend,
        layout1_blend,
        layout4_blend,
        layout_unknown,
    ):
        self.layout_position = layout_position
        self.layout_position_uv = layout_position_uv
        self.layout_no_blend = layout_no_blend
        self.layout1_blend = layout1_blend
        self.layout4_blend = layout4_blend
        self.layout_unknown = layout_unknown

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        layout_position = from_union(
            [lambda x: from_list(LayoutPositionElement.from_dict, x), from_none],
            obj.get("LayoutPosition"),
        )
        layout_position_uv = from_union(
            [lambda x: from_list(LayoutPositionUVElement.from_dict, x), from_none],
            obj.get("LayoutPositionUV"),
        )
        layout_no_blend = from_union(
            [lambda x: from_list(LayoutNoBlendElement.from_dict, x), from_none],
            obj.get("LayoutNoBlend"),
        )
        layout1_blend = from_union(
            [lambda x: from_list(Layout1BlendElement.from_dict, x), from_none],
            obj.get("Layout1Blend"),
        )
        layout4_blend = from_union(
            [lambda x: from_list(Layout4BlendElement.from_dict, x), from_none],
            obj.get("Layout4Blend"),
        )
        layout_unknown = from_union(
            [LayoutUnknown.from_dict, from_none], obj.get("LayoutUnknown")
        )
        return Vertices(
            layout_position,
            layout_position_uv,
            layout_no_blend,
            layout1_blend,
            layout4_blend,
            layout_unknown,
        )

    def to_dict(self):
        result = {}
        if self.layout_position is not None:
            result["LayoutPosition"] = from_union(
                [
                    lambda x: from_list(
                        lambda x: to_class(LayoutPositionElement, x), x
                    ),
                    from_none,
                ],
                self.layout_position,
            )
        if self.layout_position_uv is not None:
            result["LayoutPositionUV"] = from_union(
                [
                    lambda x: from_list(
                        lambda x: to_class(LayoutPositionUVElement, x), x
                    ),
                    from_none,
                ],
                self.layout_position_uv,
            )
        if self.layout_no_blend is not None:
            result["LayoutNoBlend"] = from_union(
                [
                    lambda x: from_list(lambda x: to_class(LayoutNoBlendElement, x), x),
                    from_none,
                ],
                self.layout_no_blend,
            )
        if self.layout1_blend is not None:
            result["Layout1Blend"] = from_union(
                [
                    lambda x: from_list(lambda x: to_class(Layout1BlendElement, x), x),
                    from_none,
                ],
                self.layout1_blend,
            )
        if self.layout4_blend is not None:
            result["Layout4Blend"] = from_union(
                [
                    lambda x: from_list(lambda x: to_class(Layout4BlendElement, x), x),
                    from_none,
                ],
                self.layout4_blend,
            )
        if self.layout_unknown is not None:
            result["LayoutUnknown"] = from_union(
                [lambda x: to_class(LayoutUnknown, x), from_none], self.layout_unknown
            )
        return result


class FriskySchema:
    def __init__(self, vertices):
        self.vertices = vertices

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        vertices = Vertices.from_dict(obj.get("vertices"))
        return FriskySchema(vertices)

    def to_dict(self):
        result = {}
        result["vertices"] = to_class(Vertices, self.vertices)
        return result


class PurpleMeshBuffers:
    def __init__(self, index_buffers, prim_infos, vertex_buffers):
        self.index_buffers = index_buffers
        self.prim_infos = prim_infos
        self.vertex_buffers = vertex_buffers

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        index_buffers = from_list(MagentaSchema.from_dict, obj.get("index_buffers"))
        prim_infos = from_list(PrimInfoElement.from_dict, obj.get("prim_infos"))
        vertex_buffers = from_list(FriskySchema.from_dict, obj.get("vertex_buffers"))
        return PurpleMeshBuffers(index_buffers, prim_infos, vertex_buffers)

    def to_dict(self):
        result = {}
        result["index_buffers"] = from_list(
            lambda x: to_class(MagentaSchema, x), self.index_buffers
        )
        result["prim_infos"] = from_list(
            lambda x: to_class(PrimInfoElement, x), self.prim_infos
        )
        result["vertex_buffers"] = from_list(
            lambda x: to_class(FriskySchema, x), self.vertex_buffers
        )
        return result


class BraggadociousSchema:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        data = from_list(from_int, obj.get("data"))
        return BraggadociousSchema(data)

    def to_dict(self):
        result = {}
        result["data"] = from_list(from_int, self.data)
        return result


class MischievousSchema:
    def __init__(self, morph_target_desc_relateds, name):
        self.morph_target_desc_relateds = morph_target_desc_relateds
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        morph_target_desc_relateds = from_list(
            BraggadociousSchema.from_dict, obj.get("morph_target_desc_relateds")
        )
        name = from_union([from_int, from_str], obj.get("name"))
        return MischievousSchema(morph_target_desc_relateds, name)

    def to_dict(self):
        result = {}
        result["morph_target_desc_relateds"] = from_list(
            lambda x: to_class(BraggadociousSchema, x), self.morph_target_desc_relateds
        )
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class Schema1:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        data = from_list(from_int, obj.get("data"))
        return Schema1(data)

    def to_dict(self):
        result = {}
        result["data"] = from_list(from_int, self.data)
        return result


class PurpleMorpher:
    def __init__(self, morph_target_descs, morpher_relateds):
        self.morph_target_descs = morph_target_descs
        self.morpher_relateds = morpher_relateds

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        morph_target_descs = from_list(
            MischievousSchema.from_dict, obj.get("morph_target_descs")
        )
        morpher_relateds = from_list(Schema1.from_dict, obj.get("morpher_relateds"))
        return PurpleMorpher(morph_target_descs, morpher_relateds)

    def to_dict(self):
        result = {}
        result["morph_target_descs"] = from_list(
            lambda x: to_class(MischievousSchema, x), self.morph_target_descs
        )
        result["morpher_relateds"] = from_list(
            lambda x: to_class(Schema1, x), self.morpher_relateds
        )
        return result


class TBVtxElement:
    def __init__(self, unk_vec_1, unk_vec_2):
        self.unk_vec_1 = unk_vec_1
        self.unk_vec_2 = unk_vec_2

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        unk_vec_1 = from_list(from_float, obj.get("unk_vec_1"))
        unk_vec_2 = from_list(from_float, obj.get("unk_vec_2"))
        return TBVtxElement(unk_vec_1, unk_vec_2)

    def to_dict(self):
        result = {}
        result["unk_vec_1"] = from_list(to_float, self.unk_vec_1)
        result["unk_vec_2"] = from_list(to_float, self.unk_vec_2)
        return result


class PurplePoints:
    def __init__(self, morpher, positions, tb_vtxs):
        self.morpher = morpher
        self.positions = positions
        self.tb_vtxs = tb_vtxs

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        morpher = PurpleMorpher.from_dict(obj.get("morpher"))
        positions = from_list(lambda x: from_list(from_float, x), obj.get("positions"))
        tb_vtxs = from_list(TBVtxElement.from_dict, obj.get("tb_vtxs"))
        return PurplePoints(morpher, positions, tb_vtxs)

    def to_dict(self):
        result = {}
        result["morpher"] = to_class(PurpleMorpher, self.morpher)
        result["positions"] = from_list(
            lambda x: from_list(to_float, x), self.positions
        )
        result["tb_vtxs"] = from_list(lambda x: to_class(TBVtxElement, x), self.tb_vtxs)
        return result


class SphereCol:
    def __init__(self, col_sph, flag, name):
        self.col_sph = col_sph
        self.flag = flag
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        col_sph = Sphere.from_dict(obj.get("col_sph"))
        flag = from_int(obj.get("flag"))
        name = from_union([from_int, from_str], obj.get("name"))
        return SphereCol(col_sph, flag, name)

    def to_dict(self):
        result = {}
        result["col_sph"] = to_class(Sphere, self.col_sph)
        result["flag"] = from_int(self.flag)
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class StripElement:
    def __init__(self, material_name, strip_vertices_indices, tri_order):
        self.material_name = material_name
        self.strip_vertices_indices = strip_vertices_indices
        self.tri_order = tri_order

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        material_name = from_union([from_int, from_str], obj.get("material_name"))
        strip_vertices_indices = from_list(from_int, obj.get("strip_vertices_indices"))
        tri_order = from_int(obj.get("tri_order"))
        return StripElement(material_name, strip_vertices_indices, tri_order)

    def to_dict(self):
        result = {}
        result["material_name"] = from_union([from_int, from_str], self.material_name)
        result["strip_vertices_indices"] = from_list(
            from_int, self.strip_vertices_indices
        )
        result["tri_order"] = from_int(self.tri_order)
        return result


class Schema4:
    def __init__(self, unused0, unused1):
        self.unused0 = unused0
        self.unused1 = unused1

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        unused0 = from_int(obj.get("unused0"))
        unused1 = from_int(obj.get("unused1"))
        return Schema4(unused0, unused1)

    def to_dict(self):
        result = {}
        result["unused0"] = from_int(self.unused0)
        result["unused1"] = from_int(self.unused1)
        return result


class Schema3:
    def __init__(self, unused0_s):
        self.unused0_s = unused0_s

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        unused0_s = from_list(Schema4.from_dict, obj.get("unused0s"))
        return Schema3(unused0_s)

    def to_dict(self):
        result = {}
        result["unused0s"] = from_list(lambda x: to_class(Schema4, x), self.unused0_s)
        return result


class MeshV106_63_02PCBody:
    def __init__(
        self,
        aabb_col,
        aabb_vertices,
        box_cols,
        cylindre_cols,
        drawing_cutoff_distance,
        drawing_start_distance,
        material_names,
        mesh_buffers,
        normal_count,
        normals,
        points,
        related_to_counts,
        shadow_related,
        sphere_cols,
        strips,
        unk6,
        unk_uints,
        unused4_s,
        uv_count,
        uvs,
        zero2,
    ):
        self.aabb_col = aabb_col
        self.aabb_vertices = aabb_vertices
        self.box_cols = box_cols
        self.cylindre_cols = cylindre_cols
        self.drawing_cutoff_distance = drawing_cutoff_distance
        self.drawing_start_distance = drawing_start_distance
        self.material_names = material_names
        self.mesh_buffers = mesh_buffers
        self.normal_count = normal_count
        self.normals = normals
        self.points = points
        self.related_to_counts = related_to_counts
        self.shadow_related = shadow_related
        self.sphere_cols = sphere_cols
        self.strips = strips
        self.unk6 = unk6
        self.unk_uints = unk_uints
        self.unused4_s = unused4_s
        self.uv_count = uv_count
        self.uvs = uvs
        self.zero2 = zero2

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        aabb_col = AABBCol.from_dict(obj.get("aabb_col"))
        aabb_vertices = from_list(
            lambda x: from_list(from_int, x), obj.get("aabb_vertices")
        )
        box_cols = from_list(BoxCol.from_dict, obj.get("box_cols"))
        cylindre_cols = from_list(CylindreCol.from_dict, obj.get("cylindre_cols"))
        drawing_cutoff_distance = from_float(obj.get("drawing_cutoff_distance"))
        drawing_start_distance = from_float(obj.get("drawing_start_distance"))
        material_names = from_list(
            lambda x: from_union([from_int, from_str], x), obj.get("material_names")
        )
        mesh_buffers = PurpleMeshBuffers.from_dict(obj.get("mesh_buffers"))
        normal_count = from_int(obj.get("normal_count"))
        normals = from_list(lambda x: from_list(from_float, x), obj.get("normals"))
        points = PurplePoints.from_dict(obj.get("points"))
        related_to_counts = from_list(from_int, obj.get("related_to_counts"))
        shadow_related = from_int(obj.get("shadow_related"))
        sphere_cols = from_list(SphereCol.from_dict, obj.get("sphere_cols"))
        strips = from_list(StripElement.from_dict, obj.get("strips"))
        unk6 = from_union(
            [from_none, lambda x: from_list(from_int, x)], obj.get("unk6")
        )
        unk_uints = from_list(from_int, obj.get("unk_uints"))
        unused4_s = from_list(Schema3.from_dict, obj.get("unused4s"))
        uv_count = from_int(obj.get("uv_count"))
        uvs = from_list(lambda x: from_list(from_float, x), obj.get("uvs"))
        zero2 = from_int(obj.get("zero2"))
        return MeshV106_63_02PCBody(
            aabb_col,
            aabb_vertices,
            box_cols,
            cylindre_cols,
            drawing_cutoff_distance,
            drawing_start_distance,
            material_names,
            mesh_buffers,
            normal_count,
            normals,
            points,
            related_to_counts,
            shadow_related,
            sphere_cols,
            strips,
            unk6,
            unk_uints,
            unused4_s,
            uv_count,
            uvs,
            zero2,
        )

    def to_dict(self):
        result = {}
        result["aabb_col"] = to_class(AABBCol, self.aabb_col)
        result["aabb_vertices"] = from_list(
            lambda x: from_list(from_int, x), self.aabb_vertices
        )
        result["box_cols"] = from_list(lambda x: to_class(BoxCol, x), self.box_cols)
        result["cylindre_cols"] = from_list(
            lambda x: to_class(CylindreCol, x), self.cylindre_cols
        )
        result["drawing_cutoff_distance"] = to_float(self.drawing_cutoff_distance)
        result["drawing_start_distance"] = to_float(self.drawing_start_distance)
        result["material_names"] = from_list(
            lambda x: from_union([from_int, from_str], x), self.material_names
        )
        result["mesh_buffers"] = to_class(PurpleMeshBuffers, self.mesh_buffers)
        result["normal_count"] = from_int(self.normal_count)
        result["normals"] = from_list(lambda x: from_list(to_float, x), self.normals)
        result["points"] = to_class(PurplePoints, self.points)
        result["related_to_counts"] = from_list(from_int, self.related_to_counts)
        result["shadow_related"] = from_int(self.shadow_related)
        result["sphere_cols"] = from_list(
            lambda x: to_class(SphereCol, x), self.sphere_cols
        )
        result["strips"] = from_list(lambda x: to_class(StripElement, x), self.strips)
        if self.unk6 is not None:
            result["unk6"] = from_union(
                [from_none, lambda x: from_list(from_int, x)], self.unk6
            )
        result["unk_uints"] = from_list(from_int, self.unk_uints)
        result["unused4s"] = from_list(lambda x: to_class(Schema3, x), self.unused4_s)
        result["uv_count"] = from_int(self.uv_count)
        result["uvs"] = from_list(lambda x: from_list(to_float, x), self.uvs)
        result["zero2"] = from_int(self.zero2)
        return result


class MeshV106_63_02_PC:
    def __init__(self, body, class_name, link_header, link_name, name):
        self.body = body
        self.class_name = class_name
        self.link_header = link_header
        self.link_name = link_name
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        body = MeshV106_63_02PCBody.from_dict(obj.get("body"))
        class_name = from_union([from_int, from_str], obj.get("class_name"))
        link_header = CameraZoneV106_63_02PCLinkHeader.from_dict(obj.get("link_header"))
        link_name = from_union([from_none, from_int, from_str], obj.get("link_name"))
        name = from_union([from_int, from_str], obj.get("name"))
        return MeshV106_63_02_PC(body, class_name, link_header, link_name, name)

    def to_dict(self):
        result = {}
        result["body"] = to_class(MeshV106_63_02PCBody, self.body)
        result["class_name"] = from_union([from_int, from_str], self.class_name)
        result["link_header"] = to_class(
            CameraZoneV106_63_02PCLinkHeader, self.link_header
        )
        if self.link_name is not None:
            result["link_name"] = from_union(
                [from_none, from_int, from_str], self.link_name
            )
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class CollisionAABBTriElement:
    def __init__(
        self, first_vertex_id, material_index, second_vertex_id, third_vertex_id
    ):
        self.first_vertex_id = first_vertex_id
        self.material_index = material_index
        self.second_vertex_id = second_vertex_id
        self.third_vertex_id = third_vertex_id

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        first_vertex_id = from_int(obj.get("first_vertex_id"))
        material_index = from_int(obj.get("material_index"))
        second_vertex_id = from_int(obj.get("second_vertex_id"))
        third_vertex_id = from_int(obj.get("third_vertex_id"))
        return CollisionAABBTriElement(
            first_vertex_id, material_index, second_vertex_id, third_vertex_id
        )

    def to_dict(self):
        result = {}
        result["first_vertex_id"] = from_int(self.first_vertex_id)
        result["material_index"] = from_int(self.material_index)
        result["second_vertex_id"] = from_int(self.second_vertex_id)
        result["third_vertex_id"] = from_int(self.third_vertex_id)
        return result


class Schema5:
    def __init__(self, cylindre, flag, name):
        self.cylindre = cylindre
        self.flag = flag
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        cylindre = Cylindre.from_dict(obj.get("cylindre"))
        flag = from_int(obj.get("flag"))
        name = from_union([from_int, from_str], obj.get("name"))
        return Schema5(cylindre, flag, name)

    def to_dict(self):
        result = {}
        result["cylindre"] = to_class(Cylindre, self.cylindre)
        result["flag"] = from_int(self.flag)
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class Schema6:
    def __init__(self, flags, tris):
        self.flags = flags
        self.tris = tris

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        flags = from_int(obj.get("flags"))
        tris = from_list(lambda x: from_list(from_int, x), obj.get("tris"))
        return Schema6(flags, tris)

    def to_dict(self):
        result = {}
        result["flags"] = from_int(self.flags)
        result["tris"] = from_list(lambda x: from_list(from_int, x), self.tris)
        return result


class MorpherDescMorphTargetDescRelated:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        data = from_list(from_int, obj.get("data"))
        return MorpherDescMorphTargetDescRelated(data)

    def to_dict(self):
        result = {}
        result["data"] = from_list(from_int, self.data)
        return result


class MorpherDescElement:
    def __init__(self, morph_target_desc_relateds, name):
        self.morph_target_desc_relateds = morph_target_desc_relateds
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        morph_target_desc_relateds = from_list(
            MorpherDescMorphTargetDescRelated.from_dict,
            obj.get("morph_target_desc_relateds"),
        )
        name = from_union([from_int, from_str], obj.get("name"))
        return MorpherDescElement(morph_target_desc_relateds, name)

    def to_dict(self):
        result = {}
        result["morph_target_desc_relateds"] = from_list(
            lambda x: to_class(MorpherDescMorphTargetDescRelated, x),
            self.morph_target_desc_relateds,
        )
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class Schema7:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        data = from_list(from_int, obj.get("data"))
        return Schema7(data)

    def to_dict(self):
        result = {}
        result["data"] = from_list(from_int, self.data)
        return result


class FluffyMorpher:
    def __init__(self, morpher_descs, morpher_relateds):
        self.morpher_descs = morpher_descs
        self.morpher_relateds = morpher_relateds

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        morpher_descs = from_list(
            MorpherDescElement.from_dict, obj.get("morpher_descs")
        )
        morpher_relateds = from_list(Schema7.from_dict, obj.get("morpher_relateds"))
        return FluffyMorpher(morpher_descs, morpher_relateds)

    def to_dict(self):
        result = {}
        result["morpher_descs"] = from_list(
            lambda x: to_class(MorpherDescElement, x), self.morpher_descs
        )
        result["morpher_relateds"] = from_list(
            lambda x: to_class(Schema7, x), self.morpher_relateds
        )
        return result


class UnknownElement:
    def __init__(self, data1, data2):
        self.data1 = data1
        self.data2 = data2

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        data1 = from_list(from_int, obj.get("data1"))
        data2 = from_list(from_int, obj.get("data2"))
        return UnknownElement(data1, data2)

    def to_dict(self):
        result = {}
        result["data1"] = from_list(from_int, self.data1)
        result["data2"] = from_list(from_int, self.data2)
        return result


class Schema8:
    def __init__(self, flags, vertices):
        self.flags = flags
        self.vertices = vertices

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        flags = from_int(obj.get("flags"))
        vertices = Vertices.from_dict(obj.get("vertices"))
        return Schema8(flags, vertices)

    def to_dict(self):
        result = {}
        result["flags"] = from_int(self.flags)
        result["vertices"] = to_class(Vertices, self.vertices)
        return result


class VertexGroupFlags:
    def __init__(
        self, visible, padding0, unknown0, unknown1, unknown2, morph, padding1
    ):
        self.visible = visible
        self.padding0 = padding0
        self.unknown0 = unknown0
        self.unknown1 = unknown1
        self.unknown2 = unknown2
        self.morph = morph
        self.padding1 = padding1

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        visible = from_int(obj.get("visible"))
        padding0 = from_int(obj.get("padding0"))
        unknown0 = from_int(obj.get("unknown0"))
        unknown1 = from_int(obj.get("unknown1"))
        unknown2 = from_int(obj.get("unknown2"))
        morph = from_int(obj.get("morph"))
        padding1 = from_int(obj.get("padding1"))
        return VertexGroupFlags(
            visible, padding0, unknown0, unknown1, unknown2, morph, padding1
        )

    def to_dict(self):
        result = {}
        result["visible"] = from_int(self.visible)
        result["padding0"] = from_int(self.padding0)
        result["unknown0"] = from_int(self.unknown0)
        result["unknown1"] = from_int(self.unknown1)
        result["unknown2"] = from_int(self.unknown2)
        result["morph"] = from_int(self.morph)
        result["padding1"] = from_int(self.padding1)
        return result


class Schema9:
    def __init__(
        self,
        face_count,
        flags,
        index_buffer_index_begin,
        unknown0,
        unused,
        vertex_buffer_range_begin,
        vertex_count,
        vertex_layout,
        vertex_offset_in_groups,
        zero,
        zeroes,
    ):
        self.face_count = face_count
        self.flags = flags
        self.index_buffer_index_begin = index_buffer_index_begin
        self.unknown0 = unknown0
        self.unused = unused
        self.vertex_buffer_range_begin = vertex_buffer_range_begin
        self.vertex_count = vertex_count
        self.vertex_layout = vertex_layout
        self.vertex_offset_in_groups = vertex_offset_in_groups
        self.zero = zero
        self.zeroes = zeroes

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        face_count = from_int(obj.get("face_count"))
        flags = VertexGroupFlags.from_dict(obj.get("flags"))
        index_buffer_index_begin = from_int(obj.get("index_buffer_index_begin"))
        unknown0 = from_int(obj.get("unknown0"))
        unused = from_int(obj.get("unused"))
        vertex_buffer_range_begin = from_int(obj.get("vertex_buffer_range_begin"))
        vertex_count = from_int(obj.get("vertex_count"))
        vertex_layout = from_int(obj.get("vertex_layout"))
        vertex_offset_in_groups = from_int(obj.get("vertex_offset_in_groups"))
        zero = from_int(obj.get("zero"))
        zeroes = from_list(from_int, obj.get("zeroes"))
        return Schema9(
            face_count,
            flags,
            index_buffer_index_begin,
            unknown0,
            unused,
            vertex_buffer_range_begin,
            vertex_count,
            vertex_layout,
            vertex_offset_in_groups,
            zero,
            zeroes,
        )

    def to_dict(self):
        result = {}
        result["face_count"] = from_int(self.face_count)
        result["flags"] = to_class(VertexGroupFlags, self.flags)
        result["index_buffer_index_begin"] = from_int(self.index_buffer_index_begin)
        result["unknown0"] = from_int(self.unknown0)
        result["unused"] = from_int(self.unused)
        result["vertex_buffer_range_begin"] = from_int(self.vertex_buffer_range_begin)
        result["vertex_count"] = from_int(self.vertex_count)
        result["vertex_layout"] = from_int(self.vertex_layout)
        result["vertex_offset_in_groups"] = from_int(self.vertex_offset_in_groups)
        result["zero"] = from_int(self.zero)
        result["zeroes"] = from_list(from_int, self.zeroes)
        return result


class FluffyMeshBuffers:
    def __init__(self, index_buffers, morpher, unknowns, vertex_buffers, vertex_groups):
        self.index_buffers = index_buffers
        self.morpher = morpher
        self.unknowns = unknowns
        self.vertex_buffers = vertex_buffers
        self.vertex_groups = vertex_groups

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        index_buffers = from_list(Schema6.from_dict, obj.get("index_buffers"))
        morpher = FluffyMorpher.from_dict(obj.get("morpher"))
        unknowns = from_list(UnknownElement.from_dict, obj.get("unknowns"))
        vertex_buffers = from_list(Schema8.from_dict, obj.get("vertex_buffers"))
        vertex_groups = from_list(Schema9.from_dict, obj.get("vertex_groups"))
        return FluffyMeshBuffers(
            index_buffers, morpher, unknowns, vertex_buffers, vertex_groups
        )

    def to_dict(self):
        result = {}
        result["index_buffers"] = from_list(
            lambda x: to_class(Schema6, x), self.index_buffers
        )
        result["morpher"] = to_class(FluffyMorpher, self.morpher)
        result["unknowns"] = from_list(
            lambda x: to_class(UnknownElement, x), self.unknowns
        )
        result["vertex_buffers"] = from_list(
            lambda x: to_class(Schema8, x), self.vertex_buffers
        )
        result["vertex_groups"] = from_list(
            lambda x: to_class(Schema9, x), self.vertex_groups
        )
        return result


class Schema10:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        data = from_list(from_int, obj.get("data"))
        return Schema10(data)

    def to_dict(self):
        result = {}
        result["data"] = from_list(from_int, self.data)
        return result


class Schema11:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        data = from_list(from_int, obj.get("data"))
        return Schema11(data)

    def to_dict(self):
        result = {}
        result["data"] = from_list(from_int, self.data)
        return result


class PointsRelated2Element:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        data = from_list(from_int, obj.get("data"))
        return PointsRelated2Element(data)

    def to_dict(self):
        result = {}
        result["data"] = from_list(from_int, self.data)
        return result


class FluffyPoints:
    def __init__(self, points_related0, points_related1, points_related2):
        self.points_related0 = points_related0
        self.points_related1 = points_related1
        self.points_related2 = points_related2

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        points_related0 = from_list(Schema10.from_dict, obj.get("points_related0"))
        points_related1 = from_list(Schema11.from_dict, obj.get("points_related1"))
        points_related2 = from_list(
            PointsRelated2Element.from_dict, obj.get("points_related2")
        )
        return FluffyPoints(points_related0, points_related1, points_related2)

    def to_dict(self):
        result = {}
        result["points_related0"] = from_list(
            lambda x: to_class(Schema10, x), self.points_related0
        )
        result["points_related1"] = from_list(
            lambda x: to_class(Schema11, x), self.points_related1
        )
        result["points_related2"] = from_list(
            lambda x: to_class(PointsRelated2Element, x), self.points_related2
        )
        return result


class Schema12:
    def __init__(self, unknown8, unknown8_count):
        self.unknown8 = unknown8
        self.unknown8_count = unknown8_count

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        unknown8 = from_list(from_int, obj.get("unknown8"))
        unknown8_count = from_int(obj.get("unknown8_count"))
        return Schema12(unknown8, unknown8_count)

    def to_dict(self):
        result = {}
        result["unknown8"] = from_list(from_int, self.unknown8)
        result["unknown8_count"] = from_int(self.unknown8_count)
        return result


class Unknown6Element:
    def __init__(self, unknowns):
        self.unknowns = unknowns

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        unknowns = from_list(from_int, obj.get("unknowns"))
        return Unknown6Element(unknowns)

    def to_dict(self):
        result = {}
        result["unknowns"] = from_list(from_int, self.unknowns)
        return result


class Schema13:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        data = from_list(from_int, obj.get("data"))
        return Schema13(data)

    def to_dict(self):
        result = {}
        result["data"] = from_list(from_int, self.data)
        return result


class MeshV1291_03_06PCBody:
    def __init__(
        self,
        box_cols,
        collision_aabb_tris,
        collision_aabbs,
        cylindre_cols,
        drawing_cutoff_distance,
        drawing_start_distance,
        material_names,
        mesh_buffers,
        normals,
        points,
        related_to_counts,
        shadow_related,
        sphere_cols,
        strips,
        texcoords,
        unknown4_s,
        unknown5_s,
        unknown6_s,
        unknown8_s,
        vertices,
    ):
        self.box_cols = box_cols
        self.collision_aabb_tris = collision_aabb_tris
        self.collision_aabbs = collision_aabbs
        self.cylindre_cols = cylindre_cols
        self.drawing_cutoff_distance = drawing_cutoff_distance
        self.drawing_start_distance = drawing_start_distance
        self.material_names = material_names
        self.mesh_buffers = mesh_buffers
        self.normals = normals
        self.points = points
        self.related_to_counts = related_to_counts
        self.shadow_related = shadow_related
        self.sphere_cols = sphere_cols
        self.strips = strips
        self.texcoords = texcoords
        self.unknown4_s = unknown4_s
        self.unknown5_s = unknown5_s
        self.unknown6_s = unknown6_s
        self.unknown8_s = unknown8_s
        self.vertices = vertices

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        box_cols = from_list(CollisionBoxElement.from_dict, obj.get("box_cols"))
        collision_aabb_tris = from_list(
            CollisionAABBTriElement.from_dict, obj.get("collision_aabb_tris")
        )
        collision_aabbs = from_list(
            CollisionAABBElement.from_dict, obj.get("collision_aabbs")
        )
        cylindre_cols = from_list(Schema5.from_dict, obj.get("cylindre_cols"))
        drawing_cutoff_distance = from_float(obj.get("drawing_cutoff_distance"))
        drawing_start_distance = from_float(obj.get("drawing_start_distance"))
        material_names = from_list(
            lambda x: from_union([from_int, from_str], x), obj.get("material_names")
        )
        mesh_buffers = FluffyMeshBuffers.from_dict(obj.get("mesh_buffers"))
        normals = from_list(lambda x: from_list(from_float, x), obj.get("normals"))
        points = FluffyPoints.from_dict(obj.get("points"))
        related_to_counts = from_list(from_int, obj.get("related_to_counts"))
        shadow_related = from_int(obj.get("shadow_related"))
        sphere_cols = from_list(SpheresColElement.from_dict, obj.get("sphere_cols"))
        strips = from_list(StripElement.from_dict, obj.get("strips"))
        texcoords = from_list(lambda x: from_list(from_float, x), obj.get("texcoords"))
        unknown4_s = from_union(
            [from_none, lambda x: from_list(from_int, x)], obj.get("unknown4s")
        )
        unknown5_s = from_list(Schema12.from_dict, obj.get("unknown5s"))
        unknown6_s = from_list(Unknown6Element.from_dict, obj.get("unknown6s"))
        unknown8_s = from_list(Schema13.from_dict, obj.get("unknown8s"))
        vertices = from_list(lambda x: from_list(from_int, x), obj.get("vertices"))
        return MeshV1291_03_06PCBody(
            box_cols,
            collision_aabb_tris,
            collision_aabbs,
            cylindre_cols,
            drawing_cutoff_distance,
            drawing_start_distance,
            material_names,
            mesh_buffers,
            normals,
            points,
            related_to_counts,
            shadow_related,
            sphere_cols,
            strips,
            texcoords,
            unknown4_s,
            unknown5_s,
            unknown6_s,
            unknown8_s,
            vertices,
        )

    def to_dict(self):
        result = {}
        result["box_cols"] = from_list(
            lambda x: to_class(CollisionBoxElement, x), self.box_cols
        )
        result["collision_aabb_tris"] = from_list(
            lambda x: to_class(CollisionAABBTriElement, x), self.collision_aabb_tris
        )
        result["collision_aabbs"] = from_list(
            lambda x: to_class(CollisionAABBElement, x), self.collision_aabbs
        )
        result["cylindre_cols"] = from_list(
            lambda x: to_class(Schema5, x), self.cylindre_cols
        )
        result["drawing_cutoff_distance"] = to_float(self.drawing_cutoff_distance)
        result["drawing_start_distance"] = to_float(self.drawing_start_distance)
        result["material_names"] = from_list(
            lambda x: from_union([from_int, from_str], x), self.material_names
        )
        result["mesh_buffers"] = to_class(FluffyMeshBuffers, self.mesh_buffers)
        result["normals"] = from_list(lambda x: from_list(to_float, x), self.normals)
        result["points"] = to_class(FluffyPoints, self.points)
        result["related_to_counts"] = from_list(from_int, self.related_to_counts)
        result["shadow_related"] = from_int(self.shadow_related)
        result["sphere_cols"] = from_list(
            lambda x: to_class(SpheresColElement, x), self.sphere_cols
        )
        result["strips"] = from_list(lambda x: to_class(StripElement, x), self.strips)
        result["texcoords"] = from_list(
            lambda x: from_list(to_float, x), self.texcoords
        )
        if self.unknown4_s is not None:
            result["unknown4s"] = from_union(
                [from_none, lambda x: from_list(from_int, x)], self.unknown4_s
            )
        result["unknown5s"] = from_list(
            lambda x: to_class(Schema12, x), self.unknown5_s
        )
        result["unknown6s"] = from_list(
            lambda x: to_class(Unknown6Element, x), self.unknown6_s
        )
        result["unknown8s"] = from_list(
            lambda x: to_class(Schema13, x), self.unknown8_s
        )
        result["vertices"] = from_list(lambda x: from_list(from_int, x), self.vertices)
        return result


class MeshV1291_03_06_PC:
    def __init__(self, body, class_name, link_header, link_name, name):
        self.body = body
        self.class_name = class_name
        self.link_header = link_header
        self.link_name = link_name
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        body = MeshV1291_03_06PCBody.from_dict(obj.get("body"))
        class_name = from_union([from_int, from_str], obj.get("class_name"))
        link_header = CameraZoneV106_63_02PCLinkHeader.from_dict(obj.get("link_header"))
        link_name = from_union([from_none, from_int, from_str], obj.get("link_name"))
        name = from_union([from_int, from_str], obj.get("name"))
        return MeshV1291_03_06_PC(body, class_name, link_header, link_name, name)

    def to_dict(self):
        result = {}
        result["body"] = to_class(MeshV1291_03_06PCBody, self.body)
        result["class_name"] = from_union([from_int, from_str], self.class_name)
        result["link_header"] = to_class(
            CameraZoneV106_63_02PCLinkHeader, self.link_header
        )
        if self.link_name is not None:
            result["link_name"] = from_union(
                [from_none, from_int, from_str], self.link_name
            )
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class BodyCollisionFace:
    def __init__(self, short_vec_weirds_indices, surface_type):
        self.short_vec_weirds_indices = short_vec_weirds_indices
        self.surface_type = surface_type

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        short_vec_weirds_indices = from_list(
            from_int, obj.get("short_vec_weirds_indices")
        )
        surface_type = from_int(obj.get("surface_type"))
        return BodyCollisionFace(short_vec_weirds_indices, surface_type)

    def to_dict(self):
        result = {}
        result["short_vec_weirds_indices"] = from_list(
            from_int, self.short_vec_weirds_indices
        )
        result["surface_type"] = from_int(self.surface_type)
        return result


class IndexBufferFlags:
    def __init__(self, value):
        self.value = value

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        value = from_int(obj.get("value"))
        return IndexBufferFlags(value)

    def to_dict(self):
        result = {}
        result["value"] = from_int(self.value)
        return result


class Schema14:
    def __init__(self, flags, tris):
        self.flags = flags
        self.tris = tris

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        flags = IndexBufferFlags.from_dict(obj.get("flags"))
        tris = from_list(lambda x: from_list(from_int, x), obj.get("tris"))
        return Schema14(flags, tris)

    def to_dict(self):
        result = {}
        result["flags"] = to_class(IndexBufferFlags, self.flags)
        result["tris"] = from_list(lambda x: from_list(from_int, x), self.tris)
        return result


class AABBMorphTriggersRange:
    def __init__(self, inner):
        self.inner = inner

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        inner = RangeInner.from_dict(obj.get("inner"))
        return AABBMorphTriggersRange(inner)

    def to_dict(self):
        result = {}
        result["inner"] = to_class(RangeInner, self.inner)
        return result


class AABBMorphTriggerElement:
    def __init__(self, aabb_morph_triggers_range, map_index_range, max, min):
        self.aabb_morph_triggers_range = aabb_morph_triggers_range
        self.map_index_range = map_index_range
        self.max = max
        self.min = min

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        aabb_morph_triggers_range = AABBMorphTriggersRange.from_dict(
            obj.get("aabb_morph_triggers_range")
        )
        map_index_range = Range.from_dict(obj.get("map_index_range"))
        max = from_list(from_float, obj.get("max"))
        min = from_list(from_float, obj.get("min"))
        return AABBMorphTriggerElement(
            aabb_morph_triggers_range, map_index_range, max, min
        )

    def to_dict(self):
        result = {}
        result["aabb_morph_triggers_range"] = to_class(
            AABBMorphTriggersRange, self.aabb_morph_triggers_range
        )
        result["map_index_range"] = to_class(Range, self.map_index_range)
        result["max"] = from_list(to_float, self.max)
        result["min"] = from_list(to_float, self.min)
        return result


class Map:
    def __init__(
        self,
    ):
        pass

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        return Map()

    def to_dict(self):
        result = {}
        return result


class DisplacementVectorElement:
    def __init__(self, displacement, displacement_vectors_self_index):
        self.displacement = displacement
        self.displacement_vectors_self_index = displacement_vectors_self_index

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        displacement = from_list(from_float, obj.get("displacement"))
        displacement_vectors_self_index = from_int(
            obj.get("displacement_vectors_self_index")
        )
        return DisplacementVectorElement(displacement, displacement_vectors_self_index)

    def to_dict(self):
        result = {}
        result["displacement"] = from_list(to_float, self.displacement)
        result["displacement_vectors_self_index"] = from_int(
            self.displacement_vectors_self_index
        )
        return result


class MorphElement:
    def __init__(
        self,
        base_vertex_buffer_id,
        displacement_vectors,
        displacement_vectors_indicies,
        displacement_vertex_buffer_index,
        name,
    ):
        self.base_vertex_buffer_id = base_vertex_buffer_id
        self.displacement_vectors = displacement_vectors
        self.displacement_vectors_indicies = displacement_vectors_indicies
        self.displacement_vertex_buffer_index = displacement_vertex_buffer_index
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        base_vertex_buffer_id = from_int(obj.get("base_vertex_buffer_id"))
        displacement_vectors = from_list(
            DisplacementVectorElement.from_dict, obj.get("displacement_vectors")
        )
        displacement_vectors_indicies = from_list(
            from_int, obj.get("displacement_vectors_indicies")
        )
        displacement_vertex_buffer_index = from_int(
            obj.get("displacement_vertex_buffer_index")
        )
        name = from_str(obj.get("name"))
        return MorphElement(
            base_vertex_buffer_id,
            displacement_vectors,
            displacement_vectors_indicies,
            displacement_vertex_buffer_index,
            name,
        )

    def to_dict(self):
        result = {}
        result["base_vertex_buffer_id"] = from_int(self.base_vertex_buffer_id)
        result["displacement_vectors"] = from_list(
            lambda x: to_class(DisplacementVectorElement, x), self.displacement_vectors
        )
        result["displacement_vectors_indicies"] = from_list(
            from_int, self.displacement_vectors_indicies
        )
        result["displacement_vertex_buffer_index"] = from_int(
            self.displacement_vertex_buffer_index
        )
        result["name"] = from_str(self.name)
        return result


class TentacledMorpher:
    def __init__(self, aabb_morph_triggers, displacement_vectors_indices, map, morphs):
        self.aabb_morph_triggers = aabb_morph_triggers
        self.displacement_vectors_indices = displacement_vectors_indices
        self.map = map
        self.morphs = morphs

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        aabb_morph_triggers = from_list(
            AABBMorphTriggerElement.from_dict, obj.get("aabb_morph_triggers")
        )
        displacement_vectors_indices = from_list(
            from_int, obj.get("displacement_vectors_indices")
        )
        map = Map.from_dict(obj.get("map"))
        morphs = from_list(MorphElement.from_dict, obj.get("morphs"))
        return TentacledMorpher(
            aabb_morph_triggers, displacement_vectors_indices, map, morphs
        )

    def to_dict(self):
        result = {}
        result["aabb_morph_triggers"] = from_list(
            lambda x: to_class(AABBMorphTriggerElement, x), self.aabb_morph_triggers
        )
        result["displacement_vectors_indices"] = from_list(
            from_int, self.displacement_vectors_indices
        )
        result["map"] = to_class(Map, self.map)
        result["morphs"] = from_list(lambda x: to_class(MorphElement, x), self.morphs)
        return result


class QuadElement:
    def __init__(self, normal, vertices):
        self.normal = normal
        self.vertices = vertices

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        normal = from_list(from_float, obj.get("normal"))
        vertices = from_list(lambda x: from_list(from_float, x), obj.get("vertices"))
        return QuadElement(normal, vertices)

    def to_dict(self):
        result = {}
        result["normal"] = from_list(to_float, self.normal)
        result["vertices"] = from_list(lambda x: from_list(to_float, x), self.vertices)
        return result


class Schema15:
    def __init__(self, flags, vertices):
        self.flags = flags
        self.vertices = vertices

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        flags = IndexBufferFlags.from_dict(obj.get("flags"))
        vertices = Vertices.from_dict(obj.get("vertices"))
        return Schema15(flags, vertices)

    def to_dict(self):
        result = {}
        result["flags"] = to_class(IndexBufferFlags, self.flags)
        result["vertices"] = to_class(Vertices, self.vertices)
        return result


class QuadRangeInner:
    def __init__(self, end, start):
        self.end = end
        self.start = start

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        end = from_int(obj.get("end"))
        start = from_int(obj.get("start"))
        return QuadRangeInner(end, start)

    def to_dict(self):
        result = {}
        result["end"] = from_int(self.end)
        result["start"] = from_int(self.start)
        return result


class QuadRange:
    def __init__(self, inner):
        self.inner = inner

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        inner = QuadRangeInner.from_dict(obj.get("inner"))
        return QuadRange(inner)

    def to_dict(self):
        result = {}
        result["inner"] = to_class(QuadRangeInner, self.inner)
        return result


class Unused1Element:
    def __init__(self, unused0, unused1, unused2, unused3, unused4, unused5, unused6):
        self.unused0 = unused0
        self.unused1 = unused1
        self.unused2 = unused2
        self.unused3 = unused3
        self.unused4 = unused4
        self.unused5 = unused5
        self.unused6 = unused6

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        unused0 = from_int(obj.get("unused0"))
        unused1 = from_int(obj.get("unused1"))
        unused2 = from_int(obj.get("unused2"))
        unused3 = from_int(obj.get("unused3"))
        unused4 = from_int(obj.get("unused4"))
        unused5 = from_int(obj.get("unused5"))
        unused6 = from_int(obj.get("unused6"))
        return Unused1Element(
            unused0, unused1, unused2, unused3, unused4, unused5, unused6
        )

    def to_dict(self):
        result = {}
        result["unused0"] = from_int(self.unused0)
        result["unused1"] = from_int(self.unused1)
        result["unused2"] = from_int(self.unused2)
        result["unused3"] = from_int(self.unused3)
        result["unused4"] = from_int(self.unused4)
        result["unused5"] = from_int(self.unused5)
        result["unused6"] = from_int(self.unused6)
        return result


class Schema16:
    def __init__(
        self,
        face_count,
        flags,
        index_buffer_index,
        index_buffer_index_begin,
        material_index,
        quad_range,
        unused1_s,
        vertex_buffer_index,
        vertex_buffer_range,
        vertex_buffer_range_begin_or_zero,
        vertex_count,
        vertex_layout,
        zero,
    ):
        self.face_count = face_count
        self.flags = flags
        self.index_buffer_index = index_buffer_index
        self.index_buffer_index_begin = index_buffer_index_begin
        self.material_index = material_index
        self.quad_range = quad_range
        self.unused1_s = unused1_s
        self.vertex_buffer_index = vertex_buffer_index
        self.vertex_buffer_range = vertex_buffer_range
        self.vertex_buffer_range_begin_or_zero = vertex_buffer_range_begin_or_zero
        self.vertex_count = vertex_count
        self.vertex_layout = vertex_layout
        self.zero = zero

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        face_count = from_int(obj.get("face_count"))
        flags = VertexGroupFlags.from_dict(obj.get("flags"))
        index_buffer_index = from_int(obj.get("index_buffer_index"))
        index_buffer_index_begin = from_int(obj.get("index_buffer_index_begin"))
        material_index = from_int(obj.get("material_index"))
        quad_range = QuadRange.from_dict(obj.get("quad_range"))
        unused1_s = from_list(Unused1Element.from_dict, obj.get("unused1s"))
        vertex_buffer_index = from_int(obj.get("vertex_buffer_index"))
        vertex_buffer_range = AABBMorphTriggersRange.from_dict(
            obj.get("vertex_buffer_range")
        )
        vertex_buffer_range_begin_or_zero = from_int(
            obj.get("vertex_buffer_range_begin_or_zero")
        )
        vertex_count = from_int(obj.get("vertex_count"))
        vertex_layout = from_int(obj.get("vertex_layout"))
        zero = from_int(obj.get("zero"))
        return Schema16(
            face_count,
            flags,
            index_buffer_index,
            index_buffer_index_begin,
            material_index,
            quad_range,
            unused1_s,
            vertex_buffer_index,
            vertex_buffer_range,
            vertex_buffer_range_begin_or_zero,
            vertex_count,
            vertex_layout,
            zero,
        )

    def to_dict(self):
        result = {}
        result["face_count"] = from_int(self.face_count)
        result["flags"] = to_class(VertexGroupFlags, self.flags)
        result["index_buffer_index"] = from_int(self.index_buffer_index)
        result["index_buffer_index_begin"] = from_int(self.index_buffer_index_begin)
        result["material_index"] = from_int(self.material_index)
        result["quad_range"] = to_class(QuadRange, self.quad_range)
        result["unused1s"] = from_list(
            lambda x: to_class(Unused1Element, x), self.unused1_s
        )
        result["vertex_buffer_index"] = from_int(self.vertex_buffer_index)
        result["vertex_buffer_range"] = to_class(
            AABBMorphTriggersRange, self.vertex_buffer_range
        )
        result["vertex_buffer_range_begin_or_zero"] = from_int(
            self.vertex_buffer_range_begin_or_zero
        )
        result["vertex_count"] = from_int(self.vertex_count)
        result["vertex_layout"] = from_int(self.vertex_layout)
        result["zero"] = from_int(self.zero)
        return result


class TentacledMeshBuffers:
    def __init__(self, index_buffers, morpher, quads, vertex_buffers, vertex_groups):
        self.index_buffers = index_buffers
        self.morpher = morpher
        self.quads = quads
        self.vertex_buffers = vertex_buffers
        self.vertex_groups = vertex_groups

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        index_buffers = from_list(Schema14.from_dict, obj.get("index_buffers"))
        morpher = TentacledMorpher.from_dict(obj.get("morpher"))
        quads = from_list(QuadElement.from_dict, obj.get("quads"))
        vertex_buffers = from_list(Schema15.from_dict, obj.get("vertex_buffers"))
        vertex_groups = from_list(Schema16.from_dict, obj.get("vertex_groups"))
        return TentacledMeshBuffers(
            index_buffers, morpher, quads, vertex_buffers, vertex_groups
        )

    def to_dict(self):
        result = {}
        result["index_buffers"] = from_list(
            lambda x: to_class(Schema14, x), self.index_buffers
        )
        result["morpher"] = to_class(TentacledMorpher, self.morpher)
        result["quads"] = from_list(lambda x: to_class(QuadElement, x), self.quads)
        result["vertex_buffers"] = from_list(
            lambda x: to_class(Schema15, x), self.vertex_buffers
        )
        result["vertex_groups"] = from_list(
            lambda x: to_class(Schema16, x), self.vertex_groups
        )
        return result


class BodyUnused0:
    def __init__(self, unknown0, unknown1, unknown2, unknown3):
        self.unknown0 = unknown0
        self.unknown1 = unknown1
        self.unknown2 = unknown2
        self.unknown3 = unknown3

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        unknown0 = from_int(obj.get("unknown0"))
        unknown1 = from_int(obj.get("unknown1"))
        unknown2 = from_int(obj.get("unknown2"))
        unknown3 = from_int(obj.get("unknown3"))
        return BodyUnused0(unknown0, unknown1, unknown2, unknown3)

    def to_dict(self):
        result = {}
        result["unknown0"] = from_int(self.unknown0)
        result["unknown1"] = from_int(self.unknown1)
        result["unknown2"] = from_int(self.unknown2)
        result["unknown3"] = from_int(self.unknown3)
        return result


class Schema18:
    def __init__(self, unused0, unused1):
        self.unused0 = unused0
        self.unused1 = unused1

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        unused0 = from_int(obj.get("unused0"))
        unused1 = from_int(obj.get("unused1"))
        return Schema18(unused0, unused1)

    def to_dict(self):
        result = {}
        result["unused0"] = from_int(self.unused0)
        result["unused1"] = from_int(self.unused1)
        return result


class Schema17:
    def __init__(self, unused0_s):
        self.unused0_s = unused0_s

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        unused0_s = from_list(Schema18.from_dict, obj.get("unused0s"))
        return Schema17(unused0_s)

    def to_dict(self):
        result = {}
        result["unused0s"] = from_list(lambda x: to_class(Schema18, x), self.unused0_s)
        return result


class Unused8Element:
    def __init__(self, unuseds):
        self.unuseds = unuseds

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        unuseds = from_list(from_int, obj.get("unuseds"))
        return Unused8Element(unuseds)

    def to_dict(self):
        result = {}
        result["unuseds"] = from_list(from_int, self.unuseds)
        return result


class MeshV1381_67_09PCBody:
    def __init__(
        self,
        collision_aabbs,
        collision_faces,
        material_names,
        mesh_buffers,
        normals,
        short_vec_weirds,
        strip_vertices,
        strips,
        texcoords,
        unused0_s,
        unused4_s,
        unused8_s,
    ):
        self.collision_aabbs = collision_aabbs
        self.collision_faces = collision_faces
        self.material_names = material_names
        self.mesh_buffers = mesh_buffers
        self.normals = normals
        self.short_vec_weirds = short_vec_weirds
        self.strip_vertices = strip_vertices
        self.strips = strips
        self.texcoords = texcoords
        self.unused0_s = unused0_s
        self.unused4_s = unused4_s
        self.unused8_s = unused8_s

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        collision_aabbs = from_list(
            CollisionAABBElement.from_dict, obj.get("collision_aabbs")
        )
        collision_faces = from_list(
            BodyCollisionFace.from_dict, obj.get("collision_faces")
        )
        material_names = from_list(
            lambda x: from_union([from_int, from_str], x), obj.get("material_names")
        )
        mesh_buffers = TentacledMeshBuffers.from_dict(obj.get("mesh_buffers"))
        normals = from_list(lambda x: from_list(from_float, x), obj.get("normals"))
        short_vec_weirds = from_list(
            lambda x: from_list(from_float, x), obj.get("short_vec_weirds")
        )
        strip_vertices = from_list(
            lambda x: from_list(from_float, x), obj.get("strip_vertices")
        )
        strips = from_list(StripElement.from_dict, obj.get("strips"))
        texcoords = from_list(lambda x: from_list(from_float, x), obj.get("texcoords"))
        unused0_s = from_list(BodyUnused0.from_dict, obj.get("unused0s"))
        unused4_s = from_list(Schema17.from_dict, obj.get("unused4s"))
        unused8_s = from_list(Unused8Element.from_dict, obj.get("unused8s"))
        return MeshV1381_67_09PCBody(
            collision_aabbs,
            collision_faces,
            material_names,
            mesh_buffers,
            normals,
            short_vec_weirds,
            strip_vertices,
            strips,
            texcoords,
            unused0_s,
            unused4_s,
            unused8_s,
        )

    def to_dict(self):
        result = {}
        result["collision_aabbs"] = from_list(
            lambda x: to_class(CollisionAABBElement, x), self.collision_aabbs
        )
        result["collision_faces"] = from_list(
            lambda x: to_class(BodyCollisionFace, x), self.collision_faces
        )
        result["material_names"] = from_list(
            lambda x: from_union([from_int, from_str], x), self.material_names
        )
        result["mesh_buffers"] = to_class(TentacledMeshBuffers, self.mesh_buffers)
        result["normals"] = from_list(lambda x: from_list(to_float, x), self.normals)
        result["short_vec_weirds"] = from_list(
            lambda x: from_list(to_float, x), self.short_vec_weirds
        )
        result["strip_vertices"] = from_list(
            lambda x: from_list(to_float, x), self.strip_vertices
        )
        result["strips"] = from_list(lambda x: to_class(StripElement, x), self.strips)
        result["texcoords"] = from_list(
            lambda x: from_list(to_float, x), self.texcoords
        )
        result["unused0s"] = from_list(
            lambda x: to_class(BodyUnused0, x), self.unused0_s
        )
        result["unused4s"] = from_list(lambda x: to_class(Schema17, x), self.unused4_s)
        result["unused8s"] = from_list(
            lambda x: to_class(Unused8Element, x), self.unused8_s
        )
        return result


class LinkHeaderFade:
    def __init__(self, fade_close, x, y):
        self.fade_close = fade_close
        self.x = x
        self.y = y

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        fade_close = from_float(obj.get("fade_close"))
        x = from_float(obj.get("x"))
        y = from_float(obj.get("y"))
        return LinkHeaderFade(fade_close, x, y)

    def to_dict(self):
        result = {}
        result["fade_close"] = to_float(self.fade_close)
        result["x"] = to_float(self.x)
        result["y"] = to_float(self.y)
        return result


class MeshV1381_67_09PCLinkHeader:
    def __init__(self, dyn_boxes, dyn_spheres, fade, names, resource_link_header):
        self.dyn_boxes = dyn_boxes
        self.dyn_spheres = dyn_spheres
        self.fade = fade
        self.names = names
        self.resource_link_header = resource_link_header

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        dyn_boxes = from_list(CollisionBoxElement.from_dict, obj.get("dyn_boxes"))
        dyn_spheres = from_list(SpheresColElement.from_dict, obj.get("dyn_spheres"))
        fade = LinkHeaderFade.from_dict(obj.get("fade"))
        names = from_list(
            lambda x: from_union([from_int, from_str], x), obj.get("names")
        )
        resource_link_header = CameraV1381_67_09PCLinkHeader.from_dict(
            obj.get("resource_link_header")
        )
        return MeshV1381_67_09PCLinkHeader(
            dyn_boxes, dyn_spheres, fade, names, resource_link_header
        )

    def to_dict(self):
        result = {}
        result["dyn_boxes"] = from_list(
            lambda x: to_class(CollisionBoxElement, x), self.dyn_boxes
        )
        result["dyn_spheres"] = from_list(
            lambda x: to_class(SpheresColElement, x), self.dyn_spheres
        )
        result["fade"] = to_class(LinkHeaderFade, self.fade)
        result["names"] = from_list(
            lambda x: from_union([from_int, from_str], x), self.names
        )
        result["resource_link_header"] = to_class(
            CameraV1381_67_09PCLinkHeader, self.resource_link_header
        )
        return result


class MeshV1381_67_09_PC:
    def __init__(self, body, class_name, link_header, link_name, name):
        self.body = body
        self.class_name = class_name
        self.link_header = link_header
        self.link_name = link_name
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        body = MeshV1381_67_09PCBody.from_dict(obj.get("body"))
        class_name = from_union([from_int, from_str], obj.get("class_name"))
        link_header = MeshV1381_67_09PCLinkHeader.from_dict(obj.get("link_header"))
        link_name = from_union([from_none, from_int, from_str], obj.get("link_name"))
        name = from_union([from_int, from_str], obj.get("name"))
        return MeshV1381_67_09_PC(body, class_name, link_header, link_name, name)

    def to_dict(self):
        result = {}
        result["body"] = to_class(MeshV1381_67_09PCBody, self.body)
        result["class_name"] = from_union([from_int, from_str], self.class_name)
        result["link_header"] = to_class(MeshV1381_67_09PCLinkHeader, self.link_header)
        if self.link_name is not None:
            result["link_name"] = from_union(
                [from_none, from_int, from_str], self.link_name
            )
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class Mesh:
    def __init__(self, mesh_v1_06_63_02_pc, mesh_v1_291_03_06_pc, mesh_v1_381_67_09_pc):
        self.mesh_v1_06_63_02_pc = mesh_v1_06_63_02_pc
        self.mesh_v1_291_03_06_pc = mesh_v1_291_03_06_pc
        self.mesh_v1_381_67_09_pc = mesh_v1_381_67_09_pc

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        mesh_v1_06_63_02_pc = from_union(
            [MeshV106_63_02_PC.from_dict, from_none], obj.get("MeshV1_06_63_02PC")
        )
        mesh_v1_291_03_06_pc = from_union(
            [MeshV1291_03_06_PC.from_dict, from_none], obj.get("MeshV1_291_03_06PC")
        )
        mesh_v1_381_67_09_pc = from_union(
            [MeshV1381_67_09_PC.from_dict, from_none], obj.get("MeshV1_381_67_09PC")
        )
        return Mesh(mesh_v1_06_63_02_pc, mesh_v1_291_03_06_pc, mesh_v1_381_67_09_pc)

    def to_dict(self):
        result = {}
        if self.mesh_v1_06_63_02_pc is not None:
            result["MeshV1_06_63_02PC"] = from_union(
                [lambda x: to_class(MeshV106_63_02_PC, x), from_none],
                self.mesh_v1_06_63_02_pc,
            )
        if self.mesh_v1_291_03_06_pc is not None:
            result["MeshV1_291_03_06PC"] = from_union(
                [lambda x: to_class(MeshV1291_03_06_PC, x), from_none],
                self.mesh_v1_291_03_06_pc,
            )
        if self.mesh_v1_381_67_09_pc is not None:
            result["MeshV1_381_67_09PC"] = from_union(
                [lambda x: to_class(MeshV1381_67_09_PC, x), from_none],
                self.mesh_v1_381_67_09_pc,
            )
        return result


class UnkStruct1Element:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        data = from_list(from_int, obj.get("data"))
        return UnkStruct1Element(data)

    def to_dict(self):
        result = {}
        result["data"] = from_list(from_int, self.data)
        return result


class UnkStruct2Element:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        data = from_list(from_int, obj.get("data"))
        return UnkStruct2Element(data)

    def to_dict(self):
        result = {}
        result["data"] = from_list(from_int, self.data)
        return result


class UnkStruct3Element:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        data = from_list(from_int, obj.get("data"))
        return UnkStruct3Element(data)

    def to_dict(self):
        result = {}
        result["data"] = from_list(from_int, self.data)
        return result


class UnkStruct4Element:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        data = from_list(from_int, obj.get("data"))
        return UnkStruct4Element(data)

    def to_dict(self):
        result = {}
        result["data"] = from_list(from_int, self.data)
        return result


class MeshVolume:
    def __init__(self, unk_struct1_s, unk_struct2_s, unk_struct3_s, unk_struct4_s):
        self.unk_struct1_s = unk_struct1_s
        self.unk_struct2_s = unk_struct2_s
        self.unk_struct3_s = unk_struct3_s
        self.unk_struct4_s = unk_struct4_s

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        unk_struct1_s = from_list(UnkStruct1Element.from_dict, obj.get("unk_struct1s"))
        unk_struct2_s = from_list(UnkStruct2Element.from_dict, obj.get("unk_struct2s"))
        unk_struct3_s = from_list(UnkStruct3Element.from_dict, obj.get("unk_struct3s"))
        unk_struct4_s = from_list(UnkStruct4Element.from_dict, obj.get("unk_struct4s"))
        return MeshVolume(unk_struct1_s, unk_struct2_s, unk_struct3_s, unk_struct4_s)

    def to_dict(self):
        result = {}
        result["unk_struct1s"] = from_list(
            lambda x: to_class(UnkStruct1Element, x), self.unk_struct1_s
        )
        result["unk_struct2s"] = from_list(
            lambda x: to_class(UnkStruct2Element, x), self.unk_struct2_s
        )
        result["unk_struct3s"] = from_list(
            lambda x: to_class(UnkStruct3Element, x), self.unk_struct3_s
        )
        result["unk_struct4s"] = from_list(
            lambda x: to_class(UnkStruct4Element, x), self.unk_struct4_s
        )
        return result


class StickyObjectDatas:
    def __init__(self, color, unknown):
        self.color = color
        self.unknown = unknown

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        color = from_list(from_float, obj.get("color"))
        unknown = from_float(obj.get("unknown"))
        return StickyObjectDatas(color, unknown)

    def to_dict(self):
        result = {}
        result["color"] = from_list(to_float, self.color)
        result["unknown"] = to_float(self.unknown)
        return result


class MeshDataV106_63_02PCBody:
    def __init__(self, mesh_volume, object_datas):
        self.mesh_volume = mesh_volume
        self.object_datas = object_datas

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        mesh_volume = MeshVolume.from_dict(obj.get("mesh_volume"))
        object_datas = StickyObjectDatas.from_dict(obj.get("object_datas"))
        return MeshDataV106_63_02PCBody(mesh_volume, object_datas)

    def to_dict(self):
        result = {}
        result["mesh_volume"] = to_class(MeshVolume, self.mesh_volume)
        result["object_datas"] = to_class(StickyObjectDatas, self.object_datas)
        return result


class MeshDataV106_63_02_PC:
    def __init__(self, body, class_name, link_header, link_name, name):
        self.body = body
        self.class_name = class_name
        self.link_header = link_header
        self.link_name = link_name
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        body = MeshDataV106_63_02PCBody.from_dict(obj.get("body"))
        class_name = from_union([from_int, from_str], obj.get("class_name"))
        link_header = AnimationV1291_03_06PCLinkHeader.from_dict(obj.get("link_header"))
        link_name = from_union([from_none, from_int, from_str], obj.get("link_name"))
        name = from_union([from_int, from_str], obj.get("name"))
        return MeshDataV106_63_02_PC(body, class_name, link_header, link_name, name)

    def to_dict(self):
        result = {}
        result["body"] = to_class(MeshDataV106_63_02PCBody, self.body)
        result["class_name"] = from_union([from_int, from_str], self.class_name)
        result["link_header"] = to_class(
            AnimationV1291_03_06PCLinkHeader, self.link_header
        )
        if self.link_name is not None:
            result["link_name"] = from_union(
                [from_none, from_int, from_str], self.link_name
            )
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class IndigoObjectDatas:
    def __init__(self, color, unknown_float):
        self.color = color
        self.unknown_float = unknown_float

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        color = from_list(from_float, obj.get("color"))
        unknown_float = from_float(obj.get("unknown_float"))
        return IndigoObjectDatas(color, unknown_float)

    def to_dict(self):
        result = {}
        result["color"] = from_list(to_float, self.color)
        result["unknown_float"] = to_float(self.unknown_float)
        return result


class MeshDataV1291_03_06PCBody:
    def __init__(self, object_datas):
        self.object_datas = object_datas

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        object_datas = IndigoObjectDatas.from_dict(obj.get("object_datas"))
        return MeshDataV1291_03_06PCBody(object_datas)

    def to_dict(self):
        result = {}
        result["object_datas"] = to_class(IndigoObjectDatas, self.object_datas)
        return result


class MeshDataV1291_03_06_PC:
    def __init__(self, body, class_name, link_header, link_name, name):
        self.body = body
        self.class_name = class_name
        self.link_header = link_header
        self.link_name = link_name
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        body = MeshDataV1291_03_06PCBody.from_dict(obj.get("body"))
        class_name = from_union([from_int, from_str], obj.get("class_name"))
        link_header = AnimationV1291_03_06PCLinkHeader.from_dict(obj.get("link_header"))
        link_name = from_union([from_none, from_int, from_str], obj.get("link_name"))
        name = from_union([from_int, from_str], obj.get("name"))
        return MeshDataV1291_03_06_PC(body, class_name, link_header, link_name, name)

    def to_dict(self):
        result = {}
        result["body"] = to_class(MeshDataV1291_03_06PCBody, self.body)
        result["class_name"] = from_union([from_int, from_str], self.class_name)
        result["link_header"] = to_class(
            AnimationV1291_03_06PCLinkHeader, self.link_header
        )
        if self.link_name is not None:
            result["link_name"] = from_union(
                [from_none, from_int, from_str], self.link_name
            )
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class MeshDataV1381_67_09PCBody:
    def __init__(self, flags, zeroes):
        self.flags = flags
        self.zeroes = zeroes

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        flags = ResourceDatasFlags.from_dict(obj.get("flags"))
        zeroes = from_list(from_int, obj.get("zeroes"))
        return MeshDataV1381_67_09PCBody(flags, zeroes)

    def to_dict(self):
        result = {}
        result["flags"] = to_class(ResourceDatasFlags, self.flags)
        result["zeroes"] = from_list(from_int, self.zeroes)
        return result


class MeshDataV1381_67_09_PC:
    def __init__(self, body, class_name, link_header, link_name, name):
        self.body = body
        self.class_name = class_name
        self.link_header = link_header
        self.link_name = link_name
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        body = MeshDataV1381_67_09PCBody.from_dict(obj.get("body"))
        class_name = from_union([from_int, from_str], obj.get("class_name"))
        link_header = AnimationV1381_67_09PCLinkHeader.from_dict(obj.get("link_header"))
        link_name = from_union([from_none, from_int, from_str], obj.get("link_name"))
        name = from_union([from_int, from_str], obj.get("name"))
        return MeshDataV1381_67_09_PC(body, class_name, link_header, link_name, name)

    def to_dict(self):
        result = {}
        result["body"] = to_class(MeshDataV1381_67_09PCBody, self.body)
        result["class_name"] = from_union([from_int, from_str], self.class_name)
        result["link_header"] = to_class(
            AnimationV1381_67_09PCLinkHeader, self.link_header
        )
        if self.link_name is not None:
            result["link_name"] = from_union(
                [from_none, from_int, from_str], self.link_name
            )
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class MeshData:
    def __init__(
        self,
        mesh_data_v1_06_63_02_pc,
        mesh_data_v1_291_03_06_pc,
        mesh_data_v1_381_67_09_pc,
    ):
        self.mesh_data_v1_06_63_02_pc = mesh_data_v1_06_63_02_pc
        self.mesh_data_v1_291_03_06_pc = mesh_data_v1_291_03_06_pc
        self.mesh_data_v1_381_67_09_pc = mesh_data_v1_381_67_09_pc

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        mesh_data_v1_06_63_02_pc = from_union(
            [MeshDataV106_63_02_PC.from_dict, from_none],
            obj.get("MeshDataV1_06_63_02PC"),
        )
        mesh_data_v1_291_03_06_pc = from_union(
            [MeshDataV1291_03_06_PC.from_dict, from_none],
            obj.get("MeshDataV1_291_03_06PC"),
        )
        mesh_data_v1_381_67_09_pc = from_union(
            [MeshDataV1381_67_09_PC.from_dict, from_none],
            obj.get("MeshDataV1_381_67_09PC"),
        )
        return MeshData(
            mesh_data_v1_06_63_02_pc,
            mesh_data_v1_291_03_06_pc,
            mesh_data_v1_381_67_09_pc,
        )

    def to_dict(self):
        result = {}
        if self.mesh_data_v1_06_63_02_pc is not None:
            result["MeshDataV1_06_63_02PC"] = from_union(
                [lambda x: to_class(MeshDataV106_63_02_PC, x), from_none],
                self.mesh_data_v1_06_63_02_pc,
            )
        if self.mesh_data_v1_291_03_06_pc is not None:
            result["MeshDataV1_291_03_06PC"] = from_union(
                [lambda x: to_class(MeshDataV1291_03_06_PC, x), from_none],
                self.mesh_data_v1_291_03_06_pc,
            )
        if self.mesh_data_v1_381_67_09_pc is not None:
            result["MeshDataV1_381_67_09PC"] = from_union(
                [lambda x: to_class(MeshDataV1381_67_09_PC, x), from_none],
                self.mesh_data_v1_381_67_09_pc,
            )
        return result


class PurpleCollideSeadsRect:
    def __init__(self, bottom_right, top_left):
        self.bottom_right = bottom_right
        self.top_left = top_left

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        bottom_right = from_list(from_int, obj.get("bottom_right"))
        top_left = from_list(from_int, obj.get("top_left"))
        return PurpleCollideSeadsRect(bottom_right, top_left)

    def to_dict(self):
        result = {}
        result["bottom_right"] = from_list(from_int, self.bottom_right)
        result["top_left"] = from_list(from_int, self.top_left)
        return result


class NodeV106_63_02PCBody:
    def __init__(
        self,
        b_sphere,
        bitmap_name,
        collide_seads_id1,
        collide_seads_id2,
        collide_seads_rect,
        colors,
        display_seads_id1,
        display_seads_id2,
        display_seads_rect,
        flags,
        head_child_name,
        inverse_world_transform,
        next_node_name,
        one_over_scale,
        other_scale,
        parent_name,
        placeholder_world_matrix_ptr,
        prev_node_name,
        resource_name,
        rotation,
        scale,
        translation,
        unk_float1,
        unk_mat,
        unk_name,
        unk_vec3_f,
        unk_vec3_f2,
        unk_vec3_f3,
        unknown4,
        unknown5,
        unknown6,
        user_define_name,
        world_transform,
    ):
        self.b_sphere = b_sphere
        self.bitmap_name = bitmap_name
        self.collide_seads_id1 = collide_seads_id1
        self.collide_seads_id2 = collide_seads_id2
        self.collide_seads_rect = collide_seads_rect
        self.colors = colors
        self.display_seads_id1 = display_seads_id1
        self.display_seads_id2 = display_seads_id2
        self.display_seads_rect = display_seads_rect
        self.flags = flags
        self.head_child_name = head_child_name
        self.inverse_world_transform = inverse_world_transform
        self.next_node_name = next_node_name
        self.one_over_scale = one_over_scale
        self.other_scale = other_scale
        self.parent_name = parent_name
        self.placeholder_world_matrix_ptr = placeholder_world_matrix_ptr
        self.prev_node_name = prev_node_name
        self.resource_name = resource_name
        self.rotation = rotation
        self.scale = scale
        self.translation = translation
        self.unk_float1 = unk_float1
        self.unk_mat = unk_mat
        self.unk_name = unk_name
        self.unk_vec3_f = unk_vec3_f
        self.unk_vec3_f2 = unk_vec3_f2
        self.unk_vec3_f3 = unk_vec3_f3
        self.unknown4 = unknown4
        self.unknown5 = unknown5
        self.unknown6 = unknown6
        self.user_define_name = user_define_name
        self.world_transform = world_transform

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        b_sphere = Sphere.from_dict(obj.get("b_sphere"))
        bitmap_name = from_union([from_int, from_str], obj.get("bitmap_name"))
        collide_seads_id1 = from_int(obj.get("collide_seads_id1"))
        collide_seads_id2 = from_int(obj.get("collide_seads_id2"))
        collide_seads_rect = PurpleCollideSeadsRect.from_dict(
            obj.get("collide_seads_rect")
        )
        colors = from_list(from_float, obj.get("colors"))
        display_seads_id1 = from_int(obj.get("display_seads_id1"))
        display_seads_id2 = from_int(obj.get("display_seads_id2"))
        display_seads_rect = PurpleCollideSeadsRect.from_dict(
            obj.get("display_seads_rect")
        )
        flags = from_int(obj.get("flags"))
        head_child_name = from_union([from_int, from_str], obj.get("head_child_name"))
        inverse_world_transform = from_list(
            lambda x: from_list(from_float, x), obj.get("inverse_world_transform")
        )
        next_node_name = from_union([from_int, from_str], obj.get("next_node_name"))
        one_over_scale = from_float(obj.get("one_over_scale"))
        other_scale = from_float(obj.get("other_scale"))
        parent_name = from_union([from_int, from_str], obj.get("parent_name"))
        placeholder_world_matrix_ptr = from_int(obj.get("placeholder_world_matrix_ptr"))
        prev_node_name = from_union([from_int, from_str], obj.get("prev_node_name"))
        resource_name = from_union([from_int, from_str], obj.get("resource_name"))
        rotation = from_list(from_float, obj.get("rotation"))
        scale = from_float(obj.get("scale"))
        translation = from_list(from_float, obj.get("translation"))
        unk_float1 = from_float(obj.get("unk_float1"))
        unk_mat = from_list(lambda x: from_list(from_float, x), obj.get("unk_mat"))
        unk_name = from_union([from_int, from_str], obj.get("unk_name"))
        unk_vec3_f = from_list(from_float, obj.get("unk_vec3f"))
        unk_vec3_f2 = from_list(from_float, obj.get("unk_vec3f2"))
        unk_vec3_f3 = from_list(from_float, obj.get("unk_vec3f3"))
        unknown4 = from_int(obj.get("unknown4"))
        unknown5 = from_int(obj.get("unknown5"))
        unknown6 = from_int(obj.get("unknown6"))
        user_define_name = from_union([from_int, from_str], obj.get("user_define_name"))
        world_transform = from_list(
            lambda x: from_list(from_float, x), obj.get("world_transform")
        )
        return NodeV106_63_02PCBody(
            b_sphere,
            bitmap_name,
            collide_seads_id1,
            collide_seads_id2,
            collide_seads_rect,
            colors,
            display_seads_id1,
            display_seads_id2,
            display_seads_rect,
            flags,
            head_child_name,
            inverse_world_transform,
            next_node_name,
            one_over_scale,
            other_scale,
            parent_name,
            placeholder_world_matrix_ptr,
            prev_node_name,
            resource_name,
            rotation,
            scale,
            translation,
            unk_float1,
            unk_mat,
            unk_name,
            unk_vec3_f,
            unk_vec3_f2,
            unk_vec3_f3,
            unknown4,
            unknown5,
            unknown6,
            user_define_name,
            world_transform,
        )

    def to_dict(self):
        result = {}
        result["b_sphere"] = to_class(Sphere, self.b_sphere)
        result["bitmap_name"] = from_union([from_int, from_str], self.bitmap_name)
        result["collide_seads_id1"] = from_int(self.collide_seads_id1)
        result["collide_seads_id2"] = from_int(self.collide_seads_id2)
        result["collide_seads_rect"] = to_class(
            PurpleCollideSeadsRect, self.collide_seads_rect
        )
        result["colors"] = from_list(to_float, self.colors)
        result["display_seads_id1"] = from_int(self.display_seads_id1)
        result["display_seads_id2"] = from_int(self.display_seads_id2)
        result["display_seads_rect"] = to_class(
            PurpleCollideSeadsRect, self.display_seads_rect
        )
        result["flags"] = from_int(self.flags)
        result["head_child_name"] = from_union(
            [from_int, from_str], self.head_child_name
        )
        result["inverse_world_transform"] = from_list(
            lambda x: from_list(to_float, x), self.inverse_world_transform
        )
        result["next_node_name"] = from_union([from_int, from_str], self.next_node_name)
        result["one_over_scale"] = to_float(self.one_over_scale)
        result["other_scale"] = to_float(self.other_scale)
        result["parent_name"] = from_union([from_int, from_str], self.parent_name)
        result["placeholder_world_matrix_ptr"] = from_int(
            self.placeholder_world_matrix_ptr
        )
        result["prev_node_name"] = from_union([from_int, from_str], self.prev_node_name)
        result["resource_name"] = from_union([from_int, from_str], self.resource_name)
        result["rotation"] = from_list(to_float, self.rotation)
        result["scale"] = to_float(self.scale)
        result["translation"] = from_list(to_float, self.translation)
        result["unk_float1"] = to_float(self.unk_float1)
        result["unk_mat"] = from_list(lambda x: from_list(to_float, x), self.unk_mat)
        result["unk_name"] = from_union([from_int, from_str], self.unk_name)
        result["unk_vec3f"] = from_list(to_float, self.unk_vec3_f)
        result["unk_vec3f2"] = from_list(to_float, self.unk_vec3_f2)
        result["unk_vec3f3"] = from_list(to_float, self.unk_vec3_f3)
        result["unknown4"] = from_int(self.unknown4)
        result["unknown5"] = from_int(self.unknown5)
        result["unknown6"] = from_int(self.unknown6)
        result["user_define_name"] = from_union(
            [from_int, from_str], self.user_define_name
        )
        result["world_transform"] = from_list(
            lambda x: from_list(to_float, x), self.world_transform
        )
        return result


class NodeV106_63_02_PC:
    def __init__(self, body, class_name, link_header, link_name, name):
        self.body = body
        self.class_name = class_name
        self.link_header = link_header
        self.link_name = link_name
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        body = NodeV106_63_02PCBody.from_dict(obj.get("body"))
        class_name = from_union([from_int, from_str], obj.get("class_name"))
        link_header = AnimationV1291_03_06PCLinkHeader.from_dict(obj.get("link_header"))
        link_name = from_union([from_none, from_int, from_str], obj.get("link_name"))
        name = from_union([from_int, from_str], obj.get("name"))
        return NodeV106_63_02_PC(body, class_name, link_header, link_name, name)

    def to_dict(self):
        result = {}
        result["body"] = to_class(NodeV106_63_02PCBody, self.body)
        result["class_name"] = from_union([from_int, from_str], self.class_name)
        result["link_header"] = to_class(
            AnimationV1291_03_06PCLinkHeader, self.link_header
        )
        if self.link_name is not None:
            result["link_name"] = from_union(
                [from_none, from_int, from_str], self.link_name
            )
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class FluffyCollideSeadsRect:
    def __init__(self, bottom_right, top_left):
        self.bottom_right = bottom_right
        self.top_left = top_left

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        bottom_right = from_list(from_int, obj.get("bottom_right"))
        top_left = from_list(from_int, obj.get("top_left"))
        return FluffyCollideSeadsRect(bottom_right, top_left)

    def to_dict(self):
        result = {}
        result["bottom_right"] = from_list(from_int, self.bottom_right)
        result["top_left"] = from_list(from_int, self.top_left)
        return result


class NodeV1291_03_06PCBody:
    def __init__(
        self,
        b_sphere,
        bitmap_name,
        collide_seads_id1,
        collide_seads_id2,
        collide_seads_rect,
        color,
        display_seads_id1,
        display_seads_id2,
        display_seads_rect,
        flags,
        head_child_name,
        inverse_world_transform,
        light_data_name,
        next_node_name,
        one_over_scale,
        other_scale,
        parent_name,
        placeholder_world_matrix_ptr,
        prev_node_name,
        resource_node_name,
        rotation,
        scale,
        translation,
        unknown4,
        unknown5,
        unknown6,
        unknown_float1,
        unknown_matrix,
        unknown_name,
        unknown_vec3_f1,
        unknown_vec3_f2,
        user_define_name,
        world_transform,
    ):
        self.b_sphere = b_sphere
        self.bitmap_name = bitmap_name
        self.collide_seads_id1 = collide_seads_id1
        self.collide_seads_id2 = collide_seads_id2
        self.collide_seads_rect = collide_seads_rect
        self.color = color
        self.display_seads_id1 = display_seads_id1
        self.display_seads_id2 = display_seads_id2
        self.display_seads_rect = display_seads_rect
        self.flags = flags
        self.head_child_name = head_child_name
        self.inverse_world_transform = inverse_world_transform
        self.light_data_name = light_data_name
        self.next_node_name = next_node_name
        self.one_over_scale = one_over_scale
        self.other_scale = other_scale
        self.parent_name = parent_name
        self.placeholder_world_matrix_ptr = placeholder_world_matrix_ptr
        self.prev_node_name = prev_node_name
        self.resource_node_name = resource_node_name
        self.rotation = rotation
        self.scale = scale
        self.translation = translation
        self.unknown4 = unknown4
        self.unknown5 = unknown5
        self.unknown6 = unknown6
        self.unknown_float1 = unknown_float1
        self.unknown_matrix = unknown_matrix
        self.unknown_name = unknown_name
        self.unknown_vec3_f1 = unknown_vec3_f1
        self.unknown_vec3_f2 = unknown_vec3_f2
        self.user_define_name = user_define_name
        self.world_transform = world_transform

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        b_sphere = Sphere.from_dict(obj.get("b_sphere"))
        bitmap_name = from_union([from_int, from_str], obj.get("bitmap_name"))
        collide_seads_id1 = from_union(
            [from_int, from_str], obj.get("collide_seads_id1")
        )
        collide_seads_id2 = from_union(
            [from_int, from_str], obj.get("collide_seads_id2")
        )
        collide_seads_rect = FluffyCollideSeadsRect.from_dict(
            obj.get("collide_seads_rect")
        )
        color = from_list(from_float, obj.get("color"))
        display_seads_id1 = from_union(
            [from_int, from_str], obj.get("display_seads_id1")
        )
        display_seads_id2 = from_union(
            [from_int, from_str], obj.get("display_seads_id2")
        )
        display_seads_rect = FluffyCollideSeadsRect.from_dict(
            obj.get("display_seads_rect")
        )
        flags = from_int(obj.get("flags"))
        head_child_name = from_union([from_int, from_str], obj.get("head_child_name"))
        inverse_world_transform = from_list(
            lambda x: from_list(from_float, x), obj.get("inverse_world_transform")
        )
        light_data_name = from_union([from_int, from_str], obj.get("light_data_name"))
        next_node_name = from_union([from_int, from_str], obj.get("next_node_name"))
        one_over_scale = from_float(obj.get("one_over_scale"))
        other_scale = from_float(obj.get("other_scale"))
        parent_name = from_union([from_int, from_str], obj.get("parent_name"))
        placeholder_world_matrix_ptr = from_int(obj.get("placeholder_world_matrix_ptr"))
        prev_node_name = from_union([from_int, from_str], obj.get("prev_node_name"))
        resource_node_name = from_union(
            [from_int, from_str], obj.get("resource_node_name")
        )
        rotation = from_list(from_float, obj.get("rotation"))
        scale = from_float(obj.get("scale"))
        translation = from_list(from_float, obj.get("translation"))
        unknown4 = from_int(obj.get("unknown4"))
        unknown5 = from_int(obj.get("unknown5"))
        unknown6 = from_int(obj.get("unknown6"))
        unknown_float1 = from_float(obj.get("unknown_float1"))
        unknown_matrix = from_list(
            lambda x: from_list(from_float, x), obj.get("unknown_matrix")
        )
        unknown_name = from_union([from_int, from_str], obj.get("unknown_name"))
        unknown_vec3_f1 = from_list(from_float, obj.get("unknown_vec3f1"))
        unknown_vec3_f2 = from_list(from_float, obj.get("unknown_vec3f2"))
        user_define_name = from_union([from_int, from_str], obj.get("user_define_name"))
        world_transform = from_list(
            lambda x: from_list(from_float, x), obj.get("world_transform")
        )
        return NodeV1291_03_06PCBody(
            b_sphere,
            bitmap_name,
            collide_seads_id1,
            collide_seads_id2,
            collide_seads_rect,
            color,
            display_seads_id1,
            display_seads_id2,
            display_seads_rect,
            flags,
            head_child_name,
            inverse_world_transform,
            light_data_name,
            next_node_name,
            one_over_scale,
            other_scale,
            parent_name,
            placeholder_world_matrix_ptr,
            prev_node_name,
            resource_node_name,
            rotation,
            scale,
            translation,
            unknown4,
            unknown5,
            unknown6,
            unknown_float1,
            unknown_matrix,
            unknown_name,
            unknown_vec3_f1,
            unknown_vec3_f2,
            user_define_name,
            world_transform,
        )

    def to_dict(self):
        result = {}
        result["b_sphere"] = to_class(Sphere, self.b_sphere)
        result["bitmap_name"] = from_union([from_int, from_str], self.bitmap_name)
        result["collide_seads_id1"] = from_union(
            [from_int, from_str], self.collide_seads_id1
        )
        result["collide_seads_id2"] = from_union(
            [from_int, from_str], self.collide_seads_id2
        )
        result["collide_seads_rect"] = to_class(
            FluffyCollideSeadsRect, self.collide_seads_rect
        )
        result["color"] = from_list(to_float, self.color)
        result["display_seads_id1"] = from_union(
            [from_int, from_str], self.display_seads_id1
        )
        result["display_seads_id2"] = from_union(
            [from_int, from_str], self.display_seads_id2
        )
        result["display_seads_rect"] = to_class(
            FluffyCollideSeadsRect, self.display_seads_rect
        )
        result["flags"] = from_int(self.flags)
        result["head_child_name"] = from_union(
            [from_int, from_str], self.head_child_name
        )
        result["inverse_world_transform"] = from_list(
            lambda x: from_list(to_float, x), self.inverse_world_transform
        )
        result["light_data_name"] = from_union(
            [from_int, from_str], self.light_data_name
        )
        result["next_node_name"] = from_union([from_int, from_str], self.next_node_name)
        result["one_over_scale"] = to_float(self.one_over_scale)
        result["other_scale"] = to_float(self.other_scale)
        result["parent_name"] = from_union([from_int, from_str], self.parent_name)
        result["placeholder_world_matrix_ptr"] = from_int(
            self.placeholder_world_matrix_ptr
        )
        result["prev_node_name"] = from_union([from_int, from_str], self.prev_node_name)
        result["resource_node_name"] = from_union(
            [from_int, from_str], self.resource_node_name
        )
        result["rotation"] = from_list(to_float, self.rotation)
        result["scale"] = to_float(self.scale)
        result["translation"] = from_list(to_float, self.translation)
        result["unknown4"] = from_int(self.unknown4)
        result["unknown5"] = from_int(self.unknown5)
        result["unknown6"] = from_int(self.unknown6)
        result["unknown_float1"] = to_float(self.unknown_float1)
        result["unknown_matrix"] = from_list(
            lambda x: from_list(to_float, x), self.unknown_matrix
        )
        result["unknown_name"] = from_union([from_int, from_str], self.unknown_name)
        result["unknown_vec3f1"] = from_list(to_float, self.unknown_vec3_f1)
        result["unknown_vec3f2"] = from_list(to_float, self.unknown_vec3_f2)
        result["user_define_name"] = from_union(
            [from_int, from_str], self.user_define_name
        )
        result["world_transform"] = from_list(
            lambda x: from_list(to_float, x), self.world_transform
        )
        return result


class NodeV1291_03_06_PC:
    def __init__(self, body, class_name, link_header, link_name, name):
        self.body = body
        self.class_name = class_name
        self.link_header = link_header
        self.link_name = link_name
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        body = NodeV1291_03_06PCBody.from_dict(obj.get("body"))
        class_name = from_union([from_int, from_str], obj.get("class_name"))
        link_header = AnimationV1291_03_06PCLinkHeader.from_dict(obj.get("link_header"))
        link_name = from_union([from_none, from_int, from_str], obj.get("link_name"))
        name = from_union([from_int, from_str], obj.get("name"))
        return NodeV1291_03_06_PC(body, class_name, link_header, link_name, name)

    def to_dict(self):
        result = {}
        result["body"] = to_class(NodeV1291_03_06PCBody, self.body)
        result["class_name"] = from_union([from_int, from_str], self.class_name)
        result["link_header"] = to_class(
            AnimationV1291_03_06PCLinkHeader, self.link_header
        )
        if self.link_name is not None:
            result["link_name"] = from_union(
                [from_none, from_int, from_str], self.link_name
            )
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class NodeV1381_67_09PCBody:
    def __init__(
        self,
        bitmap_name,
        collide_seads_rect,
        color,
        display_seads_rect,
        flags,
        head_child_name,
        light_data_name,
        lod_data_or_particles_data_name,
        lod_or_particles_name,
        negative_four,
        next_sibling,
        parent_name,
        prev_sibling,
        reciprocal_scale2,
        rotation,
        rotation2,
        scale,
        scale2,
        sphere,
        translation,
        unknown10,
        unused_name2,
        user_define_name,
        world_transform_mat4,
    ):
        self.bitmap_name = bitmap_name
        self.collide_seads_rect = collide_seads_rect
        self.color = color
        self.display_seads_rect = display_seads_rect
        self.flags = flags
        self.head_child_name = head_child_name
        self.light_data_name = light_data_name
        self.lod_data_or_particles_data_name = lod_data_or_particles_data_name
        self.lod_or_particles_name = lod_or_particles_name
        self.negative_four = negative_four
        self.next_sibling = next_sibling
        self.parent_name = parent_name
        self.prev_sibling = prev_sibling
        self.reciprocal_scale2 = reciprocal_scale2
        self.rotation = rotation
        self.rotation2 = rotation2
        self.scale = scale
        self.scale2 = scale2
        self.sphere = sphere
        self.translation = translation
        self.unknown10 = unknown10
        self.unused_name2 = unused_name2
        self.user_define_name = user_define_name
        self.world_transform_mat4 = world_transform_mat4

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        bitmap_name = from_union([from_int, from_str], obj.get("bitmap_name"))
        collide_seads_rect = FluffyCollideSeadsRect.from_dict(
            obj.get("collide_seads_rect")
        )
        color = from_list(from_float, obj.get("color"))
        display_seads_rect = FluffyCollideSeadsRect.from_dict(
            obj.get("display_seads_rect")
        )
        flags = from_int(obj.get("flags"))
        head_child_name = from_union([from_int, from_str], obj.get("head_child_name"))
        light_data_name = from_union([from_int, from_str], obj.get("light_data_name"))
        lod_data_or_particles_data_name = from_union(
            [from_int, from_str], obj.get("lod_data_or_particles_data_name")
        )
        lod_or_particles_name = from_union(
            [from_int, from_str], obj.get("lod_or_particles_name")
        )
        negative_four = from_int(obj.get("negative_four"))
        next_sibling = from_union([from_int, from_str], obj.get("next_sibling"))
        parent_name = from_union([from_int, from_str], obj.get("parent_name"))
        prev_sibling = from_union([from_int, from_str], obj.get("prev_sibling"))
        reciprocal_scale2 = from_float(obj.get("reciprocal_scale2"))
        rotation = from_list(from_float, obj.get("rotation"))
        rotation2 = from_list(from_float, obj.get("rotation2"))
        scale = from_float(obj.get("scale"))
        scale2 = from_float(obj.get("scale2"))
        sphere = Sphere.from_dict(obj.get("sphere"))
        translation = from_list(from_float, obj.get("translation"))
        unknown10 = from_float(obj.get("unknown10"))
        unused_name2 = from_union([from_int, from_str], obj.get("unused_name2"))
        user_define_name = from_union([from_int, from_str], obj.get("user_define_name"))
        world_transform_mat4 = from_list(
            lambda x: from_list(from_float, x), obj.get("world_transform_mat4")
        )
        return NodeV1381_67_09PCBody(
            bitmap_name,
            collide_seads_rect,
            color,
            display_seads_rect,
            flags,
            head_child_name,
            light_data_name,
            lod_data_or_particles_data_name,
            lod_or_particles_name,
            negative_four,
            next_sibling,
            parent_name,
            prev_sibling,
            reciprocal_scale2,
            rotation,
            rotation2,
            scale,
            scale2,
            sphere,
            translation,
            unknown10,
            unused_name2,
            user_define_name,
            world_transform_mat4,
        )

    def to_dict(self):
        result = {}
        result["bitmap_name"] = from_union([from_int, from_str], self.bitmap_name)
        result["collide_seads_rect"] = to_class(
            FluffyCollideSeadsRect, self.collide_seads_rect
        )
        result["color"] = from_list(to_float, self.color)
        result["display_seads_rect"] = to_class(
            FluffyCollideSeadsRect, self.display_seads_rect
        )
        result["flags"] = from_int(self.flags)
        result["head_child_name"] = from_union(
            [from_int, from_str], self.head_child_name
        )
        result["light_data_name"] = from_union(
            [from_int, from_str], self.light_data_name
        )
        result["lod_data_or_particles_data_name"] = from_union(
            [from_int, from_str], self.lod_data_or_particles_data_name
        )
        result["lod_or_particles_name"] = from_union(
            [from_int, from_str], self.lod_or_particles_name
        )
        result["negative_four"] = from_int(self.negative_four)
        result["next_sibling"] = from_union([from_int, from_str], self.next_sibling)
        result["parent_name"] = from_union([from_int, from_str], self.parent_name)
        result["prev_sibling"] = from_union([from_int, from_str], self.prev_sibling)
        result["reciprocal_scale2"] = to_float(self.reciprocal_scale2)
        result["rotation"] = from_list(to_float, self.rotation)
        result["rotation2"] = from_list(to_float, self.rotation2)
        result["scale"] = to_float(self.scale)
        result["scale2"] = to_float(self.scale2)
        result["sphere"] = to_class(Sphere, self.sphere)
        result["translation"] = from_list(to_float, self.translation)
        result["unknown10"] = to_float(self.unknown10)
        result["unused_name2"] = from_union([from_int, from_str], self.unused_name2)
        result["user_define_name"] = from_union(
            [from_int, from_str], self.user_define_name
        )
        result["world_transform_mat4"] = from_list(
            lambda x: from_list(to_float, x), self.world_transform_mat4
        )
        return result


class NodeV1381_67_09_PC:
    def __init__(self, body, class_name, link_header, link_name, name):
        self.body = body
        self.class_name = class_name
        self.link_header = link_header
        self.link_name = link_name
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        body = NodeV1381_67_09PCBody.from_dict(obj.get("body"))
        class_name = from_union([from_int, from_str], obj.get("class_name"))
        link_header = AnimationV1381_67_09PCLinkHeader.from_dict(obj.get("link_header"))
        link_name = from_union([from_none, from_int, from_str], obj.get("link_name"))
        name = from_union([from_int, from_str], obj.get("name"))
        return NodeV1381_67_09_PC(body, class_name, link_header, link_name, name)

    def to_dict(self):
        result = {}
        result["body"] = to_class(NodeV1381_67_09PCBody, self.body)
        result["class_name"] = from_union([from_int, from_str], self.class_name)
        result["link_header"] = to_class(
            AnimationV1381_67_09PCLinkHeader, self.link_header
        )
        if self.link_name is not None:
            result["link_name"] = from_union(
                [from_none, from_int, from_str], self.link_name
            )
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class Node:
    def __init__(self, node_v1_06_63_02_pc, node_v1_291_03_06_pc, node_v1_381_67_09_pc):
        self.node_v1_06_63_02_pc = node_v1_06_63_02_pc
        self.node_v1_291_03_06_pc = node_v1_291_03_06_pc
        self.node_v1_381_67_09_pc = node_v1_381_67_09_pc

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        node_v1_06_63_02_pc = from_union(
            [NodeV106_63_02_PC.from_dict, from_none], obj.get("NodeV1_06_63_02PC")
        )
        node_v1_291_03_06_pc = from_union(
            [NodeV1291_03_06_PC.from_dict, from_none], obj.get("NodeV1_291_03_06PC")
        )
        node_v1_381_67_09_pc = from_union(
            [NodeV1381_67_09_PC.from_dict, from_none], obj.get("NodeV1_381_67_09PC")
        )
        return Node(node_v1_06_63_02_pc, node_v1_291_03_06_pc, node_v1_381_67_09_pc)

    def to_dict(self):
        result = {}
        if self.node_v1_06_63_02_pc is not None:
            result["NodeV1_06_63_02PC"] = from_union(
                [lambda x: to_class(NodeV106_63_02_PC, x), from_none],
                self.node_v1_06_63_02_pc,
            )
        if self.node_v1_291_03_06_pc is not None:
            result["NodeV1_291_03_06PC"] = from_union(
                [lambda x: to_class(NodeV1291_03_06_PC, x), from_none],
                self.node_v1_291_03_06_pc,
            )
        if self.node_v1_381_67_09_pc is not None:
            result["NodeV1_381_67_09PC"] = from_union(
                [lambda x: to_class(NodeV1381_67_09_PC, x), from_none],
                self.node_v1_381_67_09_pc,
            )
        return result


class OmniV106_63_02PCBody:
    def __init__(
        self,
        color,
        end,
        intensity,
        material_anim_name,
        scaled_color,
        spot_angle_bias,
        spot_angle_half_rad,
        spot_angle_scale,
        start,
        texture_projection_matrix,
        unused,
    ):
        self.color = color
        self.end = end
        self.intensity = intensity
        self.material_anim_name = material_anim_name
        self.scaled_color = scaled_color
        self.spot_angle_bias = spot_angle_bias
        self.spot_angle_half_rad = spot_angle_half_rad
        self.spot_angle_scale = spot_angle_scale
        self.start = start
        self.texture_projection_matrix = texture_projection_matrix
        self.unused = unused

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        color = from_list(from_float, obj.get("color"))
        end = from_float(obj.get("end"))
        intensity = from_float(obj.get("intensity"))
        material_anim_name = from_union(
            [from_int, from_str], obj.get("material_anim_name")
        )
        scaled_color = from_list(from_float, obj.get("scaled_color"))
        spot_angle_bias = from_float(obj.get("spot_angle_bias"))
        spot_angle_half_rad = from_float(obj.get("spot_angle_half_rad"))
        spot_angle_scale = from_float(obj.get("spot_angle_scale"))
        start = from_float(obj.get("start"))
        texture_projection_matrix = from_list(
            lambda x: from_list(from_float, x), obj.get("texture_projection_matrix")
        )
        unused = from_float(obj.get("unused"))
        return OmniV106_63_02PCBody(
            color,
            end,
            intensity,
            material_anim_name,
            scaled_color,
            spot_angle_bias,
            spot_angle_half_rad,
            spot_angle_scale,
            start,
            texture_projection_matrix,
            unused,
        )

    def to_dict(self):
        result = {}
        result["color"] = from_list(to_float, self.color)
        result["end"] = to_float(self.end)
        result["intensity"] = to_float(self.intensity)
        result["material_anim_name"] = from_union(
            [from_int, from_str], self.material_anim_name
        )
        result["scaled_color"] = from_list(to_float, self.scaled_color)
        result["spot_angle_bias"] = to_float(self.spot_angle_bias)
        result["spot_angle_half_rad"] = to_float(self.spot_angle_half_rad)
        result["spot_angle_scale"] = to_float(self.spot_angle_scale)
        result["start"] = to_float(self.start)
        result["texture_projection_matrix"] = from_list(
            lambda x: from_list(to_float, x), self.texture_projection_matrix
        )
        result["unused"] = to_float(self.unused)
        return result


class OmniV106_63_02_PC:
    def __init__(self, body, class_name, link_header, link_name, name):
        self.body = body
        self.class_name = class_name
        self.link_header = link_header
        self.link_name = link_name
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        body = OmniV106_63_02PCBody.from_dict(obj.get("body"))
        class_name = from_union([from_int, from_str], obj.get("class_name"))
        link_header = CameraZoneV106_63_02PCLinkHeader.from_dict(obj.get("link_header"))
        link_name = from_union([from_none, from_int, from_str], obj.get("link_name"))
        name = from_union([from_int, from_str], obj.get("name"))
        return OmniV106_63_02_PC(body, class_name, link_header, link_name, name)

    def to_dict(self):
        result = {}
        result["body"] = to_class(OmniV106_63_02PCBody, self.body)
        result["class_name"] = from_union([from_int, from_str], self.class_name)
        result["link_header"] = to_class(
            CameraZoneV106_63_02PCLinkHeader, self.link_header
        )
        if self.link_name is not None:
            result["link_name"] = from_union(
                [from_none, from_int, from_str], self.link_name
            )
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class OmniV1381_67_09PCBody:
    def __init__(
        self,
        material_anim_name0,
        material_anim_name1,
        scale_matrix,
        translation_matrix,
        unknown0,
        unknown1,
        unknown10,
        unknown11,
        unknown12,
        unknown13,
        unknown14,
        unknown15,
        unknown2,
        unknown3,
        unknown4,
        unknown5,
        unknown6,
        unknown7,
        unknown8,
        unknown9,
    ):
        self.material_anim_name0 = material_anim_name0
        self.material_anim_name1 = material_anim_name1
        self.scale_matrix = scale_matrix
        self.translation_matrix = translation_matrix
        self.unknown0 = unknown0
        self.unknown1 = unknown1
        self.unknown10 = unknown10
        self.unknown11 = unknown11
        self.unknown12 = unknown12
        self.unknown13 = unknown13
        self.unknown14 = unknown14
        self.unknown15 = unknown15
        self.unknown2 = unknown2
        self.unknown3 = unknown3
        self.unknown4 = unknown4
        self.unknown5 = unknown5
        self.unknown6 = unknown6
        self.unknown7 = unknown7
        self.unknown8 = unknown8
        self.unknown9 = unknown9

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        material_anim_name0 = from_union(
            [from_int, from_str], obj.get("material_anim_name0")
        )
        material_anim_name1 = from_union(
            [from_int, from_str], obj.get("material_anim_name1")
        )
        scale_matrix = from_list(
            lambda x: from_list(from_float, x), obj.get("scale_matrix")
        )
        translation_matrix = from_list(
            lambda x: from_list(from_float, x), obj.get("translation_matrix")
        )
        unknown0 = from_float(obj.get("unknown0"))
        unknown1 = from_float(obj.get("unknown1"))
        unknown10 = from_int(obj.get("unknown10"))
        unknown11 = from_float(obj.get("unknown11"))
        unknown12 = from_float(obj.get("unknown12"))
        unknown13 = from_float(obj.get("unknown13"))
        unknown14 = from_float(obj.get("unknown14"))
        unknown15 = from_float(obj.get("unknown15"))
        unknown2 = from_float(obj.get("unknown2"))
        unknown3 = from_float(obj.get("unknown3"))
        unknown4 = from_float(obj.get("unknown4"))
        unknown5 = from_float(obj.get("unknown5"))
        unknown6 = from_float(obj.get("unknown6"))
        unknown7 = from_float(obj.get("unknown7"))
        unknown8 = from_float(obj.get("unknown8"))
        unknown9 = from_float(obj.get("unknown9"))
        return OmniV1381_67_09PCBody(
            material_anim_name0,
            material_anim_name1,
            scale_matrix,
            translation_matrix,
            unknown0,
            unknown1,
            unknown10,
            unknown11,
            unknown12,
            unknown13,
            unknown14,
            unknown15,
            unknown2,
            unknown3,
            unknown4,
            unknown5,
            unknown6,
            unknown7,
            unknown8,
            unknown9,
        )

    def to_dict(self):
        result = {}
        result["material_anim_name0"] = from_union(
            [from_int, from_str], self.material_anim_name0
        )
        result["material_anim_name1"] = from_union(
            [from_int, from_str], self.material_anim_name1
        )
        result["scale_matrix"] = from_list(
            lambda x: from_list(to_float, x), self.scale_matrix
        )
        result["translation_matrix"] = from_list(
            lambda x: from_list(to_float, x), self.translation_matrix
        )
        result["unknown0"] = to_float(self.unknown0)
        result["unknown1"] = to_float(self.unknown1)
        result["unknown10"] = from_int(self.unknown10)
        result["unknown11"] = to_float(self.unknown11)
        result["unknown12"] = to_float(self.unknown12)
        result["unknown13"] = to_float(self.unknown13)
        result["unknown14"] = to_float(self.unknown14)
        result["unknown15"] = to_float(self.unknown15)
        result["unknown2"] = to_float(self.unknown2)
        result["unknown3"] = to_float(self.unknown3)
        result["unknown4"] = to_float(self.unknown4)
        result["unknown5"] = to_float(self.unknown5)
        result["unknown6"] = to_float(self.unknown6)
        result["unknown7"] = to_float(self.unknown7)
        result["unknown8"] = to_float(self.unknown8)
        result["unknown9"] = to_float(self.unknown9)
        return result


class OmniV1381_67_09_PC:
    def __init__(self, body, class_name, link_header, link_name, name):
        self.body = body
        self.class_name = class_name
        self.link_header = link_header
        self.link_name = link_name
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        body = OmniV1381_67_09PCBody.from_dict(obj.get("body"))
        class_name = from_union([from_int, from_str], obj.get("class_name"))
        link_header = CameraV1381_67_09PCLinkHeader.from_dict(obj.get("link_header"))
        link_name = from_union([from_none, from_int, from_str], obj.get("link_name"))
        name = from_union([from_int, from_str], obj.get("name"))
        return OmniV1381_67_09_PC(body, class_name, link_header, link_name, name)

    def to_dict(self):
        result = {}
        result["body"] = to_class(OmniV1381_67_09PCBody, self.body)
        result["class_name"] = from_union([from_int, from_str], self.class_name)
        result["link_header"] = to_class(
            CameraV1381_67_09PCLinkHeader, self.link_header
        )
        if self.link_name is not None:
            result["link_name"] = from_union(
                [from_none, from_int, from_str], self.link_name
            )
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class Omni:
    def __init__(self, omni_v1_06_63_02_pc, omni_v1_381_67_09_pc):
        self.omni_v1_06_63_02_pc = omni_v1_06_63_02_pc
        self.omni_v1_381_67_09_pc = omni_v1_381_67_09_pc

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        omni_v1_06_63_02_pc = from_union(
            [OmniV106_63_02_PC.from_dict, from_none], obj.get("OmniV1_06_63_02PC")
        )
        omni_v1_381_67_09_pc = from_union(
            [OmniV1381_67_09_PC.from_dict, from_none], obj.get("OmniV1_381_67_09PC")
        )
        return Omni(omni_v1_06_63_02_pc, omni_v1_381_67_09_pc)

    def to_dict(self):
        result = {}
        if self.omni_v1_06_63_02_pc is not None:
            result["OmniV1_06_63_02PC"] = from_union(
                [lambda x: to_class(OmniV106_63_02_PC, x), from_none],
                self.omni_v1_06_63_02_pc,
            )
        if self.omni_v1_381_67_09_pc is not None:
            result["OmniV1_381_67_09PC"] = from_union(
                [lambda x: to_class(OmniV1381_67_09_PC, x), from_none],
                self.omni_v1_381_67_09_pc,
            )
        return result


class ParticlesEmitterFlags:
    def __init__(self, value):
        self.value = value

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        value = from_int(obj.get("value"))
        return ParticlesEmitterFlags(value)

    def to_dict(self):
        result = {}
        result["value"] = from_int(self.value)
        return result


class Unknown63Keyframe:
    def __init__(self, time, value):
        self.time = time
        self.value = value

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        time = from_float(obj.get("time"))
        value = from_float(obj.get("value"))
        return Unknown63Keyframe(time, value)

    def to_dict(self):
        result = {}
        result["time"] = to_float(self.time)
        result["value"] = to_float(self.value)
        return result


class Unknown63:
    def __init__(self, interpolation_type, keyframes):
        self.interpolation_type = interpolation_type
        self.keyframes = keyframes

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        interpolation_type = InterpolationType(obj.get("interpolation_type"))
        keyframes = from_list(Unknown63Keyframe.from_dict, obj.get("keyframes"))
        return Unknown63(interpolation_type, keyframes)

    def to_dict(self):
        result = {}
        result["interpolation_type"] = to_enum(
            InterpolationType, self.interpolation_type
        )
        result["keyframes"] = from_list(
            lambda x: to_class(Unknown63Keyframe, x), self.keyframes
        )
        return result


class ParticlesEmitterElement:
    def __init__(
        self,
        emitter_speed,
        emitter_speed_variation,
        flags,
        life,
        life_variation,
        loop_period,
        material_anim_name,
        max_quantity,
        off_axis,
        off_axis_variation,
        off_plane,
        off_plane_variation,
        p_cloud_offset,
        p_cloud_size,
        p_cloud_type,
        unknown60,
        unknown61,
        unknown62,
        unknown63,
        unknown64,
        unknown65,
        unknown66,
        velocity,
        velocity_variation,
    ):
        self.emitter_speed = emitter_speed
        self.emitter_speed_variation = emitter_speed_variation
        self.flags = flags
        self.life = life
        self.life_variation = life_variation
        self.loop_period = loop_period
        self.material_anim_name = material_anim_name
        self.max_quantity = max_quantity
        self.off_axis = off_axis
        self.off_axis_variation = off_axis_variation
        self.off_plane = off_plane
        self.off_plane_variation = off_plane_variation
        self.p_cloud_offset = p_cloud_offset
        self.p_cloud_size = p_cloud_size
        self.p_cloud_type = p_cloud_type
        self.unknown60 = unknown60
        self.unknown61 = unknown61
        self.unknown62 = unknown62
        self.unknown63 = unknown63
        self.unknown64 = unknown64
        self.unknown65 = unknown65
        self.unknown66 = unknown66
        self.velocity = velocity
        self.velocity_variation = velocity_variation

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        emitter_speed = from_float(obj.get("emitter_speed"))
        emitter_speed_variation = from_float(obj.get("emitter_speed_variation"))
        flags = ParticlesEmitterFlags.from_dict(obj.get("flags"))
        life = from_float(obj.get("life"))
        life_variation = from_float(obj.get("life_variation"))
        loop_period = from_float(obj.get("loop_period"))
        material_anim_name = from_union(
            [from_int, from_str], obj.get("material_anim_name")
        )
        max_quantity = from_int(obj.get("max_quantity"))
        off_axis = from_float(obj.get("off_axis"))
        off_axis_variation = from_float(obj.get("off_axis_variation"))
        off_plane = from_float(obj.get("off_plane"))
        off_plane_variation = from_float(obj.get("off_plane_variation"))
        p_cloud_offset = from_list(from_float, obj.get("p_cloud_offset"))
        p_cloud_size = from_list(from_float, obj.get("p_cloud_size"))
        p_cloud_type = from_int(obj.get("p_cloud_type"))
        unknown60 = ScaleKeyframer.from_dict(obj.get("unknown60"))
        unknown61 = ParamsKeyframer.from_dict(obj.get("unknown61"))
        unknown62 = ParamsKeyframer.from_dict(obj.get("unknown62"))
        unknown63 = Unknown63.from_dict(obj.get("unknown63"))
        unknown64 = DiffuseKeyframer.from_dict(obj.get("unknown64"))
        unknown65 = DiffuseKeyframer.from_dict(obj.get("unknown65"))
        unknown66 = Unknown63.from_dict(obj.get("unknown66"))
        velocity = from_float(obj.get("velocity"))
        velocity_variation = from_float(obj.get("velocity_variation"))
        return ParticlesEmitterElement(
            emitter_speed,
            emitter_speed_variation,
            flags,
            life,
            life_variation,
            loop_period,
            material_anim_name,
            max_quantity,
            off_axis,
            off_axis_variation,
            off_plane,
            off_plane_variation,
            p_cloud_offset,
            p_cloud_size,
            p_cloud_type,
            unknown60,
            unknown61,
            unknown62,
            unknown63,
            unknown64,
            unknown65,
            unknown66,
            velocity,
            velocity_variation,
        )

    def to_dict(self):
        result = {}
        result["emitter_speed"] = to_float(self.emitter_speed)
        result["emitter_speed_variation"] = to_float(self.emitter_speed_variation)
        result["flags"] = to_class(ParticlesEmitterFlags, self.flags)
        result["life"] = to_float(self.life)
        result["life_variation"] = to_float(self.life_variation)
        result["loop_period"] = to_float(self.loop_period)
        result["material_anim_name"] = from_union(
            [from_int, from_str], self.material_anim_name
        )
        result["max_quantity"] = from_int(self.max_quantity)
        result["off_axis"] = to_float(self.off_axis)
        result["off_axis_variation"] = to_float(self.off_axis_variation)
        result["off_plane"] = to_float(self.off_plane)
        result["off_plane_variation"] = to_float(self.off_plane_variation)
        result["p_cloud_offset"] = from_list(to_float, self.p_cloud_offset)
        result["p_cloud_size"] = from_list(to_float, self.p_cloud_size)
        result["p_cloud_type"] = from_int(self.p_cloud_type)
        result["unknown60"] = to_class(ScaleKeyframer, self.unknown60)
        result["unknown61"] = to_class(ParamsKeyframer, self.unknown61)
        result["unknown62"] = to_class(ParamsKeyframer, self.unknown62)
        result["unknown63"] = to_class(Unknown63, self.unknown63)
        result["unknown64"] = to_class(DiffuseKeyframer, self.unknown64)
        result["unknown65"] = to_class(DiffuseKeyframer, self.unknown65)
        result["unknown66"] = to_class(Unknown63, self.unknown66)
        result["velocity"] = to_float(self.velocity)
        result["velocity_variation"] = to_float(self.velocity_variation)
        return result


class ParticlesV1381_67_09PCBody:
    def __init__(self, mats, particles_emitters, unknown2, unknown3):
        self.mats = mats
        self.particles_emitters = particles_emitters
        self.unknown2 = unknown2
        self.unknown3 = unknown3

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        mats = from_list(
            lambda x: from_list(lambda x: from_list(from_float, x), x), obj.get("mats")
        )
        particles_emitters = from_list(
            ParticlesEmitterElement.from_dict, obj.get("particles_emitters")
        )
        unknown2 = from_float(obj.get("unknown2"))
        unknown3 = from_int(obj.get("unknown3"))
        return ParticlesV1381_67_09PCBody(mats, particles_emitters, unknown2, unknown3)

    def to_dict(self):
        result = {}
        result["mats"] = from_list(
            lambda x: from_list(lambda x: from_list(to_float, x), x), self.mats
        )
        result["particles_emitters"] = from_list(
            lambda x: to_class(ParticlesEmitterElement, x), self.particles_emitters
        )
        result["unknown2"] = to_float(self.unknown2)
        result["unknown3"] = from_int(self.unknown3)
        return result


class ParticlesV1381_67_09_PC:
    def __init__(self, body, class_name, link_header, link_name, name):
        self.body = body
        self.class_name = class_name
        self.link_header = link_header
        self.link_name = link_name
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        body = ParticlesV1381_67_09PCBody.from_dict(obj.get("body"))
        class_name = from_union([from_int, from_str], obj.get("class_name"))
        link_header = CameraV1381_67_09PCLinkHeader.from_dict(obj.get("link_header"))
        link_name = from_union([from_none, from_int, from_str], obj.get("link_name"))
        name = from_union([from_int, from_str], obj.get("name"))
        return ParticlesV1381_67_09_PC(body, class_name, link_header, link_name, name)

    def to_dict(self):
        result = {}
        result["body"] = to_class(ParticlesV1381_67_09PCBody, self.body)
        result["class_name"] = from_union([from_int, from_str], self.class_name)
        result["link_header"] = to_class(
            CameraV1381_67_09PCLinkHeader, self.link_header
        )
        if self.link_name is not None:
            result["link_name"] = from_union(
                [from_none, from_int, from_str], self.link_name
            )
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class Particles:
    def __init__(self, particles_v1_381_67_09_pc):
        self.particles_v1_381_67_09_pc = particles_v1_381_67_09_pc

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        particles_v1_381_67_09_pc = ParticlesV1381_67_09_PC.from_dict(
            obj.get("ParticlesV1_381_67_09PC")
        )
        return Particles(particles_v1_381_67_09_pc)

    def to_dict(self):
        result = {}
        result["ParticlesV1_381_67_09PC"] = to_class(
            ParticlesV1381_67_09_PC, self.particles_v1_381_67_09_pc
        )
        return result


class FluffyFade:
    def __init__(self, fade_close, x, y):
        self.fade_close = fade_close
        self.x = x
        self.y = y

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        fade_close = from_float(obj.get("fade_close"))
        x = from_float(obj.get("x"))
        y = from_float(obj.get("y"))
        return FluffyFade(fade_close, x, y)

    def to_dict(self):
        result = {}
        result["fade_close"] = to_float(self.fade_close)
        result["x"] = to_float(self.x)
        result["y"] = to_float(self.y)
        return result


class ParticlesDataV1381_67_09PCBody:
    def __init__(self, fade, flags, position, shorts, zero):
        self.fade = fade
        self.flags = flags
        self.position = position
        self.shorts = shorts
        self.zero = zero

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        fade = FluffyFade.from_dict(obj.get("fade"))
        flags = ResourceDatasFlags.from_dict(obj.get("flags"))
        position = from_list(from_float, obj.get("position"))
        shorts = from_list(from_int, obj.get("shorts"))
        zero = from_int(obj.get("zero"))
        return ParticlesDataV1381_67_09PCBody(fade, flags, position, shorts, zero)

    def to_dict(self):
        result = {}
        result["fade"] = to_class(FluffyFade, self.fade)
        result["flags"] = to_class(ResourceDatasFlags, self.flags)
        result["position"] = from_list(to_float, self.position)
        result["shorts"] = from_list(from_int, self.shorts)
        result["zero"] = from_int(self.zero)
        return result


class ParticlesDataV1381_67_09_PC:
    def __init__(self, body, class_name, link_header, link_name, name):
        self.body = body
        self.class_name = class_name
        self.link_header = link_header
        self.link_name = link_name
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        body = ParticlesDataV1381_67_09PCBody.from_dict(obj.get("body"))
        class_name = from_union([from_int, from_str], obj.get("class_name"))
        link_header = AnimationV1381_67_09PCLinkHeader.from_dict(obj.get("link_header"))
        link_name = from_union([from_none, from_int, from_str], obj.get("link_name"))
        name = from_union([from_int, from_str], obj.get("name"))
        return ParticlesDataV1381_67_09_PC(
            body, class_name, link_header, link_name, name
        )

    def to_dict(self):
        result = {}
        result["body"] = to_class(ParticlesDataV1381_67_09PCBody, self.body)
        result["class_name"] = from_union([from_int, from_str], self.class_name)
        result["link_header"] = to_class(
            AnimationV1381_67_09PCLinkHeader, self.link_header
        )
        if self.link_name is not None:
            result["link_name"] = from_union(
                [from_none, from_int, from_str], self.link_name
            )
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class ParticlesData:
    def __init__(self, particles_data_v1_381_67_09_pc):
        self.particles_data_v1_381_67_09_pc = particles_data_v1_381_67_09_pc

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        particles_data_v1_381_67_09_pc = ParticlesDataV1381_67_09_PC.from_dict(
            obj.get("ParticlesDataV1_381_67_09PC")
        )
        return ParticlesData(particles_data_v1_381_67_09_pc)

    def to_dict(self):
        result = {}
        result["ParticlesDataV1_381_67_09PC"] = to_class(
            ParticlesDataV1381_67_09_PC, self.particles_data_v1_381_67_09_pc
        )
        return result


class RotShapeV106_63_02PCBody:
    def __init__(
        self,
        local_uvs,
        local_vertices,
        material_anim_names,
        material_indices,
        rot_shape_type,
        scale,
    ):
        self.local_uvs = local_uvs
        self.local_vertices = local_vertices
        self.material_anim_names = material_anim_names
        self.material_indices = material_indices
        self.rot_shape_type = rot_shape_type
        self.scale = scale

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        local_uvs = from_list(lambda x: from_list(from_float, x), obj.get("local_uvs"))
        local_vertices = from_list(
            lambda x: from_list(from_float, x), obj.get("local_vertices")
        )
        material_anim_names = from_list(
            lambda x: from_union([from_int, from_str], x),
            obj.get("material_anim_names"),
        )
        material_indices = from_list(from_int, obj.get("material_indices"))
        rot_shape_type = from_int(obj.get("rot_shape_type"))
        scale = from_float(obj.get("scale"))
        return RotShapeV106_63_02PCBody(
            local_uvs,
            local_vertices,
            material_anim_names,
            material_indices,
            rot_shape_type,
            scale,
        )

    def to_dict(self):
        result = {}
        result["local_uvs"] = from_list(
            lambda x: from_list(to_float, x), self.local_uvs
        )
        result["local_vertices"] = from_list(
            lambda x: from_list(to_float, x), self.local_vertices
        )
        result["material_anim_names"] = from_list(
            lambda x: from_union([from_int, from_str], x), self.material_anim_names
        )
        result["material_indices"] = from_list(from_int, self.material_indices)
        result["rot_shape_type"] = from_int(self.rot_shape_type)
        result["scale"] = to_float(self.scale)
        return result


class Schema20:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        data = from_list(from_int, obj.get("data"))
        return Schema20(data)

    def to_dict(self):
        result = {}
        result["data"] = from_list(from_int, self.data)
        return result


class Schema19:
    def __init__(self, morph_target_desc_relateds, name):
        self.morph_target_desc_relateds = morph_target_desc_relateds
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        morph_target_desc_relateds = from_list(
            Schema20.from_dict, obj.get("morph_target_desc_relateds")
        )
        name = from_int(obj.get("name"))
        return Schema19(morph_target_desc_relateds, name)

    def to_dict(self):
        result = {}
        result["morph_target_desc_relateds"] = from_list(
            lambda x: to_class(Schema20, x), self.morph_target_desc_relateds
        )
        result["name"] = from_int(self.name)
        return result


class Schema21:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        data = from_list(from_int, obj.get("data"))
        return Schema21(data)

    def to_dict(self):
        result = {}
        result["data"] = from_list(from_int, self.data)
        return result


class LinkHeaderMorpher:
    def __init__(self, morph_target_descs, morpher_relateds):
        self.morph_target_descs = morph_target_descs
        self.morpher_relateds = morpher_relateds

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        morph_target_descs = from_list(
            Schema19.from_dict, obj.get("morph_target_descs")
        )
        morpher_relateds = from_list(Schema21.from_dict, obj.get("morpher_relateds"))
        return LinkHeaderMorpher(morph_target_descs, morpher_relateds)

    def to_dict(self):
        result = {}
        result["morph_target_descs"] = from_list(
            lambda x: to_class(Schema19, x), self.morph_target_descs
        )
        result["morpher_relateds"] = from_list(
            lambda x: to_class(Schema21, x), self.morpher_relateds
        )
        return result


class LinkHeaderPointsRelateds1:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        data = from_list(from_int, obj.get("data"))
        return LinkHeaderPointsRelateds1(data)

    def to_dict(self):
        result = {}
        result["data"] = from_list(from_int, self.data)
        return result


class RotShapeV106_63_02PCLinkHeader:
    def __init__(self, morpher, points_relateds1, resource_link_header, vertices):
        self.morpher = morpher
        self.points_relateds1 = points_relateds1
        self.resource_link_header = resource_link_header
        self.vertices = vertices

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        morpher = LinkHeaderMorpher.from_dict(obj.get("morpher"))
        points_relateds1 = from_list(
            LinkHeaderPointsRelateds1.from_dict, obj.get("points_relateds1")
        )
        resource_link_header = AnimationV1291_03_06PCLinkHeader.from_dict(
            obj.get("resource_link_header")
        )
        vertices = from_list(lambda x: from_list(from_float, x), obj.get("vertices"))
        return RotShapeV106_63_02PCLinkHeader(
            morpher, points_relateds1, resource_link_header, vertices
        )

    def to_dict(self):
        result = {}
        result["morpher"] = to_class(LinkHeaderMorpher, self.morpher)
        result["points_relateds1"] = from_list(
            lambda x: to_class(LinkHeaderPointsRelateds1, x), self.points_relateds1
        )
        result["resource_link_header"] = to_class(
            AnimationV1291_03_06PCLinkHeader, self.resource_link_header
        )
        result["vertices"] = from_list(lambda x: from_list(to_float, x), self.vertices)
        return result


class RotShapeV106_63_02_PC:
    def __init__(self, body, class_name, link_header, link_name, name):
        self.body = body
        self.class_name = class_name
        self.link_header = link_header
        self.link_name = link_name
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        body = RotShapeV106_63_02PCBody.from_dict(obj.get("body"))
        class_name = from_union([from_int, from_str], obj.get("class_name"))
        link_header = RotShapeV106_63_02PCLinkHeader.from_dict(obj.get("link_header"))
        link_name = from_union([from_none, from_int, from_str], obj.get("link_name"))
        name = from_union([from_int, from_str], obj.get("name"))
        return RotShapeV106_63_02_PC(body, class_name, link_header, link_name, name)

    def to_dict(self):
        result = {}
        result["body"] = to_class(RotShapeV106_63_02PCBody, self.body)
        result["class_name"] = from_union([from_int, from_str], self.class_name)
        result["link_header"] = to_class(
            RotShapeV106_63_02PCLinkHeader, self.link_header
        )
        if self.link_name is not None:
            result["link_name"] = from_union(
                [from_none, from_int, from_str], self.link_name
            )
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class Schema22:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        data = from_list(from_int, obj.get("data"))
        return Schema22(data)

    def to_dict(self):
        result = {}
        result["data"] = from_list(from_int, self.data)
        return result


class Schema23:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        data = from_list(from_int, obj.get("data"))
        return Schema23(data)

    def to_dict(self):
        result = {}
        result["data"] = from_list(from_int, self.data)
        return result


class TentacledPoints:
    def __init__(self, points_related0_s, points_related1_s, vertices):
        self.points_related0_s = points_related0_s
        self.points_related1_s = points_related1_s
        self.vertices = vertices

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        points_related0_s = from_list(Schema22.from_dict, obj.get("points_related0s"))
        points_related1_s = from_list(Schema23.from_dict, obj.get("points_related1s"))
        vertices = from_list(lambda x: from_list(from_float, x), obj.get("vertices"))
        return TentacledPoints(points_related0_s, points_related1_s, vertices)

    def to_dict(self):
        result = {}
        result["points_related0s"] = from_list(
            lambda x: to_class(Schema22, x), self.points_related0_s
        )
        result["points_related1s"] = from_list(
            lambda x: to_class(Schema23, x), self.points_related1_s
        )
        result["vertices"] = from_list(lambda x: from_list(to_float, x), self.vertices)
        return result


class RotShapeV1291_03_06PCBody:
    def __init__(
        self,
        local_uvs,
        local_vertices,
        material_anims,
        material_indices,
        points,
        rot_shape_type,
        scale,
    ):
        self.local_uvs = local_uvs
        self.local_vertices = local_vertices
        self.material_anims = material_anims
        self.material_indices = material_indices
        self.points = points
        self.rot_shape_type = rot_shape_type
        self.scale = scale

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        local_uvs = from_list(lambda x: from_list(from_float, x), obj.get("local_uvs"))
        local_vertices = from_list(
            lambda x: from_list(from_float, x), obj.get("local_vertices")
        )
        material_anims = from_list(
            lambda x: from_union([from_int, from_str], x), obj.get("material_anims")
        )
        material_indices = from_list(from_int, obj.get("material_indices"))
        points = TentacledPoints.from_dict(obj.get("points"))
        rot_shape_type = from_int(obj.get("rot_shape_type"))
        scale = from_float(obj.get("scale"))
        return RotShapeV1291_03_06PCBody(
            local_uvs,
            local_vertices,
            material_anims,
            material_indices,
            points,
            rot_shape_type,
            scale,
        )

    def to_dict(self):
        result = {}
        result["local_uvs"] = from_list(
            lambda x: from_list(to_float, x), self.local_uvs
        )
        result["local_vertices"] = from_list(
            lambda x: from_list(to_float, x), self.local_vertices
        )
        result["material_anims"] = from_list(
            lambda x: from_union([from_int, from_str], x), self.material_anims
        )
        result["material_indices"] = from_list(from_int, self.material_indices)
        result["points"] = to_class(TentacledPoints, self.points)
        result["rot_shape_type"] = from_int(self.rot_shape_type)
        result["scale"] = to_float(self.scale)
        return result


class RotShapeV1291_03_06_PC:
    def __init__(self, body, class_name, link_header, link_name, name):
        self.body = body
        self.class_name = class_name
        self.link_header = link_header
        self.link_name = link_name
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        body = RotShapeV1291_03_06PCBody.from_dict(obj.get("body"))
        class_name = from_union([from_int, from_str], obj.get("class_name"))
        link_header = CameraZoneV106_63_02PCLinkHeader.from_dict(obj.get("link_header"))
        link_name = from_union([from_none, from_int, from_str], obj.get("link_name"))
        name = from_union([from_int, from_str], obj.get("name"))
        return RotShapeV1291_03_06_PC(body, class_name, link_header, link_name, name)

    def to_dict(self):
        result = {}
        result["body"] = to_class(RotShapeV1291_03_06PCBody, self.body)
        result["class_name"] = from_union([from_int, from_str], self.class_name)
        result["link_header"] = to_class(
            CameraZoneV106_63_02PCLinkHeader, self.link_header
        )
        if self.link_name is not None:
            result["link_name"] = from_union(
                [from_none, from_int, from_str], self.link_name
            )
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class BillboardMode(Enum):
    COMPLETE_BILLBOARD = "CompleteBillboard"
    Y_BILLBOARD = "YBillboard"


class RotShapeV1381_67_09PCBody:
    def __init__(
        self,
        billboard_mode,
        material_anim_names,
        material_anim_names_indices,
        origins,
        scale,
        sizes,
        texcoords,
        zero,
    ):
        self.billboard_mode = billboard_mode
        self.material_anim_names = material_anim_names
        self.material_anim_names_indices = material_anim_names_indices
        self.origins = origins
        self.scale = scale
        self.sizes = sizes
        self.texcoords = texcoords
        self.zero = zero

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        billboard_mode = BillboardMode(obj.get("billboard_mode"))
        material_anim_names = from_list(
            lambda x: from_union([from_int, from_str], x),
            obj.get("material_anim_names"),
        )
        material_anim_names_indices = from_list(
            from_int, obj.get("material_anim_names_indices")
        )
        origins = from_list(lambda x: from_list(from_float, x), obj.get("origins"))
        scale = from_float(obj.get("scale"))
        sizes = from_list(lambda x: from_list(from_float, x), obj.get("sizes"))
        texcoords = from_list(lambda x: from_list(from_float, x), obj.get("texcoords"))
        zero = from_float(obj.get("zero"))
        return RotShapeV1381_67_09PCBody(
            billboard_mode,
            material_anim_names,
            material_anim_names_indices,
            origins,
            scale,
            sizes,
            texcoords,
            zero,
        )

    def to_dict(self):
        result = {}
        result["billboard_mode"] = to_enum(BillboardMode, self.billboard_mode)
        result["material_anim_names"] = from_list(
            lambda x: from_union([from_int, from_str], x), self.material_anim_names
        )
        result["material_anim_names_indices"] = from_list(
            from_int, self.material_anim_names_indices
        )
        result["origins"] = from_list(lambda x: from_list(to_float, x), self.origins)
        result["scale"] = to_float(self.scale)
        result["sizes"] = from_list(lambda x: from_list(to_float, x), self.sizes)
        result["texcoords"] = from_list(
            lambda x: from_list(to_float, x), self.texcoords
        )
        result["zero"] = to_float(self.zero)
        return result


class RotShapeV1381_67_09_PC:
    def __init__(self, body, class_name, link_header, link_name, name):
        self.body = body
        self.class_name = class_name
        self.link_header = link_header
        self.link_name = link_name
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        body = RotShapeV1381_67_09PCBody.from_dict(obj.get("body"))
        class_name = from_union([from_int, from_str], obj.get("class_name"))
        link_header = CameraV1381_67_09PCLinkHeader.from_dict(obj.get("link_header"))
        link_name = from_union([from_none, from_int, from_str], obj.get("link_name"))
        name = from_union([from_int, from_str], obj.get("name"))
        return RotShapeV1381_67_09_PC(body, class_name, link_header, link_name, name)

    def to_dict(self):
        result = {}
        result["body"] = to_class(RotShapeV1381_67_09PCBody, self.body)
        result["class_name"] = from_union([from_int, from_str], self.class_name)
        result["link_header"] = to_class(
            CameraV1381_67_09PCLinkHeader, self.link_header
        )
        if self.link_name is not None:
            result["link_name"] = from_union(
                [from_none, from_int, from_str], self.link_name
            )
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class RotShape:
    def __init__(
        self,
        rot_shape_v1_06_63_02_pc,
        rot_shape_v1_291_03_06_pc,
        rot_shape_v1_381_67_09_pc,
    ):
        self.rot_shape_v1_06_63_02_pc = rot_shape_v1_06_63_02_pc
        self.rot_shape_v1_291_03_06_pc = rot_shape_v1_291_03_06_pc
        self.rot_shape_v1_381_67_09_pc = rot_shape_v1_381_67_09_pc

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        rot_shape_v1_06_63_02_pc = from_union(
            [RotShapeV106_63_02_PC.from_dict, from_none],
            obj.get("RotShapeV1_06_63_02PC"),
        )
        rot_shape_v1_291_03_06_pc = from_union(
            [RotShapeV1291_03_06_PC.from_dict, from_none],
            obj.get("RotShapeV1_291_03_06PC"),
        )
        rot_shape_v1_381_67_09_pc = from_union(
            [RotShapeV1381_67_09_PC.from_dict, from_none],
            obj.get("RotShapeV1_381_67_09PC"),
        )
        return RotShape(
            rot_shape_v1_06_63_02_pc,
            rot_shape_v1_291_03_06_pc,
            rot_shape_v1_381_67_09_pc,
        )

    def to_dict(self):
        result = {}
        if self.rot_shape_v1_06_63_02_pc is not None:
            result["RotShapeV1_06_63_02PC"] = from_union(
                [lambda x: to_class(RotShapeV106_63_02_PC, x), from_none],
                self.rot_shape_v1_06_63_02_pc,
            )
        if self.rot_shape_v1_291_03_06_pc is not None:
            result["RotShapeV1_291_03_06PC"] = from_union(
                [lambda x: to_class(RotShapeV1291_03_06_PC, x), from_none],
                self.rot_shape_v1_291_03_06_pc,
            )
        if self.rot_shape_v1_381_67_09_pc is not None:
            result["RotShapeV1_381_67_09PC"] = from_union(
                [lambda x: to_class(RotShapeV1381_67_09_PC, x), from_none],
                self.rot_shape_v1_381_67_09_pc,
            )
        return result


class RotShapeDataV1381_67_09PCBody:
    def __init__(self, flags, pad, zeros):
        self.flags = flags
        self.pad = pad
        self.zeros = zeros

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        flags = ResourceDatasFlags.from_dict(obj.get("flags"))
        pad = from_list(from_int, obj.get("pad"))
        zeros = from_list(from_int, obj.get("zeros"))
        return RotShapeDataV1381_67_09PCBody(flags, pad, zeros)

    def to_dict(self):
        result = {}
        result["flags"] = to_class(ResourceDatasFlags, self.flags)
        result["pad"] = from_list(from_int, self.pad)
        result["zeros"] = from_list(from_int, self.zeros)
        return result


class RotShapeDataV1381_67_09_PC:
    def __init__(self, body, class_name, link_header, link_name, name):
        self.body = body
        self.class_name = class_name
        self.link_header = link_header
        self.link_name = link_name
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        body = RotShapeDataV1381_67_09PCBody.from_dict(obj.get("body"))
        class_name = from_union([from_int, from_str], obj.get("class_name"))
        link_header = AnimationV1381_67_09PCLinkHeader.from_dict(obj.get("link_header"))
        link_name = from_union([from_none, from_int, from_str], obj.get("link_name"))
        name = from_union([from_int, from_str], obj.get("name"))
        return RotShapeDataV1381_67_09_PC(
            body, class_name, link_header, link_name, name
        )

    def to_dict(self):
        result = {}
        result["body"] = to_class(RotShapeDataV1381_67_09PCBody, self.body)
        result["class_name"] = from_union([from_int, from_str], self.class_name)
        result["link_header"] = to_class(
            AnimationV1381_67_09PCLinkHeader, self.link_header
        )
        if self.link_name is not None:
            result["link_name"] = from_union(
                [from_none, from_int, from_str], self.link_name
            )
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class RotShapeData:
    def __init__(self, rot_shape_data_v1_381_67_09_pc):
        self.rot_shape_data_v1_381_67_09_pc = rot_shape_data_v1_381_67_09_pc

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        rot_shape_data_v1_381_67_09_pc = RotShapeDataV1381_67_09_PC.from_dict(
            obj.get("RotShapeDataV1_381_67_09PC")
        )
        return RotShapeData(rot_shape_data_v1_381_67_09_pc)

    def to_dict(self):
        result = {}
        result["RotShapeDataV1_381_67_09PC"] = to_class(
            RotShapeDataV1381_67_09_PC, self.rot_shape_data_v1_381_67_09_pc
        )
        return result


class AnimationOmniElement:
    def __init__(
        self, animation_omni_flag, unknown0, unknown1, unknown2, unknown_node_name_name
    ):
        self.animation_omni_flag = animation_omni_flag
        self.unknown0 = unknown0
        self.unknown1 = unknown1
        self.unknown2 = unknown2
        self.unknown_node_name_name = unknown_node_name_name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        animation_omni_flag = from_int(obj.get("animation_omni_flag"))
        unknown0 = KeyframerVec3Comp0.from_dict(obj.get("unknown0"))
        unknown1 = KeyframerFloatComp0.from_dict(obj.get("unknown1"))
        unknown2 = KeyframerFloatComp0.from_dict(obj.get("unknown2"))
        unknown_node_name_name = from_union(
            [from_int, from_str], obj.get("unknown_node_name_name")
        )
        return AnimationOmniElement(
            animation_omni_flag, unknown0, unknown1, unknown2, unknown_node_name_name
        )

    def to_dict(self):
        result = {}
        result["animation_omni_flag"] = from_int(self.animation_omni_flag)
        result["unknown0"] = to_class(KeyframerVec3Comp0, self.unknown0)
        result["unknown1"] = to_class(KeyframerFloatComp0, self.unknown1)
        result["unknown2"] = to_class(KeyframerFloatComp0, self.unknown2)
        result["unknown_node_name_name"] = from_union(
            [from_int, from_str], self.unknown_node_name_name
        )
        return result


class Unknown1Element:
    def __init__(
        self,
        rtc_animation_node_flag,
        unknown0,
        unknown1,
        unknown2,
        unknown3,
        unknown_node_name,
    ):
        self.rtc_animation_node_flag = rtc_animation_node_flag
        self.unknown0 = unknown0
        self.unknown1 = unknown1
        self.unknown2 = unknown2
        self.unknown3 = unknown3
        self.unknown_node_name = unknown_node_name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        rtc_animation_node_flag = from_int(obj.get("rtc_animation_node_flag"))
        unknown0 = KeyframerRot.from_dict(obj.get("unknown0"))
        unknown1 = KeyframerVec3Comp0.from_dict(obj.get("unknown1"))
        unknown2 = KeyframerVec3Comp0.from_dict(obj.get("unknown2"))
        unknown3 = KeyframerMessage.from_dict(obj.get("unknown3"))
        unknown_node_name = from_union(
            [from_int, from_str], obj.get("unknown_node_name")
        )
        return Unknown1Element(
            rtc_animation_node_flag,
            unknown0,
            unknown1,
            unknown2,
            unknown3,
            unknown_node_name,
        )

    def to_dict(self):
        result = {}
        result["rtc_animation_node_flag"] = from_int(self.rtc_animation_node_flag)
        result["unknown0"] = to_class(KeyframerRot, self.unknown0)
        result["unknown1"] = to_class(KeyframerVec3Comp0, self.unknown1)
        result["unknown2"] = to_class(KeyframerVec3Comp0, self.unknown2)
        result["unknown3"] = to_class(KeyframerMessage, self.unknown3)
        result["unknown_node_name"] = from_union(
            [from_int, from_str], self.unknown_node_name
        )
        return result


class Schema25:
    def __init__(self, tangent_in, tangent_out, time, value):
        self.tangent_in = tangent_in
        self.tangent_out = tangent_out
        self.time = time
        self.value = value

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        tangent_in = from_float(obj.get("tangent_in"))
        tangent_out = from_float(obj.get("tangent_out"))
        time = from_float(obj.get("time"))
        value = from_float(obj.get("value"))
        return Schema25(tangent_in, tangent_out, time, value)

    def to_dict(self):
        result = {}
        result["tangent_in"] = to_float(self.tangent_in)
        result["tangent_out"] = to_float(self.tangent_out)
        result["time"] = to_float(self.time)
        result["value"] = to_float(self.value)
        return result


class Unknown2:
    def __init__(self, interpolation_type, keyframes):
        self.interpolation_type = interpolation_type
        self.keyframes = keyframes

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        interpolation_type = InterpolationType(obj.get("interpolation_type"))
        keyframes = from_list(Schema25.from_dict, obj.get("keyframes"))
        return Unknown2(interpolation_type, keyframes)

    def to_dict(self):
        result = {}
        result["interpolation_type"] = to_enum(
            InterpolationType, self.interpolation_type
        )
        result["keyframes"] = from_list(lambda x: to_class(Schema25, x), self.keyframes)
        return result


class Schema24:
    def __init__(
        self,
        animation_camera_flag,
        unknown0,
        unknown1,
        unknown2,
        unknown3,
        unknown_node_name,
    ):
        self.animation_camera_flag = animation_camera_flag
        self.unknown0 = unknown0
        self.unknown1 = unknown1
        self.unknown2 = unknown2
        self.unknown3 = unknown3
        self.unknown_node_name = unknown_node_name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        animation_camera_flag = from_int(obj.get("animation_camera_flag"))
        unknown0 = KeyframerFloatComp0.from_dict(obj.get("unknown0"))
        unknown1 = KeyframerFloatComp0.from_dict(obj.get("unknown1"))
        unknown2 = Unknown2.from_dict(obj.get("unknown2"))
        unknown3 = KeyframerFloatComp0.from_dict(obj.get("unknown3"))
        unknown_node_name = from_union(
            [from_int, from_str], obj.get("unknown_node_name")
        )
        return Schema24(
            animation_camera_flag,
            unknown0,
            unknown1,
            unknown2,
            unknown3,
            unknown_node_name,
        )

    def to_dict(self):
        result = {}
        result["animation_camera_flag"] = from_int(self.animation_camera_flag)
        result["unknown0"] = to_class(KeyframerFloatComp0, self.unknown0)
        result["unknown1"] = to_class(KeyframerFloatComp0, self.unknown1)
        result["unknown2"] = to_class(Unknown2, self.unknown2)
        result["unknown3"] = to_class(KeyframerFloatComp0, self.unknown3)
        result["unknown_node_name"] = from_union(
            [from_int, from_str], self.unknown_node_name
        )
        return result


class Schema26:
    def __init__(
        self,
        unknown3,
        unknown4,
        unknown_name0,
        unknown_name1,
        unknown_name_name0,
        unknown_name_name1,
        unknown_name_name2,
    ):
        self.unknown3 = unknown3
        self.unknown4 = unknown4
        self.unknown_name0 = unknown_name0
        self.unknown_name1 = unknown_name1
        self.unknown_name_name0 = unknown_name_name0
        self.unknown_name_name1 = unknown_name_name1
        self.unknown_name_name2 = unknown_name_name2

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        unknown3 = from_int(obj.get("unknown3"))
        unknown4 = from_int(obj.get("unknown4"))
        unknown_name0 = from_union([from_int, from_str], obj.get("unknown_name0"))
        unknown_name1 = from_union([from_int, from_str], obj.get("unknown_name1"))
        unknown_name_name0 = from_union(
            [from_int, from_str], obj.get("unknown_name_name0")
        )
        unknown_name_name1 = from_union(
            [from_int, from_str], obj.get("unknown_name_name1")
        )
        unknown_name_name2 = from_union(
            [from_int, from_str], obj.get("unknown_name_name2")
        )
        return Schema26(
            unknown3,
            unknown4,
            unknown_name0,
            unknown_name1,
            unknown_name_name0,
            unknown_name_name1,
            unknown_name_name2,
        )

    def to_dict(self):
        result = {}
        result["unknown3"] = from_int(self.unknown3)
        result["unknown4"] = from_int(self.unknown4)
        result["unknown_name0"] = from_union([from_int, from_str], self.unknown_name0)
        result["unknown_name1"] = from_union([from_int, from_str], self.unknown_name1)
        result["unknown_name_name0"] = from_union(
            [from_int, from_str], self.unknown_name_name0
        )
        result["unknown_name_name1"] = from_union(
            [from_int, from_str], self.unknown_name_name1
        )
        result["unknown_name_name2"] = from_union(
            [from_int, from_str], self.unknown_name_name2
        )
        return result


class Unknown9Element:
    def __init__(
        self,
        unknown0,
        unknown_name0,
        unknown_name1,
        unknown_name_name0,
        unknown_name_name1,
        unknown_name_name2,
    ):
        self.unknown0 = unknown0
        self.unknown_name0 = unknown_name0
        self.unknown_name1 = unknown_name1
        self.unknown_name_name0 = unknown_name_name0
        self.unknown_name_name1 = unknown_name_name1
        self.unknown_name_name2 = unknown_name_name2

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        unknown0 = from_int(obj.get("unknown0"))
        unknown_name0 = from_union([from_int, from_str], obj.get("unknown_name0"))
        unknown_name1 = from_union([from_int, from_str], obj.get("unknown_name1"))
        unknown_name_name0 = from_union(
            [from_int, from_str], obj.get("unknown_name_name0")
        )
        unknown_name_name1 = from_union(
            [from_int, from_str], obj.get("unknown_name_name1")
        )
        unknown_name_name2 = from_union(
            [from_int, from_str], obj.get("unknown_name_name2")
        )
        return Unknown9Element(
            unknown0,
            unknown_name0,
            unknown_name1,
            unknown_name_name0,
            unknown_name_name1,
            unknown_name_name2,
        )

    def to_dict(self):
        result = {}
        result["unknown0"] = from_int(self.unknown0)
        result["unknown_name0"] = from_union([from_int, from_str], self.unknown_name0)
        result["unknown_name1"] = from_union([from_int, from_str], self.unknown_name1)
        result["unknown_name_name0"] = from_union(
            [from_int, from_str], self.unknown_name_name0
        )
        result["unknown_name_name1"] = from_union(
            [from_int, from_str], self.unknown_name_name1
        )
        result["unknown_name_name2"] = from_union(
            [from_int, from_str], self.unknown_name_name2
        )
        return result


class RTCV1381_67_09PCBody:
    def __init__(
        self,
        animation_omnis,
        duration,
        unknown1_s,
        unknown2_s,
        unknown30,
        unknown8_s,
        unknown9_s,
        unknown_names,
        unknown_names1,
        unknown_names2,
    ):
        self.animation_omnis = animation_omnis
        self.duration = duration
        self.unknown1_s = unknown1_s
        self.unknown2_s = unknown2_s
        self.unknown30 = unknown30
        self.unknown8_s = unknown8_s
        self.unknown9_s = unknown9_s
        self.unknown_names = unknown_names
        self.unknown_names1 = unknown_names1
        self.unknown_names2 = unknown_names2

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        animation_omnis = from_list(
            AnimationOmniElement.from_dict, obj.get("animation_omnis")
        )
        duration = from_float(obj.get("duration"))
        unknown1_s = from_list(Unknown1Element.from_dict, obj.get("unknown1s"))
        unknown2_s = from_list(Schema24.from_dict, obj.get("unknown2s"))
        unknown30 = KeyframerMessage.from_dict(obj.get("unknown30"))
        unknown8_s = from_list(Schema26.from_dict, obj.get("unknown8s"))
        unknown9_s = from_list(Unknown9Element.from_dict, obj.get("unknown9s"))
        unknown_names = from_list(
            lambda x: from_union([from_int, from_str], x), obj.get("unknown_names")
        )
        unknown_names1 = from_list(
            lambda x: from_union([from_int, from_str], x), obj.get("unknown_names1")
        )
        unknown_names2 = from_list(
            lambda x: from_union([from_int, from_str], x), obj.get("unknown_names2")
        )
        return RTCV1381_67_09PCBody(
            animation_omnis,
            duration,
            unknown1_s,
            unknown2_s,
            unknown30,
            unknown8_s,
            unknown9_s,
            unknown_names,
            unknown_names1,
            unknown_names2,
        )

    def to_dict(self):
        result = {}
        result["animation_omnis"] = from_list(
            lambda x: to_class(AnimationOmniElement, x), self.animation_omnis
        )
        result["duration"] = to_float(self.duration)
        result["unknown1s"] = from_list(
            lambda x: to_class(Unknown1Element, x), self.unknown1_s
        )
        result["unknown2s"] = from_list(
            lambda x: to_class(Schema24, x), self.unknown2_s
        )
        result["unknown30"] = to_class(KeyframerMessage, self.unknown30)
        result["unknown8s"] = from_list(
            lambda x: to_class(Schema26, x), self.unknown8_s
        )
        result["unknown9s"] = from_list(
            lambda x: to_class(Unknown9Element, x), self.unknown9_s
        )
        result["unknown_names"] = from_list(
            lambda x: from_union([from_int, from_str], x), self.unknown_names
        )
        result["unknown_names1"] = from_list(
            lambda x: from_union([from_int, from_str], x), self.unknown_names1
        )
        result["unknown_names2"] = from_list(
            lambda x: from_union([from_int, from_str], x), self.unknown_names2
        )
        return result


class RTCV1381_67_09_PC:
    def __init__(self, body, class_name, link_header, link_name, name):
        self.body = body
        self.class_name = class_name
        self.link_header = link_header
        self.link_name = link_name
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        body = RTCV1381_67_09PCBody.from_dict(obj.get("body"))
        class_name = from_union([from_int, from_str], obj.get("class_name"))
        link_header = AnimationV1381_67_09PCLinkHeader.from_dict(obj.get("link_header"))
        link_name = from_union([from_none, from_int, from_str], obj.get("link_name"))
        name = from_union([from_int, from_str], obj.get("name"))
        return RTCV1381_67_09_PC(body, class_name, link_header, link_name, name)

    def to_dict(self):
        result = {}
        result["body"] = to_class(RTCV1381_67_09PCBody, self.body)
        result["class_name"] = from_union([from_int, from_str], self.class_name)
        result["link_header"] = to_class(
            AnimationV1381_67_09PCLinkHeader, self.link_header
        )
        if self.link_name is not None:
            result["link_name"] = from_union(
                [from_none, from_int, from_str], self.link_name
            )
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class RTC:
    def __init__(self, rtc_v1_381_67_09_pc):
        self.rtc_v1_381_67_09_pc = rtc_v1_381_67_09_pc

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        rtc_v1_381_67_09_pc = RTCV1381_67_09_PC.from_dict(obj.get("RtcV1_381_67_09PC"))
        return RTC(rtc_v1_381_67_09_pc)

    def to_dict(self):
        result = {}
        result["RtcV1_381_67_09PC"] = to_class(
            RTCV1381_67_09_PC, self.rtc_v1_381_67_09_pc
        )
        return result


class Schema27:
    def __init__(self, bone_node_names):
        self.bone_node_names = bone_node_names

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        bone_node_names = from_list(
            lambda x: from_union([from_int, from_str], x), obj.get("bone_node_names")
        )
        return Schema27(bone_node_names)

    def to_dict(self):
        result = {}
        result["bone_node_names"] = from_list(
            lambda x: from_union([from_int, from_str], x), self.bone_node_names
        )
        return result


class Schema28:
    def __init__(
        self,
        bone_name,
        child_bone_id,
        flags,
        inverse_local_rotation,
        inverse_model_matrix_id,
        local_rotation,
        local_translation,
        model_matrix_id,
        model_rot_matrix_row1,
        model_rot_matrix_row2,
        model_rot_matrix_row3,
        next_sibling_bone_id,
        original_model_transform,
        parent_bone_id,
        placeholder_child_ptr,
        placeholder_inverse_model_matrix_ptr,
        placeholder_model_matrix_ptr,
        placeholder_next_sibling_ptr,
        placeholder_parent_ptr,
        placeholder_prev_sibling_ptr,
        prev_sibling_bone_id,
        scale,
        unknown_ptrs0,
        unknown_ptrs1,
        unknown_ptrs2,
        user_define_name,
    ):
        self.bone_name = bone_name
        self.child_bone_id = child_bone_id
        self.flags = flags
        self.inverse_local_rotation = inverse_local_rotation
        self.inverse_model_matrix_id = inverse_model_matrix_id
        self.local_rotation = local_rotation
        self.local_translation = local_translation
        self.model_matrix_id = model_matrix_id
        self.model_rot_matrix_row1 = model_rot_matrix_row1
        self.model_rot_matrix_row2 = model_rot_matrix_row2
        self.model_rot_matrix_row3 = model_rot_matrix_row3
        self.next_sibling_bone_id = next_sibling_bone_id
        self.original_model_transform = original_model_transform
        self.parent_bone_id = parent_bone_id
        self.placeholder_child_ptr = placeholder_child_ptr
        self.placeholder_inverse_model_matrix_ptr = placeholder_inverse_model_matrix_ptr
        self.placeholder_model_matrix_ptr = placeholder_model_matrix_ptr
        self.placeholder_next_sibling_ptr = placeholder_next_sibling_ptr
        self.placeholder_parent_ptr = placeholder_parent_ptr
        self.placeholder_prev_sibling_ptr = placeholder_prev_sibling_ptr
        self.prev_sibling_bone_id = prev_sibling_bone_id
        self.scale = scale
        self.unknown_ptrs0 = unknown_ptrs0
        self.unknown_ptrs1 = unknown_ptrs1
        self.unknown_ptrs2 = unknown_ptrs2
        self.user_define_name = user_define_name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        bone_name = from_union([from_int, from_str], obj.get("bone_name"))
        child_bone_id = from_int(obj.get("child_bone_id"))
        flags = from_int(obj.get("flags"))
        inverse_local_rotation = from_list(
            from_float, obj.get("inverse_local_rotation")
        )
        inverse_model_matrix_id = from_int(obj.get("inverse_model_matrix_id"))
        local_rotation = from_list(from_float, obj.get("local_rotation"))
        local_translation = from_list(from_float, obj.get("local_translation"))
        model_matrix_id = from_int(obj.get("model_matrix_id"))
        model_rot_matrix_row1 = from_list(from_float, obj.get("model_rot_matrix_row1"))
        model_rot_matrix_row2 = from_list(from_float, obj.get("model_rot_matrix_row2"))
        model_rot_matrix_row3 = from_list(from_float, obj.get("model_rot_matrix_row3"))
        next_sibling_bone_id = from_int(obj.get("next_sibling_bone_id"))
        original_model_transform = from_list(
            lambda x: from_list(from_float, x), obj.get("original_model_transform")
        )
        parent_bone_id = from_int(obj.get("parent_bone_id"))
        placeholder_child_ptr = from_int(obj.get("placeholder_child_ptr"))
        placeholder_inverse_model_matrix_ptr = from_int(
            obj.get("placeholder_inverse_model_matrix_ptr")
        )
        placeholder_model_matrix_ptr = from_int(obj.get("placeholder_model_matrix_ptr"))
        placeholder_next_sibling_ptr = from_int(obj.get("placeholder_next_sibling_ptr"))
        placeholder_parent_ptr = from_int(obj.get("placeholder_parent_ptr"))
        placeholder_prev_sibling_ptr = from_int(obj.get("placeholder_prev_sibling_ptr"))
        prev_sibling_bone_id = from_int(obj.get("prev_sibling_bone_id"))
        scale = from_list(from_float, obj.get("scale"))
        unknown_ptrs0 = from_list(from_int, obj.get("unknown_ptrs0"))
        unknown_ptrs1 = from_list(from_int, obj.get("unknown_ptrs1"))
        unknown_ptrs2 = from_list(from_int, obj.get("unknown_ptrs2"))
        user_define_name = from_union([from_int, from_str], obj.get("user_define_name"))
        return Schema28(
            bone_name,
            child_bone_id,
            flags,
            inverse_local_rotation,
            inverse_model_matrix_id,
            local_rotation,
            local_translation,
            model_matrix_id,
            model_rot_matrix_row1,
            model_rot_matrix_row2,
            model_rot_matrix_row3,
            next_sibling_bone_id,
            original_model_transform,
            parent_bone_id,
            placeholder_child_ptr,
            placeholder_inverse_model_matrix_ptr,
            placeholder_model_matrix_ptr,
            placeholder_next_sibling_ptr,
            placeholder_parent_ptr,
            placeholder_prev_sibling_ptr,
            prev_sibling_bone_id,
            scale,
            unknown_ptrs0,
            unknown_ptrs1,
            unknown_ptrs2,
            user_define_name,
        )

    def to_dict(self):
        result = {}
        result["bone_name"] = from_union([from_int, from_str], self.bone_name)
        result["child_bone_id"] = from_int(self.child_bone_id)
        result["flags"] = from_int(self.flags)
        result["inverse_local_rotation"] = from_list(
            to_float, self.inverse_local_rotation
        )
        result["inverse_model_matrix_id"] = from_int(self.inverse_model_matrix_id)
        result["local_rotation"] = from_list(to_float, self.local_rotation)
        result["local_translation"] = from_list(to_float, self.local_translation)
        result["model_matrix_id"] = from_int(self.model_matrix_id)
        result["model_rot_matrix_row1"] = from_list(
            to_float, self.model_rot_matrix_row1
        )
        result["model_rot_matrix_row2"] = from_list(
            to_float, self.model_rot_matrix_row2
        )
        result["model_rot_matrix_row3"] = from_list(
            to_float, self.model_rot_matrix_row3
        )
        result["next_sibling_bone_id"] = from_int(self.next_sibling_bone_id)
        result["original_model_transform"] = from_list(
            lambda x: from_list(to_float, x), self.original_model_transform
        )
        result["parent_bone_id"] = from_int(self.parent_bone_id)
        result["placeholder_child_ptr"] = from_int(self.placeholder_child_ptr)
        result["placeholder_inverse_model_matrix_ptr"] = from_int(
            self.placeholder_inverse_model_matrix_ptr
        )
        result["placeholder_model_matrix_ptr"] = from_int(
            self.placeholder_model_matrix_ptr
        )
        result["placeholder_next_sibling_ptr"] = from_int(
            self.placeholder_next_sibling_ptr
        )
        result["placeholder_parent_ptr"] = from_int(self.placeholder_parent_ptr)
        result["placeholder_prev_sibling_ptr"] = from_int(
            self.placeholder_prev_sibling_ptr
        )
        result["prev_sibling_bone_id"] = from_int(self.prev_sibling_bone_id)
        result["scale"] = from_list(to_float, self.scale)
        result["unknown_ptrs0"] = from_list(from_int, self.unknown_ptrs0)
        result["unknown_ptrs1"] = from_list(from_int, self.unknown_ptrs1)
        result["unknown_ptrs2"] = from_list(from_int, self.unknown_ptrs2)
        result["user_define_name"] = from_union(
            [from_int, from_str], self.user_define_name
        )
        return result


class Schema29:
    def __init__(self, bone_node_name, box_col):
        self.bone_node_name = bone_node_name
        self.box_col = box_col

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        bone_node_name = from_union([from_int, from_str], obj.get("bone_node_name"))
        box_col = CollisionBoxElement.from_dict(obj.get("box_col"))
        return Schema29(bone_node_name, box_col)

    def to_dict(self):
        result = {}
        result["bone_node_name"] = from_union([from_int, from_str], self.bone_node_name)
        result["box_col"] = to_class(CollisionBoxElement, self.box_col)
        return result


class IndecentObjectDatas:
    def __init__(self, b_sphere_local, flag):
        self.b_sphere_local = b_sphere_local
        self.flag = flag

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        b_sphere_local = Sphere.from_dict(obj.get("b_sphere_local"))
        flag = from_int(obj.get("flag"))
        return IndecentObjectDatas(b_sphere_local, flag)

    def to_dict(self):
        result = {}
        result["b_sphere_local"] = to_class(Sphere, self.b_sphere_local)
        result["flag"] = from_int(self.flag)
        return result


class Schema30:
    def __init__(self, bone_node_name, sphere_col):
        self.bone_node_name = bone_node_name
        self.sphere_col = sphere_col

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        bone_node_name = from_union([from_int, from_str], obj.get("bone_node_name"))
        sphere_col = SpheresColElement.from_dict(obj.get("sphere_col"))
        return Schema30(bone_node_name, sphere_col)

    def to_dict(self):
        result = {}
        result["bone_node_name"] = from_union([from_int, from_str], self.bone_node_name)
        result["sphere_col"] = to_class(SpheresColElement, self.sphere_col)
        return result


class SkelV106_63_02PCBody:
    def __init__(
        self,
        bone_node_groups,
        bone_nodes,
        box_col_bones,
        material_names,
        maybe_rotation,
        mesh_data_names,
        object_datas,
        sphere_col_bones1,
        sphere_col_bones2,
        unknown_names,
    ):
        self.bone_node_groups = bone_node_groups
        self.bone_nodes = bone_nodes
        self.box_col_bones = box_col_bones
        self.material_names = material_names
        self.maybe_rotation = maybe_rotation
        self.mesh_data_names = mesh_data_names
        self.object_datas = object_datas
        self.sphere_col_bones1 = sphere_col_bones1
        self.sphere_col_bones2 = sphere_col_bones2
        self.unknown_names = unknown_names

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        bone_node_groups = from_list(Schema27.from_dict, obj.get("bone_node_groups"))
        bone_nodes = from_list(Schema28.from_dict, obj.get("bone_nodes"))
        box_col_bones = from_list(Schema29.from_dict, obj.get("box_col_bones"))
        material_names = from_list(
            lambda x: from_union([from_int, from_str], x), obj.get("material_names")
        )
        maybe_rotation = from_list(from_float, obj.get("maybe_rotation"))
        mesh_data_names = from_list(
            lambda x: from_union([from_int, from_str], x), obj.get("mesh_data_names")
        )
        object_datas = IndecentObjectDatas.from_dict(obj.get("object_datas"))
        sphere_col_bones1 = from_list(Schema30.from_dict, obj.get("sphere_col_bones1"))
        sphere_col_bones2 = from_list(Schema30.from_dict, obj.get("sphere_col_bones2"))
        unknown_names = from_list(
            lambda x: from_union([from_int, from_str], x), obj.get("unknown_names")
        )
        return SkelV106_63_02PCBody(
            bone_node_groups,
            bone_nodes,
            box_col_bones,
            material_names,
            maybe_rotation,
            mesh_data_names,
            object_datas,
            sphere_col_bones1,
            sphere_col_bones2,
            unknown_names,
        )

    def to_dict(self):
        result = {}
        result["bone_node_groups"] = from_list(
            lambda x: to_class(Schema27, x), self.bone_node_groups
        )
        result["bone_nodes"] = from_list(
            lambda x: to_class(Schema28, x), self.bone_nodes
        )
        result["box_col_bones"] = from_list(
            lambda x: to_class(Schema29, x), self.box_col_bones
        )
        result["material_names"] = from_list(
            lambda x: from_union([from_int, from_str], x), self.material_names
        )
        result["maybe_rotation"] = from_list(to_float, self.maybe_rotation)
        result["mesh_data_names"] = from_list(
            lambda x: from_union([from_int, from_str], x), self.mesh_data_names
        )
        result["object_datas"] = to_class(IndecentObjectDatas, self.object_datas)
        result["sphere_col_bones1"] = from_list(
            lambda x: to_class(Schema30, x), self.sphere_col_bones1
        )
        result["sphere_col_bones2"] = from_list(
            lambda x: to_class(Schema30, x), self.sphere_col_bones2
        )
        result["unknown_names"] = from_list(
            lambda x: from_union([from_int, from_str], x), self.unknown_names
        )
        return result


class SkelV106_63_02_PC:
    def __init__(self, body, class_name, link_header, link_name, name):
        self.body = body
        self.class_name = class_name
        self.link_header = link_header
        self.link_name = link_name
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        body = SkelV106_63_02PCBody.from_dict(obj.get("body"))
        class_name = from_union([from_int, from_str], obj.get("class_name"))
        link_header = AnimationV1291_03_06PCLinkHeader.from_dict(obj.get("link_header"))
        link_name = from_union([from_none, from_int, from_str], obj.get("link_name"))
        name = from_union([from_int, from_str], obj.get("name"))
        return SkelV106_63_02_PC(body, class_name, link_header, link_name, name)

    def to_dict(self):
        result = {}
        result["body"] = to_class(SkelV106_63_02PCBody, self.body)
        result["class_name"] = from_union([from_int, from_str], self.class_name)
        result["link_header"] = to_class(
            AnimationV1291_03_06PCLinkHeader, self.link_header
        )
        if self.link_name is not None:
            result["link_name"] = from_union(
                [from_none, from_int, from_str], self.link_name
            )
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class Schema31:
    def __init__(self, bone_node_names):
        self.bone_node_names = bone_node_names

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        bone_node_names = from_list(
            lambda x: from_union([from_int, from_str], x), obj.get("bone_node_names")
        )
        return Schema31(bone_node_names)

    def to_dict(self):
        result = {}
        result["bone_node_names"] = from_list(
            lambda x: from_union([from_int, from_str], x), self.bone_node_names
        )
        return result


class Schema32:
    def __init__(
        self,
        bone_name,
        child_bone_id,
        flags,
        inverse_local_rotation,
        inverse_model_matrix_id,
        local_rotation,
        local_translation,
        model_matrix_id,
        model_rot_matrix_row1,
        model_rot_matrix_row2,
        model_rot_matrix_row3,
        next_sibling_bone_id,
        original_model_transform,
        parent_bone_id,
        placeholder_child_ptr,
        placeholder_inverse_model_matrix_ptr,
        placeholder_model_matrix_ptr,
        placeholder_next_sibling_ptr,
        placeholder_parent_ptr,
        placeholder_prev_sibling_ptr,
        prev_sibling_bone_id,
        scale,
        unknown_ptrs0,
        unknown_ptrs1,
        unknown_ptrs2,
        user_define_name,
    ):
        self.bone_name = bone_name
        self.child_bone_id = child_bone_id
        self.flags = flags
        self.inverse_local_rotation = inverse_local_rotation
        self.inverse_model_matrix_id = inverse_model_matrix_id
        self.local_rotation = local_rotation
        self.local_translation = local_translation
        self.model_matrix_id = model_matrix_id
        self.model_rot_matrix_row1 = model_rot_matrix_row1
        self.model_rot_matrix_row2 = model_rot_matrix_row2
        self.model_rot_matrix_row3 = model_rot_matrix_row3
        self.next_sibling_bone_id = next_sibling_bone_id
        self.original_model_transform = original_model_transform
        self.parent_bone_id = parent_bone_id
        self.placeholder_child_ptr = placeholder_child_ptr
        self.placeholder_inverse_model_matrix_ptr = placeholder_inverse_model_matrix_ptr
        self.placeholder_model_matrix_ptr = placeholder_model_matrix_ptr
        self.placeholder_next_sibling_ptr = placeholder_next_sibling_ptr
        self.placeholder_parent_ptr = placeholder_parent_ptr
        self.placeholder_prev_sibling_ptr = placeholder_prev_sibling_ptr
        self.prev_sibling_bone_id = prev_sibling_bone_id
        self.scale = scale
        self.unknown_ptrs0 = unknown_ptrs0
        self.unknown_ptrs1 = unknown_ptrs1
        self.unknown_ptrs2 = unknown_ptrs2
        self.user_define_name = user_define_name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        bone_name = from_union([from_int, from_str], obj.get("bone_name"))
        child_bone_id = from_int(obj.get("child_bone_id"))
        flags = from_int(obj.get("flags"))
        inverse_local_rotation = from_list(
            from_float, obj.get("inverse_local_rotation")
        )
        inverse_model_matrix_id = from_int(obj.get("inverse_model_matrix_id"))
        local_rotation = from_list(from_float, obj.get("local_rotation"))
        local_translation = from_list(from_float, obj.get("local_translation"))
        model_matrix_id = from_int(obj.get("model_matrix_id"))
        model_rot_matrix_row1 = from_list(from_float, obj.get("model_rot_matrix_row1"))
        model_rot_matrix_row2 = from_list(from_float, obj.get("model_rot_matrix_row2"))
        model_rot_matrix_row3 = from_list(from_float, obj.get("model_rot_matrix_row3"))
        next_sibling_bone_id = from_int(obj.get("next_sibling_bone_id"))
        original_model_transform = from_list(
            lambda x: from_list(from_float, x), obj.get("original_model_transform")
        )
        parent_bone_id = from_int(obj.get("parent_bone_id"))
        placeholder_child_ptr = from_int(obj.get("placeholder_child_ptr"))
        placeholder_inverse_model_matrix_ptr = from_int(
            obj.get("placeholder_inverse_model_matrix_ptr")
        )
        placeholder_model_matrix_ptr = from_int(obj.get("placeholder_model_matrix_ptr"))
        placeholder_next_sibling_ptr = from_int(obj.get("placeholder_next_sibling_ptr"))
        placeholder_parent_ptr = from_int(obj.get("placeholder_parent_ptr"))
        placeholder_prev_sibling_ptr = from_int(obj.get("placeholder_prev_sibling_ptr"))
        prev_sibling_bone_id = from_int(obj.get("prev_sibling_bone_id"))
        scale = from_list(from_float, obj.get("scale"))
        unknown_ptrs0 = from_list(from_int, obj.get("unknown_ptrs0"))
        unknown_ptrs1 = from_list(from_int, obj.get("unknown_ptrs1"))
        unknown_ptrs2 = from_list(from_int, obj.get("unknown_ptrs2"))
        user_define_name = from_union([from_int, from_str], obj.get("user_define_name"))
        return Schema32(
            bone_name,
            child_bone_id,
            flags,
            inverse_local_rotation,
            inverse_model_matrix_id,
            local_rotation,
            local_translation,
            model_matrix_id,
            model_rot_matrix_row1,
            model_rot_matrix_row2,
            model_rot_matrix_row3,
            next_sibling_bone_id,
            original_model_transform,
            parent_bone_id,
            placeholder_child_ptr,
            placeholder_inverse_model_matrix_ptr,
            placeholder_model_matrix_ptr,
            placeholder_next_sibling_ptr,
            placeholder_parent_ptr,
            placeholder_prev_sibling_ptr,
            prev_sibling_bone_id,
            scale,
            unknown_ptrs0,
            unknown_ptrs1,
            unknown_ptrs2,
            user_define_name,
        )

    def to_dict(self):
        result = {}
        result["bone_name"] = from_union([from_int, from_str], self.bone_name)
        result["child_bone_id"] = from_int(self.child_bone_id)
        result["flags"] = from_int(self.flags)
        result["inverse_local_rotation"] = from_list(
            to_float, self.inverse_local_rotation
        )
        result["inverse_model_matrix_id"] = from_int(self.inverse_model_matrix_id)
        result["local_rotation"] = from_list(to_float, self.local_rotation)
        result["local_translation"] = from_list(to_float, self.local_translation)
        result["model_matrix_id"] = from_int(self.model_matrix_id)
        result["model_rot_matrix_row1"] = from_list(
            to_float, self.model_rot_matrix_row1
        )
        result["model_rot_matrix_row2"] = from_list(
            to_float, self.model_rot_matrix_row2
        )
        result["model_rot_matrix_row3"] = from_list(
            to_float, self.model_rot_matrix_row3
        )
        result["next_sibling_bone_id"] = from_int(self.next_sibling_bone_id)
        result["original_model_transform"] = from_list(
            lambda x: from_list(to_float, x), self.original_model_transform
        )
        result["parent_bone_id"] = from_int(self.parent_bone_id)
        result["placeholder_child_ptr"] = from_int(self.placeholder_child_ptr)
        result["placeholder_inverse_model_matrix_ptr"] = from_int(
            self.placeholder_inverse_model_matrix_ptr
        )
        result["placeholder_model_matrix_ptr"] = from_int(
            self.placeholder_model_matrix_ptr
        )
        result["placeholder_next_sibling_ptr"] = from_int(
            self.placeholder_next_sibling_ptr
        )
        result["placeholder_parent_ptr"] = from_int(self.placeholder_parent_ptr)
        result["placeholder_prev_sibling_ptr"] = from_int(
            self.placeholder_prev_sibling_ptr
        )
        result["prev_sibling_bone_id"] = from_int(self.prev_sibling_bone_id)
        result["scale"] = from_list(to_float, self.scale)
        result["unknown_ptrs0"] = from_list(from_int, self.unknown_ptrs0)
        result["unknown_ptrs1"] = from_list(from_int, self.unknown_ptrs1)
        result["unknown_ptrs2"] = from_list(from_int, self.unknown_ptrs2)
        result["user_define_name"] = from_union(
            [from_int, from_str], self.user_define_name
        )
        return result


class Schema33:
    def __init__(self, bone_node_name, box_col):
        self.bone_node_name = bone_node_name
        self.box_col = box_col

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        bone_node_name = from_union([from_int, from_str], obj.get("bone_node_name"))
        box_col = CollisionBoxElement.from_dict(obj.get("box_col"))
        return Schema33(bone_node_name, box_col)

    def to_dict(self):
        result = {}
        result["bone_node_name"] = from_union([from_int, from_str], self.bone_node_name)
        result["box_col"] = to_class(CollisionBoxElement, self.box_col)
        return result


class HilariousObjectDatas:
    def __init__(self, b_sphere_local, flag):
        self.b_sphere_local = b_sphere_local
        self.flag = flag

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        b_sphere_local = Sphere.from_dict(obj.get("b_sphere_local"))
        flag = from_int(obj.get("flag"))
        return HilariousObjectDatas(b_sphere_local, flag)

    def to_dict(self):
        result = {}
        result["b_sphere_local"] = to_class(Sphere, self.b_sphere_local)
        result["flag"] = from_int(self.flag)
        return result


class Schema34:
    def __init__(self, bone_node_name, sphere_col):
        self.bone_node_name = bone_node_name
        self.sphere_col = sphere_col

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        bone_node_name = from_union([from_int, from_str], obj.get("bone_node_name"))
        sphere_col = SpheresColElement.from_dict(obj.get("sphere_col"))
        return Schema34(bone_node_name, sphere_col)

    def to_dict(self):
        result = {}
        result["bone_node_name"] = from_union([from_int, from_str], self.bone_node_name)
        result["sphere_col"] = to_class(SpheresColElement, self.sphere_col)
        return result


class SkelV1291_03_06PCBody:
    def __init__(
        self,
        bone_node_groups,
        bone_nodes,
        box_col_bones,
        material_names,
        mesh_data_names,
        object_datas,
        sphere_col_bones1,
        sphere_col_bones2,
        unknown_names,
    ):
        self.bone_node_groups = bone_node_groups
        self.bone_nodes = bone_nodes
        self.box_col_bones = box_col_bones
        self.material_names = material_names
        self.mesh_data_names = mesh_data_names
        self.object_datas = object_datas
        self.sphere_col_bones1 = sphere_col_bones1
        self.sphere_col_bones2 = sphere_col_bones2
        self.unknown_names = unknown_names

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        bone_node_groups = from_list(Schema31.from_dict, obj.get("bone_node_groups"))
        bone_nodes = from_list(Schema32.from_dict, obj.get("bone_nodes"))
        box_col_bones = from_list(Schema33.from_dict, obj.get("box_col_bones"))
        material_names = from_list(
            lambda x: from_union([from_int, from_str], x), obj.get("material_names")
        )
        mesh_data_names = from_list(
            lambda x: from_union([from_int, from_str], x), obj.get("mesh_data_names")
        )
        object_datas = HilariousObjectDatas.from_dict(obj.get("object_datas"))
        sphere_col_bones1 = from_list(Schema34.from_dict, obj.get("sphere_col_bones1"))
        sphere_col_bones2 = from_list(Schema34.from_dict, obj.get("sphere_col_bones2"))
        unknown_names = from_list(
            lambda x: from_union([from_int, from_str], x), obj.get("unknown_names")
        )
        return SkelV1291_03_06PCBody(
            bone_node_groups,
            bone_nodes,
            box_col_bones,
            material_names,
            mesh_data_names,
            object_datas,
            sphere_col_bones1,
            sphere_col_bones2,
            unknown_names,
        )

    def to_dict(self):
        result = {}
        result["bone_node_groups"] = from_list(
            lambda x: to_class(Schema31, x), self.bone_node_groups
        )
        result["bone_nodes"] = from_list(
            lambda x: to_class(Schema32, x), self.bone_nodes
        )
        result["box_col_bones"] = from_list(
            lambda x: to_class(Schema33, x), self.box_col_bones
        )
        result["material_names"] = from_list(
            lambda x: from_union([from_int, from_str], x), self.material_names
        )
        result["mesh_data_names"] = from_list(
            lambda x: from_union([from_int, from_str], x), self.mesh_data_names
        )
        result["object_datas"] = to_class(HilariousObjectDatas, self.object_datas)
        result["sphere_col_bones1"] = from_list(
            lambda x: to_class(Schema34, x), self.sphere_col_bones1
        )
        result["sphere_col_bones2"] = from_list(
            lambda x: to_class(Schema34, x), self.sphere_col_bones2
        )
        result["unknown_names"] = from_list(
            lambda x: from_union([from_int, from_str], x), self.unknown_names
        )
        return result


class SkelV1291_03_06_PC:
    def __init__(self, body, class_name, link_header, link_name, name):
        self.body = body
        self.class_name = class_name
        self.link_header = link_header
        self.link_name = link_name
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        body = SkelV1291_03_06PCBody.from_dict(obj.get("body"))
        class_name = from_union([from_int, from_str], obj.get("class_name"))
        link_header = AnimationV1291_03_06PCLinkHeader.from_dict(obj.get("link_header"))
        link_name = from_union([from_none, from_int, from_str], obj.get("link_name"))
        name = from_union([from_int, from_str], obj.get("name"))
        return SkelV1291_03_06_PC(body, class_name, link_header, link_name, name)

    def to_dict(self):
        result = {}
        result["body"] = to_class(SkelV1291_03_06PCBody, self.body)
        result["class_name"] = from_union([from_int, from_str], self.class_name)
        result["link_header"] = to_class(
            AnimationV1291_03_06PCLinkHeader, self.link_header
        )
        if self.link_name is not None:
            result["link_name"] = from_union(
                [from_none, from_int, from_str], self.link_name
            )
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class Schema35:
    def __init__(
        self,
        bone_flags,
        bone_name,
        child_bone_begin,
        child_bone_ptr_placeholder,
        child_bones_index0,
        child_bones_index1,
        parent_bone_ptr_placeholder,
        parent_index,
        placeholder_vec0,
        placeholder_vec1,
        placeholder_vec2,
        some_bone_index,
        some_bone_ptr_placeholder,
        some_mat_ptr1_placeholder,
        some_mat_ptr2_placeholder,
        some_placeholder0,
        some_placeholder1,
        transform_rotation_inverse0,
        transform_rotation_inverse1,
        transform_row0,
        transform_row1,
        transform_row2,
        transform_row3,
        transform_scale,
        transformation,
        user_define_name,
    ):
        self.bone_flags = bone_flags
        self.bone_name = bone_name
        self.child_bone_begin = child_bone_begin
        self.child_bone_ptr_placeholder = child_bone_ptr_placeholder
        self.child_bones_index0 = child_bones_index0
        self.child_bones_index1 = child_bones_index1
        self.parent_bone_ptr_placeholder = parent_bone_ptr_placeholder
        self.parent_index = parent_index
        self.placeholder_vec0 = placeholder_vec0
        self.placeholder_vec1 = placeholder_vec1
        self.placeholder_vec2 = placeholder_vec2
        self.some_bone_index = some_bone_index
        self.some_bone_ptr_placeholder = some_bone_ptr_placeholder
        self.some_mat_ptr1_placeholder = some_mat_ptr1_placeholder
        self.some_mat_ptr2_placeholder = some_mat_ptr2_placeholder
        self.some_placeholder0 = some_placeholder0
        self.some_placeholder1 = some_placeholder1
        self.transform_rotation_inverse0 = transform_rotation_inverse0
        self.transform_rotation_inverse1 = transform_rotation_inverse1
        self.transform_row0 = transform_row0
        self.transform_row1 = transform_row1
        self.transform_row2 = transform_row2
        self.transform_row3 = transform_row3
        self.transform_scale = transform_scale
        self.transformation = transformation
        self.user_define_name = user_define_name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        bone_flags = from_int(obj.get("bone_flags"))
        bone_name = from_union([from_int, from_str], obj.get("bone_name"))
        child_bone_begin = from_int(obj.get("child_bone_begin"))
        child_bone_ptr_placeholder = from_int(obj.get("child_bone_ptr_placeholder"))
        child_bones_index0 = from_int(obj.get("child_bones_index0"))
        child_bones_index1 = from_int(obj.get("child_bones_index1"))
        parent_bone_ptr_placeholder = from_int(obj.get("parent_bone_ptr_placeholder"))
        parent_index = from_int(obj.get("parent_index"))
        placeholder_vec0 = from_list(from_int, obj.get("placeholder_vec0"))
        placeholder_vec1 = from_list(from_int, obj.get("placeholder_vec1"))
        placeholder_vec2 = from_list(from_int, obj.get("placeholder_vec2"))
        some_bone_index = from_int(obj.get("some_bone_index"))
        some_bone_ptr_placeholder = from_int(obj.get("some_bone_ptr_placeholder"))
        some_mat_ptr1_placeholder = from_int(obj.get("some_mat_ptr1_placeholder"))
        some_mat_ptr2_placeholder = from_int(obj.get("some_mat_ptr2_placeholder"))
        some_placeholder0 = from_int(obj.get("some_placeholder0"))
        some_placeholder1 = from_int(obj.get("some_placeholder1"))
        transform_rotation_inverse0 = from_list(
            from_float, obj.get("transform_rotation_inverse0")
        )
        transform_rotation_inverse1 = from_list(
            from_float, obj.get("transform_rotation_inverse1")
        )
        transform_row0 = from_list(from_float, obj.get("transform_row0"))
        transform_row1 = from_list(from_float, obj.get("transform_row1"))
        transform_row2 = from_list(from_float, obj.get("transform_row2"))
        transform_row3 = from_list(from_float, obj.get("transform_row3"))
        transform_scale = from_list(from_float, obj.get("transform_scale"))
        transformation = from_list(
            lambda x: from_list(from_float, x), obj.get("transformation")
        )
        user_define_name = from_union([from_int, from_str], obj.get("user_define_name"))
        return Schema35(
            bone_flags,
            bone_name,
            child_bone_begin,
            child_bone_ptr_placeholder,
            child_bones_index0,
            child_bones_index1,
            parent_bone_ptr_placeholder,
            parent_index,
            placeholder_vec0,
            placeholder_vec1,
            placeholder_vec2,
            some_bone_index,
            some_bone_ptr_placeholder,
            some_mat_ptr1_placeholder,
            some_mat_ptr2_placeholder,
            some_placeholder0,
            some_placeholder1,
            transform_rotation_inverse0,
            transform_rotation_inverse1,
            transform_row0,
            transform_row1,
            transform_row2,
            transform_row3,
            transform_scale,
            transformation,
            user_define_name,
        )

    def to_dict(self):
        result = {}
        result["bone_flags"] = from_int(self.bone_flags)
        result["bone_name"] = from_union([from_int, from_str], self.bone_name)
        result["child_bone_begin"] = from_int(self.child_bone_begin)
        result["child_bone_ptr_placeholder"] = from_int(self.child_bone_ptr_placeholder)
        result["child_bones_index0"] = from_int(self.child_bones_index0)
        result["child_bones_index1"] = from_int(self.child_bones_index1)
        result["parent_bone_ptr_placeholder"] = from_int(
            self.parent_bone_ptr_placeholder
        )
        result["parent_index"] = from_int(self.parent_index)
        result["placeholder_vec0"] = from_list(from_int, self.placeholder_vec0)
        result["placeholder_vec1"] = from_list(from_int, self.placeholder_vec1)
        result["placeholder_vec2"] = from_list(from_int, self.placeholder_vec2)
        result["some_bone_index"] = from_int(self.some_bone_index)
        result["some_bone_ptr_placeholder"] = from_int(self.some_bone_ptr_placeholder)
        result["some_mat_ptr1_placeholder"] = from_int(self.some_mat_ptr1_placeholder)
        result["some_mat_ptr2_placeholder"] = from_int(self.some_mat_ptr2_placeholder)
        result["some_placeholder0"] = from_int(self.some_placeholder0)
        result["some_placeholder1"] = from_int(self.some_placeholder1)
        result["transform_rotation_inverse0"] = from_list(
            to_float, self.transform_rotation_inverse0
        )
        result["transform_rotation_inverse1"] = from_list(
            to_float, self.transform_rotation_inverse1
        )
        result["transform_row0"] = from_list(to_float, self.transform_row0)
        result["transform_row1"] = from_list(to_float, self.transform_row1)
        result["transform_row2"] = from_list(to_float, self.transform_row2)
        result["transform_row3"] = from_list(to_float, self.transform_row3)
        result["transform_scale"] = from_list(to_float, self.transform_scale)
        result["transformation"] = from_list(
            lambda x: from_list(to_float, x), self.transformation
        )
        result["user_define_name"] = from_union(
            [from_int, from_str], self.user_define_name
        )
        return result


class Schema36:
    def __init__(self, mat, names):
        self.mat = mat
        self.names = names

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        mat = from_list(lambda x: from_list(from_float, x), obj.get("mat"))
        names = from_list(
            lambda x: from_union([from_int, from_str], x), obj.get("names")
        )
        return Schema36(mat, names)

    def to_dict(self):
        result = {}
        result["mat"] = from_list(lambda x: from_list(to_float, x), self.mat)
        result["names"] = from_list(
            lambda x: from_union([from_int, from_str], x), self.names
        )
        return result


class SphereColBones0Element:
    def __init__(self, names, sphere):
        self.names = names
        self.sphere = sphere

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        names = from_list(
            lambda x: from_union([from_int, from_str], x), obj.get("names")
        )
        sphere = Sphere.from_dict(obj.get("sphere"))
        return SphereColBones0Element(names, sphere)

    def to_dict(self):
        result = {}
        result["names"] = from_list(
            lambda x: from_union([from_int, from_str], x), self.names
        )
        result["sphere"] = to_class(Sphere, self.sphere)
        return result


class SkelV1381_67_09PCBody:
    def __init__(
        self,
        animation_node_names_arrays,
        bones,
        bounding_sphere_center,
        box_col_bones,
        flags,
        material_names,
        mesh_data_names,
        some_names,
        sphere_col_bones0,
        sphere_col_bones1,
    ):
        self.animation_node_names_arrays = animation_node_names_arrays
        self.bones = bones
        self.bounding_sphere_center = bounding_sphere_center
        self.box_col_bones = box_col_bones
        self.flags = flags
        self.material_names = material_names
        self.mesh_data_names = mesh_data_names
        self.some_names = some_names
        self.sphere_col_bones0 = sphere_col_bones0
        self.sphere_col_bones1 = sphere_col_bones1

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        animation_node_names_arrays = from_list(
            lambda x: from_list(lambda x: from_union([from_int, from_str], x), x),
            obj.get("animation_node_names_arrays"),
        )
        bones = from_list(Schema35.from_dict, obj.get("bones"))
        bounding_sphere_center = Sphere.from_dict(obj.get("bounding_sphere_center"))
        box_col_bones = from_list(Schema36.from_dict, obj.get("box_col_bones"))
        flags = ResourceDatasFlags.from_dict(obj.get("flags"))
        material_names = from_list(
            lambda x: from_union([from_int, from_str], x), obj.get("material_names")
        )
        mesh_data_names = from_list(
            lambda x: from_union([from_int, from_str], x), obj.get("mesh_data_names")
        )
        some_names = from_list(
            lambda x: from_union([from_int, from_str], x), obj.get("some_names")
        )
        sphere_col_bones0 = from_list(
            SphereColBones0Element.from_dict, obj.get("sphere_col_bones0")
        )
        sphere_col_bones1 = from_list(
            SphereColBones0Element.from_dict, obj.get("sphere_col_bones1")
        )
        return SkelV1381_67_09PCBody(
            animation_node_names_arrays,
            bones,
            bounding_sphere_center,
            box_col_bones,
            flags,
            material_names,
            mesh_data_names,
            some_names,
            sphere_col_bones0,
            sphere_col_bones1,
        )

    def to_dict(self):
        result = {}
        result["animation_node_names_arrays"] = from_list(
            lambda x: from_list(lambda x: from_union([from_int, from_str], x), x),
            self.animation_node_names_arrays,
        )
        result["bones"] = from_list(lambda x: to_class(Schema35, x), self.bones)
        result["bounding_sphere_center"] = to_class(Sphere, self.bounding_sphere_center)
        result["box_col_bones"] = from_list(
            lambda x: to_class(Schema36, x), self.box_col_bones
        )
        result["flags"] = to_class(ResourceDatasFlags, self.flags)
        result["material_names"] = from_list(
            lambda x: from_union([from_int, from_str], x), self.material_names
        )
        result["mesh_data_names"] = from_list(
            lambda x: from_union([from_int, from_str], x), self.mesh_data_names
        )
        result["some_names"] = from_list(
            lambda x: from_union([from_int, from_str], x), self.some_names
        )
        result["sphere_col_bones0"] = from_list(
            lambda x: to_class(SphereColBones0Element, x), self.sphere_col_bones0
        )
        result["sphere_col_bones1"] = from_list(
            lambda x: to_class(SphereColBones0Element, x), self.sphere_col_bones1
        )
        return result


class SkelV1381_67_09_PC:
    def __init__(self, body, class_name, link_header, link_name, name):
        self.body = body
        self.class_name = class_name
        self.link_header = link_header
        self.link_name = link_name
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        body = SkelV1381_67_09PCBody.from_dict(obj.get("body"))
        class_name = from_union([from_int, from_str], obj.get("class_name"))
        link_header = AnimationV1381_67_09PCLinkHeader.from_dict(obj.get("link_header"))
        link_name = from_union([from_none, from_int, from_str], obj.get("link_name"))
        name = from_union([from_int, from_str], obj.get("name"))
        return SkelV1381_67_09_PC(body, class_name, link_header, link_name, name)

    def to_dict(self):
        result = {}
        result["body"] = to_class(SkelV1381_67_09PCBody, self.body)
        result["class_name"] = from_union([from_int, from_str], self.class_name)
        result["link_header"] = to_class(
            AnimationV1381_67_09PCLinkHeader, self.link_header
        )
        if self.link_name is not None:
            result["link_name"] = from_union(
                [from_none, from_int, from_str], self.link_name
            )
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class Skel:
    def __init__(self, skel_v1_06_63_02_pc, skel_v1_291_03_06_pc, skel_v1_381_67_09_pc):
        self.skel_v1_06_63_02_pc = skel_v1_06_63_02_pc
        self.skel_v1_291_03_06_pc = skel_v1_291_03_06_pc
        self.skel_v1_381_67_09_pc = skel_v1_381_67_09_pc

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        skel_v1_06_63_02_pc = from_union(
            [SkelV106_63_02_PC.from_dict, from_none], obj.get("SkelV1_06_63_02PC")
        )
        skel_v1_291_03_06_pc = from_union(
            [SkelV1291_03_06_PC.from_dict, from_none], obj.get("SkelV1_291_03_06PC")
        )
        skel_v1_381_67_09_pc = from_union(
            [SkelV1381_67_09_PC.from_dict, from_none], obj.get("SkelV1_381_67_09PC")
        )
        return Skel(skel_v1_06_63_02_pc, skel_v1_291_03_06_pc, skel_v1_381_67_09_pc)

    def to_dict(self):
        result = {}
        if self.skel_v1_06_63_02_pc is not None:
            result["SkelV1_06_63_02PC"] = from_union(
                [lambda x: to_class(SkelV106_63_02_PC, x), from_none],
                self.skel_v1_06_63_02_pc,
            )
        if self.skel_v1_291_03_06_pc is not None:
            result["SkelV1_291_03_06PC"] = from_union(
                [lambda x: to_class(SkelV1291_03_06_PC, x), from_none],
                self.skel_v1_291_03_06_pc,
            )
        if self.skel_v1_381_67_09_pc is not None:
            result["SkelV1_381_67_09PC"] = from_union(
                [lambda x: to_class(SkelV1381_67_09_PC, x), from_none],
                self.skel_v1_381_67_09_pc,
            )
        return result


class AnimClassIDS:
    def __init__(
        self,
    ):
        pass

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        return AnimClassIDS()

    def to_dict(self):
        result = {}
        return result


class BlendRelated1Element:
    def __init__(self, blend, index):
        self.blend = blend
        self.index = index

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        blend = from_float(obj.get("blend"))
        index = from_int(obj.get("index"))
        return BlendRelated1Element(blend, index)

    def to_dict(self):
        result = {}
        result["blend"] = to_float(self.blend)
        result["index"] = from_int(self.index)
        return result


class ResourceBlendElement:
    def __init__(self, blend_related1_s, blend_related2_s, unknown):
        self.blend_related1_s = blend_related1_s
        self.blend_related2_s = blend_related2_s
        self.unknown = unknown

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        blend_related1_s = from_list(
            BlendRelated1Element.from_dict, obj.get("blend_related1s")
        )
        blend_related2_s = from_list(
            BlendRelated1Element.from_dict, obj.get("blend_related2s")
        )
        unknown = from_int(obj.get("unknown"))
        return ResourceBlendElement(blend_related1_s, blend_related2_s, unknown)

    def to_dict(self):
        result = {}
        result["blend_related1s"] = from_list(
            lambda x: to_class(BlendRelated1Element, x), self.blend_related1_s
        )
        result["blend_related2s"] = from_list(
            lambda x: to_class(BlendRelated1Element, x), self.blend_related2_s
        )
        result["unknown"] = from_int(self.unknown)
        return result


class Schema37:
    def __init__(self, bone_name, resource_blends):
        self.bone_name = bone_name
        self.resource_blends = resource_blends

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        bone_name = from_union([from_int, from_str], obj.get("bone_name"))
        resource_blends = from_list(
            ResourceBlendElement.from_dict, obj.get("resource_blends")
        )
        return Schema37(bone_name, resource_blends)

    def to_dict(self):
        result = {}
        result["bone_name"] = from_union([from_int, from_str], self.bone_name)
        result["resource_blends"] = from_list(
            lambda x: to_class(ResourceBlendElement, x), self.resource_blends
        )
        return result


class MorphPacketElement:
    def __init__(self, unknown0_name, unknown1_name):
        self.unknown0_name = unknown0_name
        self.unknown1_name = unknown1_name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        unknown0_name = from_union([from_int, from_str], obj.get("unknown0_name"))
        unknown1_name = from_union([from_int, from_str], obj.get("unknown1_name"))
        return MorphPacketElement(unknown0_name, unknown1_name)

    def to_dict(self):
        result = {}
        result["unknown0_name"] = from_union([from_int, from_str], self.unknown0_name)
        result["unknown1_name"] = from_union([from_int, from_str], self.unknown1_name)
        return result


class PlaceholderMorphPacketDa:
    def __init__(self, ptr, size_capacity):
        self.ptr = ptr
        self.size_capacity = size_capacity

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        ptr = from_int(obj.get("ptr"))
        size_capacity = from_int(obj.get("size_capacity"))
        return PlaceholderMorphPacketDa(ptr, size_capacity)

    def to_dict(self):
        result = {}
        result["ptr"] = from_int(self.ptr)
        result["size_capacity"] = from_int(self.size_capacity)
        return result


class SkinSubSectionElement:
    def __init__(
        self, bone_node_names, material_name, morph_packets, placeholder_morph_packet_da
    ):
        self.bone_node_names = bone_node_names
        self.material_name = material_name
        self.morph_packets = morph_packets
        self.placeholder_morph_packet_da = placeholder_morph_packet_da

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        bone_node_names = from_list(
            lambda x: from_union([from_int, from_str], x), obj.get("bone_node_names")
        )
        material_name = from_union([from_int, from_str], obj.get("material_name"))
        morph_packets = from_list(
            MorphPacketElement.from_dict, obj.get("morph_packets")
        )
        placeholder_morph_packet_da = PlaceholderMorphPacketDa.from_dict(
            obj.get("placeholder_morph_packet_da")
        )
        return SkinSubSectionElement(
            bone_node_names, material_name, morph_packets, placeholder_morph_packet_da
        )

    def to_dict(self):
        result = {}
        result["bone_node_names"] = from_list(
            lambda x: from_union([from_int, from_str], x), self.bone_node_names
        )
        result["material_name"] = from_union([from_int, from_str], self.material_name)
        result["morph_packets"] = from_list(
            lambda x: to_class(MorphPacketElement, x), self.morph_packets
        )
        result["placeholder_morph_packet_da"] = to_class(
            PlaceholderMorphPacketDa, self.placeholder_morph_packet_da
        )
        return result


class Schema38:
    def __init__(self, skin_sub_sections):
        self.skin_sub_sections = skin_sub_sections

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        skin_sub_sections = from_list(
            SkinSubSectionElement.from_dict, obj.get("skin_sub_sections")
        )
        return Schema38(skin_sub_sections)

    def to_dict(self):
        result = {}
        result["skin_sub_sections"] = from_list(
            lambda x: to_class(SkinSubSectionElement, x), self.skin_sub_sections
        )
        return result


class SoundClassIDS:
    def __init__(
        self,
    ):
        pass

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        return SoundClassIDS()

    def to_dict(self):
        result = {}
        return result


class BodyUnknown0:
    def __init__(self, unknown1):
        self.unknown1 = unknown1

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        unknown1 = from_list(from_int, obj.get("unknown1"))
        return BodyUnknown0(unknown1)

    def to_dict(self):
        result = {}
        result["unknown1"] = from_list(from_int, self.unknown1)
        return result


class SkinV1291_03_06PCBody:
    def __init__(
        self,
        anim_class_ids,
        bones,
        is_class_id,
        matrix_cache_check,
        mesh_names,
        skin_sections,
        sound_class_ids,
        unknown0_s,
    ):
        self.anim_class_ids = anim_class_ids
        self.bones = bones
        self.is_class_id = is_class_id
        self.matrix_cache_check = matrix_cache_check
        self.mesh_names = mesh_names
        self.skin_sections = skin_sections
        self.sound_class_ids = sound_class_ids
        self.unknown0_s = unknown0_s

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        anim_class_ids = from_union(
            [from_none, AnimClassIDS.from_dict], obj.get("anim_class_ids")
        )
        bones = from_list(Schema37.from_dict, obj.get("bones"))
        is_class_id = from_int(obj.get("is_class_id"))
        matrix_cache_check = from_int(obj.get("matrix_cache_check"))
        mesh_names = from_list(
            lambda x: from_union([from_int, from_str], x), obj.get("mesh_names")
        )
        skin_sections = from_list(Schema38.from_dict, obj.get("skin_sections"))
        sound_class_ids = from_union(
            [from_none, SoundClassIDS.from_dict], obj.get("sound_class_ids")
        )
        unknown0_s = from_list(BodyUnknown0.from_dict, obj.get("unknown0s"))
        return SkinV1291_03_06PCBody(
            anim_class_ids,
            bones,
            is_class_id,
            matrix_cache_check,
            mesh_names,
            skin_sections,
            sound_class_ids,
            unknown0_s,
        )

    def to_dict(self):
        result = {}
        if self.anim_class_ids is not None:
            result["anim_class_ids"] = from_union(
                [from_none, lambda x: to_class(AnimClassIDS, x)], self.anim_class_ids
            )
        result["bones"] = from_list(lambda x: to_class(Schema37, x), self.bones)
        result["is_class_id"] = from_int(self.is_class_id)
        result["matrix_cache_check"] = from_int(self.matrix_cache_check)
        result["mesh_names"] = from_list(
            lambda x: from_union([from_int, from_str], x), self.mesh_names
        )
        result["skin_sections"] = from_list(
            lambda x: to_class(Schema38, x), self.skin_sections
        )
        if self.sound_class_ids is not None:
            result["sound_class_ids"] = from_union(
                [from_none, lambda x: to_class(SoundClassIDS, x)], self.sound_class_ids
            )
        result["unknown0s"] = from_list(
            lambda x: to_class(BodyUnknown0, x), self.unknown0_s
        )
        return result


class SkinV1291_03_06_PC:
    def __init__(self, body, class_name, link_header, link_name, name):
        self.body = body
        self.class_name = class_name
        self.link_header = link_header
        self.link_name = link_name
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        body = SkinV1291_03_06PCBody.from_dict(obj.get("body"))
        class_name = from_union([from_int, from_str], obj.get("class_name"))
        link_header = CameraZoneV106_63_02PCLinkHeader.from_dict(obj.get("link_header"))
        link_name = from_union([from_none, from_int, from_str], obj.get("link_name"))
        name = from_union([from_int, from_str], obj.get("name"))
        return SkinV1291_03_06_PC(body, class_name, link_header, link_name, name)

    def to_dict(self):
        result = {}
        result["body"] = to_class(SkinV1291_03_06PCBody, self.body)
        result["class_name"] = from_union([from_int, from_str], self.class_name)
        result["link_header"] = to_class(
            CameraZoneV106_63_02PCLinkHeader, self.link_header
        )
        if self.link_name is not None:
            result["link_name"] = from_union(
                [from_none, from_int, from_str], self.link_name
            )
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class SkinSubsectionElement:
    def __init__(self, animation_node_names, bone_names):
        self.animation_node_names = animation_node_names
        self.bone_names = bone_names

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        animation_node_names = from_list(
            lambda x: from_union([from_int, from_str], x),
            obj.get("animation_node_names"),
        )
        bone_names = from_list(
            lambda x: from_union([from_int, from_str], x), obj.get("bone_names")
        )
        return SkinSubsectionElement(animation_node_names, bone_names)

    def to_dict(self):
        result = {}
        result["animation_node_names"] = from_list(
            lambda x: from_union([from_int, from_str], x), self.animation_node_names
        )
        result["bone_names"] = from_list(
            lambda x: from_union([from_int, from_str], x), self.bone_names
        )
        return result


class Schema39:
    def __init__(self, skin_subsections):
        self.skin_subsections = skin_subsections

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        skin_subsections = from_list(
            SkinSubsectionElement.from_dict, obj.get("skin_subsections")
        )
        return Schema39(skin_subsections)

    def to_dict(self):
        result = {}
        result["skin_subsections"] = from_list(
            lambda x: to_class(SkinSubsectionElement, x), self.skin_subsections
        )
        return result


class SkinV1381_67_09PCBody:
    def __init__(
        self, bone_name_count, mesh_names, one_and_a_half, skin_sections, zeros
    ):
        self.bone_name_count = bone_name_count
        self.mesh_names = mesh_names
        self.one_and_a_half = one_and_a_half
        self.skin_sections = skin_sections
        self.zeros = zeros

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        bone_name_count = from_int(obj.get("bone_name_count"))
        mesh_names = from_list(
            lambda x: from_union([from_int, from_str], x), obj.get("mesh_names")
        )
        one_and_a_half = from_float(obj.get("one_and_a_half"))
        skin_sections = from_list(Schema39.from_dict, obj.get("skin_sections"))
        zeros = from_list(from_int, obj.get("zeros"))
        return SkinV1381_67_09PCBody(
            bone_name_count, mesh_names, one_and_a_half, skin_sections, zeros
        )

    def to_dict(self):
        result = {}
        result["bone_name_count"] = from_int(self.bone_name_count)
        result["mesh_names"] = from_list(
            lambda x: from_union([from_int, from_str], x), self.mesh_names
        )
        result["one_and_a_half"] = to_float(self.one_and_a_half)
        result["skin_sections"] = from_list(
            lambda x: to_class(Schema39, x), self.skin_sections
        )
        result["zeros"] = from_list(from_int, self.zeros)
        return result


class SkinV1381_67_09_PC:
    def __init__(self, body, class_name, link_header, link_name, name):
        self.body = body
        self.class_name = class_name
        self.link_header = link_header
        self.link_name = link_name
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        body = SkinV1381_67_09PCBody.from_dict(obj.get("body"))
        class_name = from_union([from_int, from_str], obj.get("class_name"))
        link_header = CameraV1381_67_09PCLinkHeader.from_dict(obj.get("link_header"))
        link_name = from_union([from_none, from_int, from_str], obj.get("link_name"))
        name = from_union([from_int, from_str], obj.get("name"))
        return SkinV1381_67_09_PC(body, class_name, link_header, link_name, name)

    def to_dict(self):
        result = {}
        result["body"] = to_class(SkinV1381_67_09PCBody, self.body)
        result["class_name"] = from_union([from_int, from_str], self.class_name)
        result["link_header"] = to_class(
            CameraV1381_67_09PCLinkHeader, self.link_header
        )
        if self.link_name is not None:
            result["link_name"] = from_union(
                [from_none, from_int, from_str], self.link_name
            )
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class Skin:
    def __init__(self, skin_v1_291_03_06_pc, skin_v1_381_67_09_pc):
        self.skin_v1_291_03_06_pc = skin_v1_291_03_06_pc
        self.skin_v1_381_67_09_pc = skin_v1_381_67_09_pc

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        skin_v1_291_03_06_pc = from_union(
            [SkinV1291_03_06_PC.from_dict, from_none], obj.get("SkinV1_291_03_06PC")
        )
        skin_v1_381_67_09_pc = from_union(
            [SkinV1381_67_09_PC.from_dict, from_none], obj.get("SkinV1_381_67_09PC")
        )
        return Skin(skin_v1_291_03_06_pc, skin_v1_381_67_09_pc)

    def to_dict(self):
        result = {}
        if self.skin_v1_291_03_06_pc is not None:
            result["SkinV1_291_03_06PC"] = from_union(
                [lambda x: to_class(SkinV1291_03_06_PC, x), from_none],
                self.skin_v1_291_03_06_pc,
            )
        if self.skin_v1_381_67_09_pc is not None:
            result["SkinV1_381_67_09PC"] = from_union(
                [lambda x: to_class(SkinV1381_67_09_PC, x), from_none],
                self.skin_v1_381_67_09_pc,
            )
        return result


class SoundV1291_03_06PCBody:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        data = from_list(from_int, obj.get("data"))
        return SoundV1291_03_06PCBody(data)

    def to_dict(self):
        result = {}
        result["data"] = from_list(from_int, self.data)
        return result


class PurpleFlags:
    def __init__(self, value):
        self.value = value

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        value = from_int(obj.get("value"))
        return PurpleFlags(value)

    def to_dict(self):
        result = {}
        result["value"] = from_int(self.value)
        return result


class SoundV1291_03_06PCLinkHeader:
    def __init__(self, data_size, flags, sample_rate):
        self.data_size = data_size
        self.flags = flags
        self.sample_rate = sample_rate

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        data_size = from_int(obj.get("data_size"))
        flags = PurpleFlags.from_dict(obj.get("flags"))
        sample_rate = from_int(obj.get("sample_rate"))
        return SoundV1291_03_06PCLinkHeader(data_size, flags, sample_rate)

    def to_dict(self):
        result = {}
        result["data_size"] = from_int(self.data_size)
        result["flags"] = to_class(PurpleFlags, self.flags)
        result["sample_rate"] = from_int(self.sample_rate)
        return result


class SoundV1291_03_06_PC:
    def __init__(self, body, class_name, link_header, link_name, name):
        self.body = body
        self.class_name = class_name
        self.link_header = link_header
        self.link_name = link_name
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        body = SoundV1291_03_06PCBody.from_dict(obj.get("body"))
        class_name = from_union([from_int, from_str], obj.get("class_name"))
        link_header = SoundV1291_03_06PCLinkHeader.from_dict(obj.get("link_header"))
        link_name = from_union([from_none, from_int, from_str], obj.get("link_name"))
        name = from_union([from_int, from_str], obj.get("name"))
        return SoundV1291_03_06_PC(body, class_name, link_header, link_name, name)

    def to_dict(self):
        result = {}
        result["body"] = to_class(SoundV1291_03_06PCBody, self.body)
        result["class_name"] = from_union([from_int, from_str], self.class_name)
        result["link_header"] = to_class(SoundV1291_03_06PCLinkHeader, self.link_header)
        if self.link_name is not None:
            result["link_name"] = from_union(
                [from_none, from_int, from_str], self.link_name
            )
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class SoundV1381_67_09PCBody:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        data = from_list(from_int, obj.get("data"))
        return SoundV1381_67_09PCBody(data)

    def to_dict(self):
        result = {}
        result["data"] = from_list(from_int, self.data)
        return result


class SoundV1381_67_09PCLinkHeader:
    def __init__(self, data_size, flags, link_name, sample_rate):
        self.data_size = data_size
        self.flags = flags
        self.link_name = link_name
        self.sample_rate = sample_rate

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        data_size = from_int(obj.get("data_size"))
        flags = PurpleFlags.from_dict(obj.get("flags"))
        link_name = from_union([from_int, from_str], obj.get("link_name"))
        sample_rate = from_int(obj.get("sample_rate"))
        return SoundV1381_67_09PCLinkHeader(data_size, flags, link_name, sample_rate)

    def to_dict(self):
        result = {}
        result["data_size"] = from_int(self.data_size)
        result["flags"] = to_class(PurpleFlags, self.flags)
        result["link_name"] = from_union([from_int, from_str], self.link_name)
        result["sample_rate"] = from_int(self.sample_rate)
        return result


class SoundV1381_67_09_PC:
    def __init__(self, body, class_name, link_header, link_name, name):
        self.body = body
        self.class_name = class_name
        self.link_header = link_header
        self.link_name = link_name
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        body = SoundV1381_67_09PCBody.from_dict(obj.get("body"))
        class_name = from_union([from_int, from_str], obj.get("class_name"))
        link_header = SoundV1381_67_09PCLinkHeader.from_dict(obj.get("link_header"))
        link_name = from_union([from_none, from_int, from_str], obj.get("link_name"))
        name = from_union([from_int, from_str], obj.get("name"))
        return SoundV1381_67_09_PC(body, class_name, link_header, link_name, name)

    def to_dict(self):
        result = {}
        result["body"] = to_class(SoundV1381_67_09PCBody, self.body)
        result["class_name"] = from_union([from_int, from_str], self.class_name)
        result["link_header"] = to_class(SoundV1381_67_09PCLinkHeader, self.link_header)
        if self.link_name is not None:
            result["link_name"] = from_union(
                [from_none, from_int, from_str], self.link_name
            )
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class Sound:
    def __init__(self, sound_v1_291_03_06_pc, sound_v1_381_67_09_pc):
        self.sound_v1_291_03_06_pc = sound_v1_291_03_06_pc
        self.sound_v1_381_67_09_pc = sound_v1_381_67_09_pc

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        sound_v1_291_03_06_pc = from_union(
            [SoundV1291_03_06_PC.from_dict, from_none], obj.get("SoundV1_291_03_06PC")
        )
        sound_v1_381_67_09_pc = from_union(
            [SoundV1381_67_09_PC.from_dict, from_none], obj.get("SoundV1_381_67_09PC")
        )
        return Sound(sound_v1_291_03_06_pc, sound_v1_381_67_09_pc)

    def to_dict(self):
        result = {}
        if self.sound_v1_291_03_06_pc is not None:
            result["SoundV1_291_03_06PC"] = from_union(
                [lambda x: to_class(SoundV1291_03_06_PC, x), from_none],
                self.sound_v1_291_03_06_pc,
            )
        if self.sound_v1_381_67_09_pc is not None:
            result["SoundV1_381_67_09PC"] = from_union(
                [lambda x: to_class(SoundV1381_67_09_PC, x), from_none],
                self.sound_v1_381_67_09_pc,
            )
        return result


class SegmentElement:
    def __init__(self, length, vertices):
        self.length = length
        self.vertices = vertices

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        length = from_float(obj.get("length"))
        vertices = from_list(lambda x: from_list(from_float, x), obj.get("vertices"))
        return SegmentElement(length, vertices)

    def to_dict(self):
        result = {}
        result["length"] = to_float(self.length)
        result["vertices"] = from_list(lambda x: from_list(to_float, x), self.vertices)
        return result


class BodySpline:
    def __init__(self, flag, length, point_id, segments, tangent_id):
        self.flag = flag
        self.length = length
        self.point_id = point_id
        self.segments = segments
        self.tangent_id = tangent_id

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        flag = from_int(obj.get("flag"))
        length = from_float(obj.get("length"))
        point_id = from_list(from_int, obj.get("point_id"))
        segments = from_list(SegmentElement.from_dict, obj.get("segments"))
        tangent_id = from_list(from_int, obj.get("tangent_id"))
        return BodySpline(flag, length, point_id, segments, tangent_id)

    def to_dict(self):
        result = {}
        result["flag"] = from_int(self.flag)
        result["length"] = to_float(self.length)
        result["point_id"] = from_list(from_int, self.point_id)
        result["segments"] = from_list(
            lambda x: to_class(SegmentElement, x), self.segments
        )
        result["tangent_id"] = from_list(from_int, self.tangent_id)
        return result


class SplineV106_63_02PCBody:
    def __init__(self, length, points, splines, vec):
        self.length = length
        self.points = points
        self.splines = splines
        self.vec = vec

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        length = from_float(obj.get("length"))
        points = from_list(lambda x: from_list(from_float, x), obj.get("points"))
        splines = from_list(BodySpline.from_dict, obj.get("splines"))
        vec = from_list(from_float, obj.get("vec"))
        return SplineV106_63_02PCBody(length, points, splines, vec)

    def to_dict(self):
        result = {}
        result["length"] = to_float(self.length)
        result["points"] = from_list(lambda x: from_list(to_float, x), self.points)
        result["splines"] = from_list(lambda x: to_class(BodySpline, x), self.splines)
        result["vec"] = from_list(to_float, self.vec)
        return result


class SplineV106_63_02_PC:
    def __init__(self, body, class_name, link_header, link_name, name):
        self.body = body
        self.class_name = class_name
        self.link_header = link_header
        self.link_name = link_name
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        body = SplineV106_63_02PCBody.from_dict(obj.get("body"))
        class_name = from_union([from_int, from_str], obj.get("class_name"))
        link_header = CameraZoneV106_63_02PCLinkHeader.from_dict(obj.get("link_header"))
        link_name = from_union([from_none, from_int, from_str], obj.get("link_name"))
        name = from_union([from_int, from_str], obj.get("name"))
        return SplineV106_63_02_PC(body, class_name, link_header, link_name, name)

    def to_dict(self):
        result = {}
        result["body"] = to_class(SplineV106_63_02PCBody, self.body)
        result["class_name"] = from_union([from_int, from_str], self.class_name)
        result["link_header"] = to_class(
            CameraZoneV106_63_02PCLinkHeader, self.link_header
        )
        if self.link_name is not None:
            result["link_name"] = from_union(
                [from_none, from_int, from_str], self.link_name
            )
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class Schema41:
    def __init__(self, length, p):
        self.length = length
        self.p = p

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        length = from_float(obj.get("length"))
        p = from_list(lambda x: from_list(from_float, x), obj.get("p"))
        return Schema41(length, p)

    def to_dict(self):
        result = {}
        result["length"] = to_float(self.length)
        result["p"] = from_list(lambda x: from_list(to_float, x), self.p)
        return result


class Schema40:
    def __init__(self, flags, length, p, spline_segment_subdivisions, t):
        self.flags = flags
        self.length = length
        self.p = p
        self.spline_segment_subdivisions = spline_segment_subdivisions
        self.t = t

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        flags = from_int(obj.get("flags"))
        length = from_float(obj.get("length"))
        p = from_list(from_int, obj.get("p"))
        spline_segment_subdivisions = from_list(
            Schema41.from_dict, obj.get("spline_segment_subdivisions")
        )
        t = from_list(from_int, obj.get("t"))
        return Schema40(flags, length, p, spline_segment_subdivisions, t)

    def to_dict(self):
        result = {}
        result["flags"] = from_int(self.flags)
        result["length"] = to_float(self.length)
        result["p"] = from_list(from_int, self.p)
        result["spline_segment_subdivisions"] = from_list(
            lambda x: to_class(Schema41, x), self.spline_segment_subdivisions
        )
        result["t"] = from_list(from_int, self.t)
        return result


class SplineV1381_67_09PCBody:
    def __init__(self, length, points, spline_segments, vec):
        self.length = length
        self.points = points
        self.spline_segments = spline_segments
        self.vec = vec

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        length = from_float(obj.get("length"))
        points = from_list(lambda x: from_list(from_float, x), obj.get("points"))
        spline_segments = from_list(Schema40.from_dict, obj.get("spline_segments"))
        vec = from_list(from_float, obj.get("vec"))
        return SplineV1381_67_09PCBody(length, points, spline_segments, vec)

    def to_dict(self):
        result = {}
        result["length"] = to_float(self.length)
        result["points"] = from_list(lambda x: from_list(to_float, x), self.points)
        result["spline_segments"] = from_list(
            lambda x: to_class(Schema40, x), self.spline_segments
        )
        result["vec"] = from_list(to_float, self.vec)
        return result


class SplineV1381_67_09_PC:
    def __init__(self, body, class_name, link_header, link_name, name):
        self.body = body
        self.class_name = class_name
        self.link_header = link_header
        self.link_name = link_name
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        body = SplineV1381_67_09PCBody.from_dict(obj.get("body"))
        class_name = from_union([from_int, from_str], obj.get("class_name"))
        link_header = CameraV1381_67_09PCLinkHeader.from_dict(obj.get("link_header"))
        link_name = from_union([from_none, from_int, from_str], obj.get("link_name"))
        name = from_union([from_int, from_str], obj.get("name"))
        return SplineV1381_67_09_PC(body, class_name, link_header, link_name, name)

    def to_dict(self):
        result = {}
        result["body"] = to_class(SplineV1381_67_09PCBody, self.body)
        result["class_name"] = from_union([from_int, from_str], self.class_name)
        result["link_header"] = to_class(
            CameraV1381_67_09PCLinkHeader, self.link_header
        )
        if self.link_name is not None:
            result["link_name"] = from_union(
                [from_none, from_int, from_str], self.link_name
            )
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class Spline:
    def __init__(self, spline_v1_06_63_02_pc, spline_v1_381_67_09_pc):
        self.spline_v1_06_63_02_pc = spline_v1_06_63_02_pc
        self.spline_v1_381_67_09_pc = spline_v1_381_67_09_pc

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        spline_v1_06_63_02_pc = from_union(
            [SplineV106_63_02_PC.from_dict, from_none], obj.get("SplineV1_06_63_02PC")
        )
        spline_v1_381_67_09_pc = from_union(
            [SplineV1381_67_09_PC.from_dict, from_none], obj.get("SplineV1_381_67_09PC")
        )
        return Spline(spline_v1_06_63_02_pc, spline_v1_381_67_09_pc)

    def to_dict(self):
        result = {}
        if self.spline_v1_06_63_02_pc is not None:
            result["SplineV1_06_63_02PC"] = from_union(
                [lambda x: to_class(SplineV106_63_02_PC, x), from_none],
                self.spline_v1_06_63_02_pc,
            )
        if self.spline_v1_381_67_09_pc is not None:
            result["SplineV1_381_67_09PC"] = from_union(
                [lambda x: to_class(SplineV1381_67_09_PC, x), from_none],
                self.spline_v1_381_67_09_pc,
            )
        return result


class Schema43:
    def __init__(self, length, p):
        self.length = length
        self.p = p

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        length = from_float(obj.get("length"))
        p = from_list(lambda x: from_list(from_float, x), obj.get("p"))
        return Schema43(length, p)

    def to_dict(self):
        result = {}
        result["length"] = to_float(self.length)
        result["p"] = from_list(lambda x: from_list(to_float, x), self.p)
        return result


class Schema42:
    def __init__(self, flags, length, p, spline_segment_subdivisions, t):
        self.flags = flags
        self.length = length
        self.p = p
        self.spline_segment_subdivisions = spline_segment_subdivisions
        self.t = t

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        flags = from_int(obj.get("flags"))
        length = from_float(obj.get("length"))
        p = from_list(from_int, obj.get("p"))
        spline_segment_subdivisions = from_list(
            Schema43.from_dict, obj.get("spline_segment_subdivisions")
        )
        t = from_list(from_int, obj.get("t"))
        return Schema42(flags, length, p, spline_segment_subdivisions, t)

    def to_dict(self):
        result = {}
        result["flags"] = from_int(self.flags)
        result["length"] = to_float(self.length)
        result["p"] = from_list(from_int, self.p)
        result["spline_segment_subdivisions"] = from_list(
            lambda x: to_class(Schema43, x), self.spline_segment_subdivisions
        )
        result["t"] = from_list(from_int, self.t)
        return result


class SplineGraphV1381_67_09PCBody:
    def __init__(
        self,
        length,
        point_datas,
        point_names,
        points,
        spline_segment_datas,
        spline_segments,
        vec,
    ):
        self.length = length
        self.point_datas = point_datas
        self.point_names = point_names
        self.points = points
        self.spline_segment_datas = spline_segment_datas
        self.spline_segments = spline_segments
        self.vec = vec

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        length = from_float(obj.get("length"))
        point_datas = from_list(
            lambda x: from_list(from_int, x), obj.get("point_datas")
        )
        point_names = from_list(from_int, obj.get("point_names"))
        points = from_list(lambda x: from_list(from_float, x), obj.get("points"))
        spline_segment_datas = from_list(
            lambda x: from_list(from_int, x), obj.get("spline_segment_datas")
        )
        spline_segments = from_list(Schema42.from_dict, obj.get("spline_segments"))
        vec = from_list(from_float, obj.get("vec"))
        return SplineGraphV1381_67_09PCBody(
            length,
            point_datas,
            point_names,
            points,
            spline_segment_datas,
            spline_segments,
            vec,
        )

    def to_dict(self):
        result = {}
        result["length"] = to_float(self.length)
        result["point_datas"] = from_list(
            lambda x: from_list(from_int, x), self.point_datas
        )
        result["point_names"] = from_list(from_int, self.point_names)
        result["points"] = from_list(lambda x: from_list(to_float, x), self.points)
        result["spline_segment_datas"] = from_list(
            lambda x: from_list(from_int, x), self.spline_segment_datas
        )
        result["spline_segments"] = from_list(
            lambda x: to_class(Schema42, x), self.spline_segments
        )
        result["vec"] = from_list(to_float, self.vec)
        return result


class SplineGraphV1381_67_09_PC:
    def __init__(self, body, class_name, link_header, link_name, name):
        self.body = body
        self.class_name = class_name
        self.link_header = link_header
        self.link_name = link_name
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        body = SplineGraphV1381_67_09PCBody.from_dict(obj.get("body"))
        class_name = from_union([from_int, from_str], obj.get("class_name"))
        link_header = CameraV1381_67_09PCLinkHeader.from_dict(obj.get("link_header"))
        link_name = from_union([from_none, from_int, from_str], obj.get("link_name"))
        name = from_union([from_int, from_str], obj.get("name"))
        return SplineGraphV1381_67_09_PC(body, class_name, link_header, link_name, name)

    def to_dict(self):
        result = {}
        result["body"] = to_class(SplineGraphV1381_67_09PCBody, self.body)
        result["class_name"] = from_union([from_int, from_str], self.class_name)
        result["link_header"] = to_class(
            CameraV1381_67_09PCLinkHeader, self.link_header
        )
        if self.link_name is not None:
            result["link_name"] = from_union(
                [from_none, from_int, from_str], self.link_name
            )
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class SplineGraph:
    def __init__(self, spline_graph_v1_381_67_09_pc):
        self.spline_graph_v1_381_67_09_pc = spline_graph_v1_381_67_09_pc

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        spline_graph_v1_381_67_09_pc = SplineGraphV1381_67_09_PC.from_dict(
            obj.get("SplineGraphV1_381_67_09PC")
        )
        return SplineGraph(spline_graph_v1_381_67_09_pc)

    def to_dict(self):
        result = {}
        result["SplineGraphV1_381_67_09PC"] = to_class(
            SplineGraphV1381_67_09_PC, self.spline_graph_v1_381_67_09_pc
        )
        return result


class Schema44:
    def __init__(self, edge_id, flag, sphere, unk_float, unk_uints):
        self.edge_id = edge_id
        self.flag = flag
        self.sphere = sphere
        self.unk_float = unk_float
        self.unk_uints = unk_uints

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        edge_id = from_int(obj.get("edge_id"))
        flag = from_int(obj.get("flag"))
        sphere = Sphere.from_dict(obj.get("sphere"))
        unk_float = from_float(obj.get("unk_float"))
        unk_uints = from_list(from_int, obj.get("unk_uints"))
        return Schema44(edge_id, flag, sphere, unk_float, unk_uints)

    def to_dict(self):
        result = {}
        result["edge_id"] = from_int(self.edge_id)
        result["flag"] = from_int(self.flag)
        result["sphere"] = to_class(Sphere, self.sphere)
        result["unk_float"] = to_float(self.unk_float)
        result["unk_uints"] = from_list(from_int, self.unk_uints)
        return result


class Schema45:
    def __init__(self, cache_index_maybe, edge_id, flag, sphere, unk_placeholder_ptr3):
        self.cache_index_maybe = cache_index_maybe
        self.edge_id = edge_id
        self.flag = flag
        self.sphere = sphere
        self.unk_placeholder_ptr3 = unk_placeholder_ptr3

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        cache_index_maybe = from_int(obj.get("cache_index_maybe"))
        edge_id = from_int(obj.get("edge_id"))
        flag = from_int(obj.get("flag"))
        sphere = Sphere.from_dict(obj.get("sphere"))
        unk_placeholder_ptr3 = from_int(obj.get("unk_placeholder_ptr3"))
        return Schema45(cache_index_maybe, edge_id, flag, sphere, unk_placeholder_ptr3)

    def to_dict(self):
        result = {}
        result["cache_index_maybe"] = from_int(self.cache_index_maybe)
        result["edge_id"] = from_int(self.edge_id)
        result["flag"] = from_int(self.flag)
        result["sphere"] = to_class(Sphere, self.sphere)
        result["unk_placeholder_ptr3"] = from_int(self.unk_placeholder_ptr3)
        return result


class Schema46:
    def __init__(self, p, t):
        self.p = p
        self.t = t

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        p = from_list(from_int, obj.get("p"))
        t = from_list(from_int, obj.get("t"))
        return Schema46(p, t)

    def to_dict(self):
        result = {}
        result["p"] = from_list(from_int, self.p)
        result["t"] = from_list(from_int, self.t)
        return result


class Schema47:
    def __init__(self, cdcdcdcd, edge_col_id, flag, next_patch_col_id, sphere):
        self.cdcdcdcd = cdcdcdcd
        self.edge_col_id = edge_col_id
        self.flag = flag
        self.next_patch_col_id = next_patch_col_id
        self.sphere = sphere

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        cdcdcdcd = from_list(from_int, obj.get("cdcdcdcd"))
        edge_col_id = from_int(obj.get("edge_col_id"))
        flag = from_int(obj.get("flag"))
        next_patch_col_id = from_int(obj.get("next_patch_col_id"))
        sphere = Sphere.from_dict(obj.get("sphere"))
        return Schema47(cdcdcdcd, edge_col_id, flag, next_patch_col_id, sphere)

    def to_dict(self):
        result = {}
        result["cdcdcdcd"] = from_list(from_int, self.cdcdcdcd)
        result["edge_col_id"] = from_int(self.edge_col_id)
        result["flag"] = from_int(self.flag)
        result["next_patch_col_id"] = from_int(self.next_patch_col_id)
        result["sphere"] = to_class(Sphere, self.sphere)
        return result


class PurpleCullCone:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        data = from_list(from_int, obj.get("data"))
        return PurpleCullCone(data)

    def to_dict(self):
        result = {}
        result["data"] = from_list(from_int, self.data)
        return result


class Schema48:
    def __init__(
        self,
        b_box,
        col_cache_index,
        color_indices,
        cull_cone,
        displacement_indices,
        edge_indices,
        flag,
        material_anim_index,
        material_anim_name,
        normal_indices,
        should_draw_related_start_index,
        sphere,
        unknown,
        unknown_indices,
    ):
        self.b_box = b_box
        self.col_cache_index = col_cache_index
        self.color_indices = color_indices
        self.cull_cone = cull_cone
        self.displacement_indices = displacement_indices
        self.edge_indices = edge_indices
        self.flag = flag
        self.material_anim_index = material_anim_index
        self.material_anim_name = material_anim_name
        self.normal_indices = normal_indices
        self.should_draw_related_start_index = should_draw_related_start_index
        self.sphere = sphere
        self.unknown = unknown
        self.unknown_indices = unknown_indices

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        b_box = Box.from_dict(obj.get("b_box"))
        col_cache_index = from_int(obj.get("col_cache_index"))
        color_indices = from_list(from_int, obj.get("color_indices"))
        cull_cone = PurpleCullCone.from_dict(obj.get("cull_cone"))
        displacement_indices = from_list(from_int, obj.get("displacement_indices"))
        edge_indices = from_list(from_int, obj.get("edge_indices"))
        flag = from_int(obj.get("flag"))
        material_anim_index = from_int(obj.get("material_anim_index"))
        material_anim_name = from_union(
            [from_int, from_str], obj.get("material_anim_name")
        )
        normal_indices = from_list(from_int, obj.get("normal_indices"))
        should_draw_related_start_index = from_int(
            obj.get("should_draw_related_start_index")
        )
        sphere = Sphere.from_dict(obj.get("sphere"))
        unknown = from_int(obj.get("unknown"))
        unknown_indices = from_list(from_int, obj.get("unknown_indices"))
        return Schema48(
            b_box,
            col_cache_index,
            color_indices,
            cull_cone,
            displacement_indices,
            edge_indices,
            flag,
            material_anim_index,
            material_anim_name,
            normal_indices,
            should_draw_related_start_index,
            sphere,
            unknown,
            unknown_indices,
        )

    def to_dict(self):
        result = {}
        result["b_box"] = to_class(Box, self.b_box)
        result["col_cache_index"] = from_int(self.col_cache_index)
        result["color_indices"] = from_list(from_int, self.color_indices)
        result["cull_cone"] = to_class(PurpleCullCone, self.cull_cone)
        result["displacement_indices"] = from_list(from_int, self.displacement_indices)
        result["edge_indices"] = from_list(from_int, self.edge_indices)
        result["flag"] = from_int(self.flag)
        result["material_anim_index"] = from_int(self.material_anim_index)
        result["material_anim_name"] = from_union(
            [from_int, from_str], self.material_anim_name
        )
        result["normal_indices"] = from_list(from_int, self.normal_indices)
        result["should_draw_related_start_index"] = from_int(
            self.should_draw_related_start_index
        )
        result["sphere"] = to_class(Sphere, self.sphere)
        result["unknown"] = from_int(self.unknown)
        result["unknown_indices"] = from_list(from_int, self.unknown_indices)
        return result


class Schema50:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        data = from_list(from_int, obj.get("data"))
        return Schema50(data)

    def to_dict(self):
        result = {}
        result["data"] = from_list(from_int, self.data)
        return result


class Schema49:
    def __init__(self, morph_target_desc_relateds, name):
        self.morph_target_desc_relateds = morph_target_desc_relateds
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        morph_target_desc_relateds = from_list(
            Schema50.from_dict, obj.get("morph_target_desc_relateds")
        )
        name = from_int(obj.get("name"))
        return Schema49(morph_target_desc_relateds, name)

    def to_dict(self):
        result = {}
        result["morph_target_desc_relateds"] = from_list(
            lambda x: to_class(Schema50, x), self.morph_target_desc_relateds
        )
        result["name"] = from_int(self.name)
        return result


class Schema51:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        data = from_list(from_int, obj.get("data"))
        return Schema51(data)

    def to_dict(self):
        result = {}
        result["data"] = from_list(from_int, self.data)
        return result


class StickyMorpher:
    def __init__(self, morph_target_descs, morpher_relateds):
        self.morph_target_descs = morph_target_descs
        self.morpher_relateds = morpher_relateds

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        morph_target_descs = from_list(
            Schema49.from_dict, obj.get("morph_target_descs")
        )
        morpher_relateds = from_list(Schema51.from_dict, obj.get("morpher_relateds"))
        return StickyMorpher(morph_target_descs, morpher_relateds)

    def to_dict(self):
        result = {}
        result["morph_target_descs"] = from_list(
            lambda x: to_class(Schema49, x), self.morph_target_descs
        )
        result["morpher_relateds"] = from_list(
            lambda x: to_class(Schema51, x), self.morpher_relateds
        )
        return result


class PointsRelateds0Element:
    def __init__(self, vec3):
        self.vec3 = vec3

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        vec3 = from_list(from_float, obj.get("vec3"))
        return PointsRelateds0Element(vec3)

    def to_dict(self):
        result = {}
        result["vec3"] = from_list(to_float, self.vec3)
        return result


class PointsPointsRelateds1:
    def __init__(self, vec4):
        self.vec4 = vec4

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        vec4 = from_list(from_float, obj.get("vec4"))
        return PointsPointsRelateds1(vec4)

    def to_dict(self):
        result = {}
        result["vec4"] = from_list(to_float, self.vec4)
        return result


class StickyPoints:
    def __init__(self, morpher, points_relateds0, points_relateds1):
        self.morpher = morpher
        self.points_relateds0 = points_relateds0
        self.points_relateds1 = points_relateds1

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        morpher = StickyMorpher.from_dict(obj.get("morpher"))
        points_relateds0 = from_list(
            PointsRelateds0Element.from_dict, obj.get("points_relateds0")
        )
        points_relateds1 = from_list(
            PointsPointsRelateds1.from_dict, obj.get("points_relateds1")
        )
        return StickyPoints(morpher, points_relateds0, points_relateds1)

    def to_dict(self):
        result = {}
        result["morpher"] = to_class(StickyMorpher, self.morpher)
        result["points_relateds0"] = from_list(
            lambda x: to_class(PointsRelateds0Element, x), self.points_relateds0
        )
        result["points_relateds1"] = from_list(
            lambda x: to_class(PointsPointsRelateds1, x), self.points_relateds1
        )
        return result


class Schema53:
    def __init__(self, element_count, element_entry):
        self.element_count = element_count
        self.element_entry = element_entry

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        element_count = from_int(obj.get("element_count"))
        element_entry = from_int(obj.get("element_entry"))
        return Schema53(element_count, element_entry)

    def to_dict(self):
        result = {}
        result["element_count"] = from_int(self.element_count)
        result["element_entry"] = from_int(self.element_entry)
        return result


class Schema52:
    def __init__(
        self,
        axes_1,
        axes_2,
        axes_3,
        center,
        f_size,
        hit_patch_count,
        i_size,
        patch_indices,
        sead_voxels,
        size,
        step,
        unk_ptr1,
        unk_ptr2,
        unk_ptr3,
        unk_ptr4,
        unk_ptr5,
        unk_used_in_voxel_trace,
        unk_vec4_1,
        unk_vec4_2,
        unk_vec4_3,
        unk_vec4_4,
        unk_vec4_7,
    ):
        self.axes_1 = axes_1
        self.axes_2 = axes_2
        self.axes_3 = axes_3
        self.center = center
        self.f_size = f_size
        self.hit_patch_count = hit_patch_count
        self.i_size = i_size
        self.patch_indices = patch_indices
        self.sead_voxels = sead_voxels
        self.size = size
        self.step = step
        self.unk_ptr1 = unk_ptr1
        self.unk_ptr2 = unk_ptr2
        self.unk_ptr3 = unk_ptr3
        self.unk_ptr4 = unk_ptr4
        self.unk_ptr5 = unk_ptr5
        self.unk_used_in_voxel_trace = unk_used_in_voxel_trace
        self.unk_vec4_1 = unk_vec4_1
        self.unk_vec4_2 = unk_vec4_2
        self.unk_vec4_3 = unk_vec4_3
        self.unk_vec4_4 = unk_vec4_4
        self.unk_vec4_7 = unk_vec4_7

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        axes_1 = from_list(from_float, obj.get("axes_1"))
        axes_2 = from_list(from_float, obj.get("axes_2"))
        axes_3 = from_list(from_float, obj.get("axes_3"))
        center = from_list(from_float, obj.get("center"))
        f_size = from_list(from_float, obj.get("f_size"))
        hit_patch_count = from_int(obj.get("hit_patch_count"))
        i_size = from_list(from_float, obj.get("i_size"))
        patch_indices = from_list(from_int, obj.get("patch_indices"))
        sead_voxels = from_list(Schema53.from_dict, obj.get("sead_voxels"))
        size = from_list(from_float, obj.get("size"))
        step = from_list(from_float, obj.get("step"))
        unk_ptr1 = from_int(obj.get("unk_ptr1"))
        unk_ptr2 = from_int(obj.get("unk_ptr2"))
        unk_ptr3 = from_int(obj.get("unk_ptr3"))
        unk_ptr4 = from_int(obj.get("unk_ptr4"))
        unk_ptr5 = from_int(obj.get("unk_ptr5"))
        unk_used_in_voxel_trace = from_int(obj.get("unk_used_in_voxel_trace"))
        unk_vec4_1 = from_list(from_float, obj.get("unk_vec4_1"))
        unk_vec4_2 = from_list(from_float, obj.get("unk_vec4_2"))
        unk_vec4_3 = from_list(from_float, obj.get("unk_vec4_3"))
        unk_vec4_4 = from_list(from_float, obj.get("unk_vec4_4"))
        unk_vec4_7 = from_list(from_float, obj.get("unk_vec4_7"))
        return Schema52(
            axes_1,
            axes_2,
            axes_3,
            center,
            f_size,
            hit_patch_count,
            i_size,
            patch_indices,
            sead_voxels,
            size,
            step,
            unk_ptr1,
            unk_ptr2,
            unk_ptr3,
            unk_ptr4,
            unk_ptr5,
            unk_used_in_voxel_trace,
            unk_vec4_1,
            unk_vec4_2,
            unk_vec4_3,
            unk_vec4_4,
            unk_vec4_7,
        )

    def to_dict(self):
        result = {}
        result["axes_1"] = from_list(to_float, self.axes_1)
        result["axes_2"] = from_list(to_float, self.axes_2)
        result["axes_3"] = from_list(to_float, self.axes_3)
        result["center"] = from_list(to_float, self.center)
        result["f_size"] = from_list(to_float, self.f_size)
        result["hit_patch_count"] = from_int(self.hit_patch_count)
        result["i_size"] = from_list(to_float, self.i_size)
        result["patch_indices"] = from_list(from_int, self.patch_indices)
        result["sead_voxels"] = from_list(
            lambda x: to_class(Schema53, x), self.sead_voxels
        )
        result["size"] = from_list(to_float, self.size)
        result["step"] = from_list(to_float, self.step)
        result["unk_ptr1"] = from_int(self.unk_ptr1)
        result["unk_ptr2"] = from_int(self.unk_ptr2)
        result["unk_ptr3"] = from_int(self.unk_ptr3)
        result["unk_ptr4"] = from_int(self.unk_ptr4)
        result["unk_ptr5"] = from_int(self.unk_ptr5)
        result["unk_used_in_voxel_trace"] = from_int(self.unk_used_in_voxel_trace)
        result["unk_vec4_1"] = from_list(to_float, self.unk_vec4_1)
        result["unk_vec4_2"] = from_list(to_float, self.unk_vec4_2)
        result["unk_vec4_3"] = from_list(to_float, self.unk_vec4_3)
        result["unk_vec4_4"] = from_list(to_float, self.unk_vec4_4)
        result["unk_vec4_7"] = from_list(to_float, self.unk_vec4_7)
        return result


class PurpleSeadIndex:
    def __init__(self, inner):
        self.inner = inner

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        inner = from_union([Schema52.from_dict, from_none], obj.get("inner"))
        return PurpleSeadIndex(inner)

    def to_dict(self):
        result = {}
        if self.inner is not None:
            result["inner"] = from_union(
                [lambda x: to_class(Schema52, x), from_none], self.inner
            )
        return result


class Schema54:
    def __init__(self, value):
        self.value = value

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        value = from_int(obj.get("value"))
        return Schema54(value)

    def to_dict(self):
        result = {}
        result["value"] = from_int(self.value)
        return result


class SurfaceV106_63_02PCBody:
    def __init__(
        self,
        cling_line_relateds,
        colors,
        displacement_relateds,
        edge_cols,
        edges,
        normals,
        patch_cols,
        patches,
        points,
        sead_index,
        should_draw_relateds,
    ):
        self.cling_line_relateds = cling_line_relateds
        self.colors = colors
        self.displacement_relateds = displacement_relateds
        self.edge_cols = edge_cols
        self.edges = edges
        self.normals = normals
        self.patch_cols = patch_cols
        self.patches = patches
        self.points = points
        self.sead_index = sead_index
        self.should_draw_relateds = should_draw_relateds

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        cling_line_relateds = from_list(
            Schema44.from_dict, obj.get("cling_line_relateds")
        )
        colors = from_list(lambda x: from_list(from_float, x), obj.get("colors"))
        displacement_relateds = from_list(
            lambda x: from_list(from_float, x), obj.get("displacement_relateds")
        )
        edge_cols = from_list(Schema45.from_dict, obj.get("edge_cols"))
        edges = from_list(Schema46.from_dict, obj.get("edges"))
        normals = from_list(lambda x: from_list(from_float, x), obj.get("normals"))
        patch_cols = from_list(Schema47.from_dict, obj.get("patch_cols"))
        patches = from_list(Schema48.from_dict, obj.get("patches"))
        points = StickyPoints.from_dict(obj.get("points"))
        sead_index = from_union(
            [PurpleSeadIndex.from_dict, from_none], obj.get("sead_index")
        )
        should_draw_relateds = from_list(
            Schema54.from_dict, obj.get("should_draw_relateds")
        )
        return SurfaceV106_63_02PCBody(
            cling_line_relateds,
            colors,
            displacement_relateds,
            edge_cols,
            edges,
            normals,
            patch_cols,
            patches,
            points,
            sead_index,
            should_draw_relateds,
        )

    def to_dict(self):
        result = {}
        result["cling_line_relateds"] = from_list(
            lambda x: to_class(Schema44, x), self.cling_line_relateds
        )
        result["colors"] = from_list(lambda x: from_list(to_float, x), self.colors)
        result["displacement_relateds"] = from_list(
            lambda x: from_list(to_float, x), self.displacement_relateds
        )
        result["edge_cols"] = from_list(lambda x: to_class(Schema45, x), self.edge_cols)
        result["edges"] = from_list(lambda x: to_class(Schema46, x), self.edges)
        result["normals"] = from_list(lambda x: from_list(to_float, x), self.normals)
        result["patch_cols"] = from_list(
            lambda x: to_class(Schema47, x), self.patch_cols
        )
        result["patches"] = from_list(lambda x: to_class(Schema48, x), self.patches)
        result["points"] = to_class(StickyPoints, self.points)
        if self.sead_index is not None:
            result["sead_index"] = from_union(
                [lambda x: to_class(PurpleSeadIndex, x), from_none], self.sead_index
            )
        result["should_draw_relateds"] = from_list(
            lambda x: to_class(Schema54, x), self.should_draw_relateds
        )
        return result


class SurfaceV106_63_02_PC:
    def __init__(self, body, class_name, link_header, link_name, name):
        self.body = body
        self.class_name = class_name
        self.link_header = link_header
        self.link_name = link_name
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        body = SurfaceV106_63_02PCBody.from_dict(obj.get("body"))
        class_name = from_union([from_int, from_str], obj.get("class_name"))
        link_header = AnimationV1291_03_06PCLinkHeader.from_dict(obj.get("link_header"))
        link_name = from_union([from_none, from_int, from_str], obj.get("link_name"))
        name = from_union([from_int, from_str], obj.get("name"))
        return SurfaceV106_63_02_PC(body, class_name, link_header, link_name, name)

    def to_dict(self):
        result = {}
        result["body"] = to_class(SurfaceV106_63_02PCBody, self.body)
        result["class_name"] = from_union([from_int, from_str], self.class_name)
        result["link_header"] = to_class(
            AnimationV1291_03_06PCLinkHeader, self.link_header
        )
        if self.link_name is not None:
            result["link_name"] = from_union(
                [from_none, from_int, from_str], self.link_name
            )
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class Schema55:
    def __init__(self, edge_id, flag, sphere, unknown0, unknown1, unknown2):
        self.edge_id = edge_id
        self.flag = flag
        self.sphere = sphere
        self.unknown0 = unknown0
        self.unknown1 = unknown1
        self.unknown2 = unknown2

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        edge_id = from_int(obj.get("edge_id"))
        flag = from_int(obj.get("flag"))
        sphere = Sphere.from_dict(obj.get("sphere"))
        unknown0 = from_int(obj.get("unknown0"))
        unknown1 = from_int(obj.get("unknown1"))
        unknown2 = from_float(obj.get("unknown2"))
        return Schema55(edge_id, flag, sphere, unknown0, unknown1, unknown2)

    def to_dict(self):
        result = {}
        result["edge_id"] = from_int(self.edge_id)
        result["flag"] = from_int(self.flag)
        result["sphere"] = to_class(Sphere, self.sphere)
        result["unknown0"] = from_int(self.unknown0)
        result["unknown1"] = from_int(self.unknown1)
        result["unknown2"] = to_float(self.unknown2)
        return result


class Schema56:
    def __init__(self, edge_id, flag, sphere, unknown0, unknown1):
        self.edge_id = edge_id
        self.flag = flag
        self.sphere = sphere
        self.unknown0 = unknown0
        self.unknown1 = unknown1

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        edge_id = from_int(obj.get("edge_id"))
        flag = from_int(obj.get("flag"))
        sphere = Sphere.from_dict(obj.get("sphere"))
        unknown0 = from_int(obj.get("unknown0"))
        unknown1 = from_int(obj.get("unknown1"))
        return Schema56(edge_id, flag, sphere, unknown0, unknown1)

    def to_dict(self):
        result = {}
        result["edge_id"] = from_int(self.edge_id)
        result["flag"] = from_int(self.flag)
        result["sphere"] = to_class(Sphere, self.sphere)
        result["unknown0"] = from_int(self.unknown0)
        result["unknown1"] = from_int(self.unknown1)
        return result


class Schema57:
    def __init__(self, p, t):
        self.p = p
        self.t = t

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        p = from_list(from_int, obj.get("p"))
        t = from_list(from_int, obj.get("t"))
        return Schema57(p, t)

    def to_dict(self):
        result = {}
        result["p"] = from_list(from_int, self.p)
        result["t"] = from_list(from_int, self.t)
        return result


class Schema58:
    def __init__(self, cdcdcdcd, edge_col_id, flag, next_patch_col_id, sphere):
        self.cdcdcdcd = cdcdcdcd
        self.edge_col_id = edge_col_id
        self.flag = flag
        self.next_patch_col_id = next_patch_col_id
        self.sphere = sphere

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        cdcdcdcd = from_list(from_int, obj.get("cdcdcdcd"))
        edge_col_id = from_int(obj.get("edge_col_id"))
        flag = from_int(obj.get("flag"))
        next_patch_col_id = from_int(obj.get("next_patch_col_id"))
        sphere = Sphere.from_dict(obj.get("sphere"))
        return Schema58(cdcdcdcd, edge_col_id, flag, next_patch_col_id, sphere)

    def to_dict(self):
        result = {}
        result["cdcdcdcd"] = from_list(from_int, self.cdcdcdcd)
        result["edge_col_id"] = from_int(self.edge_col_id)
        result["flag"] = from_int(self.flag)
        result["next_patch_col_id"] = from_int(self.next_patch_col_id)
        result["sphere"] = to_class(Sphere, self.sphere)
        return result


class PurpleBBox:
    def __init__(self, transformation):
        self.transformation = transformation

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        transformation = from_list(
            lambda x: from_list(from_float, x), obj.get("transformation")
        )
        return PurpleBBox(transformation)

    def to_dict(self):
        result = {}
        result["transformation"] = from_list(
            lambda x: from_list(to_float, x), self.transformation
        )
        return result


class FluffyCullCone:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        data = from_list(from_int, obj.get("data"))
        return FluffyCullCone(data)

    def to_dict(self):
        result = {}
        result["data"] = from_list(from_int, self.data)
        return result


class Schema59:
    def __init__(
        self,
        b_box,
        col_cache_index,
        color_indices,
        cull_cone,
        displacement_indices,
        edge_indices,
        flag,
        material_anim_index,
        material_anim_name,
        normal_indices,
        should_draw_related_start_index,
        sphere,
        unknown,
        unknown_indices,
    ):
        self.b_box = b_box
        self.col_cache_index = col_cache_index
        self.color_indices = color_indices
        self.cull_cone = cull_cone
        self.displacement_indices = displacement_indices
        self.edge_indices = edge_indices
        self.flag = flag
        self.material_anim_index = material_anim_index
        self.material_anim_name = material_anim_name
        self.normal_indices = normal_indices
        self.should_draw_related_start_index = should_draw_related_start_index
        self.sphere = sphere
        self.unknown = unknown
        self.unknown_indices = unknown_indices

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        b_box = PurpleBBox.from_dict(obj.get("b_box"))
        col_cache_index = from_int(obj.get("col_cache_index"))
        color_indices = from_list(from_int, obj.get("color_indices"))
        cull_cone = FluffyCullCone.from_dict(obj.get("cull_cone"))
        displacement_indices = from_list(from_int, obj.get("displacement_indices"))
        edge_indices = from_list(from_int, obj.get("edge_indices"))
        flag = from_int(obj.get("flag"))
        material_anim_index = from_int(obj.get("material_anim_index"))
        material_anim_name = from_union(
            [from_int, from_str], obj.get("material_anim_name")
        )
        normal_indices = from_list(from_int, obj.get("normal_indices"))
        should_draw_related_start_index = from_int(
            obj.get("should_draw_related_start_index")
        )
        sphere = Sphere.from_dict(obj.get("sphere"))
        unknown = from_int(obj.get("unknown"))
        unknown_indices = from_list(from_int, obj.get("unknown_indices"))
        return Schema59(
            b_box,
            col_cache_index,
            color_indices,
            cull_cone,
            displacement_indices,
            edge_indices,
            flag,
            material_anim_index,
            material_anim_name,
            normal_indices,
            should_draw_related_start_index,
            sphere,
            unknown,
            unknown_indices,
        )

    def to_dict(self):
        result = {}
        result["b_box"] = to_class(PurpleBBox, self.b_box)
        result["col_cache_index"] = from_int(self.col_cache_index)
        result["color_indices"] = from_list(from_int, self.color_indices)
        result["cull_cone"] = to_class(FluffyCullCone, self.cull_cone)
        result["displacement_indices"] = from_list(from_int, self.displacement_indices)
        result["edge_indices"] = from_list(from_int, self.edge_indices)
        result["flag"] = from_int(self.flag)
        result["material_anim_index"] = from_int(self.material_anim_index)
        result["material_anim_name"] = from_union(
            [from_int, from_str], self.material_anim_name
        )
        result["normal_indices"] = from_list(from_int, self.normal_indices)
        result["should_draw_related_start_index"] = from_int(
            self.should_draw_related_start_index
        )
        result["sphere"] = to_class(Sphere, self.sphere)
        result["unknown"] = from_int(self.unknown)
        result["unknown_indices"] = from_list(from_int, self.unknown_indices)
        return result


class Schema60:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        data = from_list(from_int, obj.get("data"))
        return Schema60(data)

    def to_dict(self):
        result = {}
        result["data"] = from_list(from_int, self.data)
        return result


class IndigoMorpher:
    def __init__(self, morpher_relateds):
        self.morpher_relateds = morpher_relateds

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        morpher_relateds = from_list(Schema60.from_dict, obj.get("morpher_relateds"))
        return IndigoMorpher(morpher_relateds)

    def to_dict(self):
        result = {}
        result["morpher_relateds"] = from_list(
            lambda x: to_class(Schema60, x), self.morpher_relateds
        )
        return result


class Schema61:
    def __init__(self, vector):
        self.vector = vector

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        vector = from_list(from_float, obj.get("vector"))
        return Schema61(vector)

    def to_dict(self):
        result = {}
        result["vector"] = from_list(to_float, self.vector)
        return result


class Schema62:
    def __init__(self, vector):
        self.vector = vector

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        vector = from_list(from_float, obj.get("vector"))
        return Schema62(vector)

    def to_dict(self):
        result = {}
        result["vector"] = from_list(to_float, self.vector)
        return result


class IndigoPoints:
    def __init__(self, morpher, points_related0_s, points_related1_s):
        self.morpher = morpher
        self.points_related0_s = points_related0_s
        self.points_related1_s = points_related1_s

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        morpher = IndigoMorpher.from_dict(obj.get("morpher"))
        points_related0_s = from_list(Schema61.from_dict, obj.get("points_related0s"))
        points_related1_s = from_list(Schema62.from_dict, obj.get("points_related1s"))
        return IndigoPoints(morpher, points_related0_s, points_related1_s)

    def to_dict(self):
        result = {}
        result["morpher"] = to_class(IndigoMorpher, self.morpher)
        result["points_related0s"] = from_list(
            lambda x: to_class(Schema61, x), self.points_related0_s
        )
        result["points_related1s"] = from_list(
            lambda x: to_class(Schema62, x), self.points_related1_s
        )
        return result


class Schema64:
    def __init__(self, element_count, element_entry):
        self.element_count = element_count
        self.element_entry = element_entry

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        element_count = from_int(obj.get("element_count"))
        element_entry = from_int(obj.get("element_entry"))
        return Schema64(element_count, element_entry)

    def to_dict(self):
        result = {}
        result["element_count"] = from_int(self.element_count)
        result["element_entry"] = from_int(self.element_entry)
        return result


class Schema63:
    def __init__(
        self,
        axes0,
        axes1,
        axes2,
        center,
        f_size,
        hit_patch_count,
        i_size,
        patch_indices,
        sead_voxels,
        size,
        step,
        unknown_ptr0,
        unknown_ptr1,
        unknown_ptr2,
        unknown_ptr3,
        unknown_ptr4,
        unknown_vec0_s,
        unknown_vec1,
        unknown_vec2,
        used_in_voxel_trace,
    ):
        self.axes0 = axes0
        self.axes1 = axes1
        self.axes2 = axes2
        self.center = center
        self.f_size = f_size
        self.hit_patch_count = hit_patch_count
        self.i_size = i_size
        self.patch_indices = patch_indices
        self.sead_voxels = sead_voxels
        self.size = size
        self.step = step
        self.unknown_ptr0 = unknown_ptr0
        self.unknown_ptr1 = unknown_ptr1
        self.unknown_ptr2 = unknown_ptr2
        self.unknown_ptr3 = unknown_ptr3
        self.unknown_ptr4 = unknown_ptr4
        self.unknown_vec0_s = unknown_vec0_s
        self.unknown_vec1 = unknown_vec1
        self.unknown_vec2 = unknown_vec2
        self.used_in_voxel_trace = used_in_voxel_trace

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        axes0 = from_list(from_float, obj.get("axes0"))
        axes1 = from_list(from_float, obj.get("axes1"))
        axes2 = from_list(from_float, obj.get("axes2"))
        center = from_list(from_float, obj.get("center"))
        f_size = from_list(from_float, obj.get("f_size"))
        hit_patch_count = from_int(obj.get("hit_patch_count"))
        i_size = from_list(from_float, obj.get("i_size"))
        patch_indices = from_list(from_int, obj.get("patch_indices"))
        sead_voxels = from_list(Schema64.from_dict, obj.get("sead_voxels"))
        size = from_list(from_float, obj.get("size"))
        step = from_list(from_float, obj.get("step"))
        unknown_ptr0 = from_int(obj.get("unknown_ptr0"))
        unknown_ptr1 = from_int(obj.get("unknown_ptr1"))
        unknown_ptr2 = from_int(obj.get("unknown_ptr2"))
        unknown_ptr3 = from_int(obj.get("unknown_ptr3"))
        unknown_ptr4 = from_int(obj.get("unknown_ptr4"))
        unknown_vec0_s = from_list(
            lambda x: from_list(from_float, x), obj.get("unknown_vec0s")
        )
        unknown_vec1 = from_list(from_float, obj.get("unknown_vec1"))
        unknown_vec2 = from_list(from_float, obj.get("unknown_vec2"))
        used_in_voxel_trace = from_int(obj.get("used_in_voxel_trace"))
        return Schema63(
            axes0,
            axes1,
            axes2,
            center,
            f_size,
            hit_patch_count,
            i_size,
            patch_indices,
            sead_voxels,
            size,
            step,
            unknown_ptr0,
            unknown_ptr1,
            unknown_ptr2,
            unknown_ptr3,
            unknown_ptr4,
            unknown_vec0_s,
            unknown_vec1,
            unknown_vec2,
            used_in_voxel_trace,
        )

    def to_dict(self):
        result = {}
        result["axes0"] = from_list(to_float, self.axes0)
        result["axes1"] = from_list(to_float, self.axes1)
        result["axes2"] = from_list(to_float, self.axes2)
        result["center"] = from_list(to_float, self.center)
        result["f_size"] = from_list(to_float, self.f_size)
        result["hit_patch_count"] = from_int(self.hit_patch_count)
        result["i_size"] = from_list(to_float, self.i_size)
        result["patch_indices"] = from_list(from_int, self.patch_indices)
        result["sead_voxels"] = from_list(
            lambda x: to_class(Schema64, x), self.sead_voxels
        )
        result["size"] = from_list(to_float, self.size)
        result["step"] = from_list(to_float, self.step)
        result["unknown_ptr0"] = from_int(self.unknown_ptr0)
        result["unknown_ptr1"] = from_int(self.unknown_ptr1)
        result["unknown_ptr2"] = from_int(self.unknown_ptr2)
        result["unknown_ptr3"] = from_int(self.unknown_ptr3)
        result["unknown_ptr4"] = from_int(self.unknown_ptr4)
        result["unknown_vec0s"] = from_list(
            lambda x: from_list(to_float, x), self.unknown_vec0_s
        )
        result["unknown_vec1"] = from_list(to_float, self.unknown_vec1)
        result["unknown_vec2"] = from_list(to_float, self.unknown_vec2)
        result["used_in_voxel_trace"] = from_int(self.used_in_voxel_trace)
        return result


class FluffySeadIndex:
    def __init__(self, inner):
        self.inner = inner

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        inner = from_union([Schema63.from_dict, from_none], obj.get("inner"))
        return FluffySeadIndex(inner)

    def to_dict(self):
        result = {}
        if self.inner is not None:
            result["inner"] = from_union(
                [lambda x: to_class(Schema63, x), from_none], self.inner
            )
        return result


class Schema65:
    def __init__(self, value):
        self.value = value

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        value = from_int(obj.get("value"))
        return Schema65(value)

    def to_dict(self):
        result = {}
        result["value"] = from_int(self.value)
        return result


class SurfaceV1291_03_06PCBody:
    def __init__(
        self,
        cling_line_relateds,
        colors,
        displacement_relateds,
        edge_cols,
        edges,
        normals,
        patch_cols,
        patches,
        points,
        sead_index,
        should_draw_relateds,
    ):
        self.cling_line_relateds = cling_line_relateds
        self.colors = colors
        self.displacement_relateds = displacement_relateds
        self.edge_cols = edge_cols
        self.edges = edges
        self.normals = normals
        self.patch_cols = patch_cols
        self.patches = patches
        self.points = points
        self.sead_index = sead_index
        self.should_draw_relateds = should_draw_relateds

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        cling_line_relateds = from_list(
            Schema55.from_dict, obj.get("cling_line_relateds")
        )
        colors = from_list(lambda x: from_list(from_float, x), obj.get("colors"))
        displacement_relateds = from_list(
            lambda x: from_list(from_float, x), obj.get("displacement_relateds")
        )
        edge_cols = from_list(Schema56.from_dict, obj.get("edge_cols"))
        edges = from_list(Schema57.from_dict, obj.get("edges"))
        normals = from_list(lambda x: from_list(from_float, x), obj.get("normals"))
        patch_cols = from_list(Schema58.from_dict, obj.get("patch_cols"))
        patches = from_list(Schema59.from_dict, obj.get("patches"))
        points = IndigoPoints.from_dict(obj.get("points"))
        sead_index = from_union(
            [FluffySeadIndex.from_dict, from_none], obj.get("sead_index")
        )
        should_draw_relateds = from_list(
            Schema65.from_dict, obj.get("should_draw_relateds")
        )
        return SurfaceV1291_03_06PCBody(
            cling_line_relateds,
            colors,
            displacement_relateds,
            edge_cols,
            edges,
            normals,
            patch_cols,
            patches,
            points,
            sead_index,
            should_draw_relateds,
        )

    def to_dict(self):
        result = {}
        result["cling_line_relateds"] = from_list(
            lambda x: to_class(Schema55, x), self.cling_line_relateds
        )
        result["colors"] = from_list(lambda x: from_list(to_float, x), self.colors)
        result["displacement_relateds"] = from_list(
            lambda x: from_list(to_float, x), self.displacement_relateds
        )
        result["edge_cols"] = from_list(lambda x: to_class(Schema56, x), self.edge_cols)
        result["edges"] = from_list(lambda x: to_class(Schema57, x), self.edges)
        result["normals"] = from_list(lambda x: from_list(to_float, x), self.normals)
        result["patch_cols"] = from_list(
            lambda x: to_class(Schema58, x), self.patch_cols
        )
        result["patches"] = from_list(lambda x: to_class(Schema59, x), self.patches)
        result["points"] = to_class(IndigoPoints, self.points)
        if self.sead_index is not None:
            result["sead_index"] = from_union(
                [lambda x: to_class(FluffySeadIndex, x), from_none], self.sead_index
            )
        result["should_draw_relateds"] = from_list(
            lambda x: to_class(Schema65, x), self.should_draw_relateds
        )
        return result


class SurfaceV1291_03_06_PC:
    def __init__(self, body, class_name, link_header, link_name, name):
        self.body = body
        self.class_name = class_name
        self.link_header = link_header
        self.link_name = link_name
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        body = SurfaceV1291_03_06PCBody.from_dict(obj.get("body"))
        class_name = from_union([from_int, from_str], obj.get("class_name"))
        link_header = CameraZoneV106_63_02PCLinkHeader.from_dict(obj.get("link_header"))
        link_name = from_union([from_none, from_int, from_str], obj.get("link_name"))
        name = from_union([from_int, from_str], obj.get("name"))
        return SurfaceV1291_03_06_PC(body, class_name, link_header, link_name, name)

    def to_dict(self):
        result = {}
        result["body"] = to_class(SurfaceV1291_03_06PCBody, self.body)
        result["class_name"] = from_union([from_int, from_str], self.class_name)
        result["link_header"] = to_class(
            CameraZoneV106_63_02PCLinkHeader, self.link_header
        )
        if self.link_name is not None:
            result["link_name"] = from_union(
                [from_none, from_int, from_str], self.link_name
            )
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class Schema66:
    def __init__(self, p, t):
        self.p = p
        self.t = t

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        p = from_list(from_int, obj.get("p"))
        t = from_list(from_int, obj.get("t"))
        return Schema66(p, t)

    def to_dict(self):
        result = {}
        result["p"] = from_list(from_int, self.p)
        result["t"] = from_list(from_int, self.t)
        return result


class Schema67:
    def __init__(
        self,
        data,
        edge_indices,
        flag,
        index_in_unk_short_da,
        mat,
        material_anim_index,
        material_anim_name,
        surface_indices_index,
        unknown3_s,
        vec4_fs_indices,
    ):
        self.data = data
        self.edge_indices = edge_indices
        self.flag = flag
        self.index_in_unk_short_da = index_in_unk_short_da
        self.mat = mat
        self.material_anim_index = material_anim_index
        self.material_anim_name = material_anim_name
        self.surface_indices_index = surface_indices_index
        self.unknown3_s = unknown3_s
        self.vec4_fs_indices = vec4_fs_indices

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        data = from_list(from_int, obj.get("data"))
        edge_indices = from_list(from_int, obj.get("edge_indices"))
        flag = from_int(obj.get("flag"))
        index_in_unk_short_da = from_int(obj.get("index_in_unk_short_da"))
        mat = from_list(lambda x: from_list(from_float, x), obj.get("mat"))
        material_anim_index = from_int(obj.get("material_anim_index"))
        material_anim_name = from_union(
            [from_int, from_str], obj.get("material_anim_name")
        )
        surface_indices_index = from_int(obj.get("surface_indices_index"))
        unknown3_s = from_list(from_int, obj.get("unknown3s"))
        vec4_fs_indices = from_list(from_int, obj.get("vec4fs_indices"))
        return Schema67(
            data,
            edge_indices,
            flag,
            index_in_unk_short_da,
            mat,
            material_anim_index,
            material_anim_name,
            surface_indices_index,
            unknown3_s,
            vec4_fs_indices,
        )

    def to_dict(self):
        result = {}
        result["data"] = from_list(from_int, self.data)
        result["edge_indices"] = from_list(from_int, self.edge_indices)
        result["flag"] = from_int(self.flag)
        result["index_in_unk_short_da"] = from_int(self.index_in_unk_short_da)
        result["mat"] = from_list(lambda x: from_list(to_float, x), self.mat)
        result["material_anim_index"] = from_int(self.material_anim_index)
        result["material_anim_name"] = from_union(
            [from_int, from_str], self.material_anim_name
        )
        result["surface_indices_index"] = from_int(self.surface_indices_index)
        result["unknown3s"] = from_list(from_int, self.unknown3_s)
        result["vec4fs_indices"] = from_list(from_int, self.vec4_fs_indices)
        return result


class Schema69:
    def __init__(self, patches_indices_range):
        self.patches_indices_range = patches_indices_range

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        patches_indices_range = Range.from_dict(obj.get("patches_indices_range"))
        return Schema69(patches_indices_range)

    def to_dict(self):
        result = {}
        result["patches_indices_range"] = to_class(Range, self.patches_indices_range)
        return result


class Unknown15:
    def __init__(self, data1, data2, patch_count_related, sead_voxel_count, unknown0_s):
        self.data1 = data1
        self.data2 = data2
        self.patch_count_related = patch_count_related
        self.sead_voxel_count = sead_voxel_count
        self.unknown0_s = unknown0_s

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        data1 = from_list(from_int, obj.get("data1"))
        data2 = from_list(from_int, obj.get("data2"))
        patch_count_related = from_int(obj.get("patch_count_related"))
        sead_voxel_count = from_int(obj.get("sead_voxel_count"))
        unknown0_s = from_list(from_int, obj.get("unknown0s"))
        return Unknown15(
            data1, data2, patch_count_related, sead_voxel_count, unknown0_s
        )

    def to_dict(self):
        result = {}
        result["data1"] = from_list(from_int, self.data1)
        result["data2"] = from_list(from_int, self.data2)
        result["patch_count_related"] = from_int(self.patch_count_related)
        result["sead_voxel_count"] = from_int(self.sead_voxel_count)
        result["unknown0s"] = from_list(from_int, self.unknown0_s)
        return result


class Schema68:
    def __init__(self, patch_count, patches_indices, sead_voxels, unknown15):
        self.patch_count = patch_count
        self.patches_indices = patches_indices
        self.sead_voxels = sead_voxels
        self.unknown15 = unknown15

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        patch_count = from_int(obj.get("patch_count"))
        patches_indices = from_list(from_int, obj.get("patches_indices"))
        sead_voxels = from_list(Schema69.from_dict, obj.get("sead_voxels"))
        unknown15 = Unknown15.from_dict(obj.get("unknown15"))
        return Schema68(patch_count, patches_indices, sead_voxels, unknown15)

    def to_dict(self):
        result = {}
        result["patch_count"] = from_int(self.patch_count)
        result["patches_indices"] = from_list(from_int, self.patches_indices)
        result["sead_voxels"] = from_list(
            lambda x: to_class(Schema69, x), self.sead_voxels
        )
        result["unknown15"] = to_class(Unknown15, self.unknown15)
        return result


class TentacledSeadIndex:
    def __init__(self, inner):
        self.inner = inner

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        inner = from_union([Schema68.from_dict, from_none], obj.get("inner"))
        return TentacledSeadIndex(inner)

    def to_dict(self):
        result = {}
        if self.inner is not None:
            result["inner"] = from_union(
                [lambda x: to_class(Schema68, x), from_none], self.inner
            )
        return result


class Schema70:
    def __init__(self, value):
        self.value = value

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        value = from_int(obj.get("value"))
        return Schema70(value)

    def to_dict(self):
        result = {}
        result["value"] = from_int(self.value)
        return result


class Unused12Element:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        data = from_list(from_int, obj.get("data"))
        return Unused12Element(data)

    def to_dict(self):
        result = {}
        result["data"] = from_list(from_int, self.data)
        return result


class Unused2Element:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        data = from_list(from_int, obj.get("data"))
        return Unused2Element(data)

    def to_dict(self):
        result = {}
        result["data"] = from_list(from_int, self.data)
        return result


class Unused3Element:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        data = from_list(from_int, obj.get("data"))
        return Unused3Element(data)

    def to_dict(self):
        result = {}
        result["data"] = from_list(from_int, self.data)
        return result


class SurfaceV1381_67_09PCBody:
    def __init__(
        self,
        edges,
        normals,
        patches,
        points,
        sead_index,
        should_draw_relateds,
        unused12_s,
        unused2_s,
        unused3_s,
        vec4_fs,
        vertex10_s,
        vertex9_s,
    ):
        self.edges = edges
        self.normals = normals
        self.patches = patches
        self.points = points
        self.sead_index = sead_index
        self.should_draw_relateds = should_draw_relateds
        self.unused12_s = unused12_s
        self.unused2_s = unused2_s
        self.unused3_s = unused3_s
        self.vec4_fs = vec4_fs
        self.vertex10_s = vertex10_s
        self.vertex9_s = vertex9_s

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        edges = from_list(Schema66.from_dict, obj.get("edges"))
        normals = from_list(lambda x: from_list(from_float, x), obj.get("normals"))
        patches = from_list(Schema67.from_dict, obj.get("patches"))
        points = from_list(lambda x: from_list(from_float, x), obj.get("points"))
        sead_index = from_union(
            [TentacledSeadIndex.from_dict, from_none], obj.get("sead_index")
        )
        should_draw_relateds = from_list(
            Schema70.from_dict, obj.get("should_draw_relateds")
        )
        unused12_s = from_list(Unused12Element.from_dict, obj.get("unused12s"))
        unused2_s = from_list(Unused2Element.from_dict, obj.get("unused2s"))
        unused3_s = from_list(Unused3Element.from_dict, obj.get("unused3s"))
        vec4_fs = from_list(lambda x: from_list(from_float, x), obj.get("vec4fs"))
        vertex10_s = from_list(lambda x: from_list(from_float, x), obj.get("vertex10s"))
        vertex9_s = from_list(lambda x: from_list(from_float, x), obj.get("vertex9s"))
        return SurfaceV1381_67_09PCBody(
            edges,
            normals,
            patches,
            points,
            sead_index,
            should_draw_relateds,
            unused12_s,
            unused2_s,
            unused3_s,
            vec4_fs,
            vertex10_s,
            vertex9_s,
        )

    def to_dict(self):
        result = {}
        result["edges"] = from_list(lambda x: to_class(Schema66, x), self.edges)
        result["normals"] = from_list(lambda x: from_list(to_float, x), self.normals)
        result["patches"] = from_list(lambda x: to_class(Schema67, x), self.patches)
        result["points"] = from_list(lambda x: from_list(to_float, x), self.points)
        if self.sead_index is not None:
            result["sead_index"] = from_union(
                [lambda x: to_class(TentacledSeadIndex, x), from_none], self.sead_index
            )
        result["should_draw_relateds"] = from_list(
            lambda x: to_class(Schema70, x), self.should_draw_relateds
        )
        result["unused12s"] = from_list(
            lambda x: to_class(Unused12Element, x), self.unused12_s
        )
        result["unused2s"] = from_list(
            lambda x: to_class(Unused2Element, x), self.unused2_s
        )
        result["unused3s"] = from_list(
            lambda x: to_class(Unused3Element, x), self.unused3_s
        )
        result["vec4fs"] = from_list(lambda x: from_list(to_float, x), self.vec4_fs)
        result["vertex10s"] = from_list(
            lambda x: from_list(to_float, x), self.vertex10_s
        )
        result["vertex9s"] = from_list(lambda x: from_list(to_float, x), self.vertex9_s)
        return result


class SurfaceV1381_67_09_PC:
    def __init__(self, body, class_name, link_header, link_name, name):
        self.body = body
        self.class_name = class_name
        self.link_header = link_header
        self.link_name = link_name
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        body = SurfaceV1381_67_09PCBody.from_dict(obj.get("body"))
        class_name = from_union([from_int, from_str], obj.get("class_name"))
        link_header = CameraV1381_67_09PCLinkHeader.from_dict(obj.get("link_header"))
        link_name = from_union([from_none, from_int, from_str], obj.get("link_name"))
        name = from_union([from_int, from_str], obj.get("name"))
        return SurfaceV1381_67_09_PC(body, class_name, link_header, link_name, name)

    def to_dict(self):
        result = {}
        result["body"] = to_class(SurfaceV1381_67_09PCBody, self.body)
        result["class_name"] = from_union([from_int, from_str], self.class_name)
        result["link_header"] = to_class(
            CameraV1381_67_09PCLinkHeader, self.link_header
        )
        if self.link_name is not None:
            result["link_name"] = from_union(
                [from_none, from_int, from_str], self.link_name
            )
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class Surface:
    def __init__(
        self, surface_v1_06_63_02_pc, surface_v1_291_03_06_pc, surface_v1_381_67_09_pc
    ):
        self.surface_v1_06_63_02_pc = surface_v1_06_63_02_pc
        self.surface_v1_291_03_06_pc = surface_v1_291_03_06_pc
        self.surface_v1_381_67_09_pc = surface_v1_381_67_09_pc

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        surface_v1_06_63_02_pc = from_union(
            [SurfaceV106_63_02_PC.from_dict, from_none], obj.get("SurfaceV1_06_63_02PC")
        )
        surface_v1_291_03_06_pc = from_union(
            [SurfaceV1291_03_06_PC.from_dict, from_none],
            obj.get("SurfaceV1_291_03_06PC"),
        )
        surface_v1_381_67_09_pc = from_union(
            [SurfaceV1381_67_09_PC.from_dict, from_none],
            obj.get("SurfaceV1_381_67_09PC"),
        )
        return Surface(
            surface_v1_06_63_02_pc, surface_v1_291_03_06_pc, surface_v1_381_67_09_pc
        )

    def to_dict(self):
        result = {}
        if self.surface_v1_06_63_02_pc is not None:
            result["SurfaceV1_06_63_02PC"] = from_union(
                [lambda x: to_class(SurfaceV106_63_02_PC, x), from_none],
                self.surface_v1_06_63_02_pc,
            )
        if self.surface_v1_291_03_06_pc is not None:
            result["SurfaceV1_291_03_06PC"] = from_union(
                [lambda x: to_class(SurfaceV1291_03_06_PC, x), from_none],
                self.surface_v1_291_03_06_pc,
            )
        if self.surface_v1_381_67_09_pc is not None:
            result["SurfaceV1_381_67_09PC"] = from_union(
                [lambda x: to_class(SurfaceV1381_67_09_PC, x), from_none],
                self.surface_v1_381_67_09_pc,
            )
        return result


class SurfaceDatasV1381_67_09PCBody:
    def __init__(self, flags):
        self.flags = flags

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        flags = ResourceDatasFlags.from_dict(obj.get("flags"))
        return SurfaceDatasV1381_67_09PCBody(flags)

    def to_dict(self):
        result = {}
        result["flags"] = to_class(ResourceDatasFlags, self.flags)
        return result


class SurfaceDatasV1381_67_09_PC:
    def __init__(self, body, class_name, link_header, link_name, name):
        self.body = body
        self.class_name = class_name
        self.link_header = link_header
        self.link_name = link_name
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        body = SurfaceDatasV1381_67_09PCBody.from_dict(obj.get("body"))
        class_name = from_union([from_int, from_str], obj.get("class_name"))
        link_header = AnimationV1381_67_09PCLinkHeader.from_dict(obj.get("link_header"))
        link_name = from_union([from_none, from_int, from_str], obj.get("link_name"))
        name = from_union([from_int, from_str], obj.get("name"))
        return SurfaceDatasV1381_67_09_PC(
            body, class_name, link_header, link_name, name
        )

    def to_dict(self):
        result = {}
        result["body"] = to_class(SurfaceDatasV1381_67_09PCBody, self.body)
        result["class_name"] = from_union([from_int, from_str], self.class_name)
        result["link_header"] = to_class(
            AnimationV1381_67_09PCLinkHeader, self.link_header
        )
        if self.link_name is not None:
            result["link_name"] = from_union(
                [from_none, from_int, from_str], self.link_name
            )
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class SurfaceDatas:
    def __init__(self, surface_datas_v1_381_67_09_pc):
        self.surface_datas_v1_381_67_09_pc = surface_datas_v1_381_67_09_pc

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        surface_datas_v1_381_67_09_pc = SurfaceDatasV1381_67_09_PC.from_dict(
            obj.get("SurfaceDatasV1_381_67_09PC")
        )
        return SurfaceDatas(surface_datas_v1_381_67_09_pc)

    def to_dict(self):
        result = {}
        result["SurfaceDatasV1_381_67_09PC"] = to_class(
            SurfaceDatasV1381_67_09_PC, self.surface_datas_v1_381_67_09_pc
        )
        return result


class UserDefineV1291_03_06_PC:
    def __init__(self, body, class_name, link_header, link_name, name):
        self.body = body
        self.class_name = class_name
        self.link_header = link_header
        self.link_name = link_name
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        body = from_dict(lambda x: x, obj.get("body"))
        class_name = from_union([from_int, from_str], obj.get("class_name"))
        link_header = AnimationV1291_03_06PCLinkHeader.from_dict(obj.get("link_header"))
        link_name = from_union([from_none, from_int, from_str], obj.get("link_name"))
        name = from_union([from_int, from_str], obj.get("name"))
        return UserDefineV1291_03_06_PC(body, class_name, link_header, link_name, name)

    def to_dict(self):
        result = {}
        result["body"] = from_dict(lambda x: x, self.body)
        result["class_name"] = from_union([from_int, from_str], self.class_name)
        result["link_header"] = to_class(
            AnimationV1291_03_06PCLinkHeader, self.link_header
        )
        if self.link_name is not None:
            result["link_name"] = from_union(
                [from_none, from_int, from_str], self.link_name
            )
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class UserDefine:
    def __init__(self, user_define_v1_291_03_06_pc):
        self.user_define_v1_291_03_06_pc = user_define_v1_291_03_06_pc

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        user_define_v1_291_03_06_pc = UserDefineV1291_03_06_PC.from_dict(
            obj.get("UserDefineV1_291_03_06PC")
        )
        return UserDefine(user_define_v1_291_03_06_pc)

    def to_dict(self):
        result = {}
        result["UserDefineV1_291_03_06PC"] = to_class(
            UserDefineV1291_03_06_PC, self.user_define_v1_291_03_06_pc
        )
        return result


class WarpV106_63_02PCBody:
    def __init__(
        self, anim_frame_names, flag, material_anim_names, node_name, vec, vertices
    ):
        self.anim_frame_names = anim_frame_names
        self.flag = flag
        self.material_anim_names = material_anim_names
        self.node_name = node_name
        self.vec = vec
        self.vertices = vertices

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        anim_frame_names = from_list(
            lambda x: from_union([from_int, from_str], x), obj.get("anim_frame_names")
        )
        flag = from_int(obj.get("flag"))
        material_anim_names = from_list(
            lambda x: from_union([from_int, from_str], x),
            obj.get("material_anim_names"),
        )
        node_name = from_union([from_int, from_str], obj.get("node_name"))
        vec = from_list(from_float, obj.get("vec"))
        vertices = from_list(lambda x: from_list(from_float, x), obj.get("vertices"))
        return WarpV106_63_02PCBody(
            anim_frame_names, flag, material_anim_names, node_name, vec, vertices
        )

    def to_dict(self):
        result = {}
        result["anim_frame_names"] = from_list(
            lambda x: from_union([from_int, from_str], x), self.anim_frame_names
        )
        result["flag"] = from_int(self.flag)
        result["material_anim_names"] = from_list(
            lambda x: from_union([from_int, from_str], x), self.material_anim_names
        )
        result["node_name"] = from_union([from_int, from_str], self.node_name)
        result["vec"] = from_list(to_float, self.vec)
        result["vertices"] = from_list(lambda x: from_list(to_float, x), self.vertices)
        return result


class WarpV106_63_02_PC:
    def __init__(self, body, class_name, link_header, link_name, name):
        self.body = body
        self.class_name = class_name
        self.link_header = link_header
        self.link_name = link_name
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        body = WarpV106_63_02PCBody.from_dict(obj.get("body"))
        class_name = from_union([from_int, from_str], obj.get("class_name"))
        link_header = AnimationV1291_03_06PCLinkHeader.from_dict(obj.get("link_header"))
        link_name = from_union([from_none, from_int, from_str], obj.get("link_name"))
        name = from_union([from_int, from_str], obj.get("name"))
        return WarpV106_63_02_PC(body, class_name, link_header, link_name, name)

    def to_dict(self):
        result = {}
        result["body"] = to_class(WarpV106_63_02PCBody, self.body)
        result["class_name"] = from_union([from_int, from_str], self.class_name)
        result["link_header"] = to_class(
            AnimationV1291_03_06PCLinkHeader, self.link_header
        )
        if self.link_name is not None:
            result["link_name"] = from_union(
                [from_none, from_int, from_str], self.link_name
            )
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class Warp:
    def __init__(self, warp_v1_06_63_02_pc):
        self.warp_v1_06_63_02_pc = warp_v1_06_63_02_pc

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        warp_v1_06_63_02_pc = WarpV106_63_02_PC.from_dict(obj.get("WarpV1_06_63_02PC"))
        return Warp(warp_v1_06_63_02_pc)

    def to_dict(self):
        result = {}
        result["WarpV1_06_63_02PC"] = to_class(
            WarpV106_63_02_PC, self.warp_v1_06_63_02_pc
        )
        return result


class Schema71:
    def __init__(
        self,
        grid_id,
        next_entry_of_resource,
        next_resource_of_entry,
        node_name,
        prev_resource_of_entry,
    ):
        self.grid_id = grid_id
        self.next_entry_of_resource = next_entry_of_resource
        self.next_resource_of_entry = next_resource_of_entry
        self.node_name = node_name
        self.prev_resource_of_entry = prev_resource_of_entry

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        grid_id = from_int(obj.get("grid_id"))
        next_entry_of_resource = from_int(obj.get("next_entry_of_resource"))
        next_resource_of_entry = from_int(obj.get("next_resource_of_entry"))
        node_name = from_union([from_int, from_str], obj.get("node_name"))
        prev_resource_of_entry = from_int(obj.get("prev_resource_of_entry"))
        return Schema71(
            grid_id,
            next_entry_of_resource,
            next_resource_of_entry,
            node_name,
            prev_resource_of_entry,
        )

    def to_dict(self):
        result = {}
        result["grid_id"] = from_int(self.grid_id)
        result["next_entry_of_resource"] = from_int(self.next_entry_of_resource)
        result["next_resource_of_entry"] = from_int(self.next_resource_of_entry)
        result["node_name"] = from_union([from_int, from_str], self.node_name)
        result["prev_resource_of_entry"] = from_int(self.prev_resource_of_entry)
        return result


class PurpleSeadHandle0:
    def __init__(
        self, first_free, free_count, grid, inv_diag, p_max, p_min, sead_entries, size
    ):
        self.first_free = first_free
        self.free_count = free_count
        self.grid = grid
        self.inv_diag = inv_diag
        self.p_max = p_max
        self.p_min = p_min
        self.sead_entries = sead_entries
        self.size = size

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        first_free = from_int(obj.get("first_free"))
        free_count = from_int(obj.get("free_count"))
        grid = from_list(from_int, obj.get("grid"))
        inv_diag = from_list(from_float, obj.get("inv_diag"))
        p_max = from_list(from_float, obj.get("p_max"))
        p_min = from_list(from_float, obj.get("p_min"))
        sead_entries = from_list(Schema71.from_dict, obj.get("sead_entries"))
        size = from_list(lambda x: x, obj.get("size"))
        return PurpleSeadHandle0(
            first_free, free_count, grid, inv_diag, p_max, p_min, sead_entries, size
        )

    def to_dict(self):
        result = {}
        result["first_free"] = from_int(self.first_free)
        result["free_count"] = from_int(self.free_count)
        result["grid"] = from_list(from_int, self.grid)
        result["inv_diag"] = from_list(to_float, self.inv_diag)
        result["p_max"] = from_list(to_float, self.p_max)
        result["p_min"] = from_list(to_float, self.p_min)
        result["sead_entries"] = from_list(
            lambda x: to_class(Schema71, x), self.sead_entries
        )
        result["size"] = from_list(lambda x: x, self.size)
        return result


class UnkStructs1Element:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        data = from_list(from_int, obj.get("data"))
        return UnkStructs1Element(data)

    def to_dict(self):
        result = {}
        result["data"] = from_list(from_int, self.data)
        return result


class PurpleSubWorldRange:
    def __init__(self, data, unk0, unk_structs1):
        self.data = data
        self.unk0 = unk0
        self.unk_structs1 = unk_structs1

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        data = from_list(from_int, obj.get("data"))
        unk0 = from_int(obj.get("unk0"))
        unk_structs1 = from_list(UnkStructs1Element.from_dict, obj.get("unk_structs1"))
        return PurpleSubWorldRange(data, unk0, unk_structs1)

    def to_dict(self):
        result = {}
        result["data"] = from_list(from_int, self.data)
        result["unk0"] = from_int(self.unk0)
        result["unk_structs1"] = from_list(
            lambda x: to_class(UnkStructs1Element, x), self.unk_structs1
        )
        return result


class Schema72:
    def __init__(
        self, data, sub_world_range, unknown0_s, unknown1_s, unknown2_s, unknown3_s
    ):
        self.data = data
        self.sub_world_range = sub_world_range
        self.unknown0_s = unknown0_s
        self.unknown1_s = unknown1_s
        self.unknown2_s = unknown2_s
        self.unknown3_s = unknown3_s

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        data = from_list(from_int, obj.get("data"))
        sub_world_range = PurpleSubWorldRange.from_dict(obj.get("sub_world_range"))
        unknown0_s = from_list(from_int, obj.get("unknown0s"))
        unknown1_s = from_list(from_int, obj.get("unknown1s"))
        unknown2_s = from_list(from_int, obj.get("unknown2s"))
        unknown3_s = from_list(from_int, obj.get("unknown3s"))
        return Schema72(
            data, sub_world_range, unknown0_s, unknown1_s, unknown2_s, unknown3_s
        )

    def to_dict(self):
        result = {}
        result["data"] = from_list(from_int, self.data)
        result["sub_world_range"] = to_class(PurpleSubWorldRange, self.sub_world_range)
        result["unknown0s"] = from_list(from_int, self.unknown0_s)
        result["unknown1s"] = from_list(from_int, self.unknown1_s)
        result["unknown2s"] = from_list(from_int, self.unknown2_s)
        result["unknown3s"] = from_list(from_int, self.unknown3_s)
        return result


class WorldV106_63_02PCBody:
    def __init__(
        self,
        anim_frame_names,
        camera_zone_names,
        crc32_unk5,
        crc32_unk6,
        crc32_s_unk4,
        game_obj_name,
        graph_names,
        linked_names,
        occluder_names,
        root_node_name,
        sead_handle0,
        sead_handle1,
        sub_world_datas,
        warp_name,
    ):
        self.anim_frame_names = anim_frame_names
        self.camera_zone_names = camera_zone_names
        self.crc32_unk5 = crc32_unk5
        self.crc32_unk6 = crc32_unk6
        self.crc32_s_unk4 = crc32_s_unk4
        self.game_obj_name = game_obj_name
        self.graph_names = graph_names
        self.linked_names = linked_names
        self.occluder_names = occluder_names
        self.root_node_name = root_node_name
        self.sead_handle0 = sead_handle0
        self.sead_handle1 = sead_handle1
        self.sub_world_datas = sub_world_datas
        self.warp_name = warp_name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        anim_frame_names = from_list(
            lambda x: from_union([from_int, from_str], x), obj.get("anim_frame_names")
        )
        camera_zone_names = from_list(
            lambda x: from_union([from_int, from_str], x), obj.get("camera_zone_names")
        )
        crc32_unk5 = from_union([from_int, from_str], obj.get("crc32_unk5"))
        crc32_unk6 = from_union([from_int, from_str], obj.get("crc32_unk6"))
        crc32_s_unk4 = from_list(
            lambda x: from_union([from_int, from_str], x), obj.get("crc32s_unk4")
        )
        game_obj_name = from_union([from_int, from_str], obj.get("game_obj_name"))
        graph_names = from_list(
            lambda x: from_union([from_int, from_str], x), obj.get("graph_names")
        )
        linked_names = from_list(
            lambda x: from_union([from_int, from_str], x), obj.get("linked_names")
        )
        occluder_names = from_list(
            lambda x: from_union([from_int, from_str], x), obj.get("occluder_names")
        )
        root_node_name = from_union([from_int, from_str], obj.get("root_node_name"))
        sead_handle0 = PurpleSeadHandle0.from_dict(obj.get("sead_handle0"))
        sead_handle1 = PurpleSeadHandle0.from_dict(obj.get("sead_handle1"))
        sub_world_datas = from_list(Schema72.from_dict, obj.get("sub_world_datas"))
        warp_name = from_union([from_int, from_str], obj.get("warp_name"))
        return WorldV106_63_02PCBody(
            anim_frame_names,
            camera_zone_names,
            crc32_unk5,
            crc32_unk6,
            crc32_s_unk4,
            game_obj_name,
            graph_names,
            linked_names,
            occluder_names,
            root_node_name,
            sead_handle0,
            sead_handle1,
            sub_world_datas,
            warp_name,
        )

    def to_dict(self):
        result = {}
        result["anim_frame_names"] = from_list(
            lambda x: from_union([from_int, from_str], x), self.anim_frame_names
        )
        result["camera_zone_names"] = from_list(
            lambda x: from_union([from_int, from_str], x), self.camera_zone_names
        )
        result["crc32_unk5"] = from_union([from_int, from_str], self.crc32_unk5)
        result["crc32_unk6"] = from_union([from_int, from_str], self.crc32_unk6)
        result["crc32s_unk4"] = from_list(
            lambda x: from_union([from_int, from_str], x), self.crc32_s_unk4
        )
        result["game_obj_name"] = from_union([from_int, from_str], self.game_obj_name)
        result["graph_names"] = from_list(
            lambda x: from_union([from_int, from_str], x), self.graph_names
        )
        result["linked_names"] = from_list(
            lambda x: from_union([from_int, from_str], x), self.linked_names
        )
        result["occluder_names"] = from_list(
            lambda x: from_union([from_int, from_str], x), self.occluder_names
        )
        result["root_node_name"] = from_union([from_int, from_str], self.root_node_name)
        result["sead_handle0"] = to_class(PurpleSeadHandle0, self.sead_handle0)
        result["sead_handle1"] = to_class(PurpleSeadHandle0, self.sead_handle1)
        result["sub_world_datas"] = from_list(
            lambda x: to_class(Schema72, x), self.sub_world_datas
        )
        result["warp_name"] = from_union([from_int, from_str], self.warp_name)
        return result


class WorldV106_63_02_PC:
    def __init__(self, body, class_name, link_header, link_name, name):
        self.body = body
        self.class_name = class_name
        self.link_header = link_header
        self.link_name = link_name
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        body = WorldV106_63_02PCBody.from_dict(obj.get("body"))
        class_name = from_union([from_int, from_str], obj.get("class_name"))
        link_header = AnimationV1291_03_06PCLinkHeader.from_dict(obj.get("link_header"))
        link_name = from_union([from_none, from_int, from_str], obj.get("link_name"))
        name = from_union([from_int, from_str], obj.get("name"))
        return WorldV106_63_02_PC(body, class_name, link_header, link_name, name)

    def to_dict(self):
        result = {}
        result["body"] = to_class(WorldV106_63_02PCBody, self.body)
        result["class_name"] = from_union([from_int, from_str], self.class_name)
        result["link_header"] = to_class(
            AnimationV1291_03_06PCLinkHeader, self.link_header
        )
        if self.link_name is not None:
            result["link_name"] = from_union(
                [from_none, from_int, from_str], self.link_name
            )
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class Schema73:
    def __init__(
        self,
        grid_id,
        next_entry_of_resource,
        next_resource_of_entry,
        node_name,
        prev_resource_of_entry,
    ):
        self.grid_id = grid_id
        self.next_entry_of_resource = next_entry_of_resource
        self.next_resource_of_entry = next_resource_of_entry
        self.node_name = node_name
        self.prev_resource_of_entry = prev_resource_of_entry

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        grid_id = from_int(obj.get("grid_id"))
        next_entry_of_resource = from_int(obj.get("next_entry_of_resource"))
        next_resource_of_entry = from_int(obj.get("next_resource_of_entry"))
        node_name = from_union([from_int, from_str], obj.get("node_name"))
        prev_resource_of_entry = from_int(obj.get("prev_resource_of_entry"))
        return Schema73(
            grid_id,
            next_entry_of_resource,
            next_resource_of_entry,
            node_name,
            prev_resource_of_entry,
        )

    def to_dict(self):
        result = {}
        result["grid_id"] = from_int(self.grid_id)
        result["next_entry_of_resource"] = from_int(self.next_entry_of_resource)
        result["next_resource_of_entry"] = from_int(self.next_resource_of_entry)
        result["node_name"] = from_union([from_int, from_str], self.node_name)
        result["prev_resource_of_entry"] = from_int(self.prev_resource_of_entry)
        return result


class FluffySeadHandle0:
    def __init__(
        self, first_free, free_count, grid, inv_diag, p_max, p_min, sead_entries, size
    ):
        self.first_free = first_free
        self.free_count = free_count
        self.grid = grid
        self.inv_diag = inv_diag
        self.p_max = p_max
        self.p_min = p_min
        self.sead_entries = sead_entries
        self.size = size

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        first_free = from_int(obj.get("first_free"))
        free_count = from_int(obj.get("free_count"))
        grid = from_list(from_int, obj.get("grid"))
        inv_diag = from_list(from_float, obj.get("inv_diag"))
        p_max = from_list(from_float, obj.get("p_max"))
        p_min = from_list(from_float, obj.get("p_min"))
        sead_entries = from_list(Schema73.from_dict, obj.get("sead_entries"))
        size = from_list(lambda x: x, obj.get("size"))
        return FluffySeadHandle0(
            first_free, free_count, grid, inv_diag, p_max, p_min, sead_entries, size
        )

    def to_dict(self):
        result = {}
        result["first_free"] = from_int(self.first_free)
        result["free_count"] = from_int(self.free_count)
        result["grid"] = from_list(from_int, self.grid)
        result["inv_diag"] = from_list(to_float, self.inv_diag)
        result["p_max"] = from_list(to_float, self.p_max)
        result["p_min"] = from_list(to_float, self.p_min)
        result["sead_entries"] = from_list(
            lambda x: to_class(Schema73, x), self.sead_entries
        )
        result["size"] = from_list(lambda x: x, self.size)
        return result


class SubWorldRangeUnknown0:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        data = from_list(from_int, obj.get("data"))
        return SubWorldRangeUnknown0(data)

    def to_dict(self):
        result = {}
        result["data"] = from_list(from_int, self.data)
        return result


class FluffySubWorldRange:
    def __init__(self, data, unknown0_s, unknown1):
        self.data = data
        self.unknown0_s = unknown0_s
        self.unknown1 = unknown1

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        data = from_list(from_int, obj.get("data"))
        unknown0_s = from_list(SubWorldRangeUnknown0.from_dict, obj.get("unknown0s"))
        unknown1 = from_int(obj.get("unknown1"))
        return FluffySubWorldRange(data, unknown0_s, unknown1)

    def to_dict(self):
        result = {}
        result["data"] = from_list(from_int, self.data)
        result["unknown0s"] = from_list(
            lambda x: to_class(SubWorldRangeUnknown0, x), self.unknown0_s
        )
        result["unknown1"] = from_int(self.unknown1)
        return result


class Schema74:
    def __init__(
        self, data, sub_world_range, unknown0_s, unknown1_s, unknown2_s, unknown3_s
    ):
        self.data = data
        self.sub_world_range = sub_world_range
        self.unknown0_s = unknown0_s
        self.unknown1_s = unknown1_s
        self.unknown2_s = unknown2_s
        self.unknown3_s = unknown3_s

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        data = from_list(from_int, obj.get("data"))
        sub_world_range = FluffySubWorldRange.from_dict(obj.get("sub_world_range"))
        unknown0_s = from_list(from_int, obj.get("unknown0s"))
        unknown1_s = from_list(from_int, obj.get("unknown1s"))
        unknown2_s = from_list(from_int, obj.get("unknown2s"))
        unknown3_s = from_list(from_int, obj.get("unknown3s"))
        return Schema74(
            data, sub_world_range, unknown0_s, unknown1_s, unknown2_s, unknown3_s
        )

    def to_dict(self):
        result = {}
        result["data"] = from_list(from_int, self.data)
        result["sub_world_range"] = to_class(FluffySubWorldRange, self.sub_world_range)
        result["unknown0s"] = from_list(from_int, self.unknown0_s)
        result["unknown1s"] = from_list(from_int, self.unknown1_s)
        result["unknown2s"] = from_list(from_int, self.unknown2_s)
        result["unknown3s"] = from_list(from_int, self.unknown3_s)
        return result


class WorldV1291_03_06PCBody:
    def __init__(
        self,
        anim_frame_names,
        camera_zone_names,
        game_obj_name,
        graph_names,
        links,
        occluder_names,
        root_node_name,
        sead_handle0,
        sead_handle1,
        sub_world_datas,
        unk0_name,
        unk1_name,
        unk2_names,
        warp_name,
    ):
        self.anim_frame_names = anim_frame_names
        self.camera_zone_names = camera_zone_names
        self.game_obj_name = game_obj_name
        self.graph_names = graph_names
        self.links = links
        self.occluder_names = occluder_names
        self.root_node_name = root_node_name
        self.sead_handle0 = sead_handle0
        self.sead_handle1 = sead_handle1
        self.sub_world_datas = sub_world_datas
        self.unk0_name = unk0_name
        self.unk1_name = unk1_name
        self.unk2_names = unk2_names
        self.warp_name = warp_name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        anim_frame_names = from_list(
            lambda x: from_union([from_int, from_str], x), obj.get("anim_frame_names")
        )
        camera_zone_names = from_list(
            lambda x: from_union([from_int, from_str], x), obj.get("camera_zone_names")
        )
        game_obj_name = from_union([from_int, from_str], obj.get("game_obj_name"))
        graph_names = from_list(
            lambda x: from_union([from_int, from_str], x), obj.get("graph_names")
        )
        links = from_list(
            lambda x: from_union([from_int, from_str], x), obj.get("links")
        )
        occluder_names = from_list(
            lambda x: from_union([from_int, from_str], x), obj.get("occluder_names")
        )
        root_node_name = from_union([from_int, from_str], obj.get("root_node_name"))
        sead_handle0 = FluffySeadHandle0.from_dict(obj.get("sead_handle0"))
        sead_handle1 = FluffySeadHandle0.from_dict(obj.get("sead_handle1"))
        sub_world_datas = from_list(Schema74.from_dict, obj.get("sub_world_datas"))
        unk0_name = from_union([from_int, from_str], obj.get("unk0_name"))
        unk1_name = from_union([from_int, from_str], obj.get("unk1_name"))
        unk2_names = from_list(
            lambda x: from_union([from_int, from_str], x), obj.get("unk2_names")
        )
        warp_name = from_union([from_int, from_str], obj.get("warp_name"))
        return WorldV1291_03_06PCBody(
            anim_frame_names,
            camera_zone_names,
            game_obj_name,
            graph_names,
            links,
            occluder_names,
            root_node_name,
            sead_handle0,
            sead_handle1,
            sub_world_datas,
            unk0_name,
            unk1_name,
            unk2_names,
            warp_name,
        )

    def to_dict(self):
        result = {}
        result["anim_frame_names"] = from_list(
            lambda x: from_union([from_int, from_str], x), self.anim_frame_names
        )
        result["camera_zone_names"] = from_list(
            lambda x: from_union([from_int, from_str], x), self.camera_zone_names
        )
        result["game_obj_name"] = from_union([from_int, from_str], self.game_obj_name)
        result["graph_names"] = from_list(
            lambda x: from_union([from_int, from_str], x), self.graph_names
        )
        result["links"] = from_list(
            lambda x: from_union([from_int, from_str], x), self.links
        )
        result["occluder_names"] = from_list(
            lambda x: from_union([from_int, from_str], x), self.occluder_names
        )
        result["root_node_name"] = from_union([from_int, from_str], self.root_node_name)
        result["sead_handle0"] = to_class(FluffySeadHandle0, self.sead_handle0)
        result["sead_handle1"] = to_class(FluffySeadHandle0, self.sead_handle1)
        result["sub_world_datas"] = from_list(
            lambda x: to_class(Schema74, x), self.sub_world_datas
        )
        result["unk0_name"] = from_union([from_int, from_str], self.unk0_name)
        result["unk1_name"] = from_union([from_int, from_str], self.unk1_name)
        result["unk2_names"] = from_list(
            lambda x: from_union([from_int, from_str], x), self.unk2_names
        )
        result["warp_name"] = from_union([from_int, from_str], self.warp_name)
        return result


class WorldV1291_03_06_PC:
    def __init__(self, body, class_name, link_header, link_name, name):
        self.body = body
        self.class_name = class_name
        self.link_header = link_header
        self.link_name = link_name
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        body = WorldV1291_03_06PCBody.from_dict(obj.get("body"))
        class_name = from_union([from_int, from_str], obj.get("class_name"))
        link_header = AnimationV1291_03_06PCLinkHeader.from_dict(obj.get("link_header"))
        link_name = from_union([from_none, from_int, from_str], obj.get("link_name"))
        name = from_union([from_int, from_str], obj.get("name"))
        return WorldV1291_03_06_PC(body, class_name, link_header, link_name, name)

    def to_dict(self):
        result = {}
        result["body"] = to_class(WorldV1291_03_06PCBody, self.body)
        result["class_name"] = from_union([from_int, from_str], self.class_name)
        result["link_header"] = to_class(
            AnimationV1291_03_06PCLinkHeader, self.link_header
        )
        if self.link_name is not None:
            result["link_name"] = from_union(
                [from_none, from_int, from_str], self.link_name
            )
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class Schema75:
    def __init__(self, index, placeholder0, placeholder1, placeholder2, unknown4, zero):
        self.index = index
        self.placeholder0 = placeholder0
        self.placeholder1 = placeholder1
        self.placeholder2 = placeholder2
        self.unknown4 = unknown4
        self.zero = zero

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        index = from_int(obj.get("index"))
        placeholder0 = from_int(obj.get("placeholder0"))
        placeholder1 = from_int(obj.get("placeholder1"))
        placeholder2 = from_int(obj.get("placeholder2"))
        unknown4 = from_int(obj.get("unknown4"))
        zero = from_int(obj.get("zero"))
        return Schema75(index, placeholder0, placeholder1, placeholder2, unknown4, zero)

    def to_dict(self):
        result = {}
        result["index"] = from_int(self.index)
        result["placeholder0"] = from_int(self.placeholder0)
        result["placeholder1"] = from_int(self.placeholder1)
        result["placeholder2"] = from_int(self.placeholder2)
        result["unknown4"] = from_int(self.unknown4)
        result["zero"] = from_int(self.zero)
        return result


class WorldV1381_67_09PCBody:
    def __init__(
        self,
        game_obj_name,
        gen_world_name,
        indices0,
        indices1,
        material_anim_name,
        node_name0,
        node_name1,
        spline_graph_names,
        unknown0,
        unknown2_s,
        unknown3_s,
        unknown5_s,
        unused10_s,
        unused12_s,
        unused14,
        unused17_s,
        unused6_s,
        unused7_s,
        unused8_s,
        unused9_s,
        unuseds,
        warp_name,
    ):
        self.game_obj_name = game_obj_name
        self.gen_world_name = gen_world_name
        self.indices0 = indices0
        self.indices1 = indices1
        self.material_anim_name = material_anim_name
        self.node_name0 = node_name0
        self.node_name1 = node_name1
        self.spline_graph_names = spline_graph_names
        self.unknown0 = unknown0
        self.unknown2_s = unknown2_s
        self.unknown3_s = unknown3_s
        self.unknown5_s = unknown5_s
        self.unused10_s = unused10_s
        self.unused12_s = unused12_s
        self.unused14 = unused14
        self.unused17_s = unused17_s
        self.unused6_s = unused6_s
        self.unused7_s = unused7_s
        self.unused8_s = unused8_s
        self.unused9_s = unused9_s
        self.unuseds = unuseds
        self.warp_name = warp_name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        game_obj_name = from_union([from_int, from_str], obj.get("game_obj_name"))
        gen_world_name = from_union([from_int, from_str], obj.get("gen_world_name"))
        indices0 = from_list(from_int, obj.get("indices0"))
        indices1 = from_list(from_int, obj.get("indices1"))
        material_anim_name = from_list(
            lambda x: from_union([from_int, from_str], x), obj.get("material_anim_name")
        )
        node_name0 = from_union([from_int, from_str], obj.get("node_name0"))
        node_name1 = from_union([from_int, from_str], obj.get("node_name1"))
        spline_graph_names = from_list(
            lambda x: from_union([from_int, from_str], x), obj.get("spline_graph_names")
        )
        unknown0 = from_list(lambda x: from_list(from_float, x), obj.get("unknown0"))
        unknown2_s = from_list(Schema75.from_dict, obj.get("unknown2s"))
        unknown3_s = from_list(lambda x: from_list(from_float, x), obj.get("unknown3s"))
        unknown5_s = from_list(Schema75.from_dict, obj.get("unknown5s"))
        unused10_s = from_list(
            lambda x: from_union([from_int, from_str], x), obj.get("unused10s")
        )
        unused12_s = from_list(
            lambda x: from_union([from_int, from_str], x), obj.get("unused12s")
        )
        unused14 = from_union([from_int, from_str], obj.get("unused14"))
        unused17_s = from_list(from_int, obj.get("unused17s"))
        unused6_s = from_list(
            lambda x: from_union([from_int, from_str], x), obj.get("unused6s")
        )
        unused7_s = from_list(
            lambda x: from_union([from_int, from_str], x), obj.get("unused7s")
        )
        unused8_s = from_list(
            lambda x: from_union([from_int, from_str], x), obj.get("unused8s")
        )
        unused9_s = from_list(
            lambda x: from_union([from_int, from_str], x), obj.get("unused9s")
        )
        unuseds = from_list(from_int, obj.get("unuseds"))
        warp_name = from_union([from_int, from_str], obj.get("warp_name"))
        return WorldV1381_67_09PCBody(
            game_obj_name,
            gen_world_name,
            indices0,
            indices1,
            material_anim_name,
            node_name0,
            node_name1,
            spline_graph_names,
            unknown0,
            unknown2_s,
            unknown3_s,
            unknown5_s,
            unused10_s,
            unused12_s,
            unused14,
            unused17_s,
            unused6_s,
            unused7_s,
            unused8_s,
            unused9_s,
            unuseds,
            warp_name,
        )

    def to_dict(self):
        result = {}
        result["game_obj_name"] = from_union([from_int, from_str], self.game_obj_name)
        result["gen_world_name"] = from_union([from_int, from_str], self.gen_world_name)
        result["indices0"] = from_list(from_int, self.indices0)
        result["indices1"] = from_list(from_int, self.indices1)
        result["material_anim_name"] = from_list(
            lambda x: from_union([from_int, from_str], x), self.material_anim_name
        )
        result["node_name0"] = from_union([from_int, from_str], self.node_name0)
        result["node_name1"] = from_union([from_int, from_str], self.node_name1)
        result["spline_graph_names"] = from_list(
            lambda x: from_union([from_int, from_str], x), self.spline_graph_names
        )
        result["unknown0"] = from_list(lambda x: from_list(to_float, x), self.unknown0)
        result["unknown2s"] = from_list(
            lambda x: to_class(Schema75, x), self.unknown2_s
        )
        result["unknown3s"] = from_list(
            lambda x: from_list(to_float, x), self.unknown3_s
        )
        result["unknown5s"] = from_list(
            lambda x: to_class(Schema75, x), self.unknown5_s
        )
        result["unused10s"] = from_list(
            lambda x: from_union([from_int, from_str], x), self.unused10_s
        )
        result["unused12s"] = from_list(
            lambda x: from_union([from_int, from_str], x), self.unused12_s
        )
        result["unused14"] = from_union([from_int, from_str], self.unused14)
        result["unused17s"] = from_list(from_int, self.unused17_s)
        result["unused6s"] = from_list(
            lambda x: from_union([from_int, from_str], x), self.unused6_s
        )
        result["unused7s"] = from_list(
            lambda x: from_union([from_int, from_str], x), self.unused7_s
        )
        result["unused8s"] = from_list(
            lambda x: from_union([from_int, from_str], x), self.unused8_s
        )
        result["unused9s"] = from_list(
            lambda x: from_union([from_int, from_str], x), self.unused9_s
        )
        result["unuseds"] = from_list(from_int, self.unuseds)
        result["warp_name"] = from_union([from_int, from_str], self.warp_name)
        return result


class WorldV1381_67_09_PC:
    def __init__(self, body, class_name, link_header, link_name, name):
        self.body = body
        self.class_name = class_name
        self.link_header = link_header
        self.link_name = link_name
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        body = WorldV1381_67_09PCBody.from_dict(obj.get("body"))
        class_name = from_union([from_int, from_str], obj.get("class_name"))
        link_header = AnimationV1381_67_09PCLinkHeader.from_dict(obj.get("link_header"))
        link_name = from_union([from_none, from_int, from_str], obj.get("link_name"))
        name = from_union([from_int, from_str], obj.get("name"))
        return WorldV1381_67_09_PC(body, class_name, link_header, link_name, name)

    def to_dict(self):
        result = {}
        result["body"] = to_class(WorldV1381_67_09PCBody, self.body)
        result["class_name"] = from_union([from_int, from_str], self.class_name)
        result["link_header"] = to_class(
            AnimationV1381_67_09PCLinkHeader, self.link_header
        )
        if self.link_name is not None:
            result["link_name"] = from_union(
                [from_none, from_int, from_str], self.link_name
            )
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class World:
    def __init__(
        self, world_v1_06_63_02_pc, world_v1_291_03_06_pc, world_v1_381_67_09_pc
    ):
        self.world_v1_06_63_02_pc = world_v1_06_63_02_pc
        self.world_v1_291_03_06_pc = world_v1_291_03_06_pc
        self.world_v1_381_67_09_pc = world_v1_381_67_09_pc

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        world_v1_06_63_02_pc = from_union(
            [WorldV106_63_02_PC.from_dict, from_none], obj.get("WorldV1_06_63_02PC")
        )
        world_v1_291_03_06_pc = from_union(
            [WorldV1291_03_06_PC.from_dict, from_none], obj.get("WorldV1_291_03_06PC")
        )
        world_v1_381_67_09_pc = from_union(
            [WorldV1381_67_09_PC.from_dict, from_none], obj.get("WorldV1_381_67_09PC")
        )
        return World(world_v1_06_63_02_pc, world_v1_291_03_06_pc, world_v1_381_67_09_pc)

    def to_dict(self):
        result = {}
        if self.world_v1_06_63_02_pc is not None:
            result["WorldV1_06_63_02PC"] = from_union(
                [lambda x: to_class(WorldV106_63_02_PC, x), from_none],
                self.world_v1_06_63_02_pc,
            )
        if self.world_v1_291_03_06_pc is not None:
            result["WorldV1_291_03_06PC"] = from_union(
                [lambda x: to_class(WorldV1291_03_06_PC, x), from_none],
                self.world_v1_291_03_06_pc,
            )
        if self.world_v1_381_67_09_pc is not None:
            result["WorldV1_381_67_09PC"] = from_union(
                [lambda x: to_class(WorldV1381_67_09_PC, x), from_none],
                self.world_v1_381_67_09_pc,
            )
        return result


class UUIDPairElement:
    def __init__(self, uuid0, uuid1):
        self.uuid0 = uuid0
        self.uuid1 = uuid1

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        uuid0 = from_int(obj.get("uuid0"))
        uuid1 = from_int(obj.get("uuid1"))
        return UUIDPairElement(uuid0, uuid1)

    def to_dict(self):
        result = {}
        result["uuid0"] = from_int(self.uuid0)
        result["uuid1"] = from_int(self.uuid1)
        return result


class WorldRefV1381_67_09PCBody:
    def __init__(
        self,
        game_obj_name,
        gen_world_name,
        init_script,
        mats,
        node_name0,
        node_name1,
        node_name2,
        point_a,
        point_b,
        unused14,
        unused17_s,
        unuseds,
        uuid_pairs,
        warp_name,
        zero,
    ):
        self.game_obj_name = game_obj_name
        self.gen_world_name = gen_world_name
        self.init_script = init_script
        self.mats = mats
        self.node_name0 = node_name0
        self.node_name1 = node_name1
        self.node_name2 = node_name2
        self.point_a = point_a
        self.point_b = point_b
        self.unused14 = unused14
        self.unused17_s = unused17_s
        self.unuseds = unuseds
        self.uuid_pairs = uuid_pairs
        self.warp_name = warp_name
        self.zero = zero

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        game_obj_name = from_union([from_int, from_str], obj.get("game_obj_name"))
        gen_world_name = from_union([from_int, from_str], obj.get("gen_world_name"))
        init_script = from_str(obj.get("init_script"))
        mats = from_list(
            lambda x: from_list(lambda x: from_list(from_float, x), x), obj.get("mats")
        )
        node_name0 = from_union([from_int, from_str], obj.get("node_name0"))
        node_name1 = from_union([from_int, from_str], obj.get("node_name1"))
        node_name2 = from_list(
            lambda x: from_union([from_int, from_str], x), obj.get("node_name2")
        )
        point_a = from_list(from_float, obj.get("point_a"))
        point_b = from_list(from_float, obj.get("point_b"))
        unused14 = from_union([from_int, from_str], obj.get("unused14"))
        unused17_s = from_list(from_int, obj.get("unused17s"))
        unuseds = from_list(from_int, obj.get("unuseds"))
        uuid_pairs = from_list(UUIDPairElement.from_dict, obj.get("uuid_pairs"))
        warp_name = from_union([from_int, from_str], obj.get("warp_name"))
        zero = from_int(obj.get("zero"))
        return WorldRefV1381_67_09PCBody(
            game_obj_name,
            gen_world_name,
            init_script,
            mats,
            node_name0,
            node_name1,
            node_name2,
            point_a,
            point_b,
            unused14,
            unused17_s,
            unuseds,
            uuid_pairs,
            warp_name,
            zero,
        )

    def to_dict(self):
        result = {}
        result["game_obj_name"] = from_union([from_int, from_str], self.game_obj_name)
        result["gen_world_name"] = from_union([from_int, from_str], self.gen_world_name)
        result["init_script"] = from_str(self.init_script)
        result["mats"] = from_list(
            lambda x: from_list(lambda x: from_list(to_float, x), x), self.mats
        )
        result["node_name0"] = from_union([from_int, from_str], self.node_name0)
        result["node_name1"] = from_union([from_int, from_str], self.node_name1)
        result["node_name2"] = from_list(
            lambda x: from_union([from_int, from_str], x), self.node_name2
        )
        result["point_a"] = from_list(to_float, self.point_a)
        result["point_b"] = from_list(to_float, self.point_b)
        result["unused14"] = from_union([from_int, from_str], self.unused14)
        result["unused17s"] = from_list(from_int, self.unused17_s)
        result["unuseds"] = from_list(from_int, self.unuseds)
        result["uuid_pairs"] = from_list(
            lambda x: to_class(UUIDPairElement, x), self.uuid_pairs
        )
        result["warp_name"] = from_union([from_int, from_str], self.warp_name)
        result["zero"] = from_int(self.zero)
        return result


class WorldRefV1381_67_09_PC:
    def __init__(self, body, class_name, link_header, link_name, name):
        self.body = body
        self.class_name = class_name
        self.link_header = link_header
        self.link_name = link_name
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        body = WorldRefV1381_67_09PCBody.from_dict(obj.get("body"))
        class_name = from_union([from_int, from_str], obj.get("class_name"))
        link_header = CameraV1381_67_09PCLinkHeader.from_dict(obj.get("link_header"))
        link_name = from_union([from_none, from_int, from_str], obj.get("link_name"))
        name = from_union([from_int, from_str], obj.get("name"))
        return WorldRefV1381_67_09_PC(body, class_name, link_header, link_name, name)

    def to_dict(self):
        result = {}
        result["body"] = to_class(WorldRefV1381_67_09PCBody, self.body)
        result["class_name"] = from_union([from_int, from_str], self.class_name)
        result["link_header"] = to_class(
            CameraV1381_67_09PCLinkHeader, self.link_header
        )
        if self.link_name is not None:
            result["link_name"] = from_union(
                [from_none, from_int, from_str], self.link_name
            )
        result["name"] = from_union([from_int, from_str], self.name)
        return result


class WorldRef:
    def __init__(self, world_ref_v1_381_67_09_pc):
        self.world_ref_v1_381_67_09_pc = world_ref_v1_381_67_09_pc

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        world_ref_v1_381_67_09_pc = WorldRefV1381_67_09_PC.from_dict(
            obj.get("WorldRefV1_381_67_09PC")
        )
        return WorldRef(world_ref_v1_381_67_09_pc)

    def to_dict(self):
        result = {}
        result["WorldRefV1_381_67_09PC"] = to_class(
            WorldRefV1381_67_09_PC, self.world_ref_v1_381_67_09_pc
        )
        return result


class Class:
    def __init__(
        self,
        animation,
        animation_graph,
        animation_graph_override,
        anim_frame,
        area_light,
        binary,
        bitmap,
        camera,
        camera_zone,
        collision_vol,
        collision_vol_data,
        conductor,
        decal,
        dialog_event,
        entity,
        flare,
        flare_data,
        fog_volume,
        fonts,
        fx_particles,
        fx_particles_data,
        game_obj,
        gen_world,
        graph,
        gw_road,
        h_fog,
        h_fog_data,
        hull_spline_zone,
        light,
        light_data,
        light_probe_volume,
        lod,
        lod_data,
        mass_instancing_volume,
        material,
        material_anim,
        material_collect,
        material_obj,
        mesh,
        mesh_data,
        net_bing_obj,
        node,
        occluder,
        omni,
        omni_data,
        override,
        particles,
        particles_data,
        prefab,
        prefab_ref,
        reflection_probe,
        rot_shape,
        rot_shape_data,
        rtc,
        shader,
        skel,
        skin,
        skin_data,
        sound,
        sound_event,
        special_effect_node,
        spline,
        spline_graph,
        spline_zone,
        surface,
        surface_datas,
        terrain,
        texture,
        txt,
        user_define,
        user_define_script,
        warp,
        world,
        world_ref,
        x_ref_node,
    ):
        self.animation = animation
        self.animation_graph = animation_graph
        self.animation_graph_override = animation_graph_override
        self.anim_frame = anim_frame
        self.area_light = area_light
        self.binary = binary
        self.bitmap = bitmap
        self.camera = camera
        self.camera_zone = camera_zone
        self.collision_vol = collision_vol
        self.collision_vol_data = collision_vol_data
        self.conductor = conductor
        self.decal = decal
        self.dialog_event = dialog_event
        self.entity = entity
        self.flare = flare
        self.flare_data = flare_data
        self.fog_volume = fog_volume
        self.fonts = fonts
        self.fx_particles = fx_particles
        self.fx_particles_data = fx_particles_data
        self.game_obj = game_obj
        self.gen_world = gen_world
        self.graph = graph
        self.gw_road = gw_road
        self.h_fog = h_fog
        self.h_fog_data = h_fog_data
        self.hull_spline_zone = hull_spline_zone
        self.light = light
        self.light_data = light_data
        self.light_probe_volume = light_probe_volume
        self.lod = lod
        self.lod_data = lod_data
        self.mass_instancing_volume = mass_instancing_volume
        self.material = material
        self.material_anim = material_anim
        self.material_collect = material_collect
        self.material_obj = material_obj
        self.mesh = mesh
        self.mesh_data = mesh_data
        self.net_bing_obj = net_bing_obj
        self.node = node
        self.occluder = occluder
        self.omni = omni
        self.omni_data = omni_data
        self.override = override
        self.particles = particles
        self.particles_data = particles_data
        self.prefab = prefab
        self.prefab_ref = prefab_ref
        self.reflection_probe = reflection_probe
        self.rot_shape = rot_shape
        self.rot_shape_data = rot_shape_data
        self.rtc = rtc
        self.shader = shader
        self.skel = skel
        self.skin = skin
        self.skin_data = skin_data
        self.sound = sound
        self.sound_event = sound_event
        self.special_effect_node = special_effect_node
        self.spline = spline
        self.spline_graph = spline_graph
        self.spline_zone = spline_zone
        self.surface = surface
        self.surface_datas = surface_datas
        self.terrain = terrain
        self.texture = texture
        self.txt = txt
        self.user_define = user_define
        self.user_define_script = user_define_script
        self.warp = warp
        self.world = world
        self.world_ref = world_ref
        self.x_ref_node = x_ref_node

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        animation = from_union([Animation.from_dict, from_none], obj.get("Animation"))
        animation_graph = from_union(
            [lambda x: from_dict(lambda x: x, x), from_none], obj.get("AnimationGraph")
        )
        animation_graph_override = from_union(
            [lambda x: from_dict(lambda x: x, x), from_none],
            obj.get("AnimationGraphOverride"),
        )
        anim_frame = from_union(
            [lambda x: from_dict(lambda x: x, x), from_none], obj.get("AnimFrame")
        )
        area_light = from_union(
            [lambda x: from_dict(lambda x: x, x), from_none], obj.get("AreaLight")
        )
        binary = from_union([Binary.from_dict, from_none], obj.get("Binary"))
        bitmap = from_union([Bitmap.from_dict, from_none], obj.get("Bitmap"))
        camera = from_union([Camera.from_dict, from_none], obj.get("Camera"))
        camera_zone = from_union(
            [CameraZone.from_dict, from_none], obj.get("CameraZone")
        )
        collision_vol = from_union(
            [CollisionVol.from_dict, from_none], obj.get("CollisionVol")
        )
        collision_vol_data = from_union(
            [lambda x: from_dict(lambda x: x, x), from_none],
            obj.get("CollisionVolData"),
        )
        conductor = from_union(
            [lambda x: from_dict(lambda x: x, x), from_none], obj.get("Conductor")
        )
        decal = from_union(
            [lambda x: from_dict(lambda x: x, x), from_none], obj.get("Decal")
        )
        dialog_event = from_union(
            [lambda x: from_dict(lambda x: x, x), from_none], obj.get("DialogEvent")
        )
        entity = from_union(
            [lambda x: from_dict(lambda x: x, x), from_none], obj.get("Entity")
        )
        flare = from_union(
            [lambda x: from_dict(lambda x: x, x), from_none], obj.get("Flare")
        )
        flare_data = from_union(
            [lambda x: from_dict(lambda x: x, x), from_none], obj.get("FlareData")
        )
        fog_volume = from_union(
            [lambda x: from_dict(lambda x: x, x), from_none], obj.get("FogVolume")
        )
        fonts = from_union([Fonts.from_dict, from_none], obj.get("Fonts"))
        fx_particles = from_union(
            [lambda x: from_dict(lambda x: x, x), from_none], obj.get("FxParticles")
        )
        fx_particles_data = from_union(
            [lambda x: from_dict(lambda x: x, x), from_none], obj.get("FxParticlesData")
        )
        game_obj = from_union([GameObj.from_dict, from_none], obj.get("GameObj"))
        gen_world = from_union([GenWorld.from_dict, from_none], obj.get("GenWorld"))
        graph = from_union(
            [lambda x: from_dict(lambda x: x, x), from_none], obj.get("Graph")
        )
        gw_road = from_union([GwRoad.from_dict, from_none], obj.get("GwRoad"))
        h_fog = from_union(
            [lambda x: from_dict(lambda x: x, x), from_none], obj.get("HFog")
        )
        h_fog_data = from_union(
            [lambda x: from_dict(lambda x: x, x), from_none], obj.get("HFogData")
        )
        hull_spline_zone = from_union(
            [lambda x: from_dict(lambda x: x, x), from_none], obj.get("HullSplineZone")
        )
        light = from_union([Light.from_dict, from_none], obj.get("Light"))
        light_data = from_union([LightData.from_dict, from_none], obj.get("LightData"))
        light_probe_volume = from_union(
            [lambda x: from_dict(lambda x: x, x), from_none],
            obj.get("LightProbeVolume"),
        )
        lod = from_union([Lod.from_dict, from_none], obj.get("Lod"))
        lod_data = from_union([LodData.from_dict, from_none], obj.get("LodData"))
        mass_instancing_volume = from_union(
            [lambda x: from_dict(lambda x: x, x), from_none],
            obj.get("MassInstancingVolume"),
        )
        material = from_union([Material.from_dict, from_none], obj.get("Material"))
        material_anim = from_union(
            [MaterialAnim.from_dict, from_none], obj.get("MaterialAnim")
        )
        material_collect = from_union(
            [lambda x: from_dict(lambda x: x, x), from_none], obj.get("MaterialCollect")
        )
        material_obj = from_union(
            [MaterialObj.from_dict, from_none], obj.get("MaterialObj")
        )
        mesh = from_union([Mesh.from_dict, from_none], obj.get("Mesh"))
        mesh_data = from_union([MeshData.from_dict, from_none], obj.get("MeshData"))
        net_bing_obj = from_union(
            [lambda x: from_dict(lambda x: x, x), from_none], obj.get("NetBingObj")
        )
        node = from_union([Node.from_dict, from_none], obj.get("Node"))
        occluder = from_union(
            [lambda x: from_dict(lambda x: x, x), from_none], obj.get("Occluder")
        )
        omni = from_union([Omni.from_dict, from_none], obj.get("Omni"))
        omni_data = from_union(
            [lambda x: from_dict(lambda x: x, x), from_none], obj.get("OmniData")
        )
        override = from_union(
            [lambda x: from_dict(lambda x: x, x), from_none], obj.get("Override")
        )
        particles = from_union([Particles.from_dict, from_none], obj.get("Particles"))
        particles_data = from_union(
            [ParticlesData.from_dict, from_none], obj.get("ParticlesData")
        )
        prefab = from_union(
            [lambda x: from_dict(lambda x: x, x), from_none], obj.get("Prefab")
        )
        prefab_ref = from_union(
            [lambda x: from_dict(lambda x: x, x), from_none], obj.get("PrefabRef")
        )
        reflection_probe = from_union(
            [lambda x: from_dict(lambda x: x, x), from_none], obj.get("ReflectionProbe")
        )
        rot_shape = from_union([RotShape.from_dict, from_none], obj.get("RotShape"))
        rot_shape_data = from_union(
            [RotShapeData.from_dict, from_none], obj.get("RotShapeData")
        )
        rtc = from_union([RTC.from_dict, from_none], obj.get("Rtc"))
        shader = from_union(
            [lambda x: from_dict(lambda x: x, x), from_none], obj.get("Shader")
        )
        skel = from_union([Skel.from_dict, from_none], obj.get("Skel"))
        skin = from_union([Skin.from_dict, from_none], obj.get("Skin"))
        skin_data = from_union(
            [lambda x: from_dict(lambda x: x, x), from_none], obj.get("SkinData")
        )
        sound = from_union([Sound.from_dict, from_none], obj.get("Sound"))
        sound_event = from_union(
            [lambda x: from_dict(lambda x: x, x), from_none], obj.get("SoundEvent")
        )
        special_effect_node = from_union(
            [lambda x: from_dict(lambda x: x, x), from_none],
            obj.get("SpecialEffectNode"),
        )
        spline = from_union([Spline.from_dict, from_none], obj.get("Spline"))
        spline_graph = from_union(
            [SplineGraph.from_dict, from_none], obj.get("SplineGraph")
        )
        spline_zone = from_union(
            [lambda x: from_dict(lambda x: x, x), from_none], obj.get("SplineZone")
        )
        surface = from_union([Surface.from_dict, from_none], obj.get("Surface"))
        surface_datas = from_union(
            [SurfaceDatas.from_dict, from_none], obj.get("SurfaceDatas")
        )
        terrain = from_union(
            [lambda x: from_dict(lambda x: x, x), from_none], obj.get("Terrain")
        )
        texture = from_union(
            [lambda x: from_dict(lambda x: x, x), from_none], obj.get("Texture")
        )
        txt = from_union(
            [lambda x: from_dict(lambda x: x, x), from_none], obj.get("Txt")
        )
        user_define = from_union(
            [UserDefine.from_dict, from_none], obj.get("UserDefine")
        )
        user_define_script = from_union(
            [lambda x: from_dict(lambda x: x, x), from_none],
            obj.get("UserDefineScript"),
        )
        warp = from_union([Warp.from_dict, from_none], obj.get("Warp"))
        world = from_union([World.from_dict, from_none], obj.get("World"))
        world_ref = from_union([WorldRef.from_dict, from_none], obj.get("WorldRef"))
        x_ref_node = from_union(
            [lambda x: from_dict(lambda x: x, x), from_none], obj.get("XRefNode")
        )
        return Class(
            animation,
            animation_graph,
            animation_graph_override,
            anim_frame,
            area_light,
            binary,
            bitmap,
            camera,
            camera_zone,
            collision_vol,
            collision_vol_data,
            conductor,
            decal,
            dialog_event,
            entity,
            flare,
            flare_data,
            fog_volume,
            fonts,
            fx_particles,
            fx_particles_data,
            game_obj,
            gen_world,
            graph,
            gw_road,
            h_fog,
            h_fog_data,
            hull_spline_zone,
            light,
            light_data,
            light_probe_volume,
            lod,
            lod_data,
            mass_instancing_volume,
            material,
            material_anim,
            material_collect,
            material_obj,
            mesh,
            mesh_data,
            net_bing_obj,
            node,
            occluder,
            omni,
            omni_data,
            override,
            particles,
            particles_data,
            prefab,
            prefab_ref,
            reflection_probe,
            rot_shape,
            rot_shape_data,
            rtc,
            shader,
            skel,
            skin,
            skin_data,
            sound,
            sound_event,
            special_effect_node,
            spline,
            spline_graph,
            spline_zone,
            surface,
            surface_datas,
            terrain,
            texture,
            txt,
            user_define,
            user_define_script,
            warp,
            world,
            world_ref,
            x_ref_node,
        )

    def to_dict(self):
        result = {}
        if self.animation is not None:
            result["Animation"] = from_union(
                [lambda x: to_class(Animation, x), from_none], self.animation
            )
        if self.animation_graph is not None:
            result["AnimationGraph"] = from_union(
                [lambda x: from_dict(lambda x: x, x), from_none], self.animation_graph
            )
        if self.animation_graph_override is not None:
            result["AnimationGraphOverride"] = from_union(
                [lambda x: from_dict(lambda x: x, x), from_none],
                self.animation_graph_override,
            )
        if self.anim_frame is not None:
            result["AnimFrame"] = from_union(
                [lambda x: from_dict(lambda x: x, x), from_none], self.anim_frame
            )
        if self.area_light is not None:
            result["AreaLight"] = from_union(
                [lambda x: from_dict(lambda x: x, x), from_none], self.area_light
            )
        if self.binary is not None:
            result["Binary"] = from_union(
                [lambda x: to_class(Binary, x), from_none], self.binary
            )
        if self.bitmap is not None:
            result["Bitmap"] = from_union(
                [lambda x: to_class(Bitmap, x), from_none], self.bitmap
            )
        if self.camera is not None:
            result["Camera"] = from_union(
                [lambda x: to_class(Camera, x), from_none], self.camera
            )
        if self.camera_zone is not None:
            result["CameraZone"] = from_union(
                [lambda x: to_class(CameraZone, x), from_none], self.camera_zone
            )
        if self.collision_vol is not None:
            result["CollisionVol"] = from_union(
                [lambda x: to_class(CollisionVol, x), from_none], self.collision_vol
            )
        if self.collision_vol_data is not None:
            result["CollisionVolData"] = from_union(
                [lambda x: from_dict(lambda x: x, x), from_none],
                self.collision_vol_data,
            )
        if self.conductor is not None:
            result["Conductor"] = from_union(
                [lambda x: from_dict(lambda x: x, x), from_none], self.conductor
            )
        if self.decal is not None:
            result["Decal"] = from_union(
                [lambda x: from_dict(lambda x: x, x), from_none], self.decal
            )
        if self.dialog_event is not None:
            result["DialogEvent"] = from_union(
                [lambda x: from_dict(lambda x: x, x), from_none], self.dialog_event
            )
        if self.entity is not None:
            result["Entity"] = from_union(
                [lambda x: from_dict(lambda x: x, x), from_none], self.entity
            )
        if self.flare is not None:
            result["Flare"] = from_union(
                [lambda x: from_dict(lambda x: x, x), from_none], self.flare
            )
        if self.flare_data is not None:
            result["FlareData"] = from_union(
                [lambda x: from_dict(lambda x: x, x), from_none], self.flare_data
            )
        if self.fog_volume is not None:
            result["FogVolume"] = from_union(
                [lambda x: from_dict(lambda x: x, x), from_none], self.fog_volume
            )
        if self.fonts is not None:
            result["Fonts"] = from_union(
                [lambda x: to_class(Fonts, x), from_none], self.fonts
            )
        if self.fx_particles is not None:
            result["FxParticles"] = from_union(
                [lambda x: from_dict(lambda x: x, x), from_none], self.fx_particles
            )
        if self.fx_particles_data is not None:
            result["FxParticlesData"] = from_union(
                [lambda x: from_dict(lambda x: x, x), from_none], self.fx_particles_data
            )
        if self.game_obj is not None:
            result["GameObj"] = from_union(
                [lambda x: to_class(GameObj, x), from_none], self.game_obj
            )
        if self.gen_world is not None:
            result["GenWorld"] = from_union(
                [lambda x: to_class(GenWorld, x), from_none], self.gen_world
            )
        if self.graph is not None:
            result["Graph"] = from_union(
                [lambda x: from_dict(lambda x: x, x), from_none], self.graph
            )
        if self.gw_road is not None:
            result["GwRoad"] = from_union(
                [lambda x: to_class(GwRoad, x), from_none], self.gw_road
            )
        if self.h_fog is not None:
            result["HFog"] = from_union(
                [lambda x: from_dict(lambda x: x, x), from_none], self.h_fog
            )
        if self.h_fog_data is not None:
            result["HFogData"] = from_union(
                [lambda x: from_dict(lambda x: x, x), from_none], self.h_fog_data
            )
        if self.hull_spline_zone is not None:
            result["HullSplineZone"] = from_union(
                [lambda x: from_dict(lambda x: x, x), from_none], self.hull_spline_zone
            )
        if self.light is not None:
            result["Light"] = from_union(
                [lambda x: to_class(Light, x), from_none], self.light
            )
        if self.light_data is not None:
            result["LightData"] = from_union(
                [lambda x: to_class(LightData, x), from_none], self.light_data
            )
        if self.light_probe_volume is not None:
            result["LightProbeVolume"] = from_union(
                [lambda x: from_dict(lambda x: x, x), from_none],
                self.light_probe_volume,
            )
        if self.lod is not None:
            result["Lod"] = from_union(
                [lambda x: to_class(Lod, x), from_none], self.lod
            )
        if self.lod_data is not None:
            result["LodData"] = from_union(
                [lambda x: to_class(LodData, x), from_none], self.lod_data
            )
        if self.mass_instancing_volume is not None:
            result["MassInstancingVolume"] = from_union(
                [lambda x: from_dict(lambda x: x, x), from_none],
                self.mass_instancing_volume,
            )
        if self.material is not None:
            result["Material"] = from_union(
                [lambda x: to_class(Material, x), from_none], self.material
            )
        if self.material_anim is not None:
            result["MaterialAnim"] = from_union(
                [lambda x: to_class(MaterialAnim, x), from_none], self.material_anim
            )
        if self.material_collect is not None:
            result["MaterialCollect"] = from_union(
                [lambda x: from_dict(lambda x: x, x), from_none], self.material_collect
            )
        if self.material_obj is not None:
            result["MaterialObj"] = from_union(
                [lambda x: to_class(MaterialObj, x), from_none], self.material_obj
            )
        if self.mesh is not None:
            result["Mesh"] = from_union(
                [lambda x: to_class(Mesh, x), from_none], self.mesh
            )
        if self.mesh_data is not None:
            result["MeshData"] = from_union(
                [lambda x: to_class(MeshData, x), from_none], self.mesh_data
            )
        if self.net_bing_obj is not None:
            result["NetBingObj"] = from_union(
                [lambda x: from_dict(lambda x: x, x), from_none], self.net_bing_obj
            )
        if self.node is not None:
            result["Node"] = from_union(
                [lambda x: to_class(Node, x), from_none], self.node
            )
        if self.occluder is not None:
            result["Occluder"] = from_union(
                [lambda x: from_dict(lambda x: x, x), from_none], self.occluder
            )
        if self.omni is not None:
            result["Omni"] = from_union(
                [lambda x: to_class(Omni, x), from_none], self.omni
            )
        if self.omni_data is not None:
            result["OmniData"] = from_union(
                [lambda x: from_dict(lambda x: x, x), from_none], self.omni_data
            )
        if self.override is not None:
            result["Override"] = from_union(
                [lambda x: from_dict(lambda x: x, x), from_none], self.override
            )
        if self.particles is not None:
            result["Particles"] = from_union(
                [lambda x: to_class(Particles, x), from_none], self.particles
            )
        if self.particles_data is not None:
            result["ParticlesData"] = from_union(
                [lambda x: to_class(ParticlesData, x), from_none], self.particles_data
            )
        if self.prefab is not None:
            result["Prefab"] = from_union(
                [lambda x: from_dict(lambda x: x, x), from_none], self.prefab
            )
        if self.prefab_ref is not None:
            result["PrefabRef"] = from_union(
                [lambda x: from_dict(lambda x: x, x), from_none], self.prefab_ref
            )
        if self.reflection_probe is not None:
            result["ReflectionProbe"] = from_union(
                [lambda x: from_dict(lambda x: x, x), from_none], self.reflection_probe
            )
        if self.rot_shape is not None:
            result["RotShape"] = from_union(
                [lambda x: to_class(RotShape, x), from_none], self.rot_shape
            )
        if self.rot_shape_data is not None:
            result["RotShapeData"] = from_union(
                [lambda x: to_class(RotShapeData, x), from_none], self.rot_shape_data
            )
        if self.rtc is not None:
            result["Rtc"] = from_union(
                [lambda x: to_class(RTC, x), from_none], self.rtc
            )
        if self.shader is not None:
            result["Shader"] = from_union(
                [lambda x: from_dict(lambda x: x, x), from_none], self.shader
            )
        if self.skel is not None:
            result["Skel"] = from_union(
                [lambda x: to_class(Skel, x), from_none], self.skel
            )
        if self.skin is not None:
            result["Skin"] = from_union(
                [lambda x: to_class(Skin, x), from_none], self.skin
            )
        if self.skin_data is not None:
            result["SkinData"] = from_union(
                [lambda x: from_dict(lambda x: x, x), from_none], self.skin_data
            )
        if self.sound is not None:
            result["Sound"] = from_union(
                [lambda x: to_class(Sound, x), from_none], self.sound
            )
        if self.sound_event is not None:
            result["SoundEvent"] = from_union(
                [lambda x: from_dict(lambda x: x, x), from_none], self.sound_event
            )
        if self.special_effect_node is not None:
            result["SpecialEffectNode"] = from_union(
                [lambda x: from_dict(lambda x: x, x), from_none],
                self.special_effect_node,
            )
        if self.spline is not None:
            result["Spline"] = from_union(
                [lambda x: to_class(Spline, x), from_none], self.spline
            )
        if self.spline_graph is not None:
            result["SplineGraph"] = from_union(
                [lambda x: to_class(SplineGraph, x), from_none], self.spline_graph
            )
        if self.spline_zone is not None:
            result["SplineZone"] = from_union(
                [lambda x: from_dict(lambda x: x, x), from_none], self.spline_zone
            )
        if self.surface is not None:
            result["Surface"] = from_union(
                [lambda x: to_class(Surface, x), from_none], self.surface
            )
        if self.surface_datas is not None:
            result["SurfaceDatas"] = from_union(
                [lambda x: to_class(SurfaceDatas, x), from_none], self.surface_datas
            )
        if self.terrain is not None:
            result["Terrain"] = from_union(
                [lambda x: from_dict(lambda x: x, x), from_none], self.terrain
            )
        if self.texture is not None:
            result["Texture"] = from_union(
                [lambda x: from_dict(lambda x: x, x), from_none], self.texture
            )
        if self.txt is not None:
            result["Txt"] = from_union(
                [lambda x: from_dict(lambda x: x, x), from_none], self.txt
            )
        if self.user_define is not None:
            result["UserDefine"] = from_union(
                [lambda x: to_class(UserDefine, x), from_none], self.user_define
            )
        if self.user_define_script is not None:
            result["UserDefineScript"] = from_union(
                [lambda x: from_dict(lambda x: x, x), from_none],
                self.user_define_script,
            )
        if self.warp is not None:
            result["Warp"] = from_union(
                [lambda x: to_class(Warp, x), from_none], self.warp
            )
        if self.world is not None:
            result["World"] = from_union(
                [lambda x: to_class(World, x), from_none], self.world
            )
        if self.world_ref is not None:
            result["WorldRef"] = from_union(
                [lambda x: to_class(WorldRef, x), from_none], self.world_ref
            )
        if self.x_ref_node is not None:
            result["XRefNode"] = from_union(
                [lambda x: from_dict(lambda x: x, x), from_none], self.x_ref_node
            )
        return result


class Platform(Enum):
    GAME_CUBE = "GameCube"
    MACI386 = "Maci386"
    MAC_PPC = "MacPPC"
    PC = "PC"
    PS2 = "PS2"
    PS3 = "PS3"
    PS4 = "PS4"
    PS5 = "PS5"
    PSP = "PSP"
    SWITCH = "Switch"
    UWP = "UWP"
    WII = "Wii"
    XBOX = "Xbox"
    XBOX360 = "Xbox360"
    XBOX_ONE = "XboxOne"


class BffClassHeader:
    def __init__(self, platform, version):
        self.platform = platform
        self.version = version

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        platform = Platform(obj.get("platform"))
        version = from_str(obj.get("version"))
        return BffClassHeader(platform, version)

    def to_dict(self):
        result = {}
        result["platform"] = to_enum(Platform, self.platform)
        result["version"] = from_str(self.version)
        return result


class BffClass:
    def __init__(self, bff_class_class, header):
        self.bff_class_class = bff_class_class
        self.header = header

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        bff_class_class = Class.from_dict(obj.get("class"))
        header = BffClassHeader.from_dict(obj.get("header"))
        return BffClass(bff_class_class, header)

    def to_dict(self):
        result = {}
        result["class"] = to_class(Class, self.bff_class_class)
        result["header"] = to_class(BffClassHeader, self.header)
        return result


def bff_class_from_dict(s):
    return BffClass.from_dict(s)


def bff_class_to_dict(x):
    return to_class(BffClass, x)
