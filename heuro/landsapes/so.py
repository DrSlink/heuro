from math import cos, pi


def rastrigin(x, a=10):
    res = a * len(x)
    for x_i in x:
        res += x_i ** 2 - a * cos(2 * pi * x_i)
    return res