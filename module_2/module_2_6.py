# Ввод данных
first_num = int(input("Введите число от 3 до 20 : "))

# Инициация переменных
result = ""
pass_list = []

for i in range(1, 20):                      # выбираем 1-е число
    for j in range(i + 1, 20):              # выбираем 2-е число
        if first_num % (i + j) == 0:        # проверяем делимость
            str_ = str(i) + str(j)          # склеиваем символы 2-х чисел
            pass_list.append(str_)          # создаем список пар
            result = "".join(pass_list )    # склеиваем список в строку

print(result)                               # выводим результат на консоль

