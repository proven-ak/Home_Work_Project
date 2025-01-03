
import math


class Figure:           # Класс фигура
    def __init__(self, sides, color):
        sides_count = 0                         # количество сторон (по умолчанию)
        self.__sides = sides                    # размеры
        self.__color = color                    # цвет
        self.filled = False                     # закрашен (по умолчанию)

    def get_color(self):
        # Возвращает список RGB цветов.
        return self.__color

    def __is_valid_color(self, r, g, b):
        # Метод служебный, принимает параметры r, g, b,
        # который проверяет корректность переданных значений перед установкой нового цвета.
        # Корректным цвет: все значения r, g, b - целые числа в диапазоне от 0 до 255(включительно).

        return all(isinstance(value, int) and 0 <= value <= 255 for value in (r, g, b))

    def set_color(self, r, g, b):
        # Метод принимает параметры r, g, b - числа и изменяет атрибут __color на соответствующие
        # значения, предварительно проверив их на корректность.
        # Если введены некорректные данные, то цвет остаётся прежним.
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)
            print("===", r, g, b)
            return
        else:
            print("---", r, g, b)
            # print("!!!!", self.__color)

    def __is_valid_sides(self):
        # метод служебный, принимает неограниченное кол-во сторон, возвращает
        # True если все стороны целые положительные числа и кол-во новых сторон совпадает с текущим,
        # False - во всех остальных случаях.

        if self.__sides >= 0:
            return True

    def get_sides(self):
        # метод возвращает значение атрибута __sides.
        return self.__sides

    def __len__(self):
        # метод возвращает периметр фигуры

        pass

    def set_sides(self, new_count):
        # метод принимает новые стороны, если их количество не равно sides_count,
        # то не изменять, в противном случае - менять.

        if new_count != self.sides_count:
            self.sides_count = new_count


class Circle(Figure):                           # Класс круг
    # Атрибуты класса Circle(sides_count = 1):
    # Каждый объект класса Circle должен обладать следующими атрибутами и методами:
    # Все атрибуты и методы класса Figure
    # Атрибут __radius, рассчитать исходя из длины окружности(одной единственной стороны).
    # Метод get_square возвращает площадь круга(можно рассчитать как через длину, так и через радиус).

    def __init__(self, sides, color):
        super().__init__(1, color)        # Количество сторон круга 1


class Triangle(Figure):                         # Класс треугольник
    # Атрибуты класса Triangle:
    # sides_count = 3
    # Каждый объект класса Triangle должен обладать следующими атрибутами и методами:
    # Все атрибуты и методы класса Figure
    # Метод get_square возвращает площадь треугольника.(можно рассчитать по формуле Герона)

    def __init__(self, sides, color):
        # sides — кортеж или список длиной 3, содержащий длины сторон треугольника
        # color - кортеж или список длиной 3, цвет треугольника
        super().__init__(3, color)  # Количество сторон треугольника равно 3
        self.sides = sides  # Длины сторон треугольника


class Cube(Figure):                             # Класс куб
    # Атрибуты класса Cube:
    # sides_count = 12
    # Каждый объект класса Cube должен обладать следующими атрибутами и методами:
    # Все атрибуты и методы класса Figure.
    # Переопределить __sides сделав список из 12 одинаковых сторон(передаётся 1 сторона)
    # Метод get_volume, возвращает объём куба.

    def __init__(self, sides, color):
        super().__init__(12, color)       # Количество сторон куба 12


