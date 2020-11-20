from __future__ import annotations
from abc import ABC, abstractmethod

from py._path.common import Visitor


class Component(ABC):
    """
    Интерфейс Компонента объявляет метод accept, который в качестве аргумента
    может получать любой объект, реализующий интерфейс посетителя.
    """

    @abstractmethod
    def accept(self, visitor: Visitor) -> None:
        pass
