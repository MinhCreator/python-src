def palin(lists):

    return lists[::-1] == lists

def func(lists):

    length = len(lists)
    max_len = 1
    start = 0

    for cl in range(2, length + 1):

        for i in range(length - cl + 1):
            next = cl + i

            if palin(lists[i:next]) and cl > max_len :

                start = i
                max_len = cl

    str_palind = " ".join([str(x) for x in lists[start:start + max_len]])
    len_palind = len(lists[start:start + max_len])
    return f"{len_palind}\n{str_palind}"

with open('XCAN26.INP', 'r') as file:
    lst_str = list(map(str, file.readline().split()))



with open('XCON26.OUT', 'w') as file:
    print(lst_str)
    #print(file=file)