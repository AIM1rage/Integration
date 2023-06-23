from parser import Parser
from integrator import Integrator
from terms.fraction_term import FractionTerm
import gralpy

def read_definite_integral_bounds(terms):
    while True:
        user_input = input(
            'Вы хотите посчитать определенный интеграл? [Y/N] ').lower()
        calculate = user_input == 'y'
        if user_input == 'y' or user_input == 'n':
            break
    if not calculate:
        return
    a = read_bound(1)
    b = read_bound(2)
    print('Определенный интеграл равен')
    print(Integrator.definite_integral(terms, a, b))


def read_bound(bound_number):
    while True:
        user_input = input(f'Введите {bound_number}-ю границу: ')
        try:
            return float(user_input)
        except ValueError:
            continue


def read_polynomial(message):
    while True:
        polynomial = input(message)
        try:
            parsed_polynomial = Parser.parse(polynomial)
            break
        except ArithmeticError:
            print(
                'Некорректный ввод! Возможно, возведение в степень многочлена')
            print()
        except ValueError as error:
            print(f'{str(error)}')
            print()
    return parsed_polynomial


if __name__ == '__main__':
    print(gralpy.integrate('1', 'x^2 + 1', 0, 1))
    numerator = read_polynomial('Введите числитель рациональной дроби: ')
    denominator = read_polynomial('Введите знаменатель рациональной дроби: ')
    fraction = FractionTerm(numerator, denominator)
    terms = Integrator.integrate(fraction)
    print()
    print('Первообразная равна')
    print(Integrator.indefinite_integral(terms))
    print()
    read_definite_integral_bounds(terms)
