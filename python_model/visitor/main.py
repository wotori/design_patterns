from python_model.visitor.shapes.circle import Circle
from python_model.visitor.client_code import client_code
from python_model.visitor.shapes.rectangle import Rectangle
from python_model.visitor.shapes.triangle import Triangle
from python_model.visitor.visitor import ConcreteVisitor1

if __name__ == "__main__":
    components = [Circle(), Rectangle(), Triangle()]

    print("Клиентский код работает со всеми посетителями через базовый интерфейс посетителей:")
    visitor1 = ConcreteVisitor1()
    client_code(components, visitor1)

    print("Размер прямоугольника: ", visitor1.rectangle.rectangle_scale)
    print("Периметр прямоугольника: ", visitor1.rectangle.rectangle_perimetr)
    print("Площадь прямоугольника: ", visitor1.rectangle.rectangle_area)
