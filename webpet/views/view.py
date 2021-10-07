from webpet.views.base_view import BaseView
from webpet.response import HTMLTemplateResponse, HTTPResponse
from webpet.exceptions import TemplateNotFoundError

HTTP_METHODS_AVAIL = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']

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

    async def options(self):
        """Handle OPTIONS method"""
        response = HTTPResponse()
        response.headers['Allow'] = ', '.join(self._allowed_methods())
        response.headers['Content-Length'] = '0'

        await self.send(response)

    def _allowed_methods(self):
        return [m.upper() for m in HTTP_METHODS_AVAIL if hasattr(self, m)]


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