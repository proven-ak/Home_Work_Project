
class Animal:               # Класс животных
    def __init__(self,live, sound, _DEGREE_OF_DANGER, speed):
        self.live = True                #
        self.sound = None               # звук(изначально отсутствует)
        self._DEGREE_OF_DANGER = 0      # степень опасности существа

        self._cords = [0, 0, 0]         # координаты в пространстве
        self.speed = speed              # скорость передвижения существа


    def move(self, dx, dy, dz):         # изменение координат

        # Метод должен менять соответствующие координаты
        # в _cords на dx, dy и dz в том же порядке, где множителем будет являться speed.
        # Если при попытке изменения координаты z в _cords значение будет меньше 0,
        # то выводить сообщение "It's too deep, i can't dive :(", при этом изменения не вносятся.

        self.dx = dx
        self.dy = dy
        self.dz = dz


    def get_cords(self):

        # который выводит координаты в формате:
        # "X: <координаты по x>, Y: <координаты по y>, Z: <координаты по z>"
        # attack(self), который выводит "Sorry, i'm peaceful :)", если степень опасности меньше 5
        # и "Be careful, i'm attacking you 0_0" , если равно или больше.
        # speak(self), который выводит строку со звуком sound.



class Bird(Animal):                 # Класс птиц. Наследуется от Animal
    def __init__(self, beak):
        super()__init__(beak)
        super().beak = True         # наличие клюва


    def lay_eggs(self):
        # Выводит строку"Here are(is) <случайное число от 1 до 4> eggs for you"
        pass


class AquaticAnimal:        # Класс плавающего животного. Наследуется от Animal
    """
    В этом классе атрибут _DEGREE_OF_DANGER = 3.

    Должен обладать методом:
    dive_in(self, dz) - где dz изменение координаты z в _cords.
    Этот метод должен всегда уменьшать координату z в _coords.
    Чтобы сделать dz положительным, берите его значение по модулю (функция abs).
    Скорость движения при нырянии должна уменьшаться в 2 раза,
    в отличии от обычного движения. (speed / 2)
    """


class PoisonousAnimal:           # Класс ядовитых животных. Наследуется от Animal.
    """
    В этом классе атрибут _DEGREE_OF_DANGER = 8.
    """


class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):                 # класс утконоса.

    """
    Порядок наследования определите сами, опираясь на ниже приведённые примеры выполнения кода.

    Объект этого класса должен обладать одним дополнительным атрибутом:
    sound = "Click-click-click" - звук, который издаёт утконос
    """

# Пример работы программы:

db = Duckbill(10)
print(db.live)
print(db.beak)
db.speak()
db.attack()
db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()
db.lay_eggs()

"""
Вывод на консоль:
True
True
Click-click-click
Be careful, i'm attacking you 0_0
X: 10 Y: 20 Z: 30
X: 10 Y: 20 Z: 0
Here are(is) 3 eggs for you # Число может быть другим (1-4)
"""
=======
class Animal:

    pass


class Bird:

    pass


class AquaticAnimal:

    pass


class PoisonousAnimal:

    pass


class Duckbill:

    pass
>>>>>>> origin/master
