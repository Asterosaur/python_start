def two_largest_product(*args):
    integers = list(args)
    largest = max(integers)
    integers.remove(largest)
    second_largest = max(integers)
    result = largest * second_largest
    return result


def main():
    print(two_largest_product(*map(int, input("Введите числа через пробел:").rstrip(" ").split(" "))))


main()
