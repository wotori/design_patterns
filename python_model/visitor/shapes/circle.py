from python_model.visitor.component import Component
from python_model.visitor.visitor import Visitor


class Circle(Component):

    def accept(self, visitor: Visitor):
        visitor.create_circle()

    def create_circle(self):
        self.circle = "Circle"
