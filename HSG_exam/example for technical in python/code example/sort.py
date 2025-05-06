def sum_list(list: list) -> list[int]:
    
    sum_tmp = 0
    list_result = []

    for num in list:

        for x in num:

            sum_tmp += int(x)

        list_result += [sum_tmp]
        sum_tmp = 0

    return list_result
        