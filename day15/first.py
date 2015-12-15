"""
Brute force approach made easy with itertools.
"""
from itertools import combinations_with_replacement as combr
from collections import Counter

def parse_input():
    with open("input.txt", 'r') as f:
        ingredients = {}

        for line in f:
            line = line.split()
            line[0] = line[0][:-1]
            ingredients[line[0]] = {}

            for idx in range(1, len(line) - 2, 2):
                ingredients[line[0]][line[idx]] = int(line[idx + 1][:-1])

            ingredients[line[0]][line[-2]] = line[-1] 

        return ingredients

"""
Ignores calories for slight optimization.
"""
def best_cookie():
    ingredients = parse_input()
    left = ingredients.keys()
    best = None

    for cookie in combr(left, 100):
        score = 1
        props = {}

        cookie = Counter(cookie)

        for ingr in iter(cookie):
            for prop in iter(ingredients[ingr]):
                if prop == "calories":
                    continue

                if prop not in props:
                    props[prop] = 0

                props[prop] += ingredients[ingr][prop] * cookie[ingr]

        for prop in iter(props):
            if prop != "calories":
                score *= max(0, props[prop])

        if best == None or score > best:
            best = score

    print(best)

best_cookie()
