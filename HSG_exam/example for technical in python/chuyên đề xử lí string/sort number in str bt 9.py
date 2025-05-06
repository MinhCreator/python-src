def sort(tmp: str) -> str:

    #Var
   
    Collect_num = tmp.split("a") 
    convert = [int(i) for i in Collect_num if i.isdigit()]
    sort_covert = sorted(convert)
    
    lst_index = []
    
    for index , value in enumerate(Collect_num):
        if not value == "":
            lst_index.append(index)
   

    
    for index, value in enumerate(lst_index):
        Collect_num[value] = str(sort_covert[index])
        # print(Collect_num)

    print(Collect_num)    
            

    # return "".join(Collect_num)
    
    
    
    
    
    
    
    
    
    
    
    
    
   
   



string = "aaa6aaa776aaaaa2823aaaa95aaa"
print(sort(string))
