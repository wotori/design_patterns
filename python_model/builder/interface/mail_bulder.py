from __future__ import annotations
from abc import ABC, abstractmethod, abstractproperty
from typing import Any


class EmailBuilder(ABC):
    """
    Интерфейс строителя.
    Объявляет создающие методы для различных частей объектов почтового сообщения.
    """

    @abstractproperty
    def mail(self) -> None:
        pass

    @abstractmethod
    def subject(self) -> None:
        pass

    @abstractmethod
    def content(self) -> None:
        pass

    @abstractmethod
    def recipient(self) -> None:
        pass

    @abstractmethod
    def recipient_copy(self) -> None:
        pass

    @abstractmethod
    def sender(self) -> None:
        pass

    @abstractmethod
    def build(self) -> None:
        pass
