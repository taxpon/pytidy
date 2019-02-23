from typing import Dict, Type

from pytidy.registry import Registry

_reg: Registry = Registry.get_instance()


def autowired(func):
    # @functools.wraps
    def wrapped(*args, **kwargs):
        arg_defs: Dict[str, Type] = func.__annotations__
        for arg_name, klass in arg_defs.items():
            kwargs[arg_name] = _reg.get(klass)
        return func(*args, **kwargs)
    return wrapped


def component(cls):
    _reg.register(cls)
    return cls
