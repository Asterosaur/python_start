class Complex:

    def __init__(self, r, i):
        self.i = i
        self.r = r

    def __str__(self):
        return f"{self.r}+{self.i}i"

    def __add__(self, other):
        return Complex(self.r + other.r, self.i + other.i)

    def __mul__(self, other):
        return Complex(self.r*other.r - self.i*other.i, self.r*other.i + self.i*other.r)

    def __truediv__(self, other):
        x = self.r * other.r + self.i * other.i
        y = self.i * other.r - self.r * other.i
        z = other.r**2 + other.i**2
        r = x / z
        i = y / z
        return Complex(r, i)


c1 = Complex(1, 1)
c2 = Complex(2, 2)

print(c1 + c2)
print(c1 / c2)
