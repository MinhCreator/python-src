def đoạn_con_dương_có_tổng_lớn_nhất(lst):
    tổng_lớn = 0
    tổng_hiện_tại = 0
    lst_lớn = []
    lst_con = []
    range_i = 0
    
    while range_i <= len(lst)-1:

        for index in range(range_i, len(lst)):
            if lst[index] > 0:
                lst_con.append(lst[index])
                tổng_hiện_tại += lst[index]
            else:
                break

        range_i = index + 1

        if tổng_hiện_tại  == tổng_lớn:
            lst_lớn.append(lst_con)
        
        if tổng_hiện_tại > tổng_lớn:
            tổng_lớn = tổng_hiện_tại
            lst_lớn = [lst_con]
        
        lst_con = []
        tổng_hiện_tại = 0
        
        
    return lst_lớn

lst = [1, 0, -1, -6, 7, 4, 1, 0, -2, 7, 2, 1, 4, 7, 10]
tmp = đoạn_con_dương_có_tổng_lớn_nhất(lst)
print(tmp)