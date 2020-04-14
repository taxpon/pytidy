from pytidy.decorators import component, autowired_cls

import sys

if sys.version_info[1] >= 7:
    from dataclasses import dataclass

    @component
    class C:
        def get(self):
            return "c"

    @autowired_cls
    @dataclass
    class D:
        c: C

        def get(self):
            return self.c.get()

    def test_class_is_inserted_to_dataclass():
        obj = D()
        another = D()
        assert obj.get() == "c"
        assert id(obj.c) == id(another.c)
