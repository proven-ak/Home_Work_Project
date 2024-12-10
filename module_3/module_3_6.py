# Дополнительное практическое задание по модулю: "Подробнее о функциях".
# Задание "Раз, два, три, четыре, пять .... Это не всё?"

# Входные данные (применение функции):
# data_structure = [
#     [1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello",
#     ((), [{(2, 'Urban', ('Urban2', 35))}])
# ]

#data_structure = {1: "a", 2: "b", 3: "c"}         # dict - словарь
#data_structure = {"a", "b", "c"}                # set - множество
#data_structure = [1, 2, 3]                      # list - список
data_structure = ["a", "b", "c"]                # list - список

result = 0


def calculate_structure_sum(data):

    global result

    if type(data) == dict:

        print("dict", type(data))
        data = list(data.items())
        print("dict", type(data), data)

    elif type(data) == set:

        print("set", type(data))
        data = list(data)
        print("set", type(data), data)

    if type(data) == list:

        num_data = [item for item in data if isinstance(item, (int, float))]
        str_data = [item for item in data if isinstance(item, (str))]

        result += len(num_data) + len(str_data)

        print(num_data, str_data)
        print(len(num_data), len(str_data))

        print("list", type(data), data)






    # if type(data) == "set":
    #     print("set", type(data))
    #
    # if type(data) == "list":
    #
    #     if type(data) == "str":
    #         print("str", type(data))
    #
    #     elif type(data) == "int":
    #         print("str", type(data))

result = calculate_structure_sum(data_structure)

print(result)