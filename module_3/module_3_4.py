# Самостоятельная работа по уроку Произвольное число параметров.

def single_root_words (root_word, *other_words):
    same_words = []

    for root in other_words:

        if root_word.upper() in root.upper() or root.upper() in root_word.upper():

            same_words.append(root)

            print("+++++", root_word, root)

        else:

            print("-----", root_word, root)

    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
print("--------------")
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print("--------------")
print(result1)
print(result2)