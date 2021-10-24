#
# def nums(number):
#     result = []
#     a, b = number // 10, number % 10
#
#     pre_result = nums(a) if a else []
#
#     result.extend(pre_result)
#     result.append(b)
#     return result
#
#
# numbers = 12341234
# print(nums(numbers))


# def flat_list(iter_object):
#     result = []
#     for i in iter_object:
#         if isinstance(i, list):
#             result.extend(flat_list(i))
#         else:
#             result.append(i)
#
#     return result
#
#
# some_list = [1, 2, [3, 4, [5, 6, 7, [8, 9, 10]]]]
# print(flat_list(some_list))


# def fibo_gen(stop):
#     memo = [0, 1]
#     for _ in range(stop):
#         result = sum(memo)
#         yield result
#         memo.pop(0)
#         memo.append(result)
#         # yield idx
#
#     return None
#
#
# for idx, i in enumerate(fibo_gen(15)):
#     print(f"{idx}: yield send {i}")
# # some = fibo_gen(15)
# # print(some)


def some_zip(*args):
    idx = 0
    while True:
        result = []
        for i in args:
            try:
                result.append(i[idx])
            except IndexError:
                return None
        yield tuple(result)
        idx += 1


a = [1, 2, 3, 4]
b = [6, 5, 4, 3]
c = [23, 423, 42, 2, 3, 3]

for i in some_zip(a, b, c):
    print(i)
