from urllib.parse import parse_qs


class HTTPRequest:
    def __init__(self, scope: dict, body: bytes) -> None:
        self.method = scope['method']
        self.path = scope['path']
        self.query = parse_qs(scope['query_string'], encoding="utf-8")
        self.query = { key.decode(): [value.decode() for value in val] for key, val in self.query.items() }
        self.headers = dict(scope['headers'])
        self.client = scope['client']
        self.server = scope['server']
        self.body = body.decode('utf-8')

    def __str__(self) -> str:
        return f"<HTTPRequest: {self.client} {self.method} {self.path}>"
