def parse_input():
    with open("input.txt", 'r') as f:
        reindeer = {}
        lines = map(lambda x: x.strip().split(), f.readlines())

        for line in lines:
            reindeer[line[0]] = (int(line[3]), int(line[6]), int(line[-2]))

        return reindeer

def simulate():
    t = 2503
    reindeer = parse_input()
    dist = {}

    best = None

    for r in reindeer.keys():
        dist[r] = ((t / (reindeer[r][1] + reindeer[r][2])) * reindeer[r][0] *
                   reindeer[r][1])
        left = (t % (reindeer[r][1] + reindeer[r][2]))
        dist[r] += min(left, reindeer[r][1]) * reindeer[r][0]

        if best == None or dist[r] > best:
            best = dist[r]

    print(best)

simulate()


                    
