def half_transpose() -> None:
    matrix = [[int(x) for x in input().split(",")]]
    size = len(matrix[0])

    while len(matrix) != size:
        row = [int(x) for x in input().split(",")]
        matrix.append(row)

    result = []

    for i in range(size):
        r = []
        for j in range(0, i + 1):
            r.append(matrix[i][j])

        for j in range(i - 1, -1, -1):
            r.append(matrix[j][i])

        result.append(r)

    return result


if __name__ == "__main__":
    result = half_transpose()
    for row in result:
        print(",".join(map(str, row)))
