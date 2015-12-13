def parse_input():
    with open("input1.txt", 'r') as f:
        return f.read()

def find_floor():
    string = parse_input()
    floor = 0

    for c in string:
        if c == '(':
            floor += 1
        elif c == ')':
            floor -= 1

    return floor

print(find_floor())
