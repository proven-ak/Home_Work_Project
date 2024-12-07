calls = 0


# Функция подсчета вызовов
def count_calls():
    global calls
    calls += 1


# Функция возвращает кортеж из: длины этой строки, строку в верхнем регистре,
# строку в нижнем регистре
def string_info(string):
    count_calls()
    return len(string), string.upper(), string.lower()


# Функция принимает два аргумента: строку и список, и
# возвращает True, если строка находится в этом списке,
# False - если отсутствует
def is_contains(string, list_to_search):
    count_calls()
   # переводим строки списка в верхний регистр
    up_list_to_search = [list_.upper() for list_ in list_to_search]
    return string.upper() in up_list_to_search

# Проверка
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)