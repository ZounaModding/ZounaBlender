from .resource import Resource
from ..bff.io import Box, Sphere


class Object(Resource):
    b_box: Box
    b_sphere: Sphere
    data_name: str
    fade_out_dist: float
    flags: int
