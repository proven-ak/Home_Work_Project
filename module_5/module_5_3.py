
class House:
    def __init__(self, name, number_of_floors):
        self.name = name                                # Название дома
        self.number_of_floors = number_of_floors        # Общее количество этажей в доме

    def _check_other(self, other):
        """Проверка, является ли other экземпляром House или целым числом (int)."""
        if isinstance(other, House):
            return "house"
        elif isinstance(other, int):
            return "int"
        elif isinstance(other, str):
            print(f"Ошибка: не удается выполнить операцию с объектом типа {type(other)}")
            return "str"
        else:
            print(f"Ошибка: не удается выполнить операцию с объектом типа {type(other)}")
            return None

    def _validate_number(self, value):
        """Проверяет, является ли значение целым числом (int)."""
        if not isinstance(value, int):
            print(f"Ошибка: {value} не является числом (int)")
            return False
        return True

    def set_number_of_floors(self, value):
        """Метод для безопасного изменения количества этажей."""
        if self._validate_number(value):
            self.number_of_floors = value
        else:
            print(f"Не удалось установить количество этажей: {value} некорректно.")

    def _validate_comparison(self, other):
        """Проверка, является ли other допустимым значением для сравнения."""
        if isinstance(other, House):
            if not self._validate_number(self.number_of_floors) or not self._validate_number(other.number_of_floors):
                return False
        elif isinstance(other, int):
            if not self._validate_number(self.number_of_floors):
                return False
        elif isinstance(other, str):
            print(f"Ошибка: не удается выполнить операцию с объектом типа {type(other)}")
            return False
        else:
            print(f"Ошибка: не удается выполнить операцию с объектом типа {type(other)}")
            return False
        return True

    def __len__(self):
        """Возвращает количество этажей в доме."""
        return self.number_of_floors

    def __str__(self):
        """Строковое представление объекта."""
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        if self._validate_comparison(other):
            if isinstance(other, House):
                return self.number_of_floors == other.number_of_floors
            elif isinstance(other, int):
                return self.number_of_floors == other
        return False

    def __lt__(self, other):
        if self._validate_comparison(other):
            if isinstance(other, House):
                return self.number_of_floors < other.number_of_floors
            elif isinstance(other, int):
                return self.number_of_floors < other
        return False

    def __le__(self, other):
        if self._validate_comparison(other):
            if isinstance(other, House):
                return self.number_of_floors <= other.number_of_floors
            elif isinstance(other, int):
                return self.number_of_floors <= other
        return False

    def __gt__(self, other):
        if self._validate_comparison(other):
            if isinstance(other, House):
                return self.number_of_floors > other.number_of_floors
            elif isinstance(other, int):
                return self.number_of_floors > other
        return False

    def __ge__(self, other):
        if self._validate_comparison(other):
            if isinstance(other, House):
                return self.number_of_floors >= other.number_of_floors
            elif isinstance(other, int):
                return self.number_of_floors >= other
        return False

    def __ne__(self, other):
        if self._validate_comparison(other):
            if isinstance(other, House):
                return self.number_of_floors != other.number_of_floors
            elif isinstance(other, int):
                return self.number_of_floors != other
        return False

    def __add__(self, value):
        if isinstance(value, int) and self._validate_number(self.number_of_floors):
            self.number_of_floors += value
        return self

    def __radd__(self, value):
        if isinstance(value, int) and self._validate_number(self.number_of_floors):
            self.number_of_floors += value
        return self

    def __iadd__(self, value):
        if isinstance(value, int) and self._validate_number(self.number_of_floors):
            self.number_of_floors += value
        return self


# Создание объектов
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# Вывод строк названия и высотности __str__
print(h1)
print(h2)

# Проверка операций
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
print('\nПроверка типа параметров:')
h1.number_of_floors = '12'  # Пример некорректного значения
print(h1 > h2)  # Ошибка валидации и возврат False

h2.number_of_floors = 'sss'  # Еще одна ошибка
print(h1 <= h2)  # Ошибка валидации и возврат False

# Дополнительные тесты с неверными типами данных:
print("\nДополнительные тесты с неверными типами данных:")

# Присвоение списка вместо числа
h1.number_of_floors = [10, 20]
print(f"Ошибка: {h1.number_of_floors} не является числом (int)")

# Попытка выполнения операции с объектом другого типа
print(f"Ошибка: {h1 + 'строка'}")  # Ошибка: не удается выполнить операцию с объектом типа <class 'str'>

print(f"Ошибка: {h1 == 'не дом'}")  # Ошибка: не удается выполнить операцию с объектом типа <class 'str'>

# Пример передачи списка в операторы сравнения
print(f"Ошибка: {h1 < [5, 6]}")  # Ошибка: не удается выполнить операцию с объектом типа <class 'list'>



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
