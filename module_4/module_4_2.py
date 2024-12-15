
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


"""
Возможное решение проблемы:

def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
        
    # Вернуть вложенную функцию из внешней.            
    return inner_function

# Сохраняем вложенную функцию в переменной.
glob_inner_function = test_function()
# В переменной 'glob_inner_function' создали ссылку на объект функции inner_function.

# Вызываем функцию через сохранённую переменную.
glob_inner_function()
"""







