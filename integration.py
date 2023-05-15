def linear_denominator(a,b,c):
    return [f"{a/b} * ln(|{b} * x + {c}|)"]


def quadratic_denominator(a,b,c,d,e):
    return [f"{a/(2*c)} * ln|{c} * x^2 + {d} * x + {e}|",  f"{(b - a*d/(2*c))/(c*((e/c - (d**2)/(4*(c**2))**0.5)))} * atan((x + {d/(2*c)}) / {(e/c - (d**2)/(4*(c**2)))**0.5})"]

#a - коэффициент, b - степень
def power_function(a,b):
    if b == -1:
        return [f"ln|{a} / x"]
    return [f"{a/(b+1)} * x^{b+1}"]

