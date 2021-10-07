from webpet.response.base_response import BaseResponse


class HTTPResponse(BaseResponse):
    def __init__(self, body='', status_code=200, content_type='text/plain'):
        super(HTTPResponse, self).__init__(body, content_type, status_code)

    async def get_body(self):
        return self.body.encode('utf-8')
