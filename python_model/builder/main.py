from python_model.builder.interface.mail_bulder import EmailBuilder

if __name__ == "__main__":
    content = "Привет, здорово, что есть такой патерн как Bulder"
    email = EmailBuilder()
    email.subject("subject")
    email.sender("ya@ya.ru")
    email.recipient("to@to.ru")
    email.recipient_copy("copyto@copyto.ru")
    email.content(content)
    email.build()


