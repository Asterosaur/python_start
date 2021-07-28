class ZeroDivError(Exception):
    def __init__(self, message):
        self.message = message


# test

try:
    num = float(input("Введите делитель: "))
    if num == 0:
        raise ZeroDivError("Делим на ноль")
        exit()
    print(10/num)
except TypeError:
    print("Не преобразуется в число")
except ZeroDivError:
    print("На ноль всё равно не делится")
    exit()
