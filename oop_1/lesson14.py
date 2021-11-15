class Some:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, data):
        if self.__a > data:
            raise ValueError("ERROR!!")
        self.__a = data


some = Some(1, 2)
print(some.a)

some.a = 22
print(some.a)
some.a = 0
print(some.a)
