def get_input_sequence() -> list[str]:
    tokens = []

    while True:
        row = input().strip()
        if not row:
            break

        tokens += [token for token in row.split()]
    return tokens


def count_unique_pairs(words: list[str]) -> int:
    unique_pairs = set()

    for i in range(len(words) - 1):
        pair = tuple(sorted([words[i], words[i + 1]]))
        if pair not in unique_pairs:
            unique_pairs.add(pair)

    pair = tuple(sorted([words[0], words[-1]]))
    if pair not in unique_pairs:
        unique_pairs.add(pair)

    return len(unique_pairs)


if __name__ == "__main__":
    words = get_input_sequence()
    len = count_unique_pairs(words)
    print(len)
