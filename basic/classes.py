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

    def gcd(m, n):
        while m%n != 0:
            oldm = m
            oldn = n

            m = oldn
            n = oldm%oldn
        return n

    def __add__(self, otherFraction):

        new_num = self.num * otherFraction.den + otherFraction.num * self.den
        new_den = self.den * otherFraction.den
        common = gcd(new_num, new_den)

        return Fraction(new_num//common, new_den//common)


myfraction = Fraction(3, 5)
# myfraction.show()
print(myfraction)
print("I ate", myfraction, "of the pizza")
myfraction.__str__()
str(myfraction)

f1 = Fraction(1, 4)
f2 = Fraction(1, 2)
f3=f1+f2
print(f3)

