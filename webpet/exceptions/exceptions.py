
class HTTPException(Exception):
    pass


class MethodNotAllowed(HTTPException):
    status_code = 405
    body = b"<h1> Method not allowed! </h1>"


class NotFound(HTTPException):
    status_code = 404
    body = b"<h1> Not Found! </h1>"
