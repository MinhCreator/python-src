def find_string(main_string, sub_string):
    """_summary_

    Args:
        main_string (_str_): is input main string
        sub_string (_str_): is input sub string

    Returns:
        if
        __index__ (__list[str[int]]__): is position of sub string in main string 
        
        else
        __index__ (idnex = 0): if func not return position of sub string in main string
    """
    lists = []

    index = -1

    while True:
        index = main_string.find(sub_string, index + 1)
        if index == -1:
            break
            
        lists += [str(index + 1)]

    if lists != []:
        return " ".join(lists)

    return 0

with open("./đề thi hsg khối 12 2023/VITRI.INP", "r") as file:

    main_string = file.readline()
    sub_string = file.read()

with open("./đề thi hsg khối 12 2023/VITRI.OUT", "w") as file:

    print(find_string(main_string, sub_string), file= file)
