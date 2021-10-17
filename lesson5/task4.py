"""4
Функция принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без операторов ** * (без умножения и без возведения в степень).
Можно и нужно использовать сложение (+) и возможно деление (/)
"""


def my_func(arg, degree: int):
    if degree == 0:
        return 1

    # remove fractional part
    fractional_count = 0
    if not isinstance(arg, int):
        integer, fractional = str(arg).split('.')
        arg = int(integer + fractional)
        fractional_count = len(fractional)

    # degree flag
    negative_flag = degree < 0

    # exponentiation
    result = arg
    count = arg
    degree = abs(degree)
    temp_degree = degree

    while temp_degree - 1:
        result += sum(arg for i in range(1, count))

        temp_degree -= 1
        arg = result

    # return fractional part
    temp_degree = degree
    while fractional_count:
        while temp_degree:
            result /= 10
            temp_degree -= 1
        fractional_count -= 1
        temp_degree = degree

    # check degree flag
    if negative_flag:
        result = 1 / result

    return result


print(my_func(13, 0)) # 1
print(my_func(5, -5)) # 0.00032
print(my_func(22, 4)) # 234256
print(my_func(5.23, -4)) # 0.0013365747259081583
print(my_func(5.23, 4)) # 748.1811384100002
