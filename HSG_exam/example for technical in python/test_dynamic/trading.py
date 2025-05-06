

def trading(number: int, list_trade : list) -> list[int]:

    # variable
    Store_list = [0] * (number + 1)
    Store_list[1] = 1
    m = len(list_trade)

    # main proccess and return result

    for value in range(2, number + 1): 
        
        infinite = float('inf')

        range_proccess = 0

        while range_proccess < m and list_trade[range_proccess] <= number :

            Store_list[value] = min(1 + Store_list[number - list_trade[range_proccess]],  infinite)

            infinite = Store_list[value]
            
            range_proccess += 1

        Store_list[value] = infinite

    return Store_list[number]


# num = 20
# list_trade = [1, 3, 5]
# print(trading(num, list_trade))

with open("./test_dynamic/trading.inp", "r") as files:

    natural_num = int(files.readline().strip("\n"))
    
    list_trade = list(map(int, files.read().split(" ")))

with open("./test_dynamic/trading.out", "w") as files:

    print(trading(natural_num, list_trade), file= files)


