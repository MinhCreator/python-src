def string(strs):
   
    f = [0] * (len(strs) + 1)
    strs = "0" + strs

    for i in range(1, len(strs)):

        if strs[i] == "a":
            f[i] = f[i - 1] + 1

        else:
            f[i] = f[i - 1] - 1
        print(f[i])
    counts = 0

    for i in range(1, len(strs)):

        for j in range(i + 1, len(strs)):

            if f[j] - f[i - 1] == 0:
                counts += 1

    return counts

print(string("abbababa"))

