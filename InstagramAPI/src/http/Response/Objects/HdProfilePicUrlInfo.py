from InstagramAPI.src.http.Response.Response import Response


class HdProfilePicUrlInfo(Response):
    def __init__(self):
        self._types = {}

        self.url = None
        self.width = None
        self.height = None
