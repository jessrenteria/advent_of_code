def print_lights(lights):
    print("")
    for row in range(len(lights)):
        s = ""
        for col in range(len(lights[row])):
            s += 'o' if lights[row][col] == 1 else ' '
        print(s)

def parse_input():
    with open("input.txt", 'r') as f:
        lights = [[0] * 100] * 100
        lines = map(lambda x: x.strip(), f.readlines())

        for idx in range(len(lines)):
            lights[idx] = map(lambda x: 0 if x == '.' else 1, lines[idx])

        print_lights(lights)
        return lights

def get_neighbors(x, y):
    neighbors = []

    for nx in range(x - 1, x + 2):
        for ny in range(y - 1, y + 2):
            if not (nx < 0 or ny < 0 or nx >= 100 or ny >= 100 or
                    (nx == x and ny == y)):
                neighbors.append((nx, ny))

    return neighbors

def num_lights():
    lights = parse_input()

    def new_state(x, y):
        neighbors = get_neighbors(x, y)
        num_on = 0
        
        for n in neighbors:
            if lights[n[1]][n[0]] == 1:
                num_on += 1
        
        if lights[y][x] == 0:
            if num_on == 3:
                return 1
        else:
            if num_on == 2 or num_on == 3:
                return 1

        return 0

    for _ in range(100):
        new_lights = [[0] * 100] * 100

        for y in range(100):
            new_lights[y] = [new_state(x, y) for x in range(len(new_lights[y]))]

        lights = new_lights
        print_lights(new_lights)

    print(sum([sum(row) for row in lights]))

num_lights()
