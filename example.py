from pytidy.decorators import component, autowired


@component
class A:
    def get(self):
        return "a"


class B:
    @autowired
    def __init__(self, a: A):
        self.a = a

    def get(self):
        return self.a.get()


b = B()
print(b.get())  # a
