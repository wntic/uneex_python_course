def squares(width: int, height: int, *args) -> None:
    field = [["." for _ in range(width)] for _ in range(height)]

    for arg_data in args:
        x, y, s, c = arg_data

        for i in range(s):
            for j in range(s):
                if y + i < height and x + j < width:
                    field[y + i][x + j] = c

    for row in field:
        print("".join(row))


if __name__ == "__main__":
    squares(20, 23, (1, 1, 5, "@"), (2, 3, 1, "!"), (4, 5, 11, "#"), (8, 11, 9, "/"))
