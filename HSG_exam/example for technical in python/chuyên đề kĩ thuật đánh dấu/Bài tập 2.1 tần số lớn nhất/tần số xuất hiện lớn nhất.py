# cho  1 list số nguyên gồm n phần tử (list[i] <= 50000, n <= 10^9) giá trị các phần tử có thể trùng nhau. ta gọi số lần xuất hiện của 1 số x trong list chính là tần số của x 
# hãy tìm ra số có tần số lớn nhất 

def fre_elements_max(lst):
    max_num = 0
    max_hz = 0
    
    list_mark = [0] * 50001 # giới hạn của list mark <= 50.000
    
    for num in lst:
        list_mark[num] += 1

        if list_mark[num] > max_hz:
            max_hz = list_mark[num]
            max_num = num
    
    return max_num, max_hz


file = open('bài tập 2.1 tần số lớn nhất\Tanso.inp', 'r')

lst_num = list(map(int, file.readline().split())) 

with open("bài tập 2.1 tần số lớn nhất\Tanso.out", "w") as file:
    
    num, num_hz = fre_elements_max(lst_num)

    file.write(str(num) + ' ' + str(num_hz))

file.close()