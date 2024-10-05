from typing import Callable


def BinPow(a: object, n: int, f: Callable):
    result = a
    power = a
    n -= 1

    while n > 0:
        if n & 1:  # Division by 2
            result = f(result, power)
        power = f(power, power)
        n //= 2

    return result
