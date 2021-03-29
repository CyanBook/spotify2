import re

from .albums import AlbumMethods
from .artists import ArtistMethods
from .tracks import TrackMethods


class Methods(AlbumMethods, ArtistMethods, TrackMethods):
    @staticmethod
    def get_id(s: str) -> str:
        if m := re.search("(?!.*/).+", s):
            return m[0].split("?")[0]
        else:
            raise ValueError("ID not valid")

    @staticmethod
    def wrapper(**kwargs):
        return {k: v for k, v in kwargs.items() if v is not None}
