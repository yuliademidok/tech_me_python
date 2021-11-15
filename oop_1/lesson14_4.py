import datetime


class SomeDecorator:
    def __init__(self, obg):
        self.obg = obg
        self.instance = None

    # def __call__(self, *args, **kwargs):
    #     return self.obg(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        self.instance = self.obg(*args, **kwargs)
        return self

    def __getattr__(self, name):
        print(f"Вызван метод {name}")
        return getattr(self.instance, name)

    # @classmethod
    # def all_deco(cls, obg):
    #     return cls(obg)


class Logger:
    def __init__(self, func, file_path):
        self.func = func
        self.file_path = file_path

    def __call__(self, *args, **kwargs):
        self.__log()
        return self.func(*args, **kwargs)

    def __log(self):
        with open(self.file_path, "a", encoding="UTF-8") as file:
            file.write(f"{datetime.datetime.now()}: {self.func.__name__}")

    @classmethod
    def to_file(cls, file_path):
        return lambda func: cls(func, file_path)


@Logger.to_file("log.txt")
def my_func(a, b):
    return a + b


result = my_func(2, 4)
print(result)


# @SomeDecorator.all_deco
@SomeDecorator
class Human:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def say(self):
        print(f"My name is {self.name} {self.surname}")


# human = Human("Kostya", "Edur")
# human.say()
