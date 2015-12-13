def parse_input():
    f = open("input.txt", 'r')

    return f.readlines()

def num_nice():
    lines = parse_input()

    vowels = "aeiou"

    def is_vowel(c):
        return 1 if c in vowels else 0

    def repeat(s):
        c = s[0]

        for idx in range(1,len(s)):
            if c == s[idx]:
                return True
            else:
                c = s[idx]

        return False

    nice = 0

    for line in lines:
        if "ab" in line or "cd" in line or "pq" in line or "xy" in line:
            continue
        elif sum(map(is_vowel, line)) >= 3 and repeat(line):
            nice += 1

    return nice

print(num_nice())
