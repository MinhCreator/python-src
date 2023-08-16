# đoạn con có các số hạng liên tiếp đan dấu nhiều nhất 


def _đan_dấu_nhiều_nhất_(lst):
    
    count = 0
    present_count = 0
    large_list = []
    sub_list = []
    range_in_lst = 0
    
    while range_in_lst <= len(lst) - 1:

        for index in range(range_in_lst, len(lst)):
            if lst[index] * lst[index - 1] < 0 :
                present_count += 1
                sub_list.append(lst[index])

            else:
                break 
        range_in_lst = index + 1
        
        if present_count == count:
            large_list.append(sub_list)
        
        if present_count > count:
            count = present_count
            large_list = [sub_list]
        
        sub_list = [lst[index]]
        present_count = 0
        
    return large_list

lst = [-1, 4, 1, -6, 7, 4, 1, -2, 7, 2, 1, 4, 7, 10]

temp = _đan_dấu_nhiều_nhất_(lst)

print(temp)