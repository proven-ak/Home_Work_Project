# Самостоятельная работа по уроку Произвольное число параметров.

# Функция для поиска слов
def single_root_words (root_word, *other_words):

    # Список для хранения слов с совпадением
    same_words = []

    # Переводим строку в верхний регистр
    root_word_upper = root_word.upper()

    # Перебор всех слов из other_words.
    for word in other_words:

        # Сравнение слов в верхнем регистре для проверки содержания.
        if word.upper() in root_word_upper or root_word_upper in word.upper():

            # Если есть совпадение, добавляем слово в список.
            same_words.append(word)

    # Возвращаем список найденных слов
    return same_words


# Тест функции.
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

# Вывод результатов
print(result1)
print(result2)