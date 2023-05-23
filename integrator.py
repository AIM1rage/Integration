from poly import Poly
from factorizer import Factorizer
from constants import *
from parser import Parser
from gauss import Solver


class Integrator:
    @staticmethod
    def integrate(numerator: Poly, denominator: Poly):
        terms = list()
        quotient = numerator / denominator
        remainder = numerator % denominator
        terms.append(quotient.integral())
        for fraction in Integrator._decompose_fraction_(remainder,
                                                        denominator):
            fraction_numerator, fraction_denominator, deg = fraction
            match len(fraction_denominator) - 1:
                case 1 if deg == 1:
                    terms.append(Integrator._integrate_linear_by_log_(
                        fraction_numerator,
                        fraction_denominator))
                case 1 if deg > 1:
                    terms.append(Integrator._integrate_linear_by_pow_function_(
                        fraction_numerator,
                        fraction_denominator,
                        deg))
                case 2 if deg >= 1:
                    terms.append(Integrator._integrate_quadratic_(
                        fraction_numerator,
                        fraction_denominator,
                        deg))
                case _:
                    raise Exception
        return terms

    @staticmethod
    def _decompose_fraction_(numerator, denominator):
        factors, scalar = Factorizer.factorize(denominator)
        solution = Integrator._get_solution_(numerator, denominator, factors)
        return Integrator._get_fractions_(factors, solution)

    @staticmethod
    def _get_solution_(numerator, denominator, factors):
        equations_count = sum(
            map(lambda y: y[1] * (len(y[0]) - 1), factors)) + 1
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
                    case _:
                        raise Exception
        return fractions

    # a / (q * x - p)
    @staticmethod
    def _integrate_linear_by_log_(numerator, denominator):
        return f'{numerator[0] / denominator[0]}*' \
               f'ln|{denominator[0]}*x+({denominator[1]})|'

    # a / (q * x - p) ^ n
    @staticmethod
    def _integrate_linear_by_pow_function_(numerator, denominator, deg):
        return f'({numerator[0] / denominator[0] / (-deg + 1)})/' \
               f'({denominator[0]}*x+({denominator[1]}))^{deg - 1}'

    # (m * x + n) / (x ^ 2 + p * x + q) ^ k
    @staticmethod
    def _integrate_quadratic_(numerator, denominator, deg):
        raise NotImplementedError


if __name__ == '__main__':
    for fraction_to_integrate in to_integrate:
        num = Parser.parse(fraction_to_integrate[0])
        den = Parser.parse(fraction_to_integrate[1])
        print(f'{num} / {den}')
        for simple_fraction in Integrator.integrate(num, den):
            print(simple_fraction)
    pass
