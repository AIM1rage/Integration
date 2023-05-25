from poly import Poly
from factorizer import Factorizer
from constants import *
from parser import Parser
from gauss import Solver
from terms.fraction_term import FractionTerm
from terms.log_term import LogTerm
from terms.atan_term import AtanTerm


class Integrator:
    @staticmethod
    def integrate(rational_fraction: FractionTerm):
        terms = list()
        numerator, denominator = rational_fraction
        quotient = numerator / denominator
        remainder = numerator % denominator
        if not quotient.is_zero():
            terms.append(quotient.integral())
        for fraction in Integrator._decompose_fraction_(remainder,
                                                        denominator):
            fraction_numerator, fraction_denominator, deg = fraction
            match len(fraction_denominator) - 1:
                case 1 if deg == 1:
                    Integrator._integrate_linear_by_log_(
                        fraction_numerator,
                        fraction_denominator,
                        terms)
                case 1 if deg > 1:
                    Integrator._integrate_linear_by_pow_function_(
                        fraction_numerator,
                        fraction_denominator,
                        deg, terms)
                case 2 if deg >= 1:
                    Integrator._integrate_quadratic_(
                        fraction_numerator,
                        fraction_denominator,
                        deg, terms)
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
    def _integrate_linear_by_log_(numerator, denominator, terms):
        coefficient = numerator[0] / denominator[0]
        Integrator.__add_term__(coefficient, terms,
                                LogTerm(coefficient, denominator))

    # a / (q * x - p) ^ n, n > 1
    @staticmethod
    def _integrate_linear_by_pow_function_(numerator, denominator, deg, terms):
        coefficient = numerator[0] / (denominator[0] * (-deg + 1))
        new_numerator = Poly([coefficient])
        Integrator.__add_term__(coefficient, terms,
                                FractionTerm(new_numerator,
                                             denominator,
                                             deg - 1))

    # (m * x + n) / (x ^ 2 + p * x + q) ^ k
    @staticmethod
    def _integrate_quadratic_(numerator, denominator, deg, terms):
        m, n = [0] * (max(0, 2 - len(numerator))) + numerator.coefficients
        _, p, q = denominator
        if deg == 1:
            coefficient = (2 * n - m * p) / (4 * q - p ** 2) ** (1 / 2)
            expression = (1 / (4 * q - p ** 2) ** (1 / 2)) * Poly([2, p])
            Integrator.__add_term__(m, terms, LogTerm(m / 2, denominator))
            Integrator.__add_term__(coefficient, terms,
                                    AtanTerm(coefficient, expression))
            return
        new_numerator = m / (2 * (-deg + 1)) * Poly([1])
        Integrator.__add_term__(new_numerator[-1], terms,
                                FractionTerm(new_numerator,
                                             denominator,
                                             deg - 1))
        multiplier = (2 * n - m * p) / 2
        fraction = FractionTerm(Poly([1]), denominator, deg)
        Integrator.__integrate_simple_quadratic__(multiplier, fraction, terms)

    @staticmethod
    def __integrate_simple_quadratic__(multiplier, fraction, terms):
        _, p, q = fraction.denominator
        m2 = 4 * q - p ** 2
        if fraction.den_deg == 1:
            coefficient = 2 * multiplier / m2 ** (1 / 2)
            expression = (1 / m2 ** (1 / 2)) * Poly([2, p])
            Integrator.__add_term__(coefficient, terms,
                                    AtanTerm(coefficient, expression))
            return
        coefficient0 = multiplier / (m2 * (fraction.den_deg - 1))
        Integrator.__add_term__(coefficient0, terms,
                                FractionTerm(coefficient0 * Poly([2, p]),
                                             fraction.denominator,
                                             fraction.den_deg - 1))
        new_mult = 2 * multiplier * (2 * fraction.den_deg - 3
                                     ) / (m2 * (fraction.den_deg - 1))
        new_frac = FractionTerm(fraction.numerator,
                                fraction.denominator,
                                fraction.den_deg - 1)
        Integrator.__integrate_simple_quadratic__(new_mult, new_frac, terms)

    @staticmethod
    def __add_term__(coefficient, terms, term):
        if abs(coefficient) > epsilon:
            terms.append(term)


if __name__ == '__main__':
    for fraction_to_integrate in to_integrate:
        num = Parser.parse(fraction_to_integrate[0])
        den = Parser.parse(fraction_to_integrate[1])
        rat_frac = FractionTerm(num, den, 1)
        print(rat_frac)
        for simple_fraction in Integrator.integrate(rat_frac):
            print(simple_fraction)
        print()
    pass
