

def next_num(num):

    list_num = [int(x) for x in str(num)]

    index = -1

    for indx, value in enumerate(list_num[::index]):
            
            if list_num[indx] < list_num[indx - 1]:
                tmp = indx
                break
    while True:

        if list_num[index - 1] > list_num[tmp]:
             list_num[index - 1], list_num[tmp] = list_num[tmp],  list_num[index - 1]

        else:
             break

    list_num[tmp + 1:] = sorted(list_num[tmp + 1:])

    list_string = [str(x) for x in list_num]

    nums = int("".join(list_string))

    if nums < num:
          return print(0, file=file)

    return print(nums, file=file)

with open("./đề thi hsg khối 12 2023/SOSATSAU.INP", "r") as file:
     num_len = int(file.readline())
     num = int(file.read())

with open("./đề thi hsg khối 12 2023/SOSATSAU.OUT", "w") as file:
     print(next_num(num))