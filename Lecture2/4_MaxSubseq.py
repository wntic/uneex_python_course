def main() -> None:
    current_len = 1
    max_len = 1

    x_0 = int(input())
    while True:
        x_1 = int(input())
        if x_1 == 0:
            if current_len > max_len:
                max_len = current_len
            break
        if x_1 >= x_0:
            current_len += 1
            x_0 = x_1
        else:
            if current_len > max_len:
                max_len = current_len
            current_len = 1
            x_0 = x_1
    print(max_len)


if __name__ == "__main__":
    main()
