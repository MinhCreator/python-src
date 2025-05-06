def paint_nha(n, s):
    
    lst = [x for x in s]
    paint = 0
    lst = [0] + lst

    for i in range(2, len(lst)):

        if lst[i - 1] == lst[i]:
            paint += 1
            lst[i] = '0'

            # print(i, paint)    
    return paint

n = 17
s = "DDTVVTDVVVTVVTDVV"
# n = 3
# s = "TXV"

# n = 11
# s = "DDTVVTDVVVT"
print(paint_nha(n, s))