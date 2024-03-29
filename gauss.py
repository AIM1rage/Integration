from constants import *
import matrix_operations


# Класс Solver реализует методы для решения СЛУ методом Гаусса.
class Solver:
    # преобразует СЛУ для применения МНК
    @staticmethod
    def convert_system(matrix, free_members):
        transposed_matrix = matrix_operations.transpose(matrix)
        new_matrix = matrix_operations.multiply(
            transposed_matrix,
            matrix)
        new_free_members = [z[0] for z in
                            matrix_operations.multiply(transposed_matrix,
                                                       [[y] for y in
                                                        free_members])]
        return new_matrix, new_free_members

    # принимает матрицу коэффициентов и массив свободных членов,
    # и возвращает массив значений неизвестных переменных.
    @staticmethod
    def solve(matrix: list[list[float]],
              free_members: list[float]):
        matrix, free_members = Solver.convert_system(matrix, free_members)
        rows_count = len(matrix)
        columns_count = len(matrix[0])

        for j in range(columns_count):
            for i in range(j, rows_count):
                if abs(matrix[i][j]) < epsilon:
                    continue
                matrix[i], matrix[j] = matrix[j], matrix[i]
                free_members[i], free_members[j] = \
                    free_members[j], free_members[i]
                Solver._eliminate_column_(matrix, free_members, j)
                break

        if Solver._is_system_unsolvable_(matrix, free_members):
            return None

        return Solver._get_solution_(matrix, free_members)

    # проверяет, можно ли решить систему линейных уравнений.
    # Если система разрешима, то функция возвращает false,
    # если она не разрешима, то возвращает true.
    @staticmethod
    def _is_system_unsolvable_(matrix, free_members):
        return any(all(abs(value) < epsilon for value in pair[0]) and
                   abs(pair[1]) > epsilon
                   for pair in zip(matrix, free_members))

    # вычисляет значения неизвестных переменных.
    @staticmethod
    def _get_solution_(matrix, free_members):
        rows_count = len(matrix)
        columns_count = len(matrix[0])
        solution = [0] * columns_count
        for i in range(rows_count):
            for j in range(i, columns_count):
                if abs(matrix[i][j]) < epsilon:
                    continue
                solution[j] = free_members[i] / matrix[i][j]
                break
        return solution

    # получает на вход матрицу, массив свободных членов и номер столбца,
    # который нужно обработать.
    # Функция вычисляет подходящий множитель и складывает строки матрицы,
    # чтобы получить нули во всех остальных строках в текущем столбце.
    @staticmethod
    def _eliminate_column_(matrix, free_members, column_to_eliminate):
        for i, row in enumerate(matrix):
            if abs(row[column_to_eliminate]) < epsilon or \
                    i == column_to_eliminate:
                continue
            scalar = -matrix[i][column_to_eliminate] / matrix[
                column_to_eliminate][column_to_eliminate]
            subtrahend = [value * scalar for value in
                          matrix[column_to_eliminate]]
            matrix[i] = Solver._add_rows_(matrix[i], subtrahend)
            free_members[i] = free_members[i] + scalar * free_members[
                column_to_eliminate]

    # складывает строки матрицы.
    @staticmethod
    def _add_rows_(row1, row2):
        return [value1 + value2 for value1, value2 in zip(row1, row2)]
