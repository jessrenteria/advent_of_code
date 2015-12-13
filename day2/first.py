def parse_input():
    f = open("input1.txt", 'r')
    lines = []

    for line in f:
        lines += [map(int, line.split('x'))]

    return lines

def get_sq_feet():
    presents = parse_input()
    total = 0

    for p in presents:
        a1 = 2 * p[0] * p[1]
        a2 = 2 * p[1] * p[2]
        a3 = 2 * p[0] * p[2]

        total += a1 + a2 + a3 + min(a1, a2, a3) / 2

    return total

print(get_sq_feet())

