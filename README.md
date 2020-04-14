[![Build Status](https://api.travis-ci.com/taxpon/pytidy.svg?branch=develop)](https://travis-ci.com/taxpon/pytidy) [![Coverage Status](https://coveralls.io/repos/github/taxpon/pytidy/badge.svg?branch=develop)](https://coveralls.io/github/taxpon/pytidy?branch=develop)
# Pytidy
A type hint based dependency injection library for python language (+3.6). While there are already several DI libraries for python, this library is inspired by Java Spring and aims to provide similar interface and functionality to Java Spring.

Supports Python 3.7 and 3.8.

# Usage
Super simple. Attach `@component` decorator to any classes which need to be injected in somewhere constructor, and attach `@autowired` decorator to constructors which need dependency injection.

```python
from pytidy.decorators import component, autowired


@component
class Hello:
    def say(self):
        print("Hello")


class Injected:
    @autowired
    def __init__(self, instance: Hello):
        self.instance = instance

    def say_proxy(self):
        self.instance.say()


a = Injected()
a.say_proxy()
```

Also supports dataclass of Python3.7+.

```python
from dataclasses import dataclass
from pytidy.decorators import component, autowired_cls


@component
class Hello:
    def say(self):
        print("Hello")


@autowired_cls
@dataclass
class Injected:
    instance: Hello

    def say_proxy(self):
        self.instance.say()


a = Injected()
a.say_proxy()
```

# License
MIT