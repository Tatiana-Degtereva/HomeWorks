# Дополнительное практическое задание по модулю: "Подробнее о функциях."
# Задание "Раз, два, три, четыре, пять .... Это не всё?":
# Наши студенты, без исключения, - очень умные ребята. Настолько умные, что иногда по утру сами путаются в том,
# что намудрили вчера вечером.
# Один из таких учеников уснул на клавиатуре в процессе упорной учёбы (ещё и трудолюбивые). Тем не менее,
# даже после сна, его код остался рабочим и выглядел следующим образом:
# data_structure = [
#   [1, 2, 3],
#   {'a': 4, 'b': 5},
#   (6, {'cube': 7, 'drum': 8}),
#   "Hello",
#   ((), [{(2, 'Urban', ('Urban2', 35))}])
# ]
# Увидев это студент задался вопросом: "А есть ли универсальное решение для подсчёта суммы всех чисел и длин всех строк?"
# Да, выглядит страшно, да и обращаться нужно к каждой внутренней структуре (списку, словарю и т.д.) по-разному.
# Ученику пришлось каждый раз использовать индексацию и обращение по ключам - универсального
# решения для таких структур он не нашёл.
# Помогите сокурснику осуществить его задумку.

def calculate_structure_sum(data_structure):
    sum = 0
    if isinstance(data_structure,list) == True:
        sum = sum + data_structure

    if isinstance(data_structure,tuple) == True:
        sum = sum + data_structure

    if isinstance(data_structure,dict) == True:
        sum = sum + data_structure

    if isinstance(data_structure,set) == True:
        sum = sum + data_structure

    if isinstance(data_structure,str) == True:
        sum = sum + len(data_structure)

    if isinstance(data_structure,int) == True:
       sum = sum+data_structure

    if isinstance(data_structure,float) == True:
        sum = sum +data_structure

    else:
        sum = sum + 0

    return sum


data_structure = 'ghjuhy'

# data_structure = [
# [1, 2, 3],
# {'a': 4, 'b': 5},
# (6, {'cube': 7, 'drum': 8}),
# "Hello",
# ((), [{(2, 'Urban', ('Urban2', 35))}])
# ]

result = calculate_structure_sum(data_structure)
print(result)