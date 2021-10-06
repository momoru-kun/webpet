from webpet.views.base_view import BaseView
from webpet.response import HTMLTemplateResponse
from webpet.exceptions import TemplateNotFoundError

class View(BaseView):
    async def send(self, http_response):
        """Send instance of HttpResponse to client and close connection

        Args:
            http_response (HttpResponse): Response
        """
        await self.asgi_send({
            "type": "http.response.start",
            "status": http_response.status_code,
            "headers": http_response.headers,
        })

        body = await http_response.get_body()
        await self.asgi_send({
            "type": "http.response.body",
            "body": body
        })


class TemplateView(View):
    """Simple View that return template on get
        Pushes request to template context so you can use it
    Raises:
        TemplateNotFoundError
    """
    template_name = None

    async def get(self):
        """Simply returns rendered templates

        Raises:
            TemplateNotFoundError: raises when you don't set template name in view or it's incorrect
        """
        if self.template_name is None:
            raise TemplateNotFoundError()
        await self.send(HTMLTemplateResponse({'request': self.request}, self.template_name))