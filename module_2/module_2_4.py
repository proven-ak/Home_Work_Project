
# Начальные данные
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Инициация итоговых переменных
primes = []
not_primes = []

for num in numbers:                         # Перебираем значение делимого
    if num == 1:                            # Исключаем из проверки значение "1"
        continue                            # Прерываем внешний цикл
    is_prime: bool = True                   # is_prime по умолчанию True
    for i in range(2, numbers[num-1]):      # Перебираем значение делителя
        if num % i == 0:                    # Проверяем на простоту
            is_prime = False                # is_prime если составное False
            break                           # Прерываем, если найдено деление без остатка

# Создаем простые и составные списки
    if is_prime:
        primes.append(num)
    else:
        not_primes.append(num)

# Выводим списки на консоль
print("Primes: ", primes)
print("Not Primes: ", not_primes)


