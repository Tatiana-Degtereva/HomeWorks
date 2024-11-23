# Cамостоятельная работа по уроку "Рекурсия"

# Задача "Рекурсивное умножение цифр":
# Напиши функцию get_multiplied_digits, которая принимает аргумент целое число number и подсчитывает произведение цифр этого числа.

def get_multiplied_digits (number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number)>1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        if int(str_number[-1]) == 0:
            return 1
        else:
            return int(str_number[-1])

result = get_multiplied_digits(40203)
print(result)
result2 = get_multiplied_digits(402030)
print(result2)