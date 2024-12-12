def get_matrix(n, m, value):                # Объявляем функцию

    matrix = []                             # Инициируем пустой список
    for i in range(n):                      # Перебираем строку
        row = []                            # Инициируем пустой столбец
        for j in range(m):                  # Перебираем столбец
            if value > 0:                   # Если значение 0 или меньше
                row.append(value)           # заполняем столбец значениями
        matrix.append(row)                  # Заполняем строку столбцами
    return matrix                           # Возвращаем matrix из функции

result = get_matrix(3,                   # Вызов функции
                    5,
                    42)
print(result)                               # Вывод результата на консоль
