import unittest
from matrix_operations import *

to_transpose = [([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]],
                 [[1, 4, 7],
                  [2, 5, 8],
                  [3, 6, 9]]),
                ([[1, 2, 3],
                  [4, 5, 6]],
                 [[1, 4],
                  [2, 5],
                  [3, 6]]),
                ([[0]], [[0]]),
                ([[]], TypeError())]

to_multiply = [([[1, 2],
                 [3, 4]],
                [[1, 2],
                 [3, 4]],
                [[7, 10],
                 [15, 22]]),
               ([[5]], [[10]], [[50]]),
               ([[1, 2],
                 [3, 4]],
                [[1, 2, 3],
                 [4, 5, 6]],
                [[9, 12, 15],
                 [19, 26, 33]]),
               ([[1]], [[1, 1], [1, 1]], TypeError()),
               ([[]], [[]], TypeError()),
               ([], [], TypeError())]


class MatrixOperationsTest(unittest.TestCase):
    def test_matrix_multiplication(self):
        for test in to_multiply:
            matrix1, matrix2, expected = test
            if isinstance(expected, TypeError):
                try:
                    _ = multiply(matrix1, matrix2)
                except TypeError:
                    continue
            actual = multiply(matrix1, matrix2)
            n, k = len(expected), len(expected[0])
            for i in range(n):
                for j in range(k):
                    self.assertAlmostEqual(first=expected[i][j],
                                           second=actual[i][j],
                                           delta=1e-12)

    def test_matrix_transposition(self):
        for test in to_transpose:
            matrix = test[0]
            expected = test[1]
            if isinstance(expected, TypeError):
                try:
                    _ = transpose(matrix)
                except TypeError:
                    continue
            actual = transpose(matrix)
            n, m = len(matrix), len(matrix[0])
            for j in range(m):
                for i in range(n):
                    self.assertAlmostEqual(first=expected[j][i],
                                           second=actual[j][i],
                                           delta=1e-12)
