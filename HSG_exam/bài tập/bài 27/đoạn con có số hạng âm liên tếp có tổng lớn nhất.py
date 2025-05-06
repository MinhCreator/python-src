# đoạn con có số hạng âm liên tếp có tổng lớn nhất

def _âm_liên_tiếp_có_tổng_lớn_nhất_(lst):
    # variable Definition
    sum_count = 0
    sum_present = 0
    large_list = []
    sub_list =  []
    range_in_list = 0
    
    # main program 
    while range_in_list <= len(lst) - 1 :
        for index in range(range_in_list, len(lst)) :

            if lst[index] < 0 :
                sub_list.append(lst[index])
                sum_present += lst[index]
            else:
                break
    
        range_in_list = index + 1

        if sum_present == sum_count :
            large_list.append(sub_list)
        
        if sum_present > sum_count :
            sum_count = sum_present
            large_list = [sub_list]

        sum_present = 0
        sub_list = []

    return large_list
            
lst = [-1, 4, 1, 6, 7, -44, 1, 0, 1, 7, 2, 1, -4, -7, 10]

tmp = _âm_liên_tiếp_có_tổng_lớn_nhất_(lst)
print(tmp)       
print('make by MinhCreatorVN')     