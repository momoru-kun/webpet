from .base_middleware import BaseMiddleware

class XFrameOptionsMiddleware(BaseMiddleware):

    def __init__(self, policy='DENY'):
        self.policy = policy

    async def before_start(self, request, status_code, headers):
        if headers.get('X-Frame-Options') is not None:
            return

        headers['X-Frame-Options'] = self.policy

        return headers