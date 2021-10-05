"""Module defines basic URL class
    TODO: parsing url params
    TODO: Regex URL
"""

class URL:
    """Describes route data (uri and view correspond with that uri)
    """
    def __init__(self, path, view):
        self.path = path
        self.view = view

    def check_match(self, path: str) -> bool:
        return path == self.path

    def __str__(self):
        return f"<URL to: {self.path}>"
