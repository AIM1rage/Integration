from integrator import Integrator
from parser import Parser
from terms.fraction_term import FractionTerm


def integrate(numerator: str, denominator: str, a=None, b=None):
    """
    Принимает рациональную функцию из числителя и знаменателя и
    возвращает неопределенный интеграл (str, str) -> float, если на вход
    функции поданы пределы интегрирования. В противном случае возращается
    неопределенный интеграл рациональной функции от a до b (str, str) -> str.
    """
    parsed_numerator = Parser.parse(numerator)
    parsed_denominator = Parser.parse(denominator)
    fraction = FractionTerm(parsed_numerator, parsed_denominator)
    indefinite_integral = Integrator.integrate(fraction)
    if a is None and b is None:
        return Integrator.indefinite_integral(indefinite_integral)
    if (type(a) == float or type(a) == int) and (
            type(b) == float or type(b) == int):
        definite_integral = Integrator.definite_integral(
            indefinite_integral, a, b)
        return definite_integral
    raise TypeError(f'Аргументы a и b должны быть числами!')
