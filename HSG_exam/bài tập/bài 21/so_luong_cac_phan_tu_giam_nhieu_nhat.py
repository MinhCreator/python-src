
def so_luong_cac_phan_tu_giam_nhieu_nhat(lst):
    max_so_luong = 1
    so_luong_hien_tai = -1
    num_start = 1
    for num in range(num_start,len(lst)):
        
        if lst[num] >= lst[num-1]:
            so_luong_hien_tai += 1

        else:
            so_luong_hien_tai = 1
        
        if so_luong_hien_tai > max_so_luong:
            max_so_luong = so_luong_hien_tai

    return max_so_luong

lst = [1,4,-2,3,-8,5,9,2]
print(so_luong_cac_phan_tu_giam_nhieu_nhat(lst))

#  dãy phan tu giảm nhiều nhất là có ai >= ai-1