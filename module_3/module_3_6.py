# Дополнительное практическое задание по модулю: "Подробнее о функциях".
# Задание "Раз, два, три, четыре, пять .... Это не всё?"

# Входные данные (применение функции):
data_structure = [
    [1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

# Переменная для промежуточного результата
sum = 0


# Объявляем функцию calculate_structure_sum
def calculate_structure_sum(data):
    # Объявляем глобальную переменную
    global sum

    # Проверяем тип если словарь преобразовываем в список кортежей
    if type(data) == dict:
        data = list(data.items())

    # Проверяем тип если множество преобразовываем в список
    if type(data) == set:
        data = list(data)

    # Проверяем тип если кортеж преобразовываем в список
    if type(data) == tuple:
        data = list(data)

    # Проверяем тип если список создает копию
    if type(data) == list:

        # Перебираем список поэлементно
        for item in data:

            # Проверяем тип элемента, если число прибавляем к результату
            if isinstance(item, (int, float)):
                sum += item

            # Проверяем тип элемента, если строка прибавляем длину строки к результату
            elif isinstance(item, (str)):
                sum += len(item)

            # Иначе повторно обращаемся к функции с этим элементом
            else:
                calculate_structure_sum(item)

    # Возврат результата по завершению функции
    return sum

# Получаем результат
result = calculate_structure_sum(data_structure)

# Выводим результат на консоль
print(result)
