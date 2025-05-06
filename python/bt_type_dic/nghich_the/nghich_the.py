def nghich_the(n: int, lst: list[int]) -> list[int]:

    lst = [0] + lst

    # p = [0] * (n)

    # tmp = []

    # q = []

    for i in range(1, n):
        
        count = 0
        
        for j in range(1, i - 1):

            # tmp = [x for x in lst[:i] if x > lst[i]]

            if lst[i] > lst[j]:
               
                count += 1    
                # p[i] = len(tmp) #len([x for x in lst[:i] if x > lst[i]])
                # p[i] = count
                # print([x for x in lst[:i] if x > lst[i]])
        print(count, end=" ")

            # else:

                # q = tmp

                # p[i] = len(q)

    # return p[1:]



print(nghich_the(7, [4, 3, 6, 2 ,1, 5]))

