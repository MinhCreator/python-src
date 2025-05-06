# ông an đến dự tiệc, buổi tiệc có n người (0 < n < 50k). mỗi người được cài lên áo mỗi bông hoa trên có ghi 1 con số nguyên x (x <= 10^6), cho biết người khách đó sẽ dự tiệc phòng x. hầu hết tất cả phòng đều có số lượng người là chẵn, duy nhất chỉ có 1 phòng là lẻ. để đảm bảo đủ cặp cho tiệc khiêu vũ nên BTC quyết định tìm phòng có số lượng người lẽ để ghi số cho ông an. 

# require: 

# file input: name: Dutiec.inp
'''first line: n  = number of room
    next line: one int per line '''

# file output: name: Dutiec.out
# one number is the number of room have a retail number of customers


def find_room(n_o_r, list):

    # variables
    tmp = n_o_r
    list_nguoi = [0] * 10 ** 6 # list chứa số người của từng phòng ban đầu bằng 0 

    # main process

    for ro in list:
        list_nguoi[ro] += 1 # tăng số người trong từng phòng lên 1 

    for room, human in enumerate(list_nguoi):    

        if human % 2 != 0 :# kiểm tra xem số lượng người trong room có là số lẻ hay không 
            return room            
            

file = open('Bài tập 2.4 xếp khách vào phòng\Dutiec.inp', 'r')

n_o_r = int(file.readline())
lst = list(map(int, file.read().split('\n')))

with open("Bài tập 2.4 xếp khách vào phòng\Dutiec.out", "w") as file:
    
    file.write(str(find_room(n_o_r, lst)))

file.close()