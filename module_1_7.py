# Начальные данные
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# Преобразуем множество students в список
students = list(students)

# Сортируем students в алфавитный порядок
sort_students = students.sort()

# Создаем переменную для списка средних оценок
list_grades = []

# Формируем список средних оценок
for sub_grades in grades:
    average_grades = sum(sub_grades) / len(sub_grades)
    list_grades.append(average_grades)

# Создаем словарь
dict_grades = dict(zip(students, list_grades))

# Выводим на консоль
print(dict_grades)