def check_even_odd(num: int) -> bool:

    if num % 2 == 0:
        return True

    elif num == 0: 
        return False
    
    else:
        return False


def happy_num(num_line_one: int, num_line_two: int) -> int:
    """_summary_
    Args:
        num_line_one (int): _description_
        num_line_two (int): _description_

    Returns:
        _int_: _description_
    """
    # reuse variable
    string_num = str(num_line_two)
    len_str = len(string_num)

    # process data and store in list 
    if check_even_odd(num_line_one) != False :

        # store index in main num 
        store_1_index = [index for index in range(0, len_str // 2)]
        end_index = store_1_index[-1] + 1
        store_2_index = [index for index in range(end_index, len_str)]
        
        # trace element in main num by index
        store_1 = [int(string_num[index]) for index in store_1_index]
        store_2 = [int(string_num[index]) for index in store_2_index]

        # return 0 or 1
        if sum(store_1) != sum(store_2):
            return 0
        
        else:
            return 1

    return 0

with open('./exam_hsg_11_2013-2014/HAPPYNUM.INP', 'r') as file:
    line_1 = int(file.readline())
    line_2 = int(file.read())
    
with open('./exam_hsg_11_2013-2014/HAPPYNUM.OUT', 'w') as file:

    print(happy_num(line_1, line_2), file=file)

           