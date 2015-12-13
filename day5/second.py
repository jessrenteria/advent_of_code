def parse_input():
    f = open("input.txt", 'r')

    return f.readlines()

def num_nice():
    lines = parse_input()

    def has_palindrome(s):
        for idx in range(0, len(s) - 2):
            if s[idx:idx + 3] == ''.join(reversed(s[idx:idx + 3])):
                return True

        return False

    def has_2_pair(s):
        for idx in range(0, len(s) - 3):
            if s[idx:idx + 2] in s[idx + 2:]:
                return True

        return False

    nice = 0

    for line in lines:
        if has_palindrome(line) and has_2_pair(line):
            nice += 1

    return nice

print(num_nice())
