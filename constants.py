import operator

epsilon = 1e-6
operators = dict([('+', operator.add),
                  ('*', operator.mul),
                  ('-', operator.sub),
                  ('^', operator.pow)])
operator_priorities = dict([('+', 1), ('-', 1), ('*', 2), ('^', 3)])
brackets = dict([('(', ')')])
read_predicates = dict([('x', lambda x: x == 'x'),
                        ('operator', lambda x: x in operators.keys()),
                        ('open bracket', lambda x: x in brackets.keys()),
                        ('close bracket', lambda x: x in brackets.values())])
