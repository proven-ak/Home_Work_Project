# Ввод 3-х чисел
first = int(input())
second = int(input())
third = int(input())

# Проверка чисел на совпадение
if first == second and first == third and second == third:
    result = 3
elif first == second:
    result = 2
elif first == third:
    result = 2
elif second == third:
    result = 2
else:
    result = 0

# Вывод результата на консоль!!!
print(result)
