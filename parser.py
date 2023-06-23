import re
from constants import *
from poly import *


class Parser:
    @staticmethod
    def parse(expression: str) -> Poly:
        if not expression:
            raise ValueError('Пустая строка ввода!')
        expression_without_spaces = str(re.sub('\\s', '', expression))
        return Parser._calculate_postfix_(
            Parser._to_postfix_(expression_without_spaces))

    @staticmethod
    def _calculate_postfix_(postfix):
        stack = list()
        for token in postfix:
            if type(token) == Poly:
                stack.append(token)
            elif token in operators:
                operand2 = stack.pop()
                operand1 = stack.pop()
                stack.append(operators[token](operand1, operand2))
            else:
                line = ' '.join(map(str, postfix))
                raise ValueError(f'Некорректный ввод! Стек: "{line}"')
        if len(stack) != 1:
            line = ' '.join(map(str, postfix))
            raise ValueError(
                f'Некорректный ввод! Стек не опустошился: "{line}"')
        return stack.pop()

    @staticmethod
    def _to_postfix_(expression):
        postfix = list()
        stack = list()
        index = 0
        previous_token = None
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
            previous_token, index = Parser._add_token_(number_result,
                                                       x_result,
                                                       operator_result,
                                                       open_bracket_result,
                                                       close_bracket_result,
                                                       expression,
                                                       postfix, stack, index,
                                                       previous_token)
        postfix.extend(reversed(stack))
        return postfix

    @staticmethod
    def _add_token_(number_result, x_result, operator_result,
                    open_bracket_result, close_bracket_result,
                    expression, postfix, stack, index, previous_token):
        if number_result or x_result:
            if number_result:
                token = Poly([number_result[0]])
                postfix.append(token)
                index = number_result[1]
            else:
                token = Poly([1, 0])
                postfix.append(token)
                index = x_result[1]
            if type(previous_token) == Poly:
                stack.append('*')
        elif operator_result:
            token = operator_result[0]
            if previous_token in operators.keys():
                raise ValueError(f'Двойной оператор! '
                                 f'Не следует операторы '
                                 f'"{previous_token}" и "{token}" подряд. '
                                 f'Выражение: "{expression}"')
            if token == '-' and (
                    previous_token is None or previous_token in brackets.keys()):
                postfix.append(0)
            while len(stack) > 0 and \
                    stack[-1] in operators.keys() and \
                    operator_priorities[stack[-1]] >= \
                    operator_priorities[operator_result[0]]:
                postfix.append(stack.pop())
            stack.append(token)
            index = operator_result[1]
        elif open_bracket_result:
            token = open_bracket_result[0]
            if previous_token == brackets[token]:
                stack.append('*')
            stack.append(token)
            index = open_bracket_result[1]
        elif close_bracket_result:
            token = close_bracket_result[0]
            while len(stack) > 0 and stack[-1] not in brackets.keys():
                postfix.append(stack.pop())
            if len(stack) == 0 or \
                    brackets[stack.pop()] != close_bracket_result[0]:
                raise ValueError(
                    f'Пропущена открывающая скобка! Выражение: "{expression}"')
            index = close_bracket_result[1]
        else:
            raise ValueError(f'Неизвестный символ "{expression[index]}"!')
        return token, index

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
