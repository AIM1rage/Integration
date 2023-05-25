import math


class AtanTerm:
    def __init__(self, coefficient, expression):
        self.coefficient = coefficient
        self.expression = expression

    def value(self, point):
        return self.coefficient * math.atan(self.expression.value(point))

    def __iter__(self):
        yield self.coefficient
        yield self.expression

    def __str__(self):
        return f'({self.coefficient})atan[{self.expression}]'
