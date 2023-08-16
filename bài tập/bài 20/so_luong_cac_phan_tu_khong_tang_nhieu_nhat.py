
# note : dãy không tăng là dãy có ai <= ai-1

def num_non_increase_2(list):

    max_so_luong = 1
    so_luong_hien_tai = -1
    num_start = 1

    for num in range(num_start, len(lst)):
        
        if lst[num] <= lst[num - 1]:
            so_luong_hien_tai += 1
        
        else:
            so_luong_hien_tai = 1
        
        if max_so_luong < so_luong_hien_tai:
            max_so_luong = so_luong_hien_tai
    
    return max_so_luong

lst = [1,4,-2,3,-8,5,9,2]
print(num_non_increase_2(lst))


