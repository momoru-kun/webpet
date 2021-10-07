class BaseResponse:
    def __init__(self, body='', content_type='text/plain', status_code=200):
        self.body = body
        self.content_type = content_type
        self.status_code = status_code
        self.headers = {
            'Content-Type': self.content_type,
            'X-Framework': 'WebPet'
        }

    async def get_body(self):
        raise NotImplementedError("Don't use base classes for building app")