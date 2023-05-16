import operator

epsilon = 1e-6
operators = dict([('+', operator.add),
                  ('*', operator.mul),
                  ('-', operator.add),
                  ('^', operator.pow),
                  ('**', operator.pow)])
operator_priorities = dict([('+', 1), ('-', 1), ('*', 2), ('**', 3), ('^', 3)])
