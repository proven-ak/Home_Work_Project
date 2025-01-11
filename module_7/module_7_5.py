
# Цель задания:
# Освоить работу с файловой системой в Python, используя модуль os.
# Научиться применять методы os.walk, os.path.join, os.path.getmtime, os.path.dirname, os.path.getsize и использование модуля time для корректного отображения времени.

# Код из вебинара
import os
print('текущая дирeктория: ', os.getcwd())
if os.path.exists('second'):
  os.chdir('second')
else:
  os.mkdir('second')
  os.chdir('second')
print('текущая дирeктория: ', os.getcwd())
os.chdir(r'C:\Users\User\PycharmProjects\Home_Work_Project\module_7')
print('текущая дирeктория: ', os.getcwd())
file = [f for f in os.listdir() if os.path.isfile(f)]
dirs = [d for d in os.listdir() if os.path.isfile(d)]
print('dirs = ', dirs)
print('file = ', file)

# Используем os.walk для обхода каталога, путь к которому указывает переменная directory


# Применяем os.path.join для формирования полного пути к файлам.


# Используем os.path.getmtime и модуль time для получения и отображения времени последнего изменения файла.


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

