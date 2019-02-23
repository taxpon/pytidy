[![Build Status](https://travis-ci.org/taxpon/pytidy.svg?branch=develop)](https://travis-ci.org/taxpon/pytidy)
# Pytidy
A type hint based dependency injection library for python language (+3.6). While there are already several DI libraries for python, this library is inspired by Java Spring and aims to provide similar interface and functionality to Java Spring.   

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

# License
MIT