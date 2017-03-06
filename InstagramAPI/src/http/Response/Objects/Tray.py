from InstagramAPI.src.http.Response.Objects.Item import Item
from InstagramAPI.src.http.Response.Response import Response


class Tray(Response):
    def __init__(self):
        self._types = {}

        self._types["id"] = str
        self.id = None
        self._types["items"] = [Item]
        self.items = None
        self.user = None
        self.can_reply = None
        self.expiring_at = None
        self.seen_ranked_position = None
        self.seen = None
        self.latest_reel_media = None
        self.ranked_position = None
        self.is_nux = None
        self.muted = None
