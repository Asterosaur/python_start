from abc import ABC


class OfficeDevice(ABC):
    name = "приблуда"

    @property
    def color(self):
        return "white"


class Printer(OfficeDevice):
    name = "printer"

    def __init__(self, print_type="laser"):
        self.print_type = print_type


class Scaner(OfficeDevice):
    name = "scaner"

    def __init__(self, dpi=1000):
        self.dpi = dpi


class Xerox(Scaner, Printer):
    name = "xerox"

    def __init__(self, print_type="laser", dpi=1000):
        self.dpi = dpi
        self.print_type = print_type
