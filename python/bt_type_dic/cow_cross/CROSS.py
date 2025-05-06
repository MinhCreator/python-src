def cross():

    f = [-1] * 100001 
    counts = 0
    with open('./cow_cross/cross.in', 'r') as file:

        n = int(file.readline())

        for qs in range(0, n):

            id, pos = map(int, file.readline().split())
            
            if f[id] != -1 and f[id] != pos:

                counts += 1

            f[id] = pos

    return counts

print(cross())