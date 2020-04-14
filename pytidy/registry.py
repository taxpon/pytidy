from logging import getLogger
from typing import ClassVar, Dict, Optional, Type, TypeVar

from pytidy.error import RegistrationError, RetrievingError

logger = getLogger(__file__)


T = TypeVar("T")


class Registry:
    __instance: Optional["Registry"] = None
    __klasses: ClassVar[Dict[str, object]] = {}

    @staticmethod
    def get_instance() -> "Registry":
        if Registry.__instance is None:
            Registry.__instance = Registry()
        return Registry.__instance

    @staticmethod
    def clear_all():
        Registry.__klasses = {}

    def __init__(self):
        # TODO: Prevent users from direct invoke
        pass

    def register(self, klass: Type):
        name: str = self.__get_name(klass)
        if name in self.__klasses:
            raise RegistrationError(
                "Already registered class: {}".format(name))
        obj = klass()
        self.__klasses[name] = obj
        logger.debug("{} is successfully registered to registry".format(name))

    def get(self, klass: Type[T]) -> T:
        name: str = self.__get_name(klass)
        if name not in self.__klasses:
            raise RetrievingError("{} is not registered".format(name))

        obj: object = self.__klasses[name]
        if not isinstance(obj, klass):
            raise RetrievingError(
                "Registered object is not compatible with {}".format(name)
            )
        return obj

    def __get_name(self, klass: Type) -> str:
        return ".".join((klass.__module__, klass.__name__))
