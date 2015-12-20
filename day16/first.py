def parse_input():
    with open("input.txt", 'r') as f:
        sues = []

        for line in f:
            line = line.strip().split()
            sue = {}

            for idx in range(2, len(line) - 2, 2):
                sue[line[idx][:-1]] = int(line[idx + 1][:-1])

            sue[line[-2][:-1]] = int(line[-1])
            sues.append(sue)

        return sues

def parse_standard():
    with open("gold_standard.txt", 'r') as f:
        gold = {}

        for line in f:
            line = line.strip().split()
            gold[line[0][:-1]] = int(line[1])

        return gold

def find_sue():
    sues = parse_input()
    gold = parse_standard()
    best_overlap = None
    best_sue = -1

    for idx in range(len(sues)):
        overlap = 0

        for trait in sues[idx].keys():
            if sues[idx][trait] == gold[trait]:
                overlap += 1

        if best_overlap == None or overlap > best_overlap:
            best_overlap = overlap
            best_sue = idx + 1

    print(best_sue)

find_sue()


