def parse_input():
    with open("input.txt", 'r') as f:
        return list(f.read().strip())

def valid(s):
    if 'i' in s or 'l' in s or 'o' in s:
        return False

    trip = False

    for idx in range(len(s) - 2):
        if (ord(s[idx]) + 1 == ord(s[idx + 1]) and
            ord(s[idx + 1]) + 1 == ord(s[idx + 2])):
            trip = True

    if not trip:
        return False

    dub = 0
    idx = 0

    while idx < len(s) - 1:
        if s[idx] == s[idx + 1]:
            dub += 1
            idx += 1
            
            if dub == 2:
                return True
        
        idx += 1

    return False

def inc(s):
    idx = -1
    s[idx] = chr(((ord(s[-1]) + 1 - ord('a')) % 26) + ord('a'))
    while idx > -len(s) and s[idx] == 'a':
        idx -= 1
        s[idx] = chr(((ord(s[idx]) + 1 - ord('a')) % 26) + ord('a'))

    return s

def new_pass():
    new = parse_input()
    new = inc(new)

    while not valid(new):
        new = inc(new)

    print(str(new))

new_pass()
