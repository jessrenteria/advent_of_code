from itertools import permutations

def parse_input():
    def happiness(s, i):
        if s == "lose":
            return -int(i)
        elif s == "gain":
            return int(i)
        else:
            raise Exception("Invalid gain / loss declaration.")

    rules = {}
    
    with open("input.txt", 'r') as f:
        for rule in f:
            rule = rule.strip().split()
            
            if rule[0] not in rules:
                rules[rule[0]] = {}
            
            rules[rule[0]][rule[-1][:-1]] = happiness(rule[2], rule[3])

    return rules

def optimize():
    rules = parse_input()
    best = None

    for arr in permutations(rules.keys()):
        net = 0

        for idx in range(len(arr)):
            net += rules[arr[idx]][arr[(idx + 1) % len(arr)]]
            net += rules[arr[(idx + 1) % len(arr)]][arr[idx]]

        if best == None or net > best:
            best = net

    print(best)

optimize()
