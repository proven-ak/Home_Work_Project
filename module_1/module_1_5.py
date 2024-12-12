
# Создадим переменную immutable_var и запишем в нее кортеж
immutable_var = (1, 3.3, "hello", True)

# Выведем переменную immutable_var на консоль
print(immutable_var)

# immutable_var[1] = 3    Элементы кортежа не изменяемые. Нельзя второй элемент кортежа 3.3 заменить на 3

# Создадим переменную mutable_list и запишем в нее список
mutable_list = [1, 3.3, "hello", True]

# Добавим к списку новый элемент в виде списка
mutable_list.append([1, 2, 3])

# Выведем обновленный список на консоль
print(mutable_list)