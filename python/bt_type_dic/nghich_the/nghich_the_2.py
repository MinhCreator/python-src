def nghich_the_2(n : int, lst : list[int]) -> list[int]:

    lst = [0] + lst
    f = [0] * (n + 1)
    re = [0] * (n + 1)
    
    for i in range(n, 0, -1):

        k = lst[i]
        j = n

        while k > 0:

            if f[j] == 0 : k -= 1

            j -= 1

        while (f[j] == 1): j -= 1

        re[i] = j

        f[j] = 1

    return " ".join(map(str, re[1:]))

with open("./nghich_the/input.inp", "r") as file:
    num = int(file.readline())
    lst = list(map(int, file.readline().split()))

with open("./nghich_the/output.out", "w") as file:
    print(nghich_the_2(num, lst), file=file)

# print(nghich_the_2(6, [0, 1, 0, 3, 4, 1]))
        