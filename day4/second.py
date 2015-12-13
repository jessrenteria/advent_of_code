from hashlib import md5

key = "bgvyzdsv"

def find_lowest():
    curr = 0
    m = md5()
    m.update(key + str(curr))

    while m.hexdigest()[:6] != "000000":
        curr += 1
        m = md5()
        m.update(key + str(curr))

    return curr

print(find_lowest())
