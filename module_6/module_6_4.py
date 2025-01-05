
import math


class Figure:           # Класс фигура
    def __init__(self, color, sides):
        sides_count = 0                         # количество сторон (по умолчанию)
        self.__sides = sides                    # размеры
        self.__color = color                    # цвет
        self.filled = False                     # закрашен (по умолчанию)

    def get_color(self):
        # Возвращает список RGB цветов.
        return list(self.__color)

    @staticmethod
    def __is_valid_color(r, g, b):
        # Метод служебный, принимает параметры r, g, b,
        # который проверяет корректность переданных значений перед установкой нового цвета.
        # Корректным цвет: все значения r, g, b - целые числа в диапазоне от 0 до 255(включительно).

        return all(isinstance(value, int) and 0 <= value <= 255 for value in (r, g, b))

    def set_color(self, r, g, b):
        # Метод принимает параметры r, g, b - числа и изменяет атрибут __color
        # на соответствующие значения, предварительно проверив их на корректность,
        # что все параметры целые числа и находятся в диапазоне от 0 до 255
        # Если введены некорректные данные, то цвет остаётся прежним.

        if all(isinstance(value, int) for value in (r, g, b)) and self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)
        else:
            return

    def __is_valid_sides(self, *new_sides):
        # Метод __is_valid_sides - служебный, принимает неограниченное кол-во сторон,
        # возвращает True если все стороны целые положительные числа и кол - во
        # новых сторон совпадает с текущим, False - во всех остальных случаях.

        if isinstance(self.__sides, (list, tuple)):
            # Проверка списка/кортежа: совпадение длины и все стороны > 0
            return len(new_sides) == len(self.__sides) and all(isinstance(s, (int, float)) and s > 0 for s in new_sides)

        elif isinstance(self.__sides, (int, float)):
            # Проверка одиночного значения
            return len(new_sides) == 1 and isinstance(new_sides[0], (int, float)) and new_sides[0] > 0

        return False  # Если тип данных неизвестен

    def get_sides(self):
        # Метод get_sides должен возвращать значения атрибута __sides

        if isinstance(self.__sides, (list, tuple)):
            return list(self.__sides)
        # Если сторона одна (например, для круга), возвращаем её в виде списка
        return [self.__sides]

    def __len__(self):
        # Возвращает периметр фигуры
        if isinstance(self.__sides, (list, tuple)):
            # Умножаем длину одной стороны (предполагаем, что все стороны равны) на их количество
            return len(self.__sides) * self.__sides[0]
        return self.__sides  # Если сторона одна (например, для круга)

    def set_sides(self, *new_sides):
        # метод принимает новые стороны, если их количество не равно sides_count,
        # то не изменять, в противном случае - менять.

        if self.__is_valid_sides(*new_sides):
            if isinstance(self.__sides, (list, tuple)):  # Если стороны хранятся как список/кортеж
                self.__sides = list(new_sides)
            elif isinstance(self.__sides, (int, float)):  # Если сторона одна (число)
                self.__sides = new_sides[0]
        else:
            print("Некорректные стороны. Значения не изменены.")


class Circle(Figure):                           # Класс круг
    # Атрибуты класса Circle(sides_count = 1):
    # Каждый объект класса Circle должен обладать всеми атрибутами и методами класса Figure

    def __init__(self, color, sides):
        super().__init__(color, sides=1)        # длина окружности
        self.__radius = sides / (2 * math.pi)   # Радиус окружности
        sides_count = 1                         # Количество сторон круга 1

    def get_square(self):
        # Возвращает площадь круга, рассчитываемую как π * r^2
        return math.pi * self.__radius ** 2

    def get_radius(self):
        # Возвращает радиус круга рассчитать исходя из длины окружности
        # (одной единственной стороны).
        return self.__radius


class Triangle(Figure):                         # Класс треугольник
    # Атрибуты класса Triangle:
    # sides_count = 3
    # Каждый объект класса Triangle должен обладать следующими атрибутами и методами:
    # Все атрибуты и методы класса Figure
    # Метод get_square возвращает площадь треугольника.(можно рассчитать по формуле Герона)

    def __init__(self, color, sides):
        # sides — кортеж или список длиной 3, содержащий длины сторон треугольника
        # color - кортеж или список длиной 3, цвет треугольника
        super().__init__(color, 3)  # Количество сторон треугольника равно 3
        self.sides = sides  # Длины сторон треугольника

    def get_square(self):
        # Рассчитывает площадь треугольника по формуле Герона:
        # Формула: S = √(p * (p - a) * (p - b) * (p - c))
        # где p — полупериметр, a, b, c — длины сторон
        a, b, c = self.sides
        # Полупериметр
        p = (a + b + c) / 2

        # Площадь по формуле Герона
        return math.sqrt(p * (p - a) * (p - b) * (p - c))


class Cube(Figure):                             # Класс куб
    # Атрибуты класса Cube:
    # sides_count = 12
    # Каждый объект класса Cube должен обладать следующими атрибутами и методами:
    # Все атрибуты и методы класса Figure.
    # Переопределить __sides сделав список из 12 одинаковых сторон(передаётся 1 сторона)
    # Метод get_volume, возвращает объём куба.

    def __init__(self, color, sides):
        super().__init__(color, 12)                # Количество сторон куба 12
        sides_count = 12
        self.__sides = [sides] * sides_count             # Список из 12 одинаковых сторон

    def get_volume(self):
        """
        Вычисляет и возвращает объём куба.
        :return: Объём куба.
        """
        side_length = self.__sides[0]           # Все стороны одинаковой длины
        return side_length ** 3

    def get_sides(self):
        """
        Возвращает список рёбер куба.
        :return: Список из 12 одинаковых сторон.
        """
        return self.__sides

    def set_sides(self, *new_count):
        return new_count


# Test Class Triangle
# Создаём треугольник со сторонами 3, 4, 5 и цветом (255, 0, 0)
triangle = Triangle((255, 0, 0), (3, 4, 5))

# Получаем цвет треугольника
print("Цвет треугольника:", triangle.get_color())  # Ожидаемый вывод: (255, 0, 0)

# Получаем площадь треугольника
print("Площадь треугольника:", round(triangle.get_square(), 2))  # Ожидаемый вывод: 6.0

print("---------")


# Test Class Circle
# Создаём круг с длиной окружности 31.4 и цветом (0, 255, 0)
circle = Circle((0, 255, 0), 31.4)

# Получаем цвет круга
print("Цвет круга:", circle.get_color())  # Ожидаемый вывод: (255, 0, 0)

# Получаем радиус круга
print("Радиус круга:", round(circle.get_radius(), 2))  # Ожидаемый вывод: 5.0

# Получаем площадь круга
print("Площадь круга:", round(circle.get_square(), 2))  # Ожидаемый вывод: 78.54

print("---------")


# Test Class Cube
# Создаём куб с длиной стороны 4 и цветом (0, 255, 0)
cube = Cube( (0, 255, 0), 4)

# Получаем цвет куба
print("Цвет куба:", cube.get_color())  # Ожидаемый вывод: (0, 255, 0)

# Получаем список сторон
print("Стороны куба:", cube.get_sides())  # [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]

# Вычисляем объём
print("Объём куба:", cube.get_volume())  # 64

print("----------------------")

# Test Code:
# Код для проверки:
circle1 = Circle((200, 200, 100), 10)        # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)              # (Цвет, стороны)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)                   # Изменится
print(list(circle1.get_color()))

cube1.set_color(300, 70, 15)                    # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)                # Не изменится
print(cube1.get_sides())

circle1.set_sides(15)                                   # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

"""
Выходные данные (консоль):
[55, 66, 77]
[222, 35, 130]
[6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
[15]
15
216
"""
