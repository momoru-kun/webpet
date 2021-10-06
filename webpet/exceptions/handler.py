from webpet.conf import Configuration
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
    try:
        view = conf.router.get_view(request.path)
        await getattr(view(request, send), request.method.lower())()
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
        })
