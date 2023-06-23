import unittest
import constants
from gralpy import integrate


class IntegralTest(unittest.TestCase):
    """
    Проверяет, найдена ли верная первообразная по 10 различным значениям
    определенного интеграла от этой первообразной
    по формуле Ньютона-Лейбница.
    """

    def test_integral_calculation(self):

        for to_antiderivative in constants.to_antiderivatives:
            numerator, denominator, expected = to_antiderivative
            for i in range(10):
                a = 100
                b = a * (i + 2)
                indefinite_integral = integrate(numerator, denominator, a, b)
                self.assertAlmostEqual(first=expected[i],
                                       second=indefinite_integral,
                                       delta=constants.epsilon)
        print('Успех!')


if __name__ == '__main__':
    unittest.main()
