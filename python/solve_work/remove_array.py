def remove_and_plus(n : int, lst: list) -> int:

    lst.sort()
    ans = 0
    l = 1
    r = n
    s = sum(lst)
    lst = [0] + lst
    
    while s != 0:

        ans += 1
        if s > 0:
            s -= lst[r]
            r -= 1

        else:
            s -= lst[l]
            l += 1

        # print(s, lst[l], lst[r])

        # print(ans)

    return ans    

n = [-4, -5, 1, 2, -3, 10]
n1 = [-3, -3, -3, 0, 0, 0, 4, 4]

print(remove_and_plus(6, n))