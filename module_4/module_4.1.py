# Домашняя работа по уроку "Модули и пакеты"

# Импортируем модули
from fake_math import divide as fake_divide
from true_math import divide as true_divide

# Используем функцию из fake_math для выполнения деления
result1 = fake_divide(69, 3)
result2 = fake_divide(3, 0)

# Используем функцию из true_math для выполнения деления
result3 = true_divide(49, 7)
result4 = true_divide(15, 0)

# Выводим результаты на консоль
print(result1)
print(result2)
print(result3)
print(result4)
