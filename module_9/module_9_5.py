
# Задание по теме "Итераторы"

# Создание пользовательского исключения
class StepValueError(Exception):
    pass


class Iterator():

    # start - целое число, с которого начинается итерация.
    # stop - целое число, на котором заканчивается итерация.
    # step - шаг, с которым совершается итерация.
    # pointer - указывает на текущее число в итерации (изначально start)

    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start

        # Проверка на нулевой шаг
        if self.step == 0:
            raise StepValueError('шаг не может быть равен 0')

    def __iter__ (self):
        # сброс значение pointer на start и возвращающий сам объект итератора.
        self.pointer = self.start
        return self

    def __next__(self):
        # увеличение атрибута pointer на step. В зависимости от знака атрибута step
        if self.step > 0:
            if self.pointer >= self.stop:
                raise StopIteration
            current = self.pointer
            self.pointer += self.step
            return current

        # Если шаг отрицательный, проверяем, не пересекли ли мы stop
        elif self.step < 0:
            if self.pointer <= self.stop:
                raise StopIteration
            current = self.pointer
            self.pointer += self.step
            return current

# Пример выполняемого кода:
try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
for i in iter2:
    print(i, end=' ')
print()

iter3 = Iterator(6, 15, 2)
for i in iter3:
    print(i, end=' ')
print()


iter4 = Iterator(5, 1, -1)
for i in iter4:
    print(i, end=' ')
print()

iter5 = Iterator(10, 1)
for i in iter5:
    print(i, end=' ')
print()

# Вывод на консоль:
# Шаг указан неверно
# -5 -4 -3 -2 -1 0 1
# 6 8 10 12 14
# 5 4 3 2 1

# Примечания:
# Особое внимание уделите методу __next__ и условиям в нём.

