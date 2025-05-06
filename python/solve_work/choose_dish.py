def choose_dish(n: int, dishes: list[int], p: int) -> int:

    dishes = [0] + dishes
    f = [0] * (n + 1)
    ans = 0
    l = 1
    r = 1
    
    for i in range(1, n + 1):

        f[i] = f[i - 1] + dishes[i]

    for i in range(1, n + 1):

        for j in range(1, n + 1):

            if f[j] - f[i - 1] >= p and j - i + 1 > ans:

                ans = j - i + 1
                l = i
                r = j

    if ans != 0 : return l, r
    else: return - 1

print(choose_dish(6, [-5, 4, -2, 5, -10, 5], 4)) 
print(choose_dish(6, [-3, 1, -2, 3, -10, 3], 4))
