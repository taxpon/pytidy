from pytidy.registry import Registry
from pytidy.error import RetrievingError, RegistrationError
from pytest import fixture, raises


class Dummy:
    pass


@fixture()
def registry():
    yield Registry.get_instance()
    Registry.clear_all()


def test_register_failure(registry):
    registry.register(Dummy)
    with raises(RegistrationError):
        registry.register(Dummy)


def test_get_failure_not_registered(registry):
    with raises(RetrievingError):
        registry.get(Dummy)


def test_get_failure_none_registered(registry):
    registry.register(Dummy)
    Registry._Registry__klasses["tests.test_registry.Dummy"] = None
    with raises(RetrievingError):
        registry.get(Dummy)
