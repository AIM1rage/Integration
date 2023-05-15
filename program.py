import poly_operations

if __name__ == '__main__':
    a = [0]
    b = [1, 3, 3, 1]
    result1 = poly_operations.multiply(b, a)
    result2 = poly_operations.derivative(result1)
    result3 = poly_operations.poly_val(b, 1)
    pass
