def sub_array( num, arr):

    counts = 0

    f = [0] * (num + 1)   

    for i in range(1, num + 1):

        f[i] = f[i - 1] + arr[i]

    for i in range(1, num + 1):

        for j in range(i, num + 1):
            
            t = f[j] - f[i - 1]
            if t == 0:
                print(j , i)
                counts += 1
    
    # return counts
"""(-1, 4, 3), (4, 3, -1), (0)"""

lst = [0, -1, -1, 4, -3, -1, 0]
# print(len(lst))
print(sub_array( 6, lst))
