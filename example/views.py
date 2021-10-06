from webpet.response import HTTPResponse
from webpet.views import View, LongPoolView, TemplateView

import asyncio
import random
import json

# Let's play with template view
class Index(TemplateView):
    template_name = 'index.html'


# Let's play with simple View and watch how webpet handle exceptions
class TestRaise(View):

    async def get(self):
        raise ValueError()

# Let's play with long pooling
class TestLong(LongPoolView):

    async def get(self):
        await self.open(status_code=200, headers=[(b'Content-type', b'application/json')])
        data = []
        ticks = 0
        while True:
            ticks += 1
            number = random.randint(0, 1000)
            data.append(number)
            if number >= 500:
                await self.send(HTTPResponse(
                    json.dumps({
                        'data': data,
                        'ticks': ticks
                    })
                ))
                break
            else:
                await asyncio.sleep(1)