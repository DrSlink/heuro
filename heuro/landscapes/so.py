from math import cos, pi


def rastrigin(x, a=10):
    res = a * len(x)
    for x_i in x:
        res += x_i ** 2 - a * cos(2 * pi * x_i)
    return res


def rosenbrock(x, a=1, b=100):
    res = 0
    for i in range(len(x) - 1):
        res += (a - x[i]) ** 2 + b * (x[i + 1] - x[i] ** 2) ** 2
    return res


def sphere(x):
    res = 0
    for x_i in x:
        res += x_i ** 2
    return res
