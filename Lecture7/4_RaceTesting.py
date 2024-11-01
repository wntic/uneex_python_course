from itertools import cycle, islice


def speed(path, stops, times):
    stops_cycle = cycle(stops)
    path_iter = iter(path)
    time_iter = iter(times)

    while True:
        stop_count = next(stops_cycle)
        distance = sum(islice(path_iter, stop_count))
        if distance == 0:
            break

        time_spent = next(time_iter)
        yield distance / time_spent
