from itertools import dropwhile, accumulate

epsilon = 1e-6


# приведение многочлена к стандартному виду (удаление нулей)
def standard_notation(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        standard_result = list(dropwhile(lambda x: abs(x) < epsilon, result))
        if not standard_result:
            return [0]
        return standard_result

    return wrapper


def poly_val(poly, value):
    return list(accumulate(poly, lambda x, y: value * x + y, initial=0))[-1]


# умножение 2 многочленов a_n * x ^ n + a_(n - 1) * x ^ (n - 1) + ... + a_0
# b_m * x ^ m + b_(m - 1) * x ^ (m - 1) + ... + b_0
@standard_notation
def multiply(poly1, poly2):
    out = [0] * (len(poly1) + len(poly2) - 1)
    for i in range(len(poly1) - 1, -1, -1):
        for j in range(len(poly2) - 1, -1, -1):
            out[i + j] += poly1[i] * poly2[j]
    out.reverse()
    return out


# деление: частное и остаток в виде пары строк (q(x), r(x))
@standard_notation
def divide(dividend, divisor):
    out = list(dividend)
    norm = divisor[0]
    for i in range(len(dividend) - len(divisor) + 1):
        out[i] /= norm
        coefficient = out[i]
        if coefficient != 0:
            for j in range(1, len(divisor)):
                out[i + j] += -divisor[j] * coefficient
    separator = 1 - len(divisor)
    return out[:separator], out[separator:]


# производная a`(x) многочлена a(x)
@standard_notation
def derivative(poly):
    if len(poly) == 0:
        return [0]
    out = list()
    n = len(poly) - 1
    for i in range(len(poly) - 1):
        out.append((n - i) * poly[i])
    return out
