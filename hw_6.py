from hw_5 import *


class ValidStorage(Storage):
    def giveaway(self, type_of_device, qty):
        if not str(qty).isdigit():
            print("ЧТО?")
            return
        return Storage.giveaway(self, type_of_device, qty)


# test
art1 = Printer("ink")
art2 = Scaner(1300)
art3 = Xerox("sublime", 3000)
art4 = Storage()
my_storage = ValidStorage()
my_storage.receive(art1, art2, art3, art1)
print(my_storage.giveaway(art1, 3))
print(my_storage.giveaway(art2, "ДВА"))
print(my_storage.giveaway(art4, 1000))
print(my_storage.storage)
