def multiply(matrix1, matrix2):
    if len(matrix1) == 0 or len(matrix2) == 0:
        raise TypeError('Одна из матриц не содержит строк!')
    n, m1 = len(matrix1), len(matrix1[0])
    m2, k = len(matrix2), len(matrix2[0])
    if m1 != m2:
        raise TypeError('Число столбцов первой матрицы должно равняться '
                        'числу строк второй матрицы!')
    m = m1
    multiplication = [[0] * k for i in range(n)]
    for i in range(n):
        for j in range(k):
            result = 0
            for x in range(m):
                result += matrix1[i][x] * matrix2[x][j]
            multiplication[i][j] = result
    return multiplication


def transpose(matrix):
    return [list(x) for x in zip(*matrix)]
