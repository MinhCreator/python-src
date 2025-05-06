def subarr(n :int, lst: list[int]): 
    lst = [0] + lst 
    s = sum(lst)
    f = [0] * len(lst)
    d = 0
    
    k = s // 3
   
    if s % 3 != 0:
        return 0
    
    for i in range(1, n + 1):
        f[i] = f[i - 1] + lst[i]

    for i in range(1, n - 1):
        if f[i] == k : 
            for j in range(i + 1, n):
                if f[j] - f[i] == k:
                    d += 1
    return d
n = 5
lst = [1, 2, 3, 0, 3]

print(subarr(n , lst))

