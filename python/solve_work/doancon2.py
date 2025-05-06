def dan_dau(n: int, lst: list[int])-> int:

    if n == 1: 
        return 1

    mark = ["o"] * (n + 1)
    f = [0] + lst
    for i in range(1, len(lst)):

        if lst[i] > 0:
            mark[i] = "+"

        else: mark[i] = "-"

    long = 0


    for i in range(1, len(mark)):

        if mark[i - 1] != mark[i] :
            long += 1
    return long

n = 5
lst = [6, 67, -8, 48, 88]
print(dan_dau(n, lst))

