import math


class LogTerm:
    def __init__(self, coefficient, expression):
        self.coefficient = coefficient
        self.expression = expression

    def value(self, point):
        if self.expression.is_root(point):
            return None
        return self.coefficient * \
            math.log(abs(self.expression.value(point)), math.e)

    def __iter__(self):
        yield self.coefficient
        yield self.expression

    def __str__(self):
        return f'({self.coefficient})ln|{self.expression}|'
