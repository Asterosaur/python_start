def negative_power(rational=0, negative=-1):
    if negative < 0:
        result = rational ** negative
        print(result)
        return result
    print("Отрицательное!")
    return


def negative_power_loop(rational=0, negative=-1):
    if negative < 0:
        result = rational
        for _ in range(negative, 1, 1):
            result *= 1 / rational
        print(result)
        return result
    print("Отрицательное!")
    return


def main():
    negative_power(float(input("введите действительное число: ")),
                   int(input("введите целое отрицательное число: ")))

    negative_power_loop(float(input("введите действительное число: ")),
                        int(input("введите целое отрицательное число: ")))

main()
