from math import inf


def divide(first, second):

    if second != 0:

        result = first / second

    else:

        result = inf if first > 0 else -inf

    return result
