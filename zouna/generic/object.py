from .resource import Resource
from ..bff.io import Box, Sphere


class Object(Resource):
    b_box: Box = (
        Box(
            matrix=[
                [1.0, 0.0, 0.0, 0.0],
                [0.0, 1.0, 0.0, 0.0],
                [0.0, 0.0, 1.0, 0.0],
            ],
            scale=1.0,
            vec=[1.0, 1.0, 1.0],
        ),
    )
    b_sphere: Sphere
    data_name: str
    fade_out_dist: float
    flags: int
