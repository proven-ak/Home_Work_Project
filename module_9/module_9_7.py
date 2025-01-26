
# Задание по теме "Декораторы"

# Задание:
# Напишите 2 функции:
# Функция, которая складывает 3 числа (sum_three)
# Функция декоратор (is_prime), которая распечатывает "Простое",
# если результат 1ой функции будет простым числом и "Составное" в противном случае.


def is_prime(func):
    def wrapper(*args, **kwargs):
        res_ = func(*args, **kwargs)
        if res_ > 1:
            for i in range(2, int(res_ ** 0.5) + 1):
                if res_ % i == 0:
                    print("Составное")
                    break
            else:
                print("Простое")
        else:
            print("Составное")
        return res_
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c



# Пример:
result = sum_three(2, 3, 6)
print(result)

# Результат консоли:
# Простое
# 11

# Примечания:
# Не забудьте написать внутреннюю функцию wrapper в is_prime
# Функция is_prime должна возвращать wrapper
# @is_prime - декоратор для функции sum_three
