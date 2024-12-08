def send_email(message, recipient, sender = "university.help@gmail.com"):
    suffix = [".com", ".ru", ".net"]

    if "@" not in recipient or "@" not in sender:
        print("Невозможно отправить письмо с адреса ", sender, "на адрес ", recipient)
        return

    for sub_suffix in suffix:
        if sub_suffix not in recipient or sub_suffix not in sender:
            print("Невозможно отправить письмо с адреса ", sender, "на адрес ", recipient)
            return

    if recipient == sender:
        print("Нельзя отправить письмо самому себе!")

    if sender == "university.help@gmail.com":
        print("Письмо успешно отправлено с адреса ", sender,  "на адрес ", recipient)








send_email('Проверка на "@"', 'urban.fan#mail.ru', sender='urban.info$gmail.com')
send_email('Проверка на "@"', 'urban.fan#mail.ru', sender='urban.info@gmail.com')
send_email('Проверка на "@"', 'urban.fan@mail.ru', sender='urban.info$gmail.com')

print("----------------------")

send_email('Проверка suffix', 'urban.fan@mail.ra', sender='urban.info"@"gmail.com')
send_email('Проверка suffix', 'urban.fan@mail.ru', sender='urban.info@gmail.cam')
send_email('Проверка suffix', 'urban.fan@mail.ra', sender='urban.info@gmail.cam')

print("----------------------")

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

