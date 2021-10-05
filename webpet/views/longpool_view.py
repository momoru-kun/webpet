
from webpet.exceptions import exceptions
from webpet.views.base_view import BaseView


class LongPoolView(BaseView):
    more_data = False

    async def open(self, status_code, headers):
        await self.asgi_send({
            "type": "http.response.start",
            "status": status_code,
            "headers": headers,
        })

    async def send(self, response):
        print(response.get_body())
        if not self.more_data:
            await self.asgi_send({
                "type": "http.response.body",
                "body": response.get_body(),
                "more_body": False
            })