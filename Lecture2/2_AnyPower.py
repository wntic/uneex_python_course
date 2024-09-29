def is_power(n: int) -> str:
    for base in range(2, int(n**0.5) + 1):
        power = base
        while power <= n:
            power *= base
            if power == n:
                return "YES"
    return "NO"


def main() -> None:
    n = int(input())
    print(is_power(n))


if __name__ == "__main__":
    main()
