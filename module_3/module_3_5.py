# Самостоятельная работа по уроку "Рекурсия".
# Задача "Рекурсивное умножение цифр.

def get_multiplied_digits(number):

    # Преобразуем число в строку
    str_number = str(number)

    # Получаем первую цифру числа (в строковом формате).
    first = str_number[0]

    # Если первая цифра равна "0", заменяем её на 1.
    if first == "0":
        return 1

    # Если в числе осталась только одна цифра, возвращаем её как результат.
    if len(str_number) <= 1:
        return int(first)

    # Умножаем первую цифру на результат рекурсивного вызова
    # функции для оставшейся части числа.
    return int(first) * get_multiplied_digits(int(str_number[1:]))


# Тестовые вызовы функции:
result = get_multiplied_digits(40203)
result2 = get_multiplied_digits(402030)

# Выводим результаты.
print(result)
print(result2)


