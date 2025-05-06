def cow_race(dict):
    ans = 0

    for x in dict.values():

        ans += x * (x - 1) // 2

    return ans


def inputs(lst):
    dt = {}

    for x in lst:
        if x in dt:
            dt[x] += 1
        else:
            dt[x] = 1
    return dt

lst = [1, 1, 5, 3, 5, 1, 3]

print(cow_race(inputs(lst)))