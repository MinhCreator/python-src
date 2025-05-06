# require
# file input : VNMODEL.INP
# file output : VNMODEL.OUT


def VNMODEL(list_top_model: list) -> list:
    
    # variables
    list_mark_top_model = [0] * 1001 
    list_tmp = []
    
    # load model
    for au in list_top_model:
        list_mark_top_model[au] += 1

    max_count = max(list_mark_top_model)

    # trả về thí sinh được bình chọn nhiều nhất 
    for num in range(1, 1001):
        if list_mark_top_model[num] == max_count:
            list_tmp.append(num)
    
    return list_tmp

folder = open("bài 2.6 vòng chung kết\VNMODEL.INP", "r")

aud = int(folder.readline())
lst_model = list(map(int, folder.read().split()))

with open("bài 2.6 vòng chung kết\VNMODEL.OUT", "w") as folder:

    for model in VNMODEL(lst_model):
        print(model, end = '\n', file=folder)        
folder.close()