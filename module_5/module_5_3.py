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

    # Метод для перехода на указанный этаж
    def go_to(self, new_floor):
        # Проверяем, существует ли указанный этаж в доме
        if 1 <= new_floor <= self.number_of_floors:
            print(new_floor)  # Печатаем номер этажа
        else:
            print("Такого этажа не существует")  # Сообщение об ошибке, если этаж вне диапазона

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def _validate_number(self):
        """Проверяет, является ли значение количества этажей целым числом (int)."""
        if not isinstance(self.number_of_floors, int):
            print(f"Ошибка: {self.number_of_floors} не является числом (int)")
            return False
        return True

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        elif isinstance(other, int):  # Добавим поддержку числовых значений
            return self.number_of_floors == other
        else:
            print("Ожидается объект (House) или число (int)")
            return False  # Возвращаем False, если тип неверный

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        elif isinstance(other, int):  # Если other - это число
            return self.number_of_floors < other
        # В случае, если другой объект не является ни числом, ни домом
        print(f"Ошибка сравнения: нельзя сравнивать {self.number_of_floors} с {other}")
        return False

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        elif isinstance(other, int):  # Если other - это число
            return self.number_of_floors <= other
        print(f"Ошибка сравнения: нельзя сравнивать {self.number_of_floors} с {other}")
        return False

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        elif isinstance(other, int):  # Если other - это число
            return self.number_of_floors > other
        print(f"Ошибка сравнения: нельзя сравнивать {self.number_of_floors} с {other}")
        return False

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        elif isinstance(other, int):  # Если other - это число
            return self.number_of_floors >= other
        print(f"Ошибка сравнения: нельзя сравнивать {self.number_of_floors} с {other}")
        return False

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        elif isinstance(other, int):  # Если other - это число
            return self.number_of_floors != other
        print(f"Ошибка сравнения: нельзя сравнивать {self.number_of_floors} с {other}")
        return False

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        return self

    def __radd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        return self

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
