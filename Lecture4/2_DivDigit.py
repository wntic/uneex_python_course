def divdigit(N: int) -> int:
    div_count = 0

    for digit in str(N):
        divisor = int(digit)
        if divisor != 0 and N % divisor == 0:
            div_count += 1

    return div_count
