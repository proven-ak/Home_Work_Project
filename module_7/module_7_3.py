# Задача "Найдёт везде":

# Напишите класс WordsFinder, объекты которого создаются следующим образом:
# WordsFinder('file1.txt, file2.txt', 'file3.txt', ...).
# Объект этого класса должен принимать при создании неограниченного количество
# названий файлов и записывать их в атрибут file_names в виде списка или кортежа.

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        # get_all_words - подготовительный метод, который возвращает словарь следующего вида:
        # {'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4'],
        #  'file3.txt': ['word5', 'word6', 'word7']}
        #
        # Где:
        # 'file1.txt', 'file2.txt', ''file3.txt'' - названия файлов.
        # ['word1', 'word2'], ['word3', 'word4'], ['word5', 'word6', 'word7']
        # - слова содержащиеся в этом файле.

        # Создаем пустой словарь.
        all_words = {}

        # Перебираем названия файлов и открываем каждый из них, используя оператор with.
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:

                # Для каждого файла считываем единые строки, переводя их в нижний регистр
                content = file.read().lower()

                # Избавляемся от пунктуации [',', '.', '=', '!', '?',';',':',' - '] в строке.
                for symbol in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    content = content.replace(symbol, ' ')

                    # Разбиваем эту строку на элементы списка методом split().
                    # (разбивается по умолчанию по пробелу)
                    words = content.split()

                    # Сохраняем список слов в словарь
                    all_words[file_name] = words

                    return all_words

    def find(self, word):
        # find(self, word) - метод, где word - искомое слово. Возвращает словарь,
        # где ключ - название файла, значение - позиция первого такого слова в списке слов этого файла.

        word_positions = {}
        word = word.lower()

        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            if word in words:
                word_positions[file_name] = words.index(word) + 1  # 1-based index
            else:
                word_positions[file_name] = None
        return word_positions

    def count(self, word):
        # count(self, word) - метод, где word - искомое слово. Возвращает словарь,
        # где ключ - название файла, значение - количество слова word в списке слов этого файла.

        word = word.lower()
        word_counts = {}
        all_words = self.get_all_words()

        for file_name, words in all_words.items():
            word_counts[file_name] = words.count(word)
        return word_counts


# Пример выполнения программы:
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())                  # Все слова
print(finder2.find('TEXT'))                     # 3 слово по счёту
print(finder2.count('teXT'))                    # 4 слова teXT в тексте всего

"""
Вывод на консоль:
{'test_file.txt': ["it's", 'a', 'text', 'for', 'task', 'найти', 'везде', 'используйте', 'его', 'для', 'самопроверки', 'успехов', 'в', 'решении', 'задачи', 'text', 'text', 'text']}
{'test_file.txt': 3}
{'test_file.txt': 4}
"""

# Запустите этот код с другими примерами предложенными здесь.
# Если решение верное, то результаты должны совпадать с предложенными.

# Примечания:
# Регистром слов при поиске можно пренебречь. ('teXT' ~ 'text')
# Решайте задачу последовательно - написав один метод, проверьте результаты его работы.

