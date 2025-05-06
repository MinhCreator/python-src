def sub(op, clo) -> int:

    n = int(op.readline())
    lst = [0] + list(map(int, op.readline().split()))
    pre = 0
    re = 0

    for i in range(2, n + 1):
        if lst[i - 1] < lst[i]:
            pre += 1
        else:
            pre = 1

    re = max(re, pre)
    print(re, file = clo)
    return ""

op = open("doancon1.inp", "r")

closes = open("doancon1.out", "w")

print(sub(op, closes))

