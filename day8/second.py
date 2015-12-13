def parse_input():
    with open("input.txt", 'r') as f:
        return map(lambda x: x.strip()[1:-1], f.readlines())

def loss(s):
    return 2 + s.count('\\') + s.count('"')

def difference():
    lines = parse_input()
    print(reduce(lambda acc, e: acc + loss(e), lines, 0))

difference()

        

