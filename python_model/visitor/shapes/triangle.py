from python_model.visitor.component import Component


class Triangle(Component):
    """
    То же самое здесь: visitConcreteComponentB => Triangle
    """

    def accept(self, visitor):
        visitor.create_triangle(self)

    def create_triangle(self) -> str:
        return "Triangle"
