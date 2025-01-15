
# Цель задания:
# Освоить работу с файловой системой в Python, используя модуль os.
# Научиться применять методы os.walk, os.path.join, os.path.getmtime,
# os.path.dirname, os.path.getsize
# и использование модуля time для корректного отображения времени.

import os
import time

# 1. Находим текущую рабочую директорию
directory_path = os.getcwd()

# Обход дерева каталогов
print("\nИщем файл file.txt")
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

            # 5. Используем os.path.dirname для получения родительской директории файла.
            parent_dir = os.path.dirname(filepath)
            file_name = os.path.basename(filepath)

            print(f'Обнаружен файл: {file_name}, Путь: {filepath}, Размер: {file_size} байт, '
                  f'Время изменения: {formatted_time}, \nРодительская директория: {parent_dir}')

# Пример возможного вывода:
# Обнаружен файл: main.py, Путь: ./main.py, Размер: 111 байт, Время изменения: 11.11.1111 11:11,
# Родительская директория.

