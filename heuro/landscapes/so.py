from math import cos, pi


def rastrigin(x: list, a: float = 10) -> float:
    """Rastrigin mathematical function.

    Rastrigin function is a non-convex non-linear multimodal function.
    Finding the minimum of this function is a fairly difficult problem
    due to its large search space and its large number of local minima
    It has a global minimum at x = [0,..,0], f(x) = 0

    # Arguments:
        x: A nonempty list of numbers
        a: Constant, usually used 10

    # Returns
        Scalar function image
    """
    res = a * len(x)
    for x_i in x:
        res += x_i ** 2 - a * cos(2 * pi * x_i)
    return res


def rosenbrock(x: list, a: float = 1, b: float = 100) -> float:
    """Rosenbrock's banana function.

    Rosenbrock function is a non-convex function.
    The global minimum is inside a long, narrow, parabolic shaped flat valley.
    To find the valley is trivial.
    To converge to the global minimum, however, is difficult.
    It has a global minimum at x = [1,..,1], f(x) = 0

    # Arguments:
        x: A nonempty list of numbers
        a: Constant, usually used 10
        b: Constant, usually used 100

    # Returns
        Scalar function image
    """
    res = 0
    for i in range(len(x) - 1):
        res += (a - x[i]) ** 2 + b * (x[i + 1] - x[i] ** 2) ** 2
    return res


def sphere(x):
    res = 0
    for x_i in x:
        res += x_i ** 2
    return res
