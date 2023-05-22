import re
from constants import *
from poly import *


class Parser:
    @staticmethod
    def parse(expression: str) -> Poly:
        expression_without_spaces = str(re.sub('\\s', '', expression))
        return Parser._calculate_postfix_(
            Parser._to_postfix_(expression_without_spaces))

    @staticmethod
    def _calculate_postfix_(postfix):
        stack = list()
        for token in postfix:
            if type(token) is int:
                stack.append(Poly([token]))
            elif token == 'x':
                stack.append(Poly([1, 0]))
            elif token in operators:
                operand2 = stack.pop()
                operand1 = stack.pop()
                Parser._check_operation_correctness_(operators[token],
                                                     operand1,
                                                     operand2)
                stack.append(operators[token](operand1, operand2))
        return stack.pop()

    @staticmethod
    def _to_postfix_(expression):
        postfix = list()
        stack = list()
        index = 0
        while index < len(expression):
            number_result = Parser._read_number_(
                expression, index)
            x_result = Parser._read_symbol_(
                expression, index, read_predicates['x'])
            operator_result = Parser._read_symbol_(
                expression, index, read_predicates['operator'])
            open_bracket_result = Parser._read_symbol_(
                expression, index, read_predicates['open bracket'])
            close_bracket_result = Parser._read_symbol_(
                expression, index, read_predicates['close bracket'])
            if number_result:
                postfix.append(number_result[0])
                index = number_result[1]
            elif x_result:
                postfix.append(x_result[0])
                index = x_result[1]
            elif operator_result:
                while len(stack) > 0 and \
                        stack[-1] in operators.keys() and \
                        operator_priorities[stack[-1]] >= \
                        operator_priorities[operator_result[0]]:
                    postfix.append(stack.pop())
                stack.append(operator_result[0])
                index = operator_result[1]
            elif open_bracket_result:
                stack.append(open_bracket_result[0])
                index = open_bracket_result[1]
            elif close_bracket_result:
                while len(stack) > 0 and stack[-1] not in brackets.keys():
                    postfix.append(stack.pop())
                if len(stack) == 0 or \
                        brackets[stack.pop()] != close_bracket_result[0]:
                    raise ArithmeticError
                index = close_bracket_result[1]
            else:
                raise ArithmeticError
        postfix.extend(reversed(stack))
        return postfix

    # пытается прочитать число и возвращает (number, index),
    # если не получилось - возвращает None
    @staticmethod
    def _read_number_(expression, index):
        digits = list()
        while index < len(expression) and str(expression[index]).isdigit():
            digits.append(expression[index])
            index += 1
        if digits:
            return int(''.join(digits)), index
        return None

    # пытается прочитать символ и возвращает (symbol, index),
    # если не получилось - возвращает None
    @staticmethod
    def _read_symbol_(expression, index, predicate):
        if index < len(expression) and predicate(expression[index]):
            index += 1
            return expression[index - 1], index
        return None

    @staticmethod
    def _check_operation_correctness_(operator_to_check, operand1, operand2):
        # TODO
        return True
