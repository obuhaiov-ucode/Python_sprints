import functools

def multiplier(l: list):
    if isinstance(l, list) and all(isinstance(i, (int, float)) for i in l):
        return functools.reduce(lambda a, b: a * b, l)
    raise ValueError('The given data is invalid.')
