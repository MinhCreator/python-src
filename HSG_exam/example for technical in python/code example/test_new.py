
def remove_and_plus(num: int) -> int:
    """_summary_

    Args:
        num (int): input with interge number <= 10^5

    Returns:
        int: sum of num after remove and computing
    """
    string = str(num)
    bin_zero = [0] *  len(string)
    bin_one = [1] * len(string)
    sum_return = 0
    
    while bin_zero < bin_one:

        index = len(string) - 1
        while bin_zero[index] == 1 :
            bin_zero[index] = 0
            index -= 1

        bin_zero[index] = 1
        print(bin_zero)
        

        num_store = 0
        for ind in range(len(string)):
            if bin_zero[ind] == 1:
                num_store = num_store * 10 + int(string[ind])
            print(num_store)
        sum_return += num_store
        print(sum_return)

    # return sum_return


print(remove_and_plus(1234))
    
