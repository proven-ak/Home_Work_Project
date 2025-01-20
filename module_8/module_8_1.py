# Домашнее задание по уроку "Try и Except".

# Описание функции:
# add_everything_up(a, b) принимает a и b, которые могут быть как числами(int, float),
# так и строками(str).
# TypeError - когда a и b окажутся разными типами (числом и строкой), то возвращать
# строковое представление этих двух данных вместе (в том же порядке). Во всех остальных
# случаях выполнять стандартные действия.

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
