from itertools import dropwhile, accumulate
from constants import epsilon


# приведение многочлена к стандартному виду (удаление нулей)
def standard_notation(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        standard_result = list(dropwhile(lambda x: abs(x) < epsilon, result))
        if not standard_result:
            return [0]
        return standard_result

    return wrapper


def value(poly, point):
    return list(accumulate(poly, lambda x, y: point * x + y, initial=0))[-1]


def is_root(poly, point):
    return abs(value(poly, point)) < epsilon


@standard_notation
def add(poly1, poly2):
    n = max(len(poly1), len(poly2))
    out = [0] * n
    for i in range(n - 1, -1, -1):
        a = 0 if i >= len(poly1) else poly1[i]
        b = 0 if i >= len(poly2) else poly2[i]
        out[i] = a + b
    out.reverse()
    return out


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
def divide_mod(dividend, divisor):
    out = list(dividend)
    norm = divisor[0]
    if all([abs(x) < epsilon for x in divisor]):
        raise ZeroDivisionError
    for i in range(len(dividend) - len(divisor) + 1):
        out[i] /= norm
        coefficient = out[i]
        if coefficient != 0:
            for j in range(1, len(divisor)):
                out[i + j] += -divisor[j] * coefficient
    separator = 1 - len(divisor)
    return out[:separator], out[separator:]


@standard_notation
def divide(dividend, divisor):
    return divide_mod(dividend, divisor)[0]


@standard_notation
def mod(dividend, divisor):
    return divide_mod(dividend, divisor)[1]


# производная a`(x) многочлена a(x)
@standard_notation
def derivative(poly):
    if not poly:
        return [0]
    out = list()
    n = len(poly) - 1
    for i in range(len(poly) - 1):
        out.append((n - i) * poly[i])
    return out
