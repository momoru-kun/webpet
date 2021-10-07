from webpet.conf import Configuration
from webpet.middleware.handler import MiddlewareHandler
from . import exceptions

import traceback


def get_traceback(traceback):
    return traceback.replace('\n', '<br>')


async def open(status_code, send):
    try:
        await send({
            "type": "http.response.start",
            "status": status_code,
            "headers": [(b'Content-Type', b'text/html')]
        })
    except ValueError:
        pass


async def handler(request, send):
    conf = Configuration()
    view = conf.router.get_view(request.path)
    if not hasattr(view, request.method.lower()):
        raise exceptions.MethodNotAllowed()

    middleware_handler = MiddlewareHandler(request, send)
    await middleware_handler.after_receive(view)
    """try:
        view = conf.router.get_view(request.path)
        if not hasattr(view, request.method.lower()):
            raise exceptions.MethodNotAllowed()

        middleware_handler = MiddleWareHandler(request, send)
        await middleware_handler.after_receive(view)

    except (exceptions.HTTPException) as e:
        await open(e.status_code, send)

        await send({
            "type": "http.response.body",
            "body": e.body
        })
    except (exceptions.ConfigurationError) as e:
        await open(500, send)

        trace = get_traceback(traceback.format_exc()) if conf.debug else ''
        body = f'<h1>Internal server error!</h1>'
        if conf.debug:
            body += f'<hr><p>{trace}</p><p><b>Hint:</b> {e.hint}</p>'

        await send({
            "type": "http.response.body",
            "body": body.encode('utf-8')
        })

    except Exception as e:
        await open(500, send)

        trace = get_traceback(traceback.format_exc()) if conf.debug else ''
        body = f'<h1>Internal server error!</h1>'
        if conf.debug:
            body += f'<hr><p>{trace}</p>'

        await send({
            "type": "http.response.body",
            "body": body.encode('utf-8')
        })"""
