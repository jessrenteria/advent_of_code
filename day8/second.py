def parse_input():
    f = open("input.txt", 'r')

    return map(lambda x: x.strip(), f.readlines())

def loss(s):
    return 2 + s.count('\\') + s.count('"')

def difference():
    lines = parse_input()
    print(reduce(lambda acc, e: acc + loss(e), lines, 0))

difference()

        

