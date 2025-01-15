
# Цель задания:
# Освоить работу с файловой системой в Python, используя модуль os.
# Научиться применять методы os.walk, os.path.join, os.path.getmtime,
# os.path.dirname, os.path.getsize
# и использование модуля time для корректного отображения времени.

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

# Обход дерева каталогов
print("\nИщем файл file.txt:\n")
for root, dirs, files in os.walk(directory_path):
    for file in files:
        if file == "file.txt":  # Проверяем имя файла

            # 2. Применяем os.path.join для формирования полного пути к файлам.
            filepath = os.path.join(root, file)

            # 3. Используем os.path.getmtime и модуль time для получения
            #    и отображения времени последнего изменения файла.
            filetime = os.path.getmtime(filepath)
            formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))

            # 4. Используем os.path.getsize для получения размера файла.
            file_size = os.path.getsize(filepath)
            print('Размер файла:', file_size)

            # 5. Используем os.path.dirname для получения родительской директории файла.
            parent_dir = os.path.dirname(filepath)
            file_name = os.path.basename(filepath)

            print(f'Обнаружен файл: {file_name}, Путь: {filepath}, Размер: {file_size} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')

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

