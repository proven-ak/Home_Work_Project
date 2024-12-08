
def send_email(message, recipient, sender = "university.help@gmail.com"):
    suffix = [".com", ".ru", ".net"]
    if recipient.find("@") or sender.find("@"):
        for sub_suffix in suffix:
            if sender.find(sub_suffix):
                if recipient.find(sub_suffix):

    else:
        print("Невозможно отправить письмо с адреса ", sender, "на адрес ", recipient)
