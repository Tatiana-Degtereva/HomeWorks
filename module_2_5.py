# Домашняя работа по уроку "Функции в Python. Функция с параметром"

# Задача "Матрица воплоти":
# Напишите функцию get_matrix с тремя параметрами n, m и value,
# которая будет создавать матрицу(вложенный список) размерами n строк и m столбцов,
# заполненную значениями value и возвращать эту матрицу в качестве результата работы.

def get_matrix(n, m, value):
    matrix = []
    for i in range (0, n):
        matrix.append([])
        for j in range(0, m):
            matrix[i].append(value)
    print(matrix)

result = get_matrix(5, 3, 27)


