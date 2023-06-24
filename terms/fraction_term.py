class FractionTerm:
    def __init__(self, numerator, denominator, den_deg: int = 1):
        self.numerator = numerator
        if denominator.is_zero():
            raise ArithmeticError('Деление на ноль!')
        self.denominator = denominator
        self.den_deg = den_deg

    def value(self, point):
        if self.denominator.is_root(point):
            return None
        return self.numerator.value(point) / self.denominator.value(
            point) ** self.den_deg

    def __iter__(self):
        yield self.numerator
        yield self.denominator

    def __str__(self):
        return f'[{self.numerator}] / [{self.denominator}]^{self.den_deg}'
