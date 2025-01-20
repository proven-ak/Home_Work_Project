# Домашнее задание по уроку "Try и Except".


def add_everything_up(a, b):
    try:
        result = a + b
        # Округляем результат до 6 знаков после запятой, если это число с плавающей точкой
        if isinstance(result, float):
            result = round(result, 6)
        return result
    except TypeError:
        return f"{a}{b}"


# Пример кода:
print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))

# Вывод в консоль:
# 123.456строка
# яблоко4215
# 130.456
