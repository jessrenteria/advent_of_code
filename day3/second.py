def parse_input():
    f = open("input.txt", 'r')

    return f.read()

def num_houses():
    data = parse_input()

    visited = set()

    current_santa = (0,0)
    current_robot = (0,0)

    visited.add(current_santa)

    santa_mover = False

    for move in data:
        santa_mover = not santa_mover
        if move == '^':
            if santa_mover:
                current_santa = (current_santa[0], current_santa[1] + 1)
            else:
                current_robot = (current_robot[0], current_robot[1] + 1)
        elif move == 'v':
            if santa_mover:
                current_santa = (current_santa[0], current_santa[1] - 1)
            else:
                current_robot = (current_robot[0], current_robot[1] - 1)
        elif move == '>':
            if santa_mover:
                current_santa = (current_santa[0] + 1, current_santa[1])
            else:
                current_robot = (current_robot[0] + 1, current_robot[1])
        elif move == '<':
            if santa_mover:
                current_santa = (current_santa[0] - 1, current_santa[1])
            else:
                current_robot = (current_robot[0] - 1, current_robot[1])

        if santa_mover:
            visited.add(current_santa)
        else:
            visited.add(current_robot)

    return len(visited)

print(num_houses())

