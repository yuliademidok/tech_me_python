"""
Дано 2 Матрицы
Необходимо получить произведение данных матриц
"""

matrix_1 = [[1, 2, 4],
            [2, 0, 3]]

matrix_2 = [[2, 5],
            [1, 3],
            [1, 1]]

transposed_2 = tuple(zip(*matrix_2))

result = []

for i in matrix_1:
    for j in transposed_2:
        result.append(sum(x * y for x, y in zip(i, j)))

print(result)
