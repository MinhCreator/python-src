# đoạn con có phần tử giảm nhiều nhất 



def _giảm_nhiều_nhất_(lst):
    present_count = 0
    count = 0
    large_lst  = []
    small_lst = []
    range_in_list  = 0
    
    # programe parts

    while range_in_list <= len(lst) - 1:
        
        # loop in lst
        for index in range(range_in_list , len(lst)):
            if lst[index] <= lst[index - 1]:
                present_count += 1
                small_lst.append(lst[index])
                
            else:
                break
        
        # jump +1 in while loop
        range_in_list = index + 1

        # compare with condition and insert small_list to large_list        
        if present_count == count :
            large_lst.append(small_lst)
        
        if present_count > count :
            count = present_count
            large_lst = [small_lst]
        
        small_lst = []
        present_count = 0
    
    return large_lst

lst = [ 6, 9, 7, 5, 3, 2, 1, 4, 10]
temp = _giảm_nhiều_nhất_(lst)
print(temp)