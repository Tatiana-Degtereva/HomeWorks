# Домашняя работа по уроку "Цикл for. Элементы списка. Полезные функции в цикле"

# Задача "Всё не так уж просто":
# Дан список чисел numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# Используя этот список составьте второй список primes содержащий только простые числа.
# А так же третий список not_primes, содержащий все не простые числа.
# Выведите списки primes и not_primes на экран(в консоль).

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(len(numbers)):
    if numbers[i] == 1:
        continue
    else:
        for j in range(2,numbers[i]):
            if numbers[i] % j == 0:
                not_primes.append(numbers[i])
                break
        else:
            primes.append(numbers[i])
            continue
print(primes)
print(not_primes)
