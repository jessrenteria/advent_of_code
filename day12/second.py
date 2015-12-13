import json

def parse_input():
    with open("input.txt", 'r') as f:
        return f.read().strip()

def sum_help(x):
    if isinstance(x, int):
        return x
    if isinstance(x, list):
        return sum(map(sum_help, x))
    if isinstance(x, dict):
        if "red" in x.values():
            return 0
        return sum(map(sum_help, x.values()))

    return 0

def sum_all():
    raw = parse_input()
    x = json.loads(raw)

    print(sum_help(x))

sum_all()
