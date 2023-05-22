import operator

epsilon = 1e-9
operators = dict([('+', operator.add),
                  ('*', operator.mul),
                  ('-', operator.sub),
                  ('^', operator.pow)])
operator_priorities = dict([('+', 1), ('-', 1), ('*', 2), ('^', 3)])
brackets = dict([('(', ')'), ('[', ']')])
read_predicates = dict([('x', lambda x: x == 'x'),
                        ('operator', lambda x: x in operators.keys()),
                        ('open bracket', lambda x: x in brackets.keys()),
                        ('close bracket', lambda x: x in brackets.values())])
to_parse = ['(x + 2) * (x + 3)',
            '(((x - 2) * x - 2) * x)',
            '(x * x * x) - (x * (x + 3))',
            '1+(2*2 - 3)',
            '1 + 1 - 1 + 1 - 1 - 1 - 1 + 1',
            '(x + 1) ^ (5 - 3)',
            '(x ^ 2 + 1) ^ 4',
            'x',
            '0',
            '(x - 1) * [x + 3] * (x ^ 2 + 2 * x + 3)']
to_decompose = [('x ^ 2 - 19 * x + 6',
                 'x ^ 3 * (x + 2) * (x + 3) ^ 2 * (x ^ 2 + 2 * x + 13)'),
                ('x ^ 2 - 19 * x + 6', '(x - 1) * (x ^ 2 + 5 * x + 6'),
                ('x ^ 2 - 6 * x + 8', 'x ^ 3 + 8'),
                ('x ^ 2 + 23', '(x + 1) * (x ^ 2 + 6 * x + 13)'),
                ('2 * x ^ 3 - 2 * x ^ 2 + 5', '(x - 1) ^ 2 * (x ^ 2 + 4)')]
to_integrate = ['']

