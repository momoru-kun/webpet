class Configuration:
    __shared_state = {
        'debug': True,
        'router': None,
        'templates_dir': None,
        'middleware': []
    }
    def __new__(cls, *args, **kwargs):
        obj = super(Configuration, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls.__shared_state
        return obj
