class Road:
    _length = 10000
    _width = 10

    def __init__(self,length,width):
        self._length = length
        self._width = width

    def calc_mass(self, nominal_mass = 25, nominal_thickness = 5):
        return self._width * self._length * nominal_mass * nominal_thickness

my_road = Road(1000, 100)
print(my_road.calc_mass())