from math import prod


def get_dots() -> list[list[float]]:
    dots = []
    while True:
        dot = input()
        if not dot:
            break
        dots.append([float(coordinate) for coordinate in dot.split(",")])
    return dots


def get_min_max_coords(dots: list[list[float]]) -> tuple[list[float]]:
    x_coords = [dot[0] for dot in dots]
    y_coords = [dot[1] for dot in dots]
    z_coords = [dot[2] for dot in dots]
    return [min(x_coords), min(y_coords), min(z_coords)], [
        max(x_coords),
        max(y_coords),
        max(z_coords),
    ]


def get_min_volume(dots: list[list[float]]) -> float:
    min, max = get_min_max_coords(dots)
    distance = [b - a for a, b in zip(min, max)]
    return prod(distance)


def main() -> None:
    dots = get_dots()
    vol = get_min_volume(dots)
    print(vol)


if __name__ == "__main__":
    main()
