from typing import List

from python_model.visitor.component import Component
from python_model.visitor.shapes.circle import Circle
from python_model.visitor.shapes.rectangle import Rectangle
from python_model.visitor.shapes.triangle import Triangle
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


if __name__ == "__main__":
    components = [Circle(), Rectangle(), Triangle()]

    print("The client code works with all visitors via the base Visitor interface:")
    # visitor1 = ConcreteVisitor1()
    # client_code(components, visitor1)
    #
    # print("It allows the same client code to work with different types of visitors:")
    # visitor2 = ConcreteVisitor2()
    # client_code(components, visitor2)
