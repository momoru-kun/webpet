class BaseResponse:
    def __init__(self, body, content_type, status_code=200):
        self.body = body
        self.content_type = content_type
        self.status_code = status_code
        self.headers = []

        self.setHeader('Content-Type', self.content_type)

    def setHeader(self, header: str, value: str):
        self.headers.append(
            (header.encode('utf-8'), value.encode('utf-8'))
        )

    async def get_body(self):
        raise NotImplementedError("Don't use base classes for building app")