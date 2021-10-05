from urllib.parse import non_hierarchical

from webpet.exceptions.exceptions import NotFound
from webpet.views.view import View

from .base_http_router import BaseHTTPRouter


class HTTPRouter(BaseHTTPRouter):
    """Impliments Simple Router that return View of mached url
        or raise 404/405
    """

    def get_view(self, url_path: str) -> View:
        """Search view by it's URL

        Args:
            url_path (str): url

        Raises:
            NotFound: Returns if we haven't url in router

        Returns:
            View: view corresponding to the path
        """
        for route in self.routes:
            if route.check_match(url_path):
                return route.view
        raise NotFound
