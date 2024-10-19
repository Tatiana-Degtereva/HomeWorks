# Домашняя работа по уроку "Цикл for. Элементы списка. Полезные функции в цикле"

# Задача "Всё не так уж просто":
# Дан список чисел numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# Используя этот список составьте второй список primes содержащий только простые числа.
# А так же третий список not_primes, содержащий все не простые числа.
# Выведите списки primes и not_primes на экран(в консоль).

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(len(numbers)): # определяется количество элементов списка numbers
    if numbers[i] == 1:  # каждый элемент списка numbers сравнивается с 1, чтобы исключить 1 из всех списков
        continue
    else:
        for j in range(2,numbers[i]): #для каждого элемента списка numbers определяются числа,
                                     # деление на которые нужно проверить(с2 до самого себя (не включительно)
            if numbers[i] % j == 0: # каждый элемент списка numbers делится на числа от 2 до самого себя (не включительно)
                not_primes.append(numbers[i]) #если деление без остатка возможно, это не простое число,
                                                # добавляем в список not_primes
                break
        else:
            primes.append(numbers[i])#если деление без остатка невозможно, это простое число, добавляем в список primes
            continue
print(primes)
print(not_primes)
