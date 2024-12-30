
class Vehicle:
    def __init__(self, owner, _model, __engine_power, __color):

        self.owner = owner                      # владелец транспорта (изменяемый)
        self._model = _model                    # модель(марка)транспорта (не изменяемый)
        self.__engine_power = __engine_power    # мощность двигателя (не изменяемый)
        self.__color = __color                  # название цвета (не изменяемый)

        self.__COLOR_VARIANTS = ["Red", "Blue", "Black", "White"]

    def get_model(self):            # возвращает строку: "Модель: <название модели транспорта>"
        pass

    def get_horsepower(self):       # возвращает строку: "Мощность двигателя: <мощность>"
        pass

    def get_color(self):            # возвращает строку: "Цвет: <цвет транспорта>"
        pass

    def print_info(self):           # распечатывает результаты методов(в том же порядке):
        pass                        # get_model, get_horsepower, get_color;

    def set_color(self, new_color):
        # принимает аргумент new_color(str), меняет цвет __color на new_color, если
        # он есть в списке __COLOR_VARIANTS, в противном случае выводит на экран надпись:
        # "Нельзя сменить цвет на <новый цвет>".

        if new_color in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    pass


"""

    Каждый объект Vehicle должен содержать следующий методы:


    а так же владельца в конце в формате "Владелец: <имя>"
    
    

"""