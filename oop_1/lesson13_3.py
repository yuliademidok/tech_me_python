import random


class SQMatrix:
    def __init__(self, data):
        self.size = len(data)
        # self._data = [[random.randint(1, 100) for _ in range(n)] for _ in range(n)]
        self._data = data

    def __add__(self, other):
        if isinstance(other, SQMatrix):
            return self._add_matrix__(other)
        elif isinstance(other, (int, float)):
            return self._add_digit__(other)

    def _add_digit__(self, num):
        return SQMatrix([[i + num for i in row] for row in self._data])

    def _add_matrix__(self, matrix):
        return SQMatrix([[sum(values) for values in zip(*pair)] for pair in zip(self._data, matrix._data)])


matrix_1 = SQMatrix([[random.randint(1, 100) for _ in range(4)] for _ in range(4)])
matrix_2 = SQMatrix([[random.randint(1, 100) for _ in range(4)] for _ in range(4)])
matrix_3 = matrix_1 + matrix_2
matrix_4 = matrix_1 + 3
print(matrix_1._data)
print(matrix_3._data)
print(matrix_4._data)

some = {matrix_1, matrix_2, matrix_3}
print(some)
