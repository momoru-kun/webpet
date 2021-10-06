class HTTPException(Exception):
    status_code = 500
    body = b'<h1> Unhandeled HTTP Exception </h1>'


class MethodNotAllowed(HTTPException):
    status_code = 405
    body = b"<h1> Method not allowed! </h1>"


class NotFound(HTTPException):
    status_code = 404
    body = b"<h1> Not Found! </h1>"


class ConfigurationError(Exception):
    hint = ''


class TemplateNotFoundError(ConfigurationError):
    hint = 'Check template name in View'


class TemplateDirNotSettedError(ConfigurationError):
    hint = 'Please, set templatesdir in webpet.conf.Configuration'
