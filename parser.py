import sympy


def parse(line: str):
    s = line.split()
    return


if __name__ == '__main__':
    f = '(2 * x) / (x^2 + 1)^2'
    print(sympy.integrate(f))
