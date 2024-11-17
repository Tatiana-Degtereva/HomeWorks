# Домашняя работа по уроку "Способы вызова функции"
# Задача "Рассылка писем":

# Создайте функцию send_email, которая принимает 2 обычных аргумента: сообщение и получатель
# и 1 обязательно именованный аргумент со значением по умолчанию - отправитель.
# Внутри функции реализовать следующую логику:
# Проверка на корректность e-mail отправителя и получателя.
# Проверка на отправку самому себе.
# Проверка на отправителя по умолчанию.

def send_email(message, recipient, *, sender = "university.help@gmail.com"):
    if recipient.find('@') == -1 or sender.find('@') == -1:
        print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
    else:
        if  recipient.endswith('.com') == False and recipient.endswith('.ru') == False and  recipient.endswith('.net') == False:
            print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
        else:
            if  sender.endswith('.com') == False and  sender.endswith('.ru') == False and  sender.endswith('.net') == False:
                print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
            else:
                if   recipient == sender:
                    print('Нельзя отправить письмо самому себе!')
                else:
                    if sender  == 'university.help@gmail.com':
                        print('Письмо успешно отправлено с адреса ', sender, ' на адрес ', recipient)
                    else:
                        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса ', sender, ' на адрес ', recipient)

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')