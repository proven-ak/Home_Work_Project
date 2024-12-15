
# Внешняя функция.
def test_function():

    # Вложенная функция.
    def inner_function():

        # Вывод сообщения на консоль.
        print("Я в области видимости функции test_function")

    # Вызов функции из локального пространства имен функции 'test_function'.
    inner_function()
    # На консоль выведено сообщение "Я в области видимости функции test_function".

# Вызов функции из глобального пространства имен.
inner_function()
# Вызов функции вызвал ошибку 'name 'inner_function' is not defined'.
# Имя функции 'inner_function' находится в локальном пространстве имен функции 'test_function'.






