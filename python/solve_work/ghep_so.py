from functools import cmp_to_key

# Mở tệp để đọc và ghi
f_inp = open('NUMCON.INP')
f_out = open('NUMCON.OUT', 'w')

# Đọc và xử lý dữ liệu
lst = list(map(str, f_inp.read().strip().split()))

# Định nghĩa hàm so sánh hai chuỗi
def sx(s1, s2):
    # if s1 + s2 > s2 + s1:
        # return -1  # Để s1 đứng trước s2
    # elif s1 + s2 < s2 + s1:
        # return 1   # Để s2 đứng trước s1
    # else:
        # return 0   # Không thay đổi vị trí

    # TEST thử cách viết rút gọn ( không liên quan)
    return -1 if s1 + s2 > s2 + s1 else 1 if s1 + s2 < s2 + s1 else 0

# Sắp xếp danh sách bằng cách dùng hàm cmp_to_key
lst.sort(key=cmp_to_key(sx))

# Ghi kết quả ra file
f_out.write(''.join(lst) + '\n')

# Đóng các tệp
f_inp.close()
f_out.close()
