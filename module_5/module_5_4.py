
class House:
    # Конструктор класса. Инициализирует имя дома и количество этажей.
    def __init__(self, name, number_of_floors):
        self.name = name  # Название дома
        self.number_of_floors = number_of_floors  # Общее количество этажей в доме

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

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
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
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)

h2 = House('ЖК Акация', 20)
print(House.houses_history)

h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)

