from math import gcd


class Fraction:
    def __init__(self, numerator, denominator):
        self.n = numerator
        self.d = denominator

    def __add__(self, other):
        nx = other.n
        dx = other.d
        n = self.n * dx + self.d * nx
        d = dx * self.d
        nok = gcd(n, d)
        return Fraction(n / nok, d / nok)

    def __sub__(self, other):
        nx = other.n
        dx = other.d
        n = self.n * dx - self.d * nx
        d = dx * self.d
        nok = gcd(n, d)
        return Fraction(n / nok, d / nok)

    def __mul__(self, other):
        nx = other.n
        dx = other.d
        n = nx * self.n
        d = dx * self.d
        nok = gcd(n, d)
        return Fraction(n / nok, d / nok)

    def __truediv__(self, other):
        dx = other.n
        nx = other.d
        n = nx * self.n
        d = dx * self.d
        nok = gcd(n, d)
        return Fraction(n / nok, d / nok)

    def __pow__(self, power, modulo=None):
        n=self.n**power
        d=self.d**power
        nok = gcd(n, d)
        return Fraction(n / nok, d / nok)



    def __str__(self):
        return "%i / %i" % (self.n, self.d)


a = Fraction(1, 2)
b = Fraction(3, 4)
c = b / a
d=3
r=b**d
print(c)
print(r)
