from itertools import permutations

def ind(x, y, n):
    return x * n + y

def parse_input():
    with open("input.txt", 'r') as f:
        lines = map(lambda x: x.split(), f.readlines())

        nodes = set()

        for line in lines:
            nodes.add(line[0])
            nodes.add(line[2])

        nodes = sorted(nodes)
        n = len(nodes)
        graph = [-1] * (n ** 2)
        
        for line in lines:
            node1 = nodes.index(line[0])
            node2 = nodes.index(line[2])
            graph[ind(node1, node2, n)] = int(line[-1])
            graph[ind(node2, node1, n)] = int(line[-1])

        return (graph, nodes)

def brute():
    (graph, nodes) = parse_input()
    n = len(nodes)
    best = None
    
    for path in permutations(range(0, n)):
        dist = 0
        
        for idx in range(0, n - 1):
            curr = graph[ind(path[idx], path[idx + 1], n)]
            
            if curr == -1:
                continue
            
            dist += curr

        if curr == -1:
            continue

        # > for second part
        if best == None or dist < best:
            best = dist

    print(best)

brute()
