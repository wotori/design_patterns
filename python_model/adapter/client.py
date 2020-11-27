def client_code(target: "Target") -> None:
    """
    Клиентский код поддерживает все классы, использующие интерфейс Target.
    """

    print(target.request(), end="")