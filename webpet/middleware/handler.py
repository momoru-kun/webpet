from webpet.conf import Configuration
from copy import deepcopy


class MiddlewareHandler:
    def __init__(self, request, asgi_send):
        self.request = deepcopy(request)
        self.asgi_send = asgi_send

    def _get_asgi_headers(self, headers):
        print(headers)
        bytes_headers = {key.encode('utf-8'): value.encode('utf-8') for key, value in headers.items()}
        return tuple(bytes_headers.items())

    async def send(self, data):
        for middleware in Configuration().middleware:

            if data['type'] == 'http.response.start':
                headers = await middleware.before_start(self.request, data['status'], data['headers'])
                data['headers'] = self._get_asgi_headers(headers)

            elif data['type'] == 'http.response.body':
                await middleware.before_body(self.request, data['body'])

        await self.asgi_send(data)

    async def after_receive(self, view):
        print("After receive hook")
        for middleware in Configuration().middleware:
            self.request = await middleware.after_receive(self.request)
        method = getattr(
            view(self.request, self.send),
            self.request.method.lower()
        )
        await method()