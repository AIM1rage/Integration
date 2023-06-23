import operator

epsilon = 1e-6
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
to_integrate = [('1', '(x^2 + 4)^2'),
                ('x^2 - 6x + 8', 'x^3 + 8'),
                ('1', '(x^2 + 1)^2'),
                ('2x', '(x^2 + 1)^2'),
                ('2x + 1', '2'),
                ('1', 'x + 1'), ('1', 'x^2 - 1'),
                ('4x^4 + 8x^3 - 3x - 3', 'x^3 + 2x^2 + x'),
                ('x^3 - 3', '(x - 1) * (x^2 - 1)'),
                ('x^2 - 1', 'x - 1'),
                ('x^2 + 23', '(x + 1) * (x^2 + 6x + 13)'),
                ('2x^3 - 2x^2 + 5', '(x - 1)^2 * (x^2 + 4)'),
                ('0', '1'),
                ('x - 1', 'x - 1'),
                ('1', '3')]
