def tia_mang(n, lst):

    dt= {}

    for i in lst:
        if i in dt:
            dt[i] += 1
        else:
            dt[i] = 1
    return " ".join([str(i) for i in dt.keys()])

def tia_mang2(n, lst):

    dt = {}

    for i in lst:

        if (i in dt) == False:
            print(i, end=" ")
        dt[i] = 1

           
# print(tia_mang(8, [7, -6, 4, -6, 7, 1, 2, -6]))

with open('./bt_type_dic/tia_array/ARR.INP', 'r') as file:

    n = int(file.readline())

    lst = list(map(int, file.read().split()))

with open('./bt_type_dic/tia_array/ARR.OUT', 'w') as file:

    print(tia_mang(n, lst), file=file)
    print(tia_mang2(n, lst))