
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
        return f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}"

    def attack(self):
        # метод выводит "Sorry, i'm peaceful :)", если степень опасности меньше 5
        if self._DEGREE_OF_DANGER < 5:
            return f"Sorry, i'm peaceful :)"
        # метод выводит "Be careful, i'm attacking you 0_0" , если равно или больше.
        else:
            return f"Be careful, i'm attacking you 0_0"

        # speak(self), который выводит строку со звуком sound.



class Bird(Animal):                 # Класс птиц. Наследуется от Animal
    def __init__(self, beak, sound, ):
        super().__init__(beak)
        super().beak = True         # наличие клюва


    def lay_eggs(self):
        # Выводит строку"Here are(is) <случайное число от 1 до 4> eggs for you"
        re


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
    def __init__(self):
    sound = "Click-click-click"

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
