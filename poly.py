from poly_operations import *


class Poly:
    def __init__(self, iterable):
        self.coefficients = list(iterable)

    def get_leading_coefficient(self):
        return self[0]

    def is_root(self, point):
        return is_root(self.coefficients, point)

    def is_zero(self):
        return all([abs(x) < epsilon for x in self])

    def poly_val(self, point):
        return value(self.coefficients, point)

    def has_root(self):
        return len(self) > 1 or abs(self[-1]) < epsilon

    def __iter__(self):
        for coefficient in self.coefficients:
            yield coefficient

    def __len__(self):
        return len(self.coefficients)

    def __add__(self, other: 'Poly') -> 'Poly':
        return Poly(add(self.coefficients, other.coefficients))

    def __sub__(self, other: 'Poly') -> 'Poly':
        return self.__add__(other.__neg__())

    def __mul__(self, other: 'Poly') -> 'Poly':
        return Poly(multiply(self.coefficients, other.coefficients))

    def __rmul__(self, other):
        return Poly(multiply(self.coefficients, [other]))

    def __truediv__(self, other: 'Poly') -> 'Poly':
        return Poly(divide(self.coefficients, other.coefficients))

    def __mod__(self, other: 'Poly') -> 'Poly':
        return Poly(mod(self.coefficients, other.coefficients))

    def __pow__(self, other):
        if isinstance(other, int):
            deg = other
        elif isinstance(other, Poly):
            for i in range(len(other) - 1):
                if abs(other[i]) > epsilon:
                    raise ValueError
            deg = other[-1]
        else:
            raise ValueError
        if deg < 0:
            raise ValueError
        elif deg == 0:
            return Poly([1])
        else:
            result = [1]
            for i in range(deg):
                result = multiply(result, self.coefficients)
            return Poly(result)

    def __neg__(self):
        return Poly(multiply(self.coefficients, [-1]))

    def __invert__(self):
        return Poly(derivative(self.coefficients))

    def __getitem__(self, index: int):
        if index < -len(self.coefficients) or index >= len(self.coefficients):
            raise IndexError
        return self.coefficients[index]

    def __str__(self):
        return str(self.coefficients)
