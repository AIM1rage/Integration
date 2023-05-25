from parser import Parser
from integrator import Integrator
from terms.fraction_term import FractionTerm


def read_definite_integral_bounds(terms):
    calculate = False
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
    value1 = value2 = 0
    for term in terms:
        value1 += term.value(a)
        value2 += term.value(b)
    print('Определенный интеграл равен')
    print(value2 - value1)


def read_bound(bound_number):
    while True:
        user_input = input(f'Введите {bound_number}-ю границу: ')
        try:
            return float(user_input)
        except ValueError:
            continue


if __name__ == '__main__':
    while True:
        numerator = input('Введите числитель рациональной дроби: ')
        try:
            parsed_numerator = Parser.parse(numerator)
            break
        except ArithmeticError:
            print('Некорректный ввод! Проблема с операциями')
            print()
        except IndexError:
            print('Некорректный ввод! Проблема с вводом')
            print()
    while True:
        denominator = input('Введите знаменатель рациональной дроби: ')
        try:
            parsed_denominator = Parser.parse(denominator)
            fraction = FractionTerm(parsed_numerator, parsed_denominator)
            terms = Integrator.integrate(fraction)
            break
        except ArithmeticError:
            print('Некорректный ввод! Проблема с операциями')
            print()
        except IndexError:
            print('Некорректный ввод! Проблема с вводом')
            print()
    print()
    print('Первообразная равна')
    print(' + '.join([str(x) for x in terms + ['C']]))
    print()
    read_definite_integral_bounds(terms)
