"""The module defines the base class of the router which we must follow when developing routers
    You cannot use this router for routing. Use instead http_router.HTTPRouter
"""
class BaseHTTPRouter:
    def __init__(self, routes: list):
        self.routes = routes

    def check_match(self, path: str):
        raise NotImplementedError("Don't use base classes for building app")
