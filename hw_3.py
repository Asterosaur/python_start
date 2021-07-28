class NaNError(Exception):
    def __init__(self, message):
        self.message = message


def add_num_to_list(list=[]):
    input_str = input("Вводите число для добавления или stop для выхода: ")

    try:
        if input_str == "stop":
            print(list)
            exit()
        if input_str.isdigit():
            list.append(float(input_str))
            add_num_to_list(list)
        else:
            raise NaNError(f"{input_str} is not a Number")
    except NaNError:
        print("Нужно ввести число!")
        add_num_to_list(list)

add_num_to_list()
