def find_sublist(arr: list, num: int):


    len_array = len(arr)
    counter = 0
    tmp = []
    for index in range(len_array):

        low = index - 1
        high = index + 1

        while low >= 0 and high < len_array :

            tmp.append(arr[low])

            if sum(tmp) % num :
                counter += 1
                # print(start,low, high, max_len)

            low -= 1
            high += 1

    return counter

