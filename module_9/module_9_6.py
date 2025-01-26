
# Задание по теме "Генераторы"
# Пример результата выполнения программы:


def all_variants(text):
    for _len in range(1, len(text) + 1):                # Длина подстроки от 1 до длины строки
        for _start in range(len(text) - _len + 1):      # Все начальные индексы для данной длины
            yield text[_start:_start + _len]            # Подстрока от _start длиной _len


# Пример работы функции:
a = all_variants("abc")
for i in a:
    print(i)

"""
Вывод на консоль:
a
b
c
ab
bc
abc
"""