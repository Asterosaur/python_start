from abc import ABC, abstractmethod


class Cloth(ABC):

    _name = ""
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @abstractmethod
    def count_fabric(self):
        pass


class Coat(Cloth):

    def count_fabric(self, v):
        return v / 6.5 + .5


class Costume(Cloth):

    def count_fabric(self, h):
        return h * 2 + .3


# test

my_coat = Coat("Пальто")
my_costume = Costume("Костюм")
print(f"{my_coat.name}: {my_coat.count_fabric(170)} ткани")
print(f"{my_costume.name}: {my_costume.count_fabric(120)} ткани")
