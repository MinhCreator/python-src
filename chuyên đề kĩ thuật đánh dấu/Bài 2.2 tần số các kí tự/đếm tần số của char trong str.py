# tần số xuất hiện các kí tự trong string
# CÁCH LÀM SỐ 2


def ts(str):
    list_mark = [0] * 257

    for element in str:
        list_mark[ord(element)] += 1
    
    return list_mark

files = open('bài 2.2 tần số các kí tự\StringCount.inp', 'r')

read = files.read()

with open('bài 2.2 tần số các kí tự\StringCount.out', 'w') as files:
    
    tmp = ts(read)

    for ele in range(256):
        if tmp[ele] > 0:
            char = chr(ele)
            # files.write(char + ' ' + str(tmp[ele]) + '\n')
            print(char, tmp[ele], file=files) # or end = ' '
files.close()
