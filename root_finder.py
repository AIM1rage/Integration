from poly import Poly
import math
import random


class RootFinder:
    # возвращает рациональные корни многочлена с учетом кратности,
    # если такового не нашлось - то возвращает None
    @staticmethod
    def find_rational_roots(poly: Poly):
        if not poly.has_root() or poly.is_zero():
            return None
        candidates = set()
        leading, constant, roots, poly = RootFinder._eliminate_x_(poly)
        constant_dividers = RootFinder._find_number_dividers_(constant)
        constant_dividers = constant_dividers + [-x for x in constant_dividers]
        leading_dividers = RootFinder._find_number_dividers_(leading)
        for p in constant_dividers:
            for q in leading_dividers:
                gcd = math.gcd(p, q)
                p, q = p // gcd, q // gcd
                if poly.is_root(p / q):
                    candidates.add((p, q))
        poly_copy = Poly(poly)
        candidates = sorted(candidates, key=lambda x: abs(x[0] / x[1]),
                            reverse=True)
        for candidate in candidates:
            deg = 0
            while poly_copy.is_root(candidate[0] / candidate[1]):
                deg += 1
                poly_copy = poly_copy / Poly([candidate[1], -candidate[0]])
            if deg > 0:
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
        if not poly.has_root() or poly.is_zero():
            return None
        derivative = ~poly
        area = max([abs(x) for x in poly])
        x_0 = point_selector(area)
        iterations_count = 1000
        tries_count = 5
        for i in range(tries_count):
            for j in range(iterations_count):
                k = 0
                while poly.is_root(x_0) and k < iterations_count:
                    x_0 = x_0 - poly.value(x_0) / derivative.value(x_0)
                    k += 1
                if poly.is_root(x_0):
                    return x_0
                x_0 = x_0 - poly.value(x_0) / derivative.value(x_0)
            x_0 = point_selector(area)
        return None

    @staticmethod
    def _eliminate_x_(poly):
        leading = poly[0]
        right_zeros_count = 0
        nonzero_index = -1
        while poly[nonzero_index] == 0:
            nonzero_index -= 1
            right_zeros_count += 1
        constant = poly[nonzero_index]
        roots = list()
        if right_zeros_count:
            roots.append((0, 1, right_zeros_count))
        poly = Poly([poly[x] for x in range(len(poly) - right_zeros_count)])
        return leading, constant, roots, poly

    @staticmethod
    def _find_number_dividers_(n):
        dividers = []
        for divider in range(1, int(abs(n) ** 0.5) + 1):
            if n % divider == 0:
                dividers.append(divider)
                if (n // divider) != divider:
                    dividers.append(n // divider)
        return sorted(dividers)
