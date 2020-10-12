from python_model.builder.interface.mail_builder_class import EmailBuilder

class Director:
    """
    Директор отвечает только за выполнение шагов построения в определённой
    последовательности. Это полезно при производстве продуктов в определённом
    порядке или особой конфигурации. Строго говоря, класс Директор необязателен,
    так как клиент может напрямую управлять строителями.
    """

    def __init__(self) -> None:
        self._email_builder = None

    @property
    def builder(self) -> EmailBuilder:
        return self._email_builder

    @builder.setter
    def builder(self, builder: EmailBuilder) -> None:
        """
        Директор работает с любым экземпляром строителя, который передаётся ему
        клиентским кодом. Таким образом, клиентский код может изменить конечный
        тип вновь собираемого продукта.
        """
        self._email_builder = builder
