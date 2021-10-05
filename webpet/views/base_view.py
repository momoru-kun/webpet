from webpet.request.HttpRequest import HTTPRequest
from webpet.exceptions import exceptions

class BaseView:
    def __init__(self, request: HTTPRequest, asgi_send):
        self.request = request
        self.asgi_send = asgi_send

    async def send(self, response):
        raise NotImplementedError("Don't use base classes for building app")

    async def get(self):
        raise exceptions.MethodNotAllowed()

    async def head(self):
        raise exceptions.MethodNotAllowed()

    async def post(self):
        raise exceptions.MethodNotAllowed()

    async def put(self):
        raise exceptions.MethodNotAllowed()

    async def connect(self):
        raise exceptions.MethodNotAllowed()

    async def options(self):
        raise exceptions.MethodNotAllowed()

    async def trace(self):
        raise exceptions.MethodNotAllowed()

    async def delete(self):
        raise exceptions.MethodNotAllowed()

    async def patch(self):
        raise exceptions.MethodNotAllowed()

