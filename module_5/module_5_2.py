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


# Создание объектов
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# Вывод строк названия и высотности __str__
print(h1)
print(h2)

# Вывод высоты здания __len__
print(len(h1))
print(len(h2))



