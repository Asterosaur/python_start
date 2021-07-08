# 1

def divide(a, b):
    if b != 0:
        result = a / b
        print(result)
        return result
    print(f"На ноль не делим")
    return


def main():
    divide(*map(int, input("Введите два числа через пробел:").rstrip(" ").split(" ")))


main()
