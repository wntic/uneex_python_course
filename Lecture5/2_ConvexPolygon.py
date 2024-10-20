import math


def get_polygon_coords() -> list[tuple[int]]:
    coords = []
    while True:
        coord = input()
        if not coord:
            break
        x, y = map(int, coord.split(", "))
        coords.append((x, y))
    return coords


def vector_product(origin, point_a, point_b):
    return (point_a[0] - origin[0]) * (point_b[1] - origin[1]) - (
        point_a[1] - origin[1]
    ) * (point_b[0] - origin[0])


def convex_polygon(points):
    start_point = min(points, key=lambda p: (p[1], p[0]))
    points.remove(start_point)
    points.sort(
        key=lambda p: (
            math.atan2(p[1] - start_point[1], p[0] - start_point[0]),
            p[0],
            p[1],
        )
    )
    points.insert(0, start_point)

    boundary = [points[0], points[1]]

    for i in range(2, len(points)):
        while (
            len(boundary) > 1
            and vector_product(boundary[-2], boundary[-1], points[i]) <= 0
        ):
            boundary.pop()
        boundary.append(points[i])

    return len(boundary) == len(points)


def main():
    polygon_coords = get_polygon_coords()
    print(convex_polygon(polygon_coords))


if __name__ == "__main__":
    main()
