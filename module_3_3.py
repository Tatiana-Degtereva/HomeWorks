# Домашнее задание по уроку "Распаковка позиционных параметров".

# Задача "Распаковка":
# 1.Функция с параметрами по умолчанию:
# Создайте функцию print_params(a = 1, b = 'строка', c = True), которая принимает три параметра со значениями
# по умолчанию (например сейчас это: 1, 'строка', True).
# Функция должна выводить эти параметры.
# Вызовите функцию print_params с разным количеством аргументов, включая вызов без аргументов.
# Проверьте, работают ли вызовы print_params(b = 25) print_params(c = [1,2,3])

# 2.Распаковка параметров:
# Создайте список values_list с тремя элементами разных типов.
# Создайте словарь values_dict с тремя ключами, соответствующими параметрам функции print_params, и значениями разных типов.
# Передайте values_list и values_dict в функцию print_params, используя распаковку параметров (* для списка и ** для словаря).
# 3.Распаковка + отдельные параметры:
# Создайте список values_list_2 с двумя элементами разных типов
# Проверьте, работает ли print_params(*values_list_2, 42)

def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(100, 200, 300)
print_params(1,2)
print_params(b = 5, c = 20)
print_params(a = 2, c = 7)
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [100, 'hello', False]
values_dict = {'a' : False, 'b' : 1000, 'c' : 'element'}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)