# Задание по теме "Создание функций на лету"

# 1. Lambda-функция
# Цель: Реализовать выражение list(map(lambda_func, first, second)),
# чтобы получить список совпадений символов двух строк.

first = 'Мама мыла раму'
second = 'Рамена мало было'

# lambda-функция для сравнения двух строк должен быть список совпадения букв в той же позиции
# Где True - совпало, False - не совпало.

print(list(map(lambda f, s: f == s, first, second)))


# Вывод на консоль:
# [False, True, True, False, False, False, False, False, True, False, False, False, False, False]

#############################################

# 2. Замыкание
# Цель: Реализовать функцию get_advanced_writer(file_name) с вложенной
# функцией write_everything(*data_set).

# Функция get_advanced_writer принимает название файла для записи.
def get_advanced_writer(file_name):
    # Функция добавляет в файл file_name все данные из data_set - параметр принимающий
    # неограниченное количество данных любого типа.
    def write_everything(*data_set):
        # Открытие файла для добавления записей.
        with open(file_name, 'a', encoding='utf-8') as file:
            # Запись переданных данных(включая списки и строки) в файл построчно.
            file.write(f'File: {file_name}\n')
            # Перебираем данные из data_set
            for item in data_set:
                # Записываем каждый элемент из data_set на новой строке
                file.write(f'{item}\n')

    # Возврат вложенной функции write_everything из get_advanced_writer
    return write_everything


# Тест код:
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# Вывод в файл example.txt
# File: example.txt
# Это строчка
# ['А', 'это', 'уже', 'число', 5, 'в', 'списке']

#############################################

# 3. Метод __call__
# Цель: Реализовать класс MysticBall с функционалом случайного выбора слова
# из списка при вызове объекта.

from random import choice


# Создание класса MysticBall.
class MysticBall:
    # Определение атрибута words для хранения списка строк, переданных при создании объекта.
    def __init__(self, *words):
        self.words = words

    # Создание метода __call__, который использует функцию choice из модуля random
    # для случайного выбора элемента из words.
    def __call__(self):
        # Возвращаем случайное слово
        return choice(self.words)


# Создание объекта MysticBall с набором строк. Возвращает выбранное слово.
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())

# Примерный результат (может отличаться из-за случайности выбора):
# Да
# Да
# Наверное
