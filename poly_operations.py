# перемножает 2 многочлена a_n * x ^ n + a_(n - 1) * x ^ (n - 1) + ... + a_0
# b_m * x ^ m + b_(m - 1) * x ^ (m - 1) + ... + b_0
def multiply(a, b):
    raise NotImplementedError


# возращает частное и остаток в виде пары строк (q(x), r(x))
def divide(a, b):
    raise NotImplementedError


# возращает производную многочлена a`(x)
def derivative(a):
    raise NotImplementedError
