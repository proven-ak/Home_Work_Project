
class House:
    # Конструктор класса. Инициализирует имя дома и количество этажей.
    def __init__(self, name, number_of_floors):
        self.name = name                                # Название дома
        self.number_of_floors = number_of_floors        # Общее количество этажей в доме

    """
    Следует заметить, что other может быть не только числом, но и вообще любым объектом другого класса.
    Для более точной логики работы методов __eq__, __add__  и других методов сравнения и арифметики 
    перед выполняемыми действиями лучше убедиться в принадлежности к типу при помощи функции isinstance:
    isinstance(other, int) - other указывает на объект типа int.
    isinstance(other, House) - other указывает на объект типа House.
    """

    def _check_other(self, other):
        """Проверка, является ли other экземпляром House или целым числом (int)."""
        if isinstance(other, House):
            return "house"
        elif isinstance(other, int):
            return "int"
        else:
            print(f"Ошибка: нельзя работать с объектом типа {type(other)}")
            return None

    # Метод для перехода на указанный этаж
    def go_to(self, new_floor):
        """Переход на указанный этаж."""
        if 1 <= new_floor <= self.number_of_floors:
            print(f"Переход на этаж {new_floor}")
        else:
            print("Такого этажа не существует")

    def __len__(self):
        """Возвращает количество этажей в доме."""
        return self.number_of_floors

    def __str__(self):
        """Строковое представление объекта."""
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def _validate_number(self):
        """Проверяет, является ли количество этажей целым числом."""
        if not isinstance(self.number_of_floors, int):
            print(f"Ошибка: {self.number_of_floors} не является числом (int)")
            return False
        return True

    # Перегрузка оператора равенства (==)
    def __eq__(self, other):
        other_type = self._check_other(other)
        if other_type == "house":
            return self.number_of_floors == other.number_of_floors
        elif other_type == "int":
            return self.number_of_floors == other
        return False

    # Перегрузка оператора меньше (<)
    def __lt__(self, other):
        other_type = self._check_other(other)
        if other_type == "house":
            return self.number_of_floors < other.number_of_floors
        elif other_type == "int":
            return self.number_of_floors < other
        return False

    # Перегрузка оператора меньше или равно (<=)
    def __le__(self, other):
        other_type = self._check_other(other)
        if other_type == "house":
            return self.number_of_floors <= other.number_of_floors
        elif other_type == "int":
            return self.number_of_floors <= other
        return False

    # Перегрузка оператора больше (>)
    def __gt__(self, other):
        other_type = self._check_other(other)
        if other_type == "house":
            return self.number_of_floors > other.number_of_floors
        elif other_type == "int":
            return self.number_of_floors > other
        return False

    # Перегрузка оператора больше или равно (>=)
    def __ge__(self, other):
        other_type = self._check_other(other)
        if other_type == "house":
            return self.number_of_floors >= other.number_of_floors
        elif other_type == "int":
            return self.number_of_floors >= other
        return False

    # Перегрузка оператора не равно (!=)
    def __ne__(self, other):
        other_type = self._check_other(other)
        if other_type == "house":
            return self.number_of_floors != other.number_of_floors
        elif other_type == "int":
            return self.number_of_floors != other
        return False

    # Перегрузка оператора сложения (+)
    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        return self

    # Перегрузка оператора сложения (в обратном порядке, например 10 + h2)
    def __radd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        return self

    # Перегрузка оператора увеличения (+=)
    def __iadd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        return self


# Создание объектов
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# Вывод строк названия и высотности __str__
print(h1)
print(h2)

print(h1 == h2)     # __eq__

h1 = h1 + 10
print(h1)
print(h1 == h2)     # __add__

h1 += 10            # __iadd__
print(h1)

h2 = 10 + h2        # __radd__
print(h2)

print(h1 > h2)      # __gt__
print(h1 >= h2)     # __ge__

print(h1 < h2)      # __lt__
print(h1 <= h2)     # __le__
print(h1 != h2)     # __ne__

# Проверка типа параметров
h1.number_of_floors = "12"  # Пример некорректного значения
print(h1 > h2)  # Ошибка валидации и возврат False

h2.number_of_floors = "sss"  # Еще одна ошибка
print(h1 <= h2)  # Ошибка валидации и возврат False

"""
Вывод на консоль:
Название: ЖК Эльбрус, кол-во этажей: 10
Название: ЖК Акация, кол-во этажей: 20
False
Название: ЖК Эльбрус, кол-во этажей: 20
True
Название: ЖК Эльбрус, кол-во этажей: 30
Название: ЖК Акация, кол-во этажей: 30
False
True
False
True
False
"""
