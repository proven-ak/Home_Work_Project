
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

class Sedan(Vehicle):
    pass

