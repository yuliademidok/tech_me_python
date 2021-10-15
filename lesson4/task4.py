# Дано 2 целых числа, написать алгоритм поиска наибольшего общего делителя

a = 12
b = 20

min_range = range(min(a, b), 0, -1)
result = 1

for i in min_range:
    if a % i == 0 and b % i == 0:
        result = i
        break

print(result)
