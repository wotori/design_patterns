```
if __name__ == "__main__":
    mail_client: MailClient = MailClient
    mail_client.user_name = "Anton Chigurh"
    mail_client.message = "Hello, World!"

    print("Имя пользователя: ", mail_client.user_name)
    print("Тело письма: ", mail_client.message)

    encoded = Decorator(mail_client)
    print("Имя пользователя: ", encoded.user_name)
    print("Тело письма: ", encoded.message)
```

```
--> Имя пользователя:  Anton Chigurh
--> Тело письма:  Hello, World!
--> Имя пользователя:  Имя пользователя закодировано
--> Тело письма:  Тело письма закодировано
```
