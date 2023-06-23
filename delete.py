import sympy
import constants

for function in constants.to_antiderivatives:
    numerator, denominator, _ = function
    values = [float(sympy.integrate(f'({numerator}) / ({denominator})',
                                    ('x', 100, 100 * (i + 2))))
              for i in range(10)]
    print(f'("{numerator}", "{denominator}", [{", ".join(map(str, values))}]),')
    print()
