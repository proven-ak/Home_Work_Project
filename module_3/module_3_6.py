# Дополнительное практическое задание по модулю: "Подробнее о функциях".
# Задание "Раз, два, три, четыре, пять .... Это не всё?"

# Входные данные (применение функции):

data_structure = [
    [1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

#data_structure = {1: "a", 2: "b", 3: "c"}       # dict - словарь
#data_structure = {"a", "b", "c"}                # set - множество
#data_structure = ("a", "b", "c")                # tuple - кортеж
#data_structure = [1, 2, 3]                      # list - список
#data_structure = ["a", "b", "c"]                # list - список

result = 0
ddd = ("a", "b", "c")
print(type(ddd))

def calculate_structure_sum(data):
    global result

    if type(data) == dict:
        data = list(data.items())
        print("dict", type(data), data)

    if type(data) == set:
        data = list(data)
        print("set", type(data), data)

    if type(data) == tuple:
        data = list(data)
        print("tuple", type(data), data)

    if type(data) == list:
        print("data", data)
        copy_data = list(data)

        for item in copy_data:

            print("item = ", item, "result = ", result)

            if isinstance(item, (int, float)):
                result += item

            elif isinstance(item, (str)):
                result += len(item)

            else:
                calculate_structure_sum(item)

    print(result)
    print("-------------------")

    return result



result = calculate_structure_sum(data_structure)

print(result)
