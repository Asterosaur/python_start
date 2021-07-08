def capitalize(string: str):
    return string.capitalize()


def capitalize_string_list(string_list):
    return " ".join(list(map(capitalize, string_list)))


def main():
    print(capitalize_string_list(input("Вводите слова:").split(" ")))

main()
