from python_model.visitor.component import Component
from random import randint


class Rectangle(Component):
    """
    Каждый Конкретный Компонент должен реализовать метод accept таким образом,
    чтобы он вызывал метод посетителя, соответствующий классу компонента.
    """

    def accept(self, visitor) -> None:
        print("программа создаёт прямоугольник...")
        visitor.create_rectangle(self)
        visitor.rectangle.draw()
        visitor.rectangle.getPerimetr()
        visitor.rectangle.getArea()

    def draw(self):
        self.rectangle_scale = {"x": randint(1, 100), "y": randint(1, 100)}

    def getPerimetr(self):
        self.rectangle_perimetr = (self.rectangle_scale["x"] + self.rectangle_scale["y"]) * 2

    def getArea(self):
        self.rectangle_area = (self.rectangle_scale["x"] + self.rectangle_scale["y"]) ** 2
