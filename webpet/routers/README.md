# Routers

Here we have two classes:
- `HTTPRouter` implements simple router that links urls with [correspond views](../views/README.md)
- `URL` implements simple URL (links path with view)

*If you want implement router by yoursetl you need to inherit from `base_http_router.BaseHTTPRouter`*

### Usage

```python
    router = HttpRouter([
        URL('/path1', view1),
        URL('/path2', view2),
        # ...
    ])
```