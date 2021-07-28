class Date:

    def __init__(self, input_str="15111989"):
        self.day = input_str[:2]
        self.month = input_str[2:-4]
        self.year = input_str[-4:]

    @classmethod
    def extract_int(cls, input_str="15111989"):
        return [*map(int, [input_str[:2], input_str[2:-4], input_str[-4:]])]

    @staticmethod
    def validate_input(input_str="15111989"):
        if 0 < Date.extract_int(input_str)[0] < 32 & 0 < Date.extract_int(input_str)[1] < 13:
            return True
        return False


# test

my_date = Date("12012000")
print(my_date.extract_int("12012000"))
print(Date.validate_input("3313123"))
