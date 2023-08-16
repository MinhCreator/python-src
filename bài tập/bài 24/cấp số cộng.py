def cấp_số_cộng(lst):
    Max_so_luong = 2
    present = 2
    sublists = []
    sublst = [lst[0], lst[1]]
    i = 2
    cong_sai = lst[1] - lst[0]

    while i <= len(lst)-2:
       
        for index in range(i, len(lst)):
            if lst[index] - lst[index - 1] == cong_sai:
                present += 1
                sublst.append(lst[index])
            else:
                break
        i = index + 1
        
        if present == Max_so_luong:
            sublists.append(sublst)

        if present > Max_so_luong:
            Max_so_luong = present
            sublists = [sublst]
        
        sublst = [lst[index]]
        present = 1

        if i > len(lst)-1:
            break
        else:
            cong_sai = lst[i] - lst[i-1]

    return sublists 
        
lst = [1, 0, -1, -6, 7, 4, 1, 0, -2, 7, 2, 1, 4, 7, 10]
kq = cấp_số_cộng(lst)
print(kq)