def số_đan_dấu(lst):
    Max_sl = 0
    sl_hien_tai = 0

    for num in range(1,len(lst)) :
        
        if lst[num] * lst[num-1] < 0 :
            sl_hien_tai += 1
        
        else :
            sl_hien_tai = 1

        if sl_hien_tai > Max_sl :
            Max_sl = sl_hien_tai
    return Max_sl
 
lst = [1, 20, -2, 3,-8, 5, 9, 2, -3]

print(số_đan_dấu(lst))