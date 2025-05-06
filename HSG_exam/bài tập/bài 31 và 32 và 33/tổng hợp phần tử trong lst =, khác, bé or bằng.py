

def so_luong_cac_phan_tu_bang_so_nguyen_cho_truoc(lst, N):
    count = 0 

    for num in lst: 

        if num == N :
            count += 1
    
    return count

def so_luong_cac_phan_tu_khac_so_nguyen_cho_duoi(lst, N):
    count = 0 

    for num in lst: 

        if num != N :
            count += 1
    
    return count

def so_luong_cac_phan_tu_be_or_bang_so_nguyen_cho_sau(lst, N):
    count = 0

    for num in lst:

        if num <= N :
            count += 1

    return count


N = int(input('nhap N nguyen: '))

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

print(so_luong_cac_phan_tu_bang_so_nguyen_cho_truoc(lst, N))
print(so_luong_cac_phan_tu_khac_so_nguyen_cho_duoi(lst, N))
print(so_luong_cac_phan_tu_be_or_bang_so_nguyen_cho_sau(lst, N))