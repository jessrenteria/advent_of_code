def parse_input():
    with open("input1.txt", 'r') as f:
        return f.read()

# Prints the number of the first instruction that lands us at the basement.
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
                print(pos)
                return

    print(-1)


find_basement()
