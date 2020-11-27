from python_model.visitor.component import Component
from python_model.visitor.visitor import Visitor


class Triangle(Component):
    """
    То же самое здесь: visitConcreteComponentB => Triangle
    """

    def accept(self, visitor: Visitor):
        print("программа создаёт триугольник...")
        visitor.create_triangle(self)

    def create_triangle(self):
        self.triangle = "Triangle"
