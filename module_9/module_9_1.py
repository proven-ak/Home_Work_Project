
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

        # Добавляем в словарь название функции и результат её работы с int_list
        results[func.__name__] = func(int_list)

    # Возвращаем словарь с результатами
    return results


# Пример результата выполнения программы:

# В примере используются следующие функции:
# min - принимает список, возвращает минимальное значение из него.
# max - принимает список, возвращает максимальное значение из него.
# len - принимает список, возвращает кол-во элементов в нём.
# sum - принимает список, возвращает сумму его элементов.
# sorted - принимает список, возвращает новый отсортированный список на основе переданного.


# Пример работы кода:
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))

print(apply_all_func(["6", "20", "15", "9"], max, min))
print(apply_all_func(["6", "20", "15", "9"], len, sum, sorted))

# Вывод на консоль:
# {'max': 20, 'min': 6} {'len': 4, 'sum': 50, 'sorted': [6, 9, 15, 20]}

# Примечания:
# Для того, чтобы взять название функции можно обратиться к атрибуту __name__
# При попытке передачи, например, списка из строк, некоторые функции могут работать некорректно
# или вовсе не работать. Используйте списки чисел.

