from python_model.builder.interface.mail_bulder_interface import EmailBuilderInterface
from python_model.builder.interface.mail_basic_class import MailBasic

class EmailBuilder(EmailBuilderInterface):
    """
    Классы конкретного Строителя наследуют интерфейс строителя и представляют
    конкретные реализации шагов построения. Наша программа может иметь несколько
    вариантов строителей, реализованных по разному
    """

    def __init__(self) -> None:
        """
        Новый экземпляр строителя должен содержать пустой объект продукта,
        который используется в дальнейшей сборке.
        """
        self.reset()

    def reset(self) -> None:
        self._mail = MailBasic()

    @property
    def mail(self) -> MailBasic:
        """
        Конкретные Строители должны предоставить свои собственные методы
        получения результатов. Это связано с тем, что различные типы строителей
        могут создавать совершенно разные продукты с разными интерфейсами.
        Поэтому такие методы не могут быть объявлены в базовом интерфейсе
        Строителя (по крайней мере, в статически типизированном языке
        программирования).

        Как правило, после возвращения конечного результата клиенту, экземпляр
        строителя должен быть готов к началу производства следующего продукта.
        Поэтому обычной практикой является вызов метода сброса в конце тела
        метода getProduct. Однако такое поведение не является обязательным, вы
        можете заставить своих строителей ждать явного запроса на сброс из кода
        клиента, прежде чем избавиться от предыдущего результата.
        """
        mail = self._main
        self.reset()
        return mail

    def subject(self, subject, signature) -> None:
        self._mail.subject = subject
        self._mail.signature = subject

    def content(self, content) -> None:
        self._mail.content = content

    def recipient(self, recipient) -> None:
        self._mail.recipient = recipient

    def recipient_copy(self, recipient_copy) -> None:
        self._mail.recipient_copy = recipient_copy

    def sender(self, sender) -> None:
        self._mail.sender = sender

    def build(self) -> None:
        self.result = {
            "subject": self._mail.subject,
            "content": self._mail.content,
            "recipient": self._mail.recipient,
            "recipient_copy": self._mail.recipient_copy,
        }
        return self.result

