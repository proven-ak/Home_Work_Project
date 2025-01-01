
import random


class Animal:               # Класс животных
    def __init__(self, speed):

        self.live = True                # живое (по умолчанию True)
        self.sound = None               # звук(по умолчанию отсутствует)
        self._DEGREE_OF_DANGER = 0      # степень опасности существа (по умолчанию 0)

        self._cords = [0, 0, 0]         # координаты в пространстве(по умолчанию [0, 0, 0])
        self.speed = speed              # скорость передвижения существа (определяется при создании объекта)

    """
    Необходимо написать 5 классов:
    Animal - класс описывающий животных.
    Класс обладает следующими атрибутами:
    live = True
    sound = None - звук (изначально отсутствует)
    _DEGREE_OF_DANGER = 0 - степень опасности существа
    
    Объект этого класса обладает следующими атрибутами:
    _cords = [0, 0, 0] - координаты в пространстве.
    speed = ... - скорость передвижения существа (определяется при создании объекта)
    
    И методами:
    move(self, dx, dy, dz), который должен менять соответствующие координаты в _cords на dx, dy и dz в том же порядке, где множетелем будет являтся speed. Если при попытке изменения координаты z в _cords значение будет меньше 0, то выводить сообщение "It's too deep, i can't dive :(" , при этом изменения не вносяться.
    get_cords(self), который выводит координаты в формате: "X: <координаты по x>, Y: <координаты по y>, Z: <координаты по z>"
    attack(self), который выводит "Sorry, i'm peaceful :)", если степень опасности меньше 5 и "Be careful, i'm attacking you 0_0" , если равно или больше.
    speak(self), который выводит строку со звуком sound.
    """
    def move(self, dx, dy, dz):         # изменение координат
        # Изменение координат с учетом скорости
        # dx - смещение по оси X
        # dy - смещение по оси Y
        # dz - смещение по оси Z

        # Проверяем возможность изменения координаты Z
        new_z = self._cords[2] + dz * self.speed            # смещение по оси Z
        if new_z < 0:
            print("It's too deep, I can't dive :(")
        else:
            self._cords[0] += dx * self.speed               # смещение по оси X
            self._cords[1] += dy * self.speed               # смещение по оси Y
            self._cords[2] = new_z                          # смещение по оси Z

        # Метод должен менять соответствующие координаты
        # в _cords на dx, dy и dz в том же порядке, где множителем будет являться speed.
        # Если при попытке изменения координаты z в _cords значение будет меньше 0,
        # то выводить сообщение "It's too deep, i can't dive :(", при этом изменения не вносятся.

    def get_cords(self):
        # метод выводит координаты в формате:
        # "X: <координаты по x>, Y: <координаты по y>, Z: <координаты по z>"
        print(f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}")

    def attack(self):
        # метод выводит "Sorry, i'm peaceful :)", если степень опасности меньше 5
        if self._DEGREE_OF_DANGER < 5:
            return "Sorry, i'm peaceful :)"
        # метод выводит "Be careful, i'm attacking you 0_0" , если равно или больше.
        else:
            return "Be careful, i'm attacking you 0_0"

    def speak(self):
        # метод выводит звук
        print(self.sound)


class Bird(Animal):
    # Класс птиц. Наследуется от Animal
    """
    Bird - класс описывающий птиц. Наследуется от Animal.
    Должен обладать атрибутом:
    beak = True - наличие клюва
    И методом:
    lay_eggs(self), который выводит строку "Here are(is) <случайное число от 1 до 4> eggs for you"
    """

    def __init__(self, speed):
        """
        Инициализация объекта Bird.
        :param speed: Скорость передвижения птицы.
        """
        super().__init__(speed)  # Инициализация родительского класса Animal
        self.beak = True  # Атрибут наличия клюва

    def lay_eggs(self):             # откладывание яиц
        # выводит количество снесенных яиц.
        eggs = random.randint(1, 4)  # Случайное число от 1 до 4
        print(f"Here are(is) {eggs} eggs for you")


class AquaticAnimal(Animal):        # Класс плавающего животного. Наследуется от Animal
    """
    В этом классе атрибут _DEGREE_OF_DANGER = 3.
    Должен обладать методом:
    dive_in(self, dz) - где dz изменение координаты z в _cords.
    Этот метод должен всегда уменьшать координату z в _coords.
    Чтобы сделать dz положительным, берите его значение по модулю (функция abs).
    Скорость движения при нырянии должна уменьшаться в 2 раза,
    в отличии от обычного движения. (speed / 2)
    """
    def __init__(self, speed):
        super().__init__(speed)
        self._DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        dz = abs(dz)  # Всегда работаем с положительным значением dz
        new_z = self._cords[2] - dz * (self.speed / 2)  # Уменьшение Z с учётом уменьшенной скорости
        if new_z < 0:
            print("It's too deep, I can't dive :(")
        else:
            self._cords[2] = new_z  # Применяем новое значение Z


class PoisonousAnimal(Animal):           # Класс ядовитых животных. Наследуется от Animal.
    """
    В этом классе атрибут _DEGREE_OF_DANGER = 8.
    """
    def __init__(self, speed=None):
        super().__init__(speed)
        self._DEGREE_OF_DANGER = 8


class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):                 # класс утконоса.

    def __init__(self, speed):
        Animal.__init__(self, speed)
        Bird.__init__(self, speed)  # Инициализация от Bird (клюв и скорость)
        AquaticAnimal.__init__(self, speed)  # Инициализация от AquaticAnimal (плавание и скорость)
        PoisonousAnimal.__init__(self, speed)  # Инициализация от PoisonousAnimal (ядовитость)

        self.sound = "Click-click-click"

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

