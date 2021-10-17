"""3
Реализовать функцию my_func(),
которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(arg1, arg2, arg3):
    arr = sorted([arg1, arg2, arg3])
    return arr[1] + arr[2]


print(my_func('56', '2', '4'))
print(my_func(56, 2, 4))
