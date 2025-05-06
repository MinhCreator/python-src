def find_text(string: str) -> str:
    
    choose_num = ""
    max_choose = ""
    #choose num in string and find text in string remaning
    for i in range(1, len(string) + 1):

        
        choose_num = string[:i]

        str_remain = string[i:]

        if choose_num in str_remain: 
            max_choose = choose_num
            position_choose = len(string) - len(str_remain) + str_remain.find(max_choose) + 1

        else:
            break
        

        
    return len(max_choose), position_choose
    # return choose_num, position_choose 
    
    
    
    
    
string = "12312312312"
print(find_text(string))