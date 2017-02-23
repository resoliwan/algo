"""Fraction class"""


class Fraction:
    """Fraction class"""
    def __init__(self, top, bottom):
        self.num = top #numerator
        self.den = bottom #denominator

    def show(self):
        """print the state"""
        print(self.num, "/", self.den)


myfraction = Fraction(3, 5)
myfraction.show()
print(myfraction)
