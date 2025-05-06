def palin(list):

    return list[::-1] == list

def func(list):

    length = len(list)
    max_len = 1
    start = 0

    for cl in range(2, length + 1):

        for i in range(length - cl + 1):
            next = cl + i

            if palin(list[i:next]) and cl > max_len :

                start = i
                max_len = cl

    tmp = " ".join([str(x) for x in list[start:start + max_len]])
    
    return str(len(list[start:start + max_len])) + "\n" + tmp

with open('./exam_hsg_11_2013-2014/PALIN.inp', 'r') as file:
    len_num = int(file.readline())
    list_num = [int(x) for x in file.read().split()]

with open('./exam_hsg_11_2013-2014/PALIN.out', 'w') as file:

    print(func(list_num), file=file)