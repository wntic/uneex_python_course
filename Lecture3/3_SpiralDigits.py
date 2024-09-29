def get_matrix_size() -> tuple[int]:
    N, M = map(int, input().split(","))
    return N, M


def update_fill_num(num):
    if num == 9:
        return 0
    return num + 1


def spiral_digits() -> None:
    N, M = get_matrix_size()
    spiral = [[-1 for _ in range(N)] for _ in range(M)]

    # Spiral bounds
    top, bottom, left, right = 0, M - 1, 0, N - 1

    fill_num = 0
    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            spiral[top][i] = fill_num
            fill_num = update_fill_num(fill_num)
        top += 1

        for i in range(top, bottom + 1):
            spiral[i][right] = fill_num
            fill_num = update_fill_num(fill_num)
        right -= 1

        if top <= bottom:
            for i in range(right, left - 1, -1):
                spiral[bottom][i] = fill_num
                fill_num = update_fill_num(fill_num)
            bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                spiral[i][left] = fill_num
                fill_num = update_fill_num(fill_num)
            left += 1

    return spiral


if __name__ == "__main__":
    spiral = spiral_digits()
    for i in range(len(spiral)):
        print(*spiral[i])
