
def so_luong_cac_phan_tu_tang_nhieu_nhat(lst):

    lst_num_increase = [0] * len(lst)
    size = 0

    for num in lst:
        nums , Size = 0 , size

        while nums != Size:
            num_and_Size = (nums + Size) // 2
            if lst_num_increase[num_and_Size] < num:
                nums = num_and_Size + 1
            
            else:
                Size = num_and_Size
        
        lst_num_increase[nums] = num
        size = max(size , nums + 1)

    return size
    


lst = [1,4,-2,3,-8,5,9,2]
print(so_luong_cac_phan_tu_tang_nhieu_nhat(lst))    