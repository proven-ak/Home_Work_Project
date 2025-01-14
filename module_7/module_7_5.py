
# Цель задания:
# Освоить работу с файловой системой в Python, используя модуль os.
# Научиться применять методы os.walk, os.path.join, os.path.getmtime,
# os.path.dirname, os.path.getsize
# и использование модуля time для корректного отображения времени.

# Код из вебинара
# os.getcwd()         - Возвращает текущую рабочую директорию.
# os.path.exists('')  - Проверяет, существует ли файл или папка по указанному пути. True, если существует, или False.
# os.chdir('')        - Изменяет текущую рабочую директорию на указанную. Путь должен указывать
#                       на существующую директорию, иначе возникнет ошибка.
# os.listdir()        - Возвращает список файлов и папок в указанной директории. Если путь не указан,
#                       используется текущая рабочая директория.
# os.path.isfile(f)   - Проверяет, является ли указанный путь файлом. Возвращает True,
#                       если это файл, и False в остальных случаях (например, если это папка).

# print('текущая дирeктория: ', os.getcwd())
# if os.path.exists('second'):
#   os.chdir('second')
# else:
#   os.mkdir('second')
#   os.chdir('second')
# print('текущая дирeктория: ', os.getcwd())
# os.chdir(r'C:\Users\User\PycharmProjects\Home_Work_Project\module_7')
# print('текущая дирeктория: ', os.getcwd())
# file = [f for f in os.listdir() if os.path.isfile(f)]
# dirs = [d for d in os.listdir() if os.path.isfile(d)]
# print('dirs = ', dirs)
# print('file = ', file)

# os.walk             - Рекурсивно обходит дерево каталогов, начиная с указанной директории.
#                       Возвращает кортеж из трёх элементов для каждой директории
# os.path.join        - Объединяет несколько частей пути в один корректный путь.
#                       Учитывает особенности операционной системы (например, косые черты в Windows и Linux).
# os.path.getmtime    - Возвращает время последнего изменения файла или каталога (в виде таймстампа).
#                       Таймстамп можно преобразовать в понятный формат с помощью модуля datetime.
# os.path.dirname     - Возвращает путь к директории, содержащей указанный файл или путь.
# os.path.getsize     - Возвращает размер файла (в байтах).

import os
import time
# Находим текущую рабочую директорию
directory_path = os.getcwd()
print('directory_path = ', directory_path)

# 1. Используем os.walk для обхода каталога, путь к которому указывает переменная directory
directory = os.walk(directory_path)
print('directory = ', directory)

# Применяем os.path.join для формирования полного пути к файлам.
path = os.path.join('C:\\Users', 'User', 'Documents', 'file.txt')
print(path)

# Используем os.path.getmtime и модуль time для получения и отображения времени последнего изменения файла.
# Проверяем, существует ли файл
if not os.path.exists(path):
    # Создаем файл, если он отсутствует
    with open(path, 'w') as file:
        file.write('')  # Пустой файл
# Получаем время последнего изменения файла
filetime = os.path.getmtime(path)
formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
print('Время последнего изменения файла:', formatted_time)

# Используем os.path.getsize для получения размера файла.


# Используем os.path.dirname для получения родительской директории файла.



# Комментарии к заданию:
# Ключевая идея – использование вложенного for
"""
for root, dirs, files in os.walk(directory):
  for file in files:
    filepath = ?
    filetime = ?
    formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
    filesize = ?
    parent_dir = ?
    print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')

"""

# Так как в разных операционных системах разная схема расположения папок, тестировать проще всего
# в папке проекта (directory = “.”)

# Пример возможного вывода:
# Обнаружен файл: main.py, Путь: ./main.py, Размер: 111 байт, Время изменения: 11.11.1111 11:11,
# Родительская директория.

