# Задание по теме "Создание исключений"

class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


# Класс Car обладает следующими свойствами:
# Атрибут объекта model - название автомобиля (строка).
# Атрибут объекта __vin - vin номер автомобиля (целое число). Уровень доступа private.


class Car:
    def __init__(self, model, vin_number, numbers):
        self.model = model

        # Проверка и присваивание vin_number
        if self.__is_valid_vin(vin_number):
            self.__vin = vin_number

        # Проверка и присваивание numbers
        if self.__is_valid_numbers(numbers):
            self.__numbers = numbers

    def get_vin(self):  # Метод для доступа к приватному атрибуту
        return self.__vin

    # __is_valid_vin(vin_number)
    # Выбрасывает исключение IncorrectVinNumber с сообщением 'Некорректный тип vin номер',
    # если передано не целое число. (тип данных можно проверить функцией isinstance).
    # Выбрасывает исключение IncorrectVinNumber с сообщением 'Неверный диапазон для vin номера',
    # если переданное число находится не в диапазоне от 1000000 до 9999999 включительно.
    # Возвращает True, если исключения не были выброшены.

    def __is_valid_vin(self, vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        if not (1000000 <= vin_number <= 9999999):
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        return True

    # __is_valid_numbers
    # Выбрасывает исключение IncorrectCarNumbers с сообщением 'Некорректный тип данных для номеров',
    # если передана не строка. (тип данных можно проверить функцией isinstance).
    # Выбрасывает исключение IncorrectCarNumbers с сообщением 'Неверная длина номера',
    # переданная строка должна состоять ровно из 6 символов.
    # Возвращает True, если исключения не были выброшены.

    def __is_valid_numbers(self, numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        return True


# Пример выполняемого кода:
try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')

"""
Вывод на консоль:
Model1 успешно создан
Неверный диапазон для vin номера
Неверная длина номера
"""


