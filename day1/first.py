def parse_input():
    with open("input1.txt", 'r') as f:
        return f.read()

# Prints the current floor after following the instructions in the input.
def find_floor():
    string = parse_input()
    floor = 0

    for c in string:
        if c == '(':
            floor += 1
        elif c == ')':
            floor -= 1

    print(floor)

find_floor()
