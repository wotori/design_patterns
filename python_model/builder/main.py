from python_model.builder.interface.mail_builder_class import EmailBuilder

if __name__ == "__main__":
    content = "Привет, здорово, что есть такой паттерн как Bulder"
    builder = EmailBuilder()
    builder.subject('Тестовое письмо', 'С важением, админ')
    builder.content(content)
    builder.sender("ya@ya.ru")
    builder.recipient("to@to.ru")
    builder.recipient_copy("copyto@copyto.ru")
    mail = builder.build()

    print(mail)


