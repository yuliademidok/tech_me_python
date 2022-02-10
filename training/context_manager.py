class Vector:
    def __init__(self, v):
        self.__v = v

    def __enter__(self):
        self.__temp = self.__v[:]
        return self.__temp

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not exc_type:
            self.__v[:] = self.__temp


v1 = [2, 3, 4]
v2 = [1, 2]


try:
    with Vector(v1) as vector:
        for i, j in enumerate(v1):
            vector[i] += v2[i]
except IndexError:
    pass

print(v1)
