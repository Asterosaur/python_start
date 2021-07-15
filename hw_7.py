def fact(n):
    if n == 0:
        return "0! = 1 "

    result = 1
    for i in range(1, n + 1):
        result *= i
        yield f"{i}! = {result} \n"


print(*(fact(int(input("введите целое число: ")))))
