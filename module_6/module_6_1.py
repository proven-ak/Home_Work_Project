class Animal:                   # Класс Животное

    def __init__(self, name):

        self.alive = True       # живой
        self.fed = False        # накормленный
        self.name = name        # индивидуальное название каждого животного

    def eat(self, food):        # метод Съесть

        # eat(self, food) - метод
        # food - параметр, принимающий объекты классов растений.

        # self.food = food

        # print('+++++food: ', food.name, food.edible)
        # print('-----self: ', self.name, self.fed)

        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False


class Plant:                    # Класс Растение

    def __init__(self, name):

        self.edible = False     # съедобность
        self.name = name        # индивидуальное название каждого растения


class Mammal(Animal):         # Класс Млекопитающее

    # food - это параметр, принимающий объекты классов растений.
    # Метод eat должен работать следующим образом:
    # Если переданное растение(food) съедобное - выводит
    # на экран ("<self.name> съел <food.name>",
    # меняется) атрибут fed на True.

    # Если переданное растение(food) не съедобное - выводит на экран
    # ("<self.name> не стал есть <food.name>",
    # меняется) атрибут alive на False.

    # Т.е если животному дать съедобное растение, то
    # животное насытится, если не съедобное - погибнет.

    # def eat(self, food):
    pass


class Predator(Animal):         # Класс Хищник
    pass


class Flower(Plant):            # Класс Цветы

    def __init__(self, name):

        super().__init__(name)
        self.edible = False     # съедобность
        self.name = name        # индивидуальное название каждого растения


class Fruit(Plant):             # Класс Фрукты
    def __init__(self, name):

        super().__init__(name)
        self.edible = True  # съедобность
        self.name = name  # индивидуальное название каждого растения


# Выполняемый код(для проверки):
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
# print(a2.name)
print(p1.name)
# print(p2.name)

print(a1.alive)
# print(a2.alive)
# print(a1.fed)
print(a2.fed)

a1.eat(p1)
# a2.eat(p1)
# a1.eat(p2)
a2.eat(p2)

print(a1.alive)
# print(a2.alive)
# print(a1.fed)
print(a2.fed)

"""
Вывод на консоль:
Волк с Уолл-Стрит
Цветик семицветик
True
False
Волк с Уолл-Стрит не стал есть Цветик семицветик
Хатико съел Заводной апельсин
False
True
"""
