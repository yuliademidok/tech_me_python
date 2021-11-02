import random


# user_name = ["Gauss", "Bill", "Illon", "R2D2"]
# homes = ["Berlin", "LA", "Death Star"]
#
# users = [
#     {
#         "name": random.choice(user_name),
#         "age": random.randint(30, 80),
#         "home": random.choice(homes),
#     }
#     for _ in range(20)
# ]
# delim = ','

# file = open("users", "w", encoding="UTF-8")
# try:
#     for idx, itm in enumerate(users):
#         if not idx:
#             file.write(f"{delim.join(itm.keys())}\n")
#         file.write(f"{delim.join(map(str, itm.values()))}\n")
# except Exception as exc:
#     pass
# finally:
#     file.close()


# result = []
# keys = []
# file = open("users", 'r', encoding="UTF-8")
#
# # переместиться на конец 1й строки
# for idx, line in enumerate(file):
#     if not idx:
#         keys = line[:-1].split(delim)
#     else:
#         values = line[:-1].split(delim)
#         result.append(dict(zip(keys, values)))
# file.close()
# print(result)



# file = open("test_file", "r")
#
# try:
#     file.seek(0, 2)
#     data = file.read()
#     print(file.tell())
#     # data2 = file.read(3)
# except Exception as exc:
#     pass
# finally:
#     file.close()
#

from typing import List

prices: tuple[int, ...] = (1, 2)
