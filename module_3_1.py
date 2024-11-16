# Домашняя работа по уроку "Пространство имён"
# Задача "Счётчик вызовов":
# Вам необходимо написать 3 функции:
# Функция count_calls подсчитывающая вызовы остальных функций.
# Функция string_info принимает аргумент - строку и возвращает кортеж из: длины этой строки, строку в верхнем регистре,
# строку в нижнем регистре.
# Функция is_contains принимает два аргумента: строку и список, и возвращает True, если строка находится в этом списке,
# False - если отсутствует. Регистром строки при проверке пренебречь: UrbaN ~ URBAN.

calls = 0

def count_calls():
    global calls
    return (calls  := calls + 1)

def string_info (string):
    global calls
    count_calls()
    return (len(string), string.upper(), string.lower())

def is_contains (string, list_to_search):
    global calls
    count_calls()
    list_to_search_lower = []
    for i in list_to_search:
        list_to_search_lower.append(i.lower())
    return(string.lower() in list_to_search_lower)

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
