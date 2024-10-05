from typing import Callable
from math import *


def superposition(funmod: Callable, funseq: tuple[Callable]):
    funres = []

    def apply_funmod(func: Callable) -> Callable:
        return lambda x: funmod(func(x))

    funres = [apply_funmod(func) for func in funseq]
    return funres
