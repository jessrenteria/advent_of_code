def parse_input():
    with open("input.txt", 'r') as f:
        return f.read()

def handle_move(move, current):
    if move == '^':
        current = (current[0], current[1] + 1)
    elif move == 'v':
        current = (current[0], current[1] - 1)
    elif move == '>':
        current = (current[0] + 1, current[1])
    elif move == '<':
        current = (current[0] - 1, current[1])

    return current


def num_houses():
    data = parse_input()
    visited = set()

    current_santa = (0,0)
    current_robot = (0,0)

    visited.add(current_santa)
    santa_mover = False

    for move in data:
        santa_mover = not santa_mover

        if santa_mover:
            current_santa = handle_move(move, current_santa)
            visited.add(current_santa)
        else:
            current_robot = handle_move(move, current_robot)
            visited.add(current_robot)

    print(len(visited))

num_houses()

