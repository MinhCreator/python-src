def switching_pos(lst):
    giu_cho = 0

    for num in range(len(lst)):
        
        if lst[num] > 0:
            lst[num], lst[giu_cho] = lst[giu_cho], lst[num] 
            giu_cho += 1

    return "lst after processing: "+ str(lst)



lst = [-1,-4,-5,-3,6,8,3,9,8]
print(switching_pos(lst))
