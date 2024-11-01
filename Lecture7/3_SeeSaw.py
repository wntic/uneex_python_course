from itertools import tee, zip_longest


def seesaw(sequence):
    sequence1, sequence2 = tee(sequence)

    even_iter = (x for x in sequence1 if x % 2 == 0)
    odd_iter = (x for x in sequence2 if x % 2 != 0)

    for even, odd in zip_longest(even_iter, odd_iter):
        if even is not None:
            yield even
        if odd is not None:
            yield odd
