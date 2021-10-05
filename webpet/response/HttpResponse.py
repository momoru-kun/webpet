class HTTPResponse():
    def __init__(self, body, status_code=200, content_type='text/plain'):
        self.body = body
        self.content_type = content_type
        self.status_code = status_code
        self.headers = []

        self.setHeader('Content-Type', self.content_type)

    def setHeader(self, header: str, value: str):
        self.headers.append(
            (header.encode('latin-1'), value.encode('latin-1'))
        )

    def get_body(self):
        return self.body.encode('latin-1')
