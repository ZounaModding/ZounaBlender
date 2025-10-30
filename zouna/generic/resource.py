from ..bff.io import Platform
from ...common.constants import Game


class Resource:
    file_path: str = None
    file_name: str = "DefaultFileName"
    name: str = "DefaultName"
    platform: Platform = None
    game: Game = None
    data: bytes = None
    data_ext: str = None
