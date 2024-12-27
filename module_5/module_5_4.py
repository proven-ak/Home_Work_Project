
class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        # Создаем новый объект
        instance = super().__new__(cls)
        return instance

    # Конструктор класса. Инициализирует имя дома и количество этажей.
    def __init__(self, name, number_of_floors):
        self.name = name                                    # Название дома
        self.number_of_floors = number_of_floors            # Общее количество этажей в доме
        self.__class__.houses_history.append(self.name)     # Добавляем имя дома в историю

    def __del__(self):
        # Удаляем объект, но оставляем в списке houses_history
        print(f'{self.name} снесён, но он останется в истории')

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

# Выводим список построенных домов
print(House.houses_history)

del h2      # Удаление 'ЖК Акация'
del h3      # Удаление 'ЖК Матрёшки'

# Выводим список построенных домов
print(House.houses_history)

del h1      # Удаление 'ЖК Эльбрус'


"""
Вывод на консоль:
['ЖК Эльбрус']
['ЖК Эльбрус', 'ЖК Акация']
['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']
ЖК Акация снесён, но он останется в истории
ЖК Матрёшки снесён, но он останется в истории
['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']
ЖК Эльбрус снесён, но он останется в истории
"""

