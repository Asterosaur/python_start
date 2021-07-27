class CellError(Exception):
    """Raised when slots are lower than 1"""
    pass


class Cell:

    def __init__(self, slots):

        if slots > 0:
            self.slots = slots
        else:
            raise CellError("Количество ячеек не дб отрицательным или равным нулю")

    def __add__(self, other):
        return Cell(self.slots + other.slots)

    def __sub__(self, other):
        return Cell(self.slots - other.slots)

    def __mul__(self, other):
        return Cell(self.slots * other.slots)

    def __truediv__(self, other):
        return Cell(self.slots / other.slots)

    def make_order(self, row_length):
        rows = self.slots // row_length
        overflow = self.slots % row_length
        return ("*" * row_length + "\n") * rows + "*" * overflow


# test
my_cell_10 = Cell(10)
my_cell_100 = Cell(100)

print((my_cell_10 + my_cell_100).slots)
print((my_cell_10 - my_cell_100).slots)
print(my_cell_100.make_order(13))
