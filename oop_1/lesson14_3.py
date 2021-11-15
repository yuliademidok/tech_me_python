from abc import ABC, abstractmethod


class SomePeople(ABC):

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def say(self, data: str) -> None:
        pass


class Person(SomePeople):
    def __init__(self):
        self.name = "SOME"

    def get_name(self) -> str:
        return self.name

    def say(self, data: str) -> None:
        print(data)


human = Person()
human.say("Hello")
