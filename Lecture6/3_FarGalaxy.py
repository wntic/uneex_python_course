def get_galaxies() -> list[tuple]:
    galaxies = set()
    while True:
        row = input()
        if " " not in row:
            break

        x, y, z, name = row.split()
        galaxies.add((float(x), float(y), float(z), str(name)))
    return list(galaxies)


def galaxy_distance(g1: tuple, g2: tuple) -> float:
    x1, y1, z1, _ = g1
    x2, y2, z2, _ = g2

    return ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** 0.5


def far_galaxy(g: list[tuple]) -> list[str]:
    max_dist = 0.0

    for i in range(len(galaxies)):
        for j in range(1, len(galaxies)):
            dist = galaxy_distance(g[i], g[j])
            if dist > max_dist:
                max_dist = dist
                far_galaxies = [g[i][-1], g[j][-1]]

    return sorted(far_galaxies)


if __name__ == "__main__":
    galaxies = get_galaxies()
    res = far_galaxy(galaxies)
    print(*res)
