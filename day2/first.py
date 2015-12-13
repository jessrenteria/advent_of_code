def parse_input():
    with open("input1.txt", 'r') as f:
        return map(lambda l: map(int, l.split('x')), f.readlines())

def get_sq_feet():
    presents = parse_input()
    total = 0

    for p in presents:
        a1 = 2 * p[0] * p[1]
        a2 = 2 * p[1] * p[2]
        a3 = 2 * p[0] * p[2]

        total += a1 + a2 + a3 + min(a1, a2, a3) / 2

    print(total)

get_sq_feet()

