from parser import Parser
from integrator import Integrator
from terms.fraction_term import FractionTerm


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
        except ArithmeticError as arithmetic_error:
            print(str(arithmetic_error))
            print()
        except ValueError as value_error:
            print(str(value_error))
            print()
    return parsed_polynomial


if __name__ == '__main__':
    while True:
        try:
            numerator = read_polynomial(
                'Введите числитель рациональной дроби: ')
            denominator = read_polynomial(
                'Введите знаменатель рациональной дроби: ')
            fraction = FractionTerm(numerator, denominator)
            break
        except ArithmeticError as error:
            print(str(error))
    terms = Integrator.integrate(fraction)
    print()
    print('Первообразная равна')
    print(Integrator.indefinite_integral(terms))
    print()
    read_definite_integral_bounds(terms)
