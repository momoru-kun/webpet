from urllib.parse import parse_qs


class HTTPRequest:
    def __init__(self, scope: dict) -> None:
        self.method = scope['method']
        self.path = scope['path']
        self.query = parse_qs(scope['query_string'], encoding="utf-8")
        self.headers = dict(scope['headers'])
        self.client = scope['client']
        self.server = scope['server']

    def __str__(self) -> str:
        return f"<HTTPRequest: {self.client} {self.method} {self.path}>"