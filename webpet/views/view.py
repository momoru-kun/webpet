from webpet.exceptions import exceptions
from webpet.request.HttpRequest import HTTPRequest
from webpet.views.base_view import BaseView


class View(BaseView):
    async def send(self, http_response):
        await self.asgi_send({
            "type": "http.response.start",
            "status": http_response.status_code,
            "headers": http_response.headers,
        })

        await self.asgi_send({
            "type": "http.response.body",
            "body": http_response.get_body()
        })
