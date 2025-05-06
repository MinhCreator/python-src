

def find_max_len_sum_of_negatives(num , lst):

    """
    _function_

    input: num is integer, lst is list 
    
    Returns:
        _type_: _int_
    """
    # variable 
    prefix_sum = [0]
    start = -1
    maxt = 0

    # another proccess
    for tmp in lst:
         prefix_sum.append(prefix_sum[-1] + tmp)    

    # main proccess
    for index in range(num):

        for jndex in range(index + 1, num + 1):

            if prefix_sum[jndex] - prefix_sum[index] < 0 and jndex - index > maxt:                        
                    start = index 
                    maxt = jndex - index

    store_lst = lst[start: start + maxt]
        
        
    return len(store_lst)

with open("./SUMOFNEG.INP", "r") as file:
    num, lst = int(file.readline()), [int(x) for x in file.readline().split()]
# 
with open("./SUMOFNEG.OUT", "w") as file:
    print(find_max_len_sum_of_negatives(num, lst), file=file)
