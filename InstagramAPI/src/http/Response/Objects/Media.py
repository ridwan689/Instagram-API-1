from InstagramAPI.src.http.Response.Response import Response


class Media(Response):
    def __init__(self):
        self._types = {}

        self.image = None
        self._types["id"] = str
        self.id = None
