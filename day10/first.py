def parse_input():
    f = open("input.txt", 'r')

    return f.read().strip()

def look_and_say():
    s = parse_input()
    
    for _ in range(40):
        tmp = s
        s = ""
        idx = 0
        curr = ""
        curr_count = 0

        while idx < len(tmp):
            if tmp[idx] == curr:
                curr_count += 1
            else:
                if curr_count > 0:
                    s += str(curr_count) + curr
                curr_count = 1
                curr = tmp[idx]
            
            idx += 1

        if curr_count > 0:
            s += str(curr_count) + curr

    print(len(s))

look_and_say()


