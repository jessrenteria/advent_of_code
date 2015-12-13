def parse_input():
    f = open("input1.txt", 'r')
    lines = []

    for line in f:
        lines += [map(int, line.split('x'))]

    return lines

def get_ribbon():
    presents = parse_input()
    total = 0

    for p in presents:
        total += p[0] * p[1] * p[2]
        total += min(p) * 2
        p.remove(min(p))
        total += min(p) * 2

    return total

print(get_ribbon())

