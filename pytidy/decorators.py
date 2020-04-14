from typing import Dict, Type

from pytidy.registry import Registry

_reg: Registry = Registry.get_instance()


def autowired(func):
    # @functools.wraps
    def wrapped(*args, **kwargs):
        arg_defs: Dict[str, Type] = func.__annotations__
        for arg_name, klass in arg_defs.items():
            if arg_name not in "return":
                kwargs[arg_name] = _reg.get(klass)
        return func(*args, **kwargs)

    return wrapped


def autowired_cls(cls):
    setattr(cls, "__init__", autowired(getattr(cls, "__init__")))
    return cls


def component(cls):
    _reg.register(cls)
    return cls
