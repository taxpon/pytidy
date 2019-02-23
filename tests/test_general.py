from pytidy.decorators import autowired, component


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


def test_properly_working():
    b = B()
    assert b.get() == "a"
