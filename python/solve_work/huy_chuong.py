def champion(opens, closes):

    n, k = map(int, opens.readline().split())
    lst_cow = list(map(int, opens.readline().split()))

    # medal of cow taken
    gold = [0] * (10**5)
    silver = [0] * (10**5)
    bronze = [0] * (10**5)
    lst_cow = [0] + lst_cow

    for i in range(1, n + 1):

        gold[i] = gold[i - 1] + 1 if lst_cow[i] == 1 else gold[i - 1]

        silver[i] = silver[i - 1] + 1 if lst_cow[i] == 2 else silver[i - 1]
           
        bronze[i] = bronze[i - 1] + 1 if lst_cow[i] == 3 else bronze[i - 1]
            
    for i in range(1, k + 1):

        l, r = map(int, opens.readline().split())

        print(gold[r] - gold[l - 1], silver[r] - silver[l - 1], bronze[r] - bronze[l - 1], file = closes)
    
    return 0

opens = open("./huy_chuong.inp", "r")
closes = open("./huy_chuong.out", "w")

print(champion(opens, closes))



