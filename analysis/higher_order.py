def curry2(f):
    """Returns a function g such that g(x)(y) == f(x, y)

    >>> from operator import add
    >>> add_three = curry2(add)(3)
    >>> add_three(4)
    """
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g
