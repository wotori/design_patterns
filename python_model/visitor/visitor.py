from abc import ABC


class Visitor(ABC):
    """
    Интерфейс Посетителя объявляет набор методов посещения, соответствующих
    классам компонентов. Сигнатура метода посещения позволяет посетителю
    определить конкретный класс компонента, с которым он имеет дело.
    """

    def create_rectangle(self, element) -> None:
        self.rectangle = "rectangle"

    def create_triangle(self, element) -> None:
        self.triangle = "triangle"

    def create_circle(self):
        self.circle = "Circle"


"""
Конкретные Посетители реализуют несколько версий одного и того же алгоритма,
которые могут работать со всеми классами конкретных компонентов.

Максимальную выгоду от паттерна Посетитель вы почувствуете, используя его со
сложной структурой объектов, такой как дерево Компоновщика. В этом случае было
бы полезно хранить некоторое промежуточное состояние алгоритма при выполнении
методов посетителя над различными объектами структуры.
"""


class ConcreteVisitor1(Visitor):
    def visit_concrete_component_a(self, element) -> None:
        print(f"{element.exclusive_method_of_concrete_component_a()} + ConcreteVisitor1")

    def visit_concrete_component_b(self, element) -> None:
        print(f"{element.special_method_of_concrete_component_b()} + ConcreteVisitor1")

# class ConcreteVisitor2(Visitor):
#     def visit_concrete_component_a(self, element) -> None:
#         print(f"{element.exclusive_method_of_concrete_component_a()} + ConcreteVisitor2")
#
#     def visit_concrete_component_b(self, element) -> None:
#         print(f"{element.special_method_of_concrete_component_b()} + ConcreteVisitor2")
