# Задание:
# Создайте новый проект или продолжите работу в текущем проекте.
# Напишите код, который форматирует строки для следующих сценариев.
# Укажите переменные, которые должны быть вставлены в каждую строку:

# Входные данные:
team1_num = 5                   # Количество участников команды 1
team2_num = 6                   # Количество участников команды 2
score_1 = 40                    # количество задач решённых командой 1
score_2 = 42                    # количество задач решённых командой 2
team1_time = 1552.512           # время за которое команда 1 решила задачи
team2_time = 2153.31451         # время за которое команда 2 решила задачи
tasks_total = 82                # количество задач
time_avg = 45.2                 # среднее время решения
challenge_result = ""           # исход соревнования

# Определение исхода соревнования
if score_1 > score_2 or (score_1 == score_2 and team1_time > team2_time):
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or (score_1 == score_2 and team1_time < team2_time):
    challenge_result = 'Победа команды Волшебники данных!'
else:
    challenge_result = 'Ничья!'

# Использование %:
# 1. Количество участников первой команды (team1_num)
team1_string = "В команде Мастера кода участников: %d !" % team1_num

# 2. Строка с количеством участников в обеих командах (team1_num, team2_num).
teams_string = "Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num)

# Использование format():
# 3. Количество задач решённых командой 2 (score_2).
score_2_string = "Команда Волшебники данных решила задач: {} !".format(score_2)

# 4. Время за которое команда 2 решила задачи (team1_time).
team2_time_string = "Волшебники данных решили задачи за {:.1f} с !".format(team2_time)

# Использование f-строк:
# 5. Количество решённых задач обеими командами (score_1, score_2).
scores_string = f"Команды решили {score_1} и {score_2} задач."

# 6. Исход соревнования (challenge_result).
challenge_result_string = f"Результат битвы: {challenge_result}"

# Комментарии к заданию:
# В русском языке окончания слов меняются (1 участник, 2 участника),
# пока что давайте не обращать на это внимания.
# Переменные challenge_result, tasks_total, time_avg можно задать вручную или рассчитать.
# На пример, для challenge_result:
#
    # if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    #   result = ‘Победа команды Мастера кода!’
    # elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    #   result = ‘Победа команды Волшебники Данных!’
    # else:
    #   result = ‘Ничья!’

# Вывод результатов
print(team1_string)
print(teams_string)
print(score_2_string)
print(team2_time_string)
print(scores_string)
print(challenge_result_string)
