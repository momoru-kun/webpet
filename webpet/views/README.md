# Views

For this time implemented 2 types of HTTP Views:

- `View` - simple View
- `TemplateView` - view for render HTML template (Jinja2 syntax - watch [docs](https://jinja.palletsprojects.com/en/3.0.x/))
- `LongPoolView` - view for longpooling that have method `open` which opens connection

If you want send response you need to use `self.send()` method that requires `HTTPResponse` (with `LongPoolView` you also need to open connection and send status and headers)

If you need to get [HTTPRequest](../request/README.md) use `self.request` field

## Simple usage

```python
class IndexView(TemplateView):
    template_name = 'index.html'


class HelloView(View)

    async def get(self):
        name = self.request.query.get('name')
        if name is None:
            await self.send(
                HTTPResponse(
                    f'<h1>Hello World, {name}</h1>',
                    content_type='text/html'
                )
            )
            return

        await self.send(
            HTTPResponse(
                f'<h1>Hello World, Anon!</h1>',
                content_type='text/html'
            )
        )

    async def post(self):
        name = json.loads(self.request.body).get('name')

        if name is None:
            await self.send(
                HTTPResponse(
                    f'<h1>Hello World, {name}</h1>',
                    content_type='text/html'
                )
            )
            return

        await self.send(
            HTTPResponse(
                f'<h1>Hello World, Anon!</h1>',
                content_type='text/html'
            )
        )
```