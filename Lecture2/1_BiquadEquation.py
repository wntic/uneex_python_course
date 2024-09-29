from typing import List


def sqrt_root(x: float) -> list[float]:
    if x <= 0:
        return []
    return [-(x**0.5), x**0.5]


def solve_biquadratic_equation(a: int, b: int, c: int) -> List[float]:
    if a == b == c == 0:
        return [
            -1,
        ]

    roots = []
    if a != 0:
        D = b**2 - 4 * a * c
        if D < 0:
            return [
                0,
            ]
        elif D == 0:
            x = -b / (2 * a)
            roots += sqrt_root(x)
        else:
            x1 = (-b + D**0.5) / (2 * a)
            x2 = (-b - D**0.5) / (2 * a)
            roots += sqrt_root(x1) + sqrt_root(x2)
            if x1 == 0 or x2 == 0:
                roots.append(0)
    else:
        if b == 0:
            roots.append(0)
        else:
            x = -c / b
            roots += sqrt_root(x)

    if not roots:
        return [
            0,
        ]
    return sorted(roots)


def print_roots(roots: List[float]) -> None:
    for i in range(len(roots)):
        if i != len(roots) - 1:
            print(roots[i], end=" ")
        else:
            print(roots[i])


def main() -> None:
    a, b, c = map(int, input().split(","))
    roots = solve_biquadratic_equation(a, b, c)
    print_roots(roots)


if __name__ == "__main__":
    main()
