from . import exceptions

import traceback


def get_traceback(traceback):
    return traceback.replace('\n', '<br>')


async def handler(request, send, router):
    try:
        view = router.get_view(request.path)
        await getattr(view(request, send), request.method.lower())()
    except (exceptions.HTTPException) as e:
        try:
            await send({
                "type": "http.response.start",
                "status": e.status_code,
                "headers": [(b'Content-Type', b'text/html')]
            })
        except ValueError:
            pass

        await send({
            "type": "http.response.body",
            "body": e.body
        })
    except Exception as e:
        trace = get_traceback(traceback.format_exc())
        try:
            await send({
                "type": "http.response.start",
                "status": 500,
                "headers": [(b'Content-Type', b'text/html')]
            })
        except ValueError:
            pass

        await send({
            "type": "http.response.body",
            "body": (
                f'<h1>Internal server error!</h1> <p> {trace} </p>'
            ).encode('latin-1')
        })
