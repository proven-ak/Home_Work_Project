
class Animal:                   # Класс Животное

    def __init__(self, name):

        self.alive = True       # живой (по умолчанию)
        self.fed = False        # накормленный (по умолчанию)
        self.name = name        # индивидуальное название каждого животного

    def eat(self, food):        # метод Съесть

        # self - параметр, принимающий объекты классов животных
        # food - параметр, принимающий объекты классов растений
        # food.name - название растения
        # food.edible - съедобность растения
        # self.fed - сытость животного
        # self.alive - живое животное

        if food.edible:
            # если растение съедобное
            print(f'{self.name} съел {food.name}')
            self.fed = True

        else:
            # если растение несъедобное
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False


class Plant:                    # Класс Растение

    def __init__(self, name):

        self.edible = False     # съедобность растения (по умолчанию)
        self.name = name        # индивидуальное название каждого растения


class Mammal(Animal):           # Класс Млекопитающее
    pass


class Predator(Animal):         # Класс Хищник
    pass


class Flower(Plant):            # Класс Цветы

    def __init__(self, name):
        super().__init__(name)
        self.edible = False     # съедобность (переопределено)
        self.name = name        # индивидуальное название каждого растения


class Fruit(Plant):             # Класс Фрукты

    def __init__(self, name):
        super().__init__(name)
        self.edible = True      # съедобность (переопределено)
        self.name = name        # индивидуальное название каждого растения


# Выполняемый код(для проверки):
if __name__ == "__main__":

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
