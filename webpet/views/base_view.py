from webpet.request.HttpRequest import HTTPRequest


class BaseView:
    def __init__(self, request: HTTPRequest, asgi_send):
        self.request = request
        self.asgi_send = asgi_send

    async def send(self, response):
        raise NotImplementedError("Don't use base classes for building app")
