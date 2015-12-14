def parse_input():
    with open("input.txt", 'r') as f:
        reindeer = {}
        lines = map(lambda x: x.strip().split(), f.readlines())

        for line in lines:
            reindeer[line[0]] = (int(line[3]), int(line[6]), int(line[-2]))

        return reindeer

"""
Simulates a single timestep of the Reindeer Olympics.

    reindeer: reindeer -> [speed, flight time, rest time]
    state: reindeer -> [flight time left, rest time left, current distance]
    points: reindeer -> current points
"""
def step(reindeer, state, points):
    best = None
    
    for r in reindeer.keys():
        if state[r][0] > 0:
            state[r][0] -= 1
            state[r][2] += reindeer[r][0]
        elif state[r][1] > 0:
            state[r][1] -= 1
            if state[r][1] == 0:
                state[r][1] = reindeer[r][2]
                state[r][0] = reindeer[r][1]

        if best == None or state[r][2] > best:
            best = state[r][2]

    for r in reindeer.keys():
        if state[r][2] == best:
            points[r] += 1

    return state, points

def simulate():
    t = 2503
    reindeer = parse_input()
    state = {}
    points = {}

    for r in reindeer.keys():
        state[r] = [reindeer[r][1], reindeer[r][2], 0]
        points[r] = 0

    best = None

    for _ in range(t):
        state, points = step(reindeer, state, points)

    for r in reindeer.keys():
        if best == None or points[r] > best:
            best = points[r]

    print(best)

simulate()


                    
