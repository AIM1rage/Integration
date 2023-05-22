from poly import Poly
from root_finder import RootFinder
from parser import Parser


class Factorizer:
    @staticmethod
    def factorize(poly: Poly) -> list[tuple[Poly, int]]:
        factors = list()
        rational_roots = RootFinder.find_rational_roots(poly)
        if rational_roots:
            factors.extend(
                map(lambda x: (Poly([x[1], -x[0]]), x[2]), rational_roots[0]))
            poly = rational_roots[1]
        while RootFinder.find_real_root(poly):
            real_root = RootFinder.find_real_root(poly)
            deg = 0
            factor = Poly([1, -real_root])
            while poly.is_root(real_root):
                poly = poly / factor
                deg += 1
            factors.append((factor, deg))
        while RootFinder.find_complex_root(poly):
            complex_root = RootFinder.find_complex_root(poly)
            deg = 0
            factor = Poly([1, -complex_root]) * Poly(
                [1, -complex_root.conjugate()])
            while poly.is_root(complex_root):
                poly = poly / factor
                deg += 1
            factors.append((factor, deg))
        return factors


if __name__ == '__main__':
    expression = '(x ^ 4 + 1) * (x - 1) * ((x - 3) ^ 2) ^ 10 * (2 * x - 5) ^ 2'
    parsed_poly = Parser.parse(expression)
    print(parsed_poly.poly_val(9 / 4))
    factors = Factorizer.factorize(parsed_poly)
    for factor in factors:
        print(factor[0], factor[1])
    pass
