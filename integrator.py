from poly import Poly
from factorizer import Factorizer
from constants import *
from parser import Parser
from gauss import Solver


class Integrator:
    def __init__(self):
        self.terms = list()

    def integrate(self, numerator: Poly, denominator: Poly):
        quotient = numerator / denominator
        remainder = numerator % denominator
        self._integrate_poly_(quotient)
        for fraction in self._decompose_fraction_(remainder, denominator):
            # TODO передавать дроби соответствующим методам
            pass
        return self.terms

    @staticmethod
    def _decompose_fraction_(numerator, denominator):
        factors, scalar = Factorizer.factorize(denominator)
        solution = Integrator._get_solution_(numerator, denominator, factors)
        return Integrator._get_fractions_(factors, solution)

    @staticmethod
    def _get_solution_(numerator, denominator, factors):
        equations_count = sum(
            map(lambda x: x[1] * (len(x[0]) - 1), factors)) + 1
        matrix = [[0 for _ in range(equations_count)] for _ in
                  range(equations_count)]
        var_index = 0
        for factor in factors:
            for k in range(1, factor[1] + 1):
                poly = denominator / (factor[0] ** k)
                for j in range(len(factor[0]) - 1):
                    for i in range(len(poly)):
                        matrix[i + j][var_index] = poly[len(poly) - 1 - i]
                    var_index += 1
        free_members = list(reversed(numerator)) + [0] * (
                equations_count - len(numerator))
        return Solver.solve(matrix, free_members)

    @staticmethod
    def _get_fractions_(factors, solution):
        fractions = list()
        var_index = 0
        for factor in factors:
            for k in range(1, factor[1] + 1):
                deg = len(factor[0]) - 1
                match deg:
                    case 1:
                        fractions.append(
                            (Poly([solution[var_index]]), factor[0], k))
                        var_index += 1
                    case 2:
                        fractions.append((
                            Poly([solution[var_index + 1],
                                  solution[var_index]]),
                            factor[0], k))
                        var_index += 2
        return fractions

    def _integrate_poly_(self, poly):
        for i in range(len(poly)):
            coefficient = poly[i]
            deg = len(poly) - 1 - i
            if abs(poly[i]) > epsilon:
                self.terms.append(f'{coefficient / (deg + 1)}*x^{deg + 1}')

    # a / (q * x - p)
    def _integrate_linear_by_log_(self):
        raise NotImplementedError

    # a / (q * x - p) ^ n
    def _integrate_linear_by_power_function_(self):
        raise NotImplementedError

    # (m * x + n) / (x ^ 2 + p * x + q) ^ k
    def _integrate_quadratic_(self):
        raise NotImplementedError


if __name__ == '__main__':
    for fraction_to_decompose in to_decompose:
        num = Parser.parse(fraction_to_decompose[0])
        den = Parser.parse(fraction_to_decompose[1])
        print(f'{num} / {den}')
        for fraction in Integrator._decompose_fraction_(num, den):
            print(fraction[0], fraction[1], fraction[2])
    pass
