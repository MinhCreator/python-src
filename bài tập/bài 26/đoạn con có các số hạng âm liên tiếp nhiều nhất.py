
def _đoạn_con_âm_liên_tiếp_nhiều_nhất_(lst):
    Max_count = 0
    Max_present = 0 
    large_list = []
    sub_list = []
    range_in_lst = 0

    while range_in_lst <= len(lst) - 1 :
        for index in range(range_in_lst, len(lst)):

            if lst[index] < 0:
                sub_list.append(lst[index])
                Max_present += 1
            
            else:
                break
        range_in_lst = index + 1

        if Max_present == Max_count:
            large_list.append(sub_list)

        if Max_present > Max_count:
            Max_count = Max_present
            large_list = [sub_list]
        
        Max_present = 0
        sub_list = []
    
    return large_list

lst = [1, 0, -1, -6, 7, 4, 1, 0, -2, -7, -2, -1, -4, -7, -10]
tmp = _đoạn_con_âm_liên_tiếp_nhiều_nhất_(lst)
print(tmp)