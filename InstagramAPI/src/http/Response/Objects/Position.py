from InstagramAPI.src.http.Response.Response import Response


class Position(Response):
    def __init__(self):
        self._types = {}

        self.pos1 = None
        self.pos2 = None
