# def my_sum(*args, start=0):
#     """
#     Return a sum of start number (default: 0) and objects
#     """
#     for i in args:
#         start += i
#     return start
#
#
# print(my_sum(59, 2, 3))


# def my_enumerate(iter_obj, start=0):
#     result = zip(range(start, start + len(iter_obj)), iter_obj)
#     return tuple(result)
#
#
# print(my_enumerate([4, 5, 6]))



# hello = [1, 2, 3, 4]
#
# def example_func(some_list):
#     # some_list = some_list[:]
#     sum_list = sum(some_list)
#     some_list.append(sum_list)
#     return some_list
#
# result = example_func(hello)
# print(result)
# print(hello)
# print(result == hello)


# hello = [1, 2, 3, 4]
#
# def example_func():
#     return sum(hello)
#
# print(example_func())


# hello = [1, 2, 3, 4]
#
# def example_func():
#     global hello
#     hello = [23, 32]
#     return sum(hello)
#
# print(example_func())
# print(hello)


# a = 22
# b = 5
# c = b if b > a else 15
#
# print(c)



# def mul(a, b):
#     return a * b
#
#
# def div(a, b):
#     return a / b
#
#
# some_list = [2, 3, 4, 5, 6, 7, 8]
#
#
# def my_reduce(func, iter_object):
#     flag = True
#     result = None
#     for i in iter_object:
#         if flag:
#             result = i
#             flag = not flag
#             continue
#         result = func(result, i)
#     return result
#
#
# print(my_reduce(mul, some_list))
#
# import functools
# print(functools.reduce(div, some_list))


# some_list = (2, 3, 4, 5, 6, 7, 8)
# some_list_2 = (6, 7, 8, 9)
# result = list(map(sum, zip(some_list, some_list_2)))
# print(result)


# some_list = (2, 3, 4, 5, 6, 7, 8)
# result = list(map(lambda n: n ** 2 if n & 1 else n ** 3, some_list))
# print(result)


# anon_func = (lambda x: x**2)(3)
# print(anon_func)
# print((lambda x: x**2)(3))


a = [0, 0, 1, 0, 1, 1, 0]
print(any(a))
print(all(a))
