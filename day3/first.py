def parse_input():
    f = open("input.txt", 'r')

    return f.read()

def num_houses():
    data = parse_input()

    visited = set()

    current = (0,0)

    visited.add(current)

    for move in data:
        if move == '^':
            current = (current[0], current[1] + 1)
        elif move == 'v':
            current = (current[0], current[1] - 1)
        elif move == '>':
            current = (current[0] + 1, current[1])
        elif move == '<':
            current = (current[0] - 1, current[1])

        visited.add(current)

    return len(visited)

print(num_houses())

