from python_model.adapter.target import Target


class Adaptee:

    def specific_request(self) -> str:
        return 'мымеатич тскет лаледс аретпада дотеМ'


class Adapter(Target, Adaptee):

    def request(self) -> str:
        return f"Adapter: (Переведено адаптером) {self.specific_request()[::-1]}"
