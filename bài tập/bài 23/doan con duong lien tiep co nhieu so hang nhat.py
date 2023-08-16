
def list_child_positive_numbers(list_of_numbers):
    Max_so_luong = 0
    present = 0
    sublists = []
    sublst = []
    range1 = 0

    while range1 <= len(list_of_numbers)-1:
        for index in range(range1, len(list_of_numbers)):
            if list_of_numbers[index] > 0:
                present += 1
                sublists.append(list_of_numbers[index])
            else:
                break
        range1 = index + 1
        
        if present == Max_so_luong:
            sublists.append(sublst)
        if present > Max_so_luong:
            Max_so_luong = present
            sublists = [sublst]
        
        sublst = []
        present = 0 

    return sublists 
        

        
    
lst = [1,4,7,2,3,8,-5,9,2]
for intenger in list_child_positive_numbers(lst):
    print(intenger)