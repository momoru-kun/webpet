class BaseMiddleware:

    async def after_receive(self, request):
        return request

    async def before_start(self, request, status_code, headers):
        pass

    async def before_body(self, request, body):
        pass