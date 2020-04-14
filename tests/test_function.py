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


class B2:
    @autowired
    def __init__(self, a: A) -> None:  # Has return type "None"
        self.a = a

    def get(self):
        return self.a.get()


def test_object_insertion():
    obj = B()
    another = B()
    assert obj.get() == "a"
    assert id(obj.a) == id(another.a)


def test_return_type_none():
    obj = B2()
    another = B()
    assert obj.get() == "a"
    assert id(obj.a) == id(another.a)
