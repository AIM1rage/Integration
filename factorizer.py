from poly import Poly
from root_finder import RootFinder


class Factorizer:
    @staticmethod
    def factorize(poly: Poly):
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
            factor = Poly(map(lambda x: x.real,
                              Poly([1, -complex_root]) *
                              Poly([1, -complex_root.conjugate()])))
            while poly.is_root(complex_root):
                poly = poly / factor
                deg += 1
            factors.append((factor, deg))
        scalar = poly[-1]
        return factors, scalar
