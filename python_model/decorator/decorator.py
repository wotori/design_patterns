from python_model.decorator.mail_client import MailClient


class Decorator(MailClient):
    _component: MailClient = None

    def __init__(self, component: MailClient) -> None:
        self._component = component
        self._component.user_name = self.operation_encode_name()
        self._component.message = self.operation_encode_message()

    @property
    def component(self):
        return self._component

    def operation_encode_name(self) -> str:
        return "Имя пользователя закодировано"

    def operation_encode_message(self) -> str:
        return "Тело письма закодировано"
