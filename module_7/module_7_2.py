# Задача "Записать и запомнить":

def custom_write(file_name, strings):
    # Создаём словарь для записи позиций строк
    strings_positions = {}

    # Открываем файл для записи
    with open(file_name, 'w', encoding='utf-8') as file:

        # Проходим по каждой строке в списке
        for line_number, string in enumerate(strings):
            # enumerate используется для создания итератора, который возвращает кортежи,
            # содержащие индекс и значение каждого элемента из списка strings

            # Получаем текущую позицию в байтах перед записью строки
            byte_position = file.tell()

            # Записываем строку с символом новой строки
            file.write(string + '\n')

            # Добавляем в словарь позицию строки
            strings_positions[(line_number, byte_position)] = string

    return strings_positions


# Пример выполняемого кода
info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
        ]

result = custom_write('test.txt', info)

for elem in result.items():
    print(elem)


"""
Вывод на консоль:
((1, 0), 'Text for tell.')
((2, 16), 'Используйте кодировку utf-8.')
((3, 66), 'Because there are 2 languages!')
((4, 98), 'Спасибо!')
Как выглядит файл после запуска:
"""
