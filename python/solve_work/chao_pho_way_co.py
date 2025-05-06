def noodle(opens, closes):
    file = opens
    thia, dua, khach = map(int, file.readline().split())

    a = [0] * (10**5)
    b = [0] * (10**5)

    f = [0] * (10**5)

    for i in range(1, khach + 1):
        t, d, q = map(int, file.readline().split())

        for j in range(1, i):
            if f[j] == 1 and a[j] <= t:
                thia += 1

                if b[i] == 1:
                    dua += 1

                f[j] = 0

        if (q == 0 and thia > 0) or (q == 1 and thia > 0 and dua > 0):
            a[i] = t + d
            b[i] = q
            f[i] = 1
            print("yes", file=closes)
            thia -= 1
            if q == 1:
                dua -= 1

        else:
            print("no", file=closes)

    return 0


opens = open("./chao_va_pho.inp", "r")

closes = open("./chao_va_pho.out", "w")

print(noodle(opens, closes))

