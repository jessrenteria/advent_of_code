from itertools import permutations

def parse_input():
    def happy(s, i):
        if s == "lose":
            return -int(i)
        elif s == "gain":
            return int(i)
        else:
            raise Exception("Invalid input to happy")

    lines = []
    
    with open("input.txt", 'r') as f:
        for line in f:
            line = line.strip().split()
            lines.append((line[0], line[-1][:-1], happy(line[2], line[3])))

    return lines

def optimize():
    lines = parse_input()
    rules = {}

    for rule in lines:
        if rule[0] not in rules:
            rules[rule[0]] = {}

        rules[rule[0]][rule[1]] = rule[2]

    rules["Me"] = {}

    for guest in rules.keys():
        rules[guest]["Me"] = 0
        rules["Me"][guest] = 0

    best = -100000000

    for arr in permutations(rules.keys()):
        net = 0

        for idx in range(len(arr)):
            net += rules[arr[idx]][arr[(idx + 1) % len(arr)]]
            net += rules[arr[(idx + 1) % len(arr)]][arr[idx]]

        if net > best:
            best = net

    print(best)

optimize()


