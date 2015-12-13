def parse_input():
    with open("input1.txt", 'r') as f:
        return map(lambda l: map(int, l.split('x')), f.readlines())

def get_ribbon():
    presents = parse_input()
    total = 0

    for p in presents:
        total += p[0] * p[1] * p[2]
        total += min(p) * 2
        p.remove(min(p))
        total += min(p) * 2

    print(total)

get_ribbon()

