def tan_so(n, lst):
    
    dic = {}

    for x in sorted(lst):
        if x in dic:
            dic[x] += 1
        else:
            dic[x] = 1
    return dic

def displayed_and_write_to_file(n, lst):
    tmp = tan_so(n, lst)

    with open('./bt_type_dic/tan_so/output.out', 'w') as file:
        for key, values in tmp.items():
            print(key, values, file=file)

n = 10
lst = [1, -1, 2, 7, 2, 2, -1, 3, 7, 7]
print(displayed_and_write_to_file(n, lst))

