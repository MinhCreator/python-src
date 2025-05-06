def brick_temperatures(n: int, a: list[int]) -> int:

    # sort increasing
    a.sort()

    # cal sum of temperatures
    s = sum(a)

    a = [0] + a


    for i in range(1, (n // 2) + 1):

        s += a[n - i + 1] - a[i]


    if n % 2 !=0 : 
        
        s += a[n // 2 + 1]
        
    return s

n = 7
te = [5, 4, 1, 7, 9, 6, 8]

print(brick_temperatures(n, te))

