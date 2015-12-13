def parse_input():
    f = open("input.txt", 'r')

    return map(lambda x: x.strip()[1:-1], f.readlines())

def loss(s):
    l = 2
    idx = 0

    while idx < len(s):
        if s[idx] == '\\':
            if s[idx + 1] == '\\':
                l += 1
                idx += 1
            elif s[idx + 1] == '"':
                l += 1
                idx += 1
            elif s[idx + 1] == 'x':
                l += 3
                idx += 3
            else:
                print('WHOOPS\n')
        idx += 1

    return l

def difference():
    lines = parse_input()
    print(reduce(lambda acc, e: acc + loss(e), lines, 0))

difference()

        

