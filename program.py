from poly import Poly

if __name__ == '__main__':
    a = Poly([1, 2, 1])
    b = Poly([1, 3, 3, 1])
    result1 = a + b
    result2 = a * b
    result3 = b / a
    result4 = (a + b).poly_val(1)
    result5 = 2 * a
    result6 = b.is_root(-1)
    result7 = b.is_root(1)
    pass
