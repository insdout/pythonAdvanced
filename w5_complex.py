class Complex:
    # Part 1
    def __init__(self, re=0, im=0):
        if isinstance(re, (float, int)) & isinstance(im, (float, int)):
            self.re = re
            self.im = im
        else:
            raise TypeError

    def __str__(self):
        if self.im >= 0:
            sign = "+"
        else:
            sign = ""
        return "".join(map(str, [self.re, sign, self.im, "i"]))

    # Part 2
    def __add__(self, other):
        if isinstance(other, (int, float)):
            self.re += other

        elif isinstance(other, Complex):
            self.re += other.re
            self.im += other.im
        else:
            raise TypeError
        return self

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            self.re -= other

        elif isinstance(other, Complex):
            self.re -= other.re
            self.im -= other.im
        else:
            raise TypeError
        return self

    # Part 3
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            a = self.re
            b = self.im
            c = other
            d = 0

        elif isinstance(other, Complex):
            a = self.re
            b = self.im
            c = other.re
            d = other.im
        else:
            raise TypeError
        return Complex(a * c - b * d, b * c + a * d)

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            a = self.re
            b = self.im
            c = other
            d = 0

        elif isinstance(other, Complex):
            a = self.re
            b = self.im
            c = other.re
            d = other.im
        else:
            raise TypeError
        return Complex(
            (a * c + b * d) / (c ** 2 + d ** 2),
            (b * c - a * d) / (c ** 2 + d ** 2)
        )

    # Part 4
    def __eq__(self, other):
        if isinstance(other, (int, float)):
            return (self.re == other) & (self.im == 0)

        elif isinstance(other, Complex):
            return (self.re == other.re) & (self.im == other.im)

        else:
            raise TypeError

    def __abs__(self):
        return (self.re ** 2 + self.im ** 2) ** (1 / 2)
