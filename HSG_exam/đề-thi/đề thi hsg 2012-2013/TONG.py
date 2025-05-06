


def split_num(num):

    list_nums = [num + " " for num in num]

    return list_nums


with open("./đề thi hsg 2012-2013/TONG.INP", "r") as file:

    line_num_one = int(file.readline())
    list_num_1 = file.readline().split(" ")
    line_num_two = int(file.readline())
    list_num_2 = file.readline().split(" ")

    join_1 = int("".join(list_num_1))
    join_2 = int("".join(list_num_2))

    sums = join_1 + join_2

    re = split_num(str(sums))
    length = len(re)

    

with open("./đề thi hsg 2012-2013/TONG.OUT", "w") as file:
    # print(length,"\n" + "".join(re), file= file)
    print(length, file= file)
    print("".join(re), file= file)