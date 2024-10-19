# Домашняя работа по уроку "Условная конструкция. Операторы if, elif, else"

# Задача "Все ли равны?":
# На вход программе подаются 3 целых числа и записываются в переменные first, second и third соответственно.
# Ваша задача написать условную конструкцию (из if, elif, else), которая выводит кол-во одинаковых чисел среди 3-х введённых.

first = input('введите целое число ')
second = input('введите целое число ')
third = input('введите целое число ')
if first == second and second == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
else:
    print(0)