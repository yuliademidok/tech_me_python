import time
import datetime
import random

# d = datetime.datetime.strptime('12.03.2023', '%d.%m.%Y')
# print(d)
#
# now = datetime.datetime.now()
# print(now.strftime("%H:%m -- %d.%m.%Y"))


# a = ['Bob', 'Nebob', 'Robert']
# print(random.randint(10, 20))
# print(random.choice(a))
#
# random.shuffle(a)
# print(a)


# matrix_1 = [[1, 2, 3, 4], [11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33, 34]]
# matrix_2 = [[11, 12, 13, 14], [211, 212, 213, 214], [321, 322, 323, 324], [431, 432, 433, 434]]
# matrix_sum = []
#
# for rows in zip(matrix_1, matrix_1):
#     row = []
#     for elements in zip(*rows):
#         row.append(sum(elements))
#     matrix_sum.append(row)
#
# print(matrix_sum)



# some_list = ('cat', 'dog', 'rat')
# some_list2 = (1, 2, 3)
# some_dict = dict(zip(some_list2, some_list))
#
# for i in some_dict:
#     print(i)
#
# print(some_dict)


# words = ('hel', 'low', 'frog', 'hello', 'lohel', 'hlelo', 'leh')
# groups = {}
#
# for word in words:
#     sort_world = tuple(sorted(word))
#     if sort_world in groups:
#         groups[sort_world].append(word)
#     else:
#         groups[sort_world] = [word]
#
# print(list(groups.values()))


# example_list = [1, 2, 3, [4, 5, 6, [7, 8, [1, 2, 3]]]]
#
# result = []
# while example_list:
#     i = example_list.pop(0)
#     if isinstance(i, list):
#         result.extend(example_list)
#         example_list = i
#     else:
#         result.append(i)
#
#
# print(result)


# user_word = ['asd', 'fgh', 'jkl']
#
# for idx, i in enumerate(user_word, 1):
#     print(f"{idx}: {i}")




