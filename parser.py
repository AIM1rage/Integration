from poly import *
from constants import operators


def parse(expression: str) -> Poly:
    return Poly(list())


def calculate_postfix(postfix):
    stack = list()
    for token in postfix:
        if type(token) is int:
            stack.append(token)
        elif type(token) is Poly:
            stack.append(token)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            stack.append(operators[token](operand1, operand2))
    return stack.pop()


def to_postfix(expression):

    pass


def read_number(expression, index):
    pass


def read_x(expression, index):
    pass


def read_operator(expression, index):
    pass


if __name__ == '__main__':
    input1 = list([3, 4, '-'])
    input2 = list([2, 7, '^'])
    result1 = calculate_postfix(input1)
    result2 = calculate_postfix(input2)
    pass
