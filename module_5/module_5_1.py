class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            print(new_floor)
        else:
            print("Такого этажа не существует")


h1 = House('Вишневый сад', 14)
h2 = House('Алексеевский', 9)
h3 = House('Равновесие', 5)

h1.go_to(1)
h2.go_to(2)
h3.go_to(3)
h1.go_to(4)
h2.go_to(5)
h3.go_to(6)