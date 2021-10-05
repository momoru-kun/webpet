# Request

There is one class `HTTPRequests` taht is a simple wrapper on HTTP request

### Fields:
- `method` - stores current method
- `path` - stores path
- `query` - stores querystring in dict format
- `headers` - stores headers from client if dict
- `client` - stores client IP and Port
- `server` - stores server IP and Port
- `body` - stores request body (if presented)