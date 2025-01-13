
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

    @staticmethod
    def _validate_number(value):
        if not isinstance(value, (int, House)):
            raise TypeError("Ожидается число (int)")

    def __eq__(self, other):
        self._validate_number(other)
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        self._validate_number(other)  # Проверяем, что other — число
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        self._validate_number(other)  # Проверяем, что other — число
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        self._validate_number(other)  # Проверяем, что other — число
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        self._validate_number(other)  # Проверяем, что other — число
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        self._validate_number(other)  # Проверяем, что other — число
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        self.number_of_floors += value
        return self

    def __radd__(self, value):
        self.number_of_floors += value
        return self

    def __iadd__(self, value):
        self.number_of_floors += value
        return self


# Создание объектов
h1 = House('ЖК Эльбрус', 10)      # Проверка на неправильный тип данных
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

h1.number_of_floors = "12"
print(h1 > h2)

h2.number_of_floors = "sss"
print(h1 <= h2)

