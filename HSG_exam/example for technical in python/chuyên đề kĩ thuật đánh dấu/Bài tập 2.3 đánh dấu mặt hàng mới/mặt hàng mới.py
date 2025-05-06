# 1 kho chứa hàng có chứa n mặt hàng (0 < n < 5000k) mỗi mặt hàng được đánh 1 mã số không trùng nhau từ 0 -> 10^9. mã số của các mặt hàng được lưu không tuần tự trong file. qua thời gian mặt hàng nào được bán đi thì mã số được xóa bỏ. hãy tìm 1 mã số nhỏ nhất thỏa mãn để đánh cho mặt hàng mới nhập kho.



def new_items(lst):
    int_len = len(lst)
    list_mark = [False] * 1000000000
    
    for num in lst:
        list_mark[num] = True
        
    for num in range(1000000001):
        if not list_mark[num]:
            return num

    return int_len + 2
    


file = open("Bài tập 2.3 đánh dấu mặt hàng mới\Code.inp", "r")

list_items =list(map(int, file.read().split()))

with open("Bài tập 2.3 đánh dấu mặt hàng mới\Code.out", "w") as file:
    file.write(str(new_items(list_items)))

file.close()