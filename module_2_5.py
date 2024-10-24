# Домашняя работа по уроку "Функции в Python. Функция с параметром"

# Задача "Матрица воплоти":
# Напишите функцию get_matrix с тремя параметрами n, m и value,
# которая будет создавать матрицу(вложенный список) размерами n строк и m столбцов,
# заполненную значениями value и возвращать эту матрицу в качестве результата работы.

def get_matrix(n, m, value):
    matrix = []
    for i in range (0, n):
        if n <= 0 or m <=0: break
        else:
            matrix.append([])
        for j in range(0, m):
            matrix[i].append(value)
    return matrix

result1 = get_matrix(2, 3, 23)
result2 = get_matrix(4, 0, 40)
result3 = get_matrix(-1, 2, 12)
print(result1)
print(result2)
print(result3)


