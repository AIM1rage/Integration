from parser import Parser
from poly import Poly
import math
import random


class RootFinder:
    # возвращает рациональные корни многочлена с учетом кратности,
    # если такового не нашлось - то возвращает None
    @staticmethod
    def find_rational_roots(poly: Poly):
        roots = list()
        leading = poly[0]
        constant = poly[-1]
        candidates = set()
        constant_dividers = RootFinder._find_number_dividers_(constant)
        constant_dividers = constant_dividers + [-x for x in constant_dividers]
        leading_dividers = RootFinder._find_number_dividers_(leading)
        for p in constant_dividers:
            for q in leading_dividers:
                gcd = math.gcd(p, q)
                if poly.is_root(p / q):
                    candidates.add((p // gcd, q // gcd))
        poly_copy = Poly(poly)
        for candidate in candidates:
            deg = 0
            while poly_copy.is_root(candidate[0] / candidate[1]):
                deg += 1
                poly_copy = poly_copy / Poly([candidate[1], -candidate[0]])
            roots.append((candidate[0], candidate[1], deg))
        return (roots, poly_copy) if roots else None

    # возвращает действительный корень многочлена,
    # если такового не нашлось - то возвращает None
    @staticmethod
    def find_real_root(poly: Poly):
        return RootFinder._find_root_by_newton_(
            poly,
            lambda x: random.uniform(-x, x))

    # возвращает комплексный корень многочлена,
    # если такового не нашлось - то возвращает None
    @staticmethod
    def find_complex_root(poly: Poly):
        return RootFinder._find_root_by_newton_(
            poly,
            lambda x: complex(random.uniform(-x, x), random.uniform(-x, x)))

    @staticmethod
    def _find_root_by_newton_(poly: Poly, point_selector):
        derivative = ~poly
        area = max([abs(x) for x in poly])
        x_0 = point_selector(area)
        iterations_count = 1000
        tries_count = 5
        for i in range(tries_count):
            for j in range(iterations_count):
                k = 0
                while poly.is_root(x_0) and k < iterations_count:
                    x_0 = x_0 - poly.poly_val(x_0) / derivative.poly_val(x_0)
                    k += 1
                if poly.is_root(x_0):
                    return x_0
                x_0 = x_0 - poly.poly_val(x_0) / derivative.poly_val(x_0)
            x_0 = point_selector(area)
        return None

    @staticmethod
    def _find_number_dividers_(n):
        dividers = []
        for divider in range(1, int(abs(n) ** 0.5) + 1):
            if n % divider == 0:
                dividers.append(divider)
                if (n // divider) != divider:
                    dividers.append(n // divider)
        return sorted(dividers)


if __name__ == '__main__':
    expression = '(x ^ 3 - 2 * x ^ 2 + 2)'
    right_root = '-0.83928675521416113255185256465328660'
    parsed_poly = Parser.parse(expression)
    real_root = RootFinder.find_real_root(parsed_poly)
    complex_root = RootFinder.find_complex_root(
        parsed_poly / Poly([1, -real_root]))
    poly_divider = Poly([1, -complex_root]) * Poly(
        [1, -complex_root.conjugate()])
    print(right_root)
    print(real_root)
    print(poly_divider)
    print(parsed_poly / poly_divider)
