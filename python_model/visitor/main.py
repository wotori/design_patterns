from python_model.visitor.shapes.circle import Circle
from python_model.visitor.shapes.client_code import client_code
from python_model.visitor.shapes.rectangle import Rectangle
from python_model.visitor.shapes.triangle import Triangle
from python_model.visitor.visitor import ConcreteVisitor1

if __name__ == "__main__":
    components = [Circle(), Rectangle(), Triangle()]

    print("The client code works with all visitors via the base Visitor interface:")
    visitor1 = ConcreteVisitor1()
    client_code(components, visitor1)
    print(visitor1.circle, visitor1.rectangle, visitor1.triangle)
