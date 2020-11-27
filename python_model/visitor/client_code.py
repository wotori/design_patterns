from typing import List

from python_model.visitor.component import Component
from python_model.visitor.visitor import Visitor


def client_code(components: List[Component], visitor: Visitor) -> None:
    """
    Клиентский код может выполнять операции посетителя над любым набором
    элементов, не выясняя их конкретных классов. Операция принятия направляет
    вызов к соответствующей операции в объекте посетителя.
    """

    # ...
    for component in components:
        component.accept(visitor)
    # ...
