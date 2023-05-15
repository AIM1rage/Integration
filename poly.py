from poly_operations import *


class Poly:
    def __init__(self, iterable):
        self.coefficients = list(iterable)

    def __add__(self, other: 'Poly') -> 'Poly':
        return Poly(add(self.coefficients, other.coefficients))

    def __mul__(self, other: 'Poly') -> 'Poly':
        return Poly(multiply(self.coefficients, other.coefficients))

    def __truediv__(self, other: 'Poly') -> 'Poly':
        return Poly(divide(self.coefficients, other.coefficients))

    def __mod__(self, other: 'Poly') -> 'Poly':
        return Poly(mod(self.coefficients, other.coefficients))

    def __neg__(self):
        return Poly(multiply(self.coefficients, [-1]))

    def __invert__(self):
        return Poly(derivative(self.coefficients))

    def __str__(self):
        return self.coefficients.__str__()
