
# Задание по теме "Введение в функциональное программирование"

# Эта функция вызывает каждую функцию к переданному списку int_list.
# Возвращает словарь, где ключом будет название вызванной функции,
# а значением - её результат работы со списком int_list.

def apply_all_func(int_list, *functions):

    # int_list - список из чисел (int, float)
    # *functions - неограниченное кол-во функций (которые применимы к спискам, состоящим из чисел)

    # Создаем пустой словарь для результатов
    results = {}

    # Проверяем, что все элементы в int_list - числа
    if not all(isinstance(x, (int, float)) for x in int_list):
        print("Все элементы списка должны быть числами (int или float)")
        return  # Выход из функции, если данные некорректны

    # Перебираем все функции из *functions
    for func in functions:
        try:
            # Пытаемся выполнить функцию с int_list
            results[func.__name__] = func(int_list)
        except Exception as e:
            # В случае ошибки выводим название функции и текст ошибки
            results[func.__name__] = f"Ошибка: {str(e)}"

    # Возвращаем словарь с результатами
    return results


# Пример работы кода:
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))

# Пример работы некорректных данных:
# print(apply_all_func(["6", "20", "15", "9"], max, min))
# print(apply_all_func([6, 20, 15, 9], len, sum, setattr))

# Вывод на консоль:
# {'max': 20, 'min': 6} {'len': 4, 'sum': 50, 'sorted': [6, 9, 15, 20]}
