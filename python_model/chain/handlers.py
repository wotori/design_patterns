from abc import ABC, abstractmethod
from typing import Any, Optional


class Handler(ABC):
    """
    Интерфейс Обработчика объявляет метод построения цепочки обработчиков. Он
    также объявляет метод для выполнения запроса.
    """

    @abstractmethod
    def set_next(self, handler):
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


class AbstractHandler(Handler):
    """
    Поведение цепочки по умолчанию может быть реализовано внутри базового класса
    обработчика.
    """

    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)

        return None


"""
Все Конкретные Обработчики либо обрабатывают запрос, либо передают его
следующему обработчику в цепочке.
"""

import math


class MoneySpliter(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request >= 1000:
            frac, whole = math.modf(request / 1000)
            frac = frac.__round__(2)
            if frac >= 0.05:
                print(f"на выдачу {int(whole)} банкноты по 1000 и одна банкнота {int(frac * 1000)}")
                return True
        else:
            return False


class BelowThousand(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request < 1000:
            return f"Введённая сумма меньше тысячи: {request}"
        else:
            return super().handle(request)
