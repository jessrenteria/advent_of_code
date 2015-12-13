def parse_input():
    with open("input1.txt", 'r') as f:
        return f.read()

def find_basement():
    string = parse_input()
    floor = 0
    pos = 0

    for c in string:
        if c == '(':
            pos += 1
            floor += 1
        elif c == ')':
            pos += 1
            floor -= 1
            if floor == -1:
                return pos

    return -1


print(find_basement())
