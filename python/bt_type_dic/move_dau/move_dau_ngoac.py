def move(strings: str):

    strings = "@" + strings
    counts = 0
    k = 0

    for i in range(1, len(strings)):

        if strings[i] == "(" : k += 1

        else: k -= 1

        if k < 0 : 
            k = 0
            counts += 1

    return counts

print(move(")("))

print(move("()()"))

print(move("())()()("))

print(move(")))((((())"))