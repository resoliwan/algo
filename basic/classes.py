"""Fraction class"""


class Fraction:
    """Fraction class"""
    def __init__(self, top, bottom):
        self.num = top  # numerator
        self.den = bottom  # denominator

    def show(self):
        """print the state"""
        print(self.num, "/", self.den)

    def __str__(self):
        """print str"""
        return str(self.num)+"/"+str(self.den)

    def gcd(self, m, n):
        while m % n != 0:
            oldm = m
            oldn = n

            m = oldn
            n = oldm % oldn
        return n

    def __add__(self, otherfraction):

        new_num = self.num * otherfraction.den + otherfraction.num * self.den
        new_den = self.den * otherfraction.den
        common = self.gcd(new_num, new_den)

        return Fraction(new_num//common, new_den//common)

    def __eq__(self, otherfraction):
        firstnum = self.num * otherfraction.den
        secondnum = otherfraction.num * self.den

        return firstnum == secondnum

    def __mul__(self, other):
        num = self.num * other.num
        den = self.den * other.den
        common = self.gcd(num, den)
        return Fraction(num//common, den//common)

    def __truediv__(self, other):
        num = self.num * other.den
        den = self.den * other.num
        common = self.gcd(num, den)

        return Fraction(num//common, den//common)

    def __sub__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        new_num = firstnum - secondnum
        new_den = self.den * other.den
        common = self.gcd(new_num, new_den)

        return Fraction(new_num//common, new_den//common)

    def __lt__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum < secondnum

    def __gt__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum > secondnum


myfraction = Fraction(3, 5)
# myfraction.show()
print(myfraction)
print("I ate", myfraction, "of the pizza")
myfraction.__str__()
str(myfraction)

f1 = Fraction(1, 4)
f2 = Fraction(1, 2)
f3 = f1 + f2
print(f3)

f4 = Fraction(1, 4)
f5 = Fraction(1, 4)
print(f4 == f5)

f1 < f2
f1 > f2


