# 1.6 Практическое задание по теме: "Словари и множества"

# 1. В проекте, где вы решаете домашние задания, создайте модуль 'module_1_6.py' и напишите весь код в нём.
# 2. Работа со словарями:
#   - Создайте переменную my_dict и присвойте ей словарь из нескольких пар ключ-значение.
# Например: Имя(str)-Год рождения(int).
#   - Выведите на экран словарь my_dict.
#   - Выведите на экран одно значение по существующему ключу, одно по отсутствующему из словаря my_dict без ошибки.
#   - Добавьте ещё две произвольные пары того же формата в словарь my_dict.
#  - Удалите одну из пар в словаре по существующему ключу из словаря my_dict и выведите значение из этой пары на экран.
#   - Выведите на экран словарь my_dict.
# 3. Работа с множествами:
#   - Создайте переменную my_set и присвойте ей множество, состоящее из разных типов данных с повторяющимися значениями.
#   - Выведите на экран множество my_set (должны отобразиться только уникальные значения).
#   - Добавьте 2 произвольных элемента в множество my_set, которых ещё нет.
#   - Удалите один любой элемент из множества my_set.
#   - Выведите на экран измененное множество my_set.

my_dict = {'Misha': 1990, 'Masha': 2000, 'Ira': 2010 }
print(my_dict)
print(my_dict.get('Misha'))
print(my_dict.get('Olga', "Нет такого значения в списке"))
my_dict.update({'Alex': 1975, 'Max': 1988 })
a=my_dict.pop('Ira')
print(a)
print(my_dict)

my_set = {1, 2.5, 1, True, 2.5, 'abc',}
print(my_set)
my_set.add(75)
my_set.add('qwerty')
my_set.discard(2.5)
print(my_set)

