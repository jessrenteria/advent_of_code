from itertools import combinations

def parse_input():
    with open("input.txt", 'r') as f:
        containers = []

        for line in f:
            containers.append(int(line.strip()))

        return containers

def num_combinations():
    containers = parse_input()
    r_min = None

    for r in range(1, len(containers) + 1):
        for comb in combinations(containers, r):
            if sum(comb) == 150:
                r_min = r
                break
        if r_min != None:
            break

    total = 0

    for comb in combinations(containers, r_min):
        if sum(comb) == 150:
            total += 1

    print(total)

num_combinations()

