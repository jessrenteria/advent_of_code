def parse_input():
    f = open("input.txt", 'r')

    return map(lambda x: x.split(), f.readlines())

def num_lights_on():
    lines = parse_input()

    lights = [[0] * 1000 for _ in range(1000)]

    for line in lines:
        if line[0] == "turn":
            [x1, y1] = map(int, line[2].split(','))
            [x2, y2] = map(int, line[4].split(','))

            if line[1] == "on":
                for x in range(x1, x2 + 1):
                    for y in range(y1, y2 + 1):
                        lights[x][y] += 1
            elif line[1] == "off":
                for x in range(x1, x2 + 1):
                    for y in range(y1, y2 + 1):
                        lights[x][y] = max(lights[x][y] - 1, 0)
        elif line[0] == "toggle":
            [x1, y1] = map(int, line[1].split(','))
            [x2, y2] = map(int, line[3].split(','))

            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    lights[x][y] += 2

    return sum(map(sum, lights))

print(num_lights_on())
