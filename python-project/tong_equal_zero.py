def zero(num : int, lst: list) :

    lm = 0 
    dicts = {}

    b = [0, lst[0]]
    start = 1
    
    for index in range(start, num):
        b.append(lst[index] + b[index]) # cộng dồn vào list b
        # print(b, lst[index], b[index])

    for index in range(num + 1):

        if b[index] not in dicts:
            dicts.update({b[index]: index})
            # print(dicts)            
        else:
            l = index - dicts[b[index]]

            if l > lm:
                lm = l

    return dicts, b
print(zero(5, [2, 1, -2, 3, -2]))

