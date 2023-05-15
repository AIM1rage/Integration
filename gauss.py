from constants import epsilon


class NoSolutionException(Exception):
    pass


# Класс Solver реализует методы для решения СЛУ методом Гаусса.

class Solver:
    # принимает матрицу коэффициентов и массив свободных членов,
    # и возвращает массив значений неизвестных переменных.
    def solve(matrix: list[list[float]],
              free_members: list[float]) -> list[float]:
        inner_matrix = [row[:] for row in matrix]
        inner_free_members = free_members[:]
        rows_count = len(inner_matrix)
        columns_count = len(inner_matrix[0])

        for j in range(columns_count):
            for i in range(j, rows_count):
                if abs(inner_matrix[i][j]) < Solver.epsilon:
                    continue
                inner_matrix[i], inner_matrix[j] = inner_matrix[j], \
                    inner_matrix[i]
                inner_free_members[i], inner_free_members[j] = \
                    inner_free_members[j], inner_free_members[i]
                Solver.eliminate_column(inner_matrix, inner_free_members, j)
                break

        if Solver.is_system_unsolvable(inner_matrix, inner_free_members):
            raise NoSolutionException("No solution")

        return Solver.get_solution(inner_matrix, inner_free_members)

    # проверяет, можно ли решить систему линейных уравнений.
    # Если система разрешима, то функция возвращает false,
    # если она не разрешима, то возвращает true.
    def is_system_unsolvable(matrix: list[list[float]],
                             free_members: list[float]) -> bool:
        return any(all(abs(value) < epsilon for value in pair[0]) and
                   abs(pair[1]) > epsilon
                   for pair in zip(matrix, free_members))

    # вычисляет значения неизвестных переменных.
    def get_solution(matrix: list[list[float]], free_members: list[float]) -> \
            list[float]:
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
    def eliminate_column(matrix: list[list[float]], free_members: list[float],
                         column_to_eliminate: int):
        for i, row in enumerate(matrix):
            if abs(row[column_to_eliminate]) < epsilon or \
                    i == column_to_eliminate:
                continue
            scalar = -matrix[i][column_to_eliminate] / matrix[
                column_to_eliminate][column_to_eliminate]
            subtrahend = [value * scalar for value in
                          matrix[column_to_eliminate]]
            matrix[i], free_members[i] = Solver.add_rows(
                matrix[i], subtrahend), \
                free_members[i] + scalar * free_members[column_to_eliminate]

    # складывает строки матрицы.
    def add_rows(row1: list[float], row2: list[float]) -> list[float]:
        return [value1 + value2 for value1, value2 in zip(row1, row2)]
