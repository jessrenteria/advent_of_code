def parse_input():
    f = open("input.txt", 'r')

    # command, routed, operands
    commands = [[], [], []]

    lines = map(lambda x: x.split(), f.readlines())

    for idx in range(len(lines)):
        if len(lines[idx]) == 5:
            commands[0].append(lines[idx][1])
            commands[1].append(lines[idx][-1])
            commands[2].append((lines[idx][0], lines[idx][2]))
        elif len(lines[idx]) == 4:
            commands[0].append(lines[idx][0])
            commands[1].append(lines[idx][-1])
            commands[2].append((lines[idx][1], 0))
        elif len(lines[idx]) == 3:
            commands[0].append("ASSIGN")
            commands[1].append(lines[idx][-1])
            commands[2].append((lines[idx][0], 0))

    return commands

def simulate():
    c = parse_input()

    wires = {}

    done = set()

    for idx in range(len(c[0])):
        if c[0][idx] == "ASSIGN":
            x = 0
            try:
                x = int(c[2][idx][0])
            except ValueError:
                continue

            wires[c[1][idx]] = x
            done.add(idx)

    def ready(x):
        try:
            int(x)
            return True
        except ValueError:
            return x in wires

    def val(x):
        try:
            return int(x)
        except ValueError:
            return wires[x]

    while len(done) != len(c[0]):
        for idx in range(len(c[0])):
            if idx not in done:
                op = c[2][idx]

                if (not ready(op[0])) or (not ready(op[1])):
                    continue

                op = map(val, c[2][idx])

                if c[0][idx] == "AND":
                    wires[c[1][idx]] = op[0] & op[1]
                elif c[0][idx] == "OR":
                    wires[c[1][idx]] = op[0] | op[1]
                elif c[0][idx] == "NOT":
                    wires[c[1][idx]] = ~op[0]
                elif c[0][idx] == "LSHIFT":
                    wires[c[1][idx]] = op[0] << op[1]
                elif c[0][idx] == "RSHIFT":
                    wires[c[1][idx]] = op[0] >> op[1]
                elif c[0][idx] == "ASSIGN":
                    wires[c[1][idx]] = op[0]
                
                done.add(idx)

    for (wire, value) in wires.items():
        print("wire %s: %d\n" %  (wire, value))

simulate()
