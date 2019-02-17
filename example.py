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

b = Injected()
b.say_proxy()

print(a.instance == b.instance)
