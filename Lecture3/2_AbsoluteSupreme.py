from itertools import permutations


def get_input_sequence() -> list[list[int]]:
    triples = []

    while True:
        triple = input()
        if not triple:
            break
        triples.append([int(x) for x in triple.split(",")])

    return triples


def is_not_less(a: list[int], b: list[int]) -> bool:
    for i, j, k in permutations([0, 1, 2]):
        if a[0] <= b[i] and a[1] <= b[j] and a[2] <= b[k]:
            if a[0] < b[i] or a[1] < b[j] or a[2] < b[k]:
                return False
    return True


def find_first_not_less(triples) -> int:
    n = len(triples)

    for i in range(n):
        is_not_less_than_all = True
        for j in range(i + 1, n):
            if not is_not_less(triples[i], triples[j]):
                is_not_less_than_all = False
                break
        if is_not_less_than_all:
            return i
    return 0


def sort_triples(triples: list[list[int]]) -> list[list[int]]:
    sorted_triples = []

    while triples:
        idx = find_first_not_less(triples)
        sorted_triples.insert(0, triples.pop(idx))

    return reversed(sorted_triples)


def absolute_supreme() -> None:
    triples = get_input_sequence()
    sorted_triples = sort_triples(triples)

    for triple in sorted_triples:
        print(", ".join(map(str, triple)))


if __name__ == "__main__":
    absolute_supreme()
