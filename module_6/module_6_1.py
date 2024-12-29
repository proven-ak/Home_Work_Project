class Animal:                   # Класс Животное

    def __init__(self, name):

        self.alive = True       # живой
        self.fed = False        # накормленный
        self.name = name        # индивидуальное название каждого животного



class Plant:                    # Класс Растение

    def __init__(self, name):

        self.edible = False     # съедобность
        self.name = name        # индивидуальное название каждого растения


class Mammal(Animal):           # Класс Млекопитающее




class Predator(Animal):         # Класс Хищник




class Flower(Plant):            # Класс Цветы




class Fruit(Plant):             # Класс Фрукты
