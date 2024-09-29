def main() -> None:
    count_matrix = [[0 for _ in range(101)] for _ in range(101)]

    while True:
        pair = input()
        if not pair:
            break
        i, j = map(int, pair.split(","))

        count_matrix[i][j] += 1

    for i in range(101):
        for j in range(101):
            if count_matrix[i][j] > 0:
                for _ in range(count_matrix[i][j]):
                    print(f"{i}, {j}")


if __name__ == "__main__":
    main()
