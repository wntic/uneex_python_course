def turtle(coord, direction):
    x, y = coord  # начальные координаты

    while True:
        command = yield (x, y)
        if command == "f":  # Forward
            if direction == 0:  # East
                x += 1
            elif direction == 1:  # North
                y += 1
            elif direction == 2:  # West
                x -= 1
            elif direction == 3:  # South
                y -= 1
        elif command == "l":  # Left
            direction = (direction + 1) % 4
        elif command == "r":  # Right
            direction = (direction - 1) % 4
