from poly import Poly

if __name__ == '__main__':
    a = Poly([1, 2, 1])
    b = Poly([1, 3, 3, 1])
    result1 = a + b
    result2 = a * b
    result3 = b / a
    result4 = (a + b).poly_val(1)
    pass
