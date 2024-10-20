from bisect import bisect_left


def get_input_sequence() -> set[int]:
    seq = set(eval(input()))
    return seq


def three_squares(input_seq: set[int]) -> int:
    M = max(input_seq)  # max sequence item

    squares_sum = set()
    max_sqrt = int(M**0.5)
    squares = [i * i for i in range(max_sqrt + 1)]

    for i in range(1, max_sqrt + 1):
        i2 = squares[i]  # i**2
        for j in range(i, max_sqrt + 1):
            j2 = squares[j]  # j**2
            if i2 + j2 > M:
                break
            for k in range(j, max_sqrt + 1):
                k2 = squares[k]  # k**2
                sum_squares = i2 + j2 + k2
                if sum_squares <= M:
                    squares_sum.add(sum_squares)
                else:
                    break
    squares_sum = sorted(squares_sum)

    count = 0
    for num in input_seq:
        bisect = bisect_left(squares_sum, num)
        if bisect < len(squares_sum) and squares_sum[bisect] == num:
            count += 1

    return count


def main():
    input_seq = get_input_sequence()
    res = three_squares(input_seq)
    print(res)


if __name__ == "__main__":
    main()
