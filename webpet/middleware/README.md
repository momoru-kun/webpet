# Middlewares

Middleware is a set of request, response start, send response body hooks

In webpet already implemented current middlewares:

- `BaseMiddleware`: bare-bone middleware to build middlewares
- `XFrameOptionsMiddleware`: middleware that contols clickjacking. Inits with policy param. Default is DENY

## Hooks

There is three async hooks:

- `after_receive(request)` - calls after we have HTTPRequest and before loadgin View. With
- `before_start(request, status_code, headers)` - calls before webpet sends response headers to client
- `before_body(request, body)` - calls before webpet sends response body to client

## Usecase

Let's write simple middleware that count time between get request and send response

```python
from webpet.middleware import BaseMiddleware
from datetime import datetime


class TimeMiddleware(BaseMiddleware):
    def after_receive(request):
        request.request_time = datetime.now()

    def before_body(request):
        print(f"Response time: {datetime.now() - request.request_time}")
```

## Initialization

To init middleware in your project, you need to initialize it in configuration

```python
from webpet.conf import Configuration

Configuration().middleware.append(TimeMiddleware())
```

## **And yes, webpet calls middlewares in FIFO order**
e.g. we have 2 middlewares: `[Middleware1(), Middleware2()]`
First webpet call Middleware1 and then Middleware2
