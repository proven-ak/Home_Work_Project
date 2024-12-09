# Самостоятельная работа по уроку Произвольное число параметров.

def single_root_words (root_word, *other_words):

    # Список для хранения слов с совпадением
    same_words = []

    # Перебор всех слов из other_words.
    for root in other_words:

        # Сравнение слов в верхнем регистре для проверки содержания.
        if root_word.upper() in root.upper() or root.upper() in root_word.upper():

            # Если есть совпадение, добавляем слово в список.
            same_words.append(root)

    # Возвращаем список найденных слов
    return same_words

# Тест функции.
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

# Вывод результатов
print(result1)
print(result2)