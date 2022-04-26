import abc
import sys


class UIElement(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            hasattr(subclass, 'handle_events')
            and callable(subclass.handle_events) and
            hasattr(subclass, 'draw')
            and callable(subclass.draw)
            or NotImplemented
        )

    @abc.abstractmethod
    def __init__(self) -> None:
        pass
    
    @abc.abstractmethod
    def handle_events(self, events):
        pass

    @abc.abstractmethod
    def get_rect(self):
        pass

