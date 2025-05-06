def tmp(k, strs):

   # t = str(0) + strs

    f = [0] * (len(strs) + 1)
    strs = "0" + strs
    counts = 0

    for i in range(1, len(strs)):
         
        if strs[i] == "1":
            f[i] = f[i - 1] + 1

        else: 
            f[i] = f[i - 1] 

    for i in range(1, len(strs)):

        for j in range(i + 1, len(strs)):

            if f[j] - f[i - 1] == k: 
                counts += 1

    return counts

strs = "01010"
print(tmp(2, strs))
