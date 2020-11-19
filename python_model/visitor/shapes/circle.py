from python_model.visitor.component import Component
from python_model.visitor.visitor import Visitor


class Circle(Component):
    """
    То же самое здесь: visitConcreteComponentB => ConcreteComponentB
    """

    def accept(self, visitor: Visitor):
        visitor.create_circle(self)

    def create_circle(self) -> str:
        return "Circle"
