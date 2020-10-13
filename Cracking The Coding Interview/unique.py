string = str(input())

def UniqueStr(string):
    if len(string) > 128:
        return False

    char_set = [False for _ in range(128)]

    for s in string:
        uni = ord(s)
        if char_set[uni]:
            return False

        char_set[uni] = True

    return True

print(UniqueStr(string))