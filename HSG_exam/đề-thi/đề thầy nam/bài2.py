def Hz_num(list_num: list) -> int:

    counter = 0
    mark = [0] * 10**5

    for index in list_num:
        mark[index] += 1

        if mark[index] > counter:
            counter = mark[index]
            num = index

    return str(num) + " " + str(counter)

with open("./đề thầy nam/bai2.inp", "r") as file:
    num = file.readline()
    list_num = [int(num) for num in file.read() if num != "\n"]

with open("./đề thầy nam/bai2.out", "w") as file:
    print(Hz_num(list_num), file=file)