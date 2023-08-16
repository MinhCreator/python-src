# cho 1 str (có thể rất dài). hãy đếm số lần xuất hiện của từng kí tự có trong str
# CÁCH LÀM SỐ 1


def _frequency_element_(str): # hàm trả về tần số xuất hiện của các kí tự xuất hiện trong string
    lst_ky_tu = []
    
    lst_mark = [0] * len(str) # list đánh dấu tần số xuất hiện của các kí tự có trong string


    # Main Process Program
    for alpha in str : 

        if alpha not in lst_ky_tu :    
            lst_ky_tu.append(alpha)

    for index, al in enumerate(lst_ky_tu) :  # vòng lặp này trả về chỉ số (index) và kí tự (al) có trong list kí tự

            counter = str.count(al)
            lst_mark[index] = counter
            
    return lst_ky_tu, lst_mark

    

opener = open("tần số các kí tự\StringCount.inp", "r")

string_read = opener.read()

with open("tần số các kí tự\StringCount.out", "w") as opener:

    lst_ky_tu, list_mark = _frequency_element_(string_read)

    for index in range(len(lst_ky_tu)):
                
        opener.write('kí tự {}: {} lần\n'.format(lst_ky_tu[index], list_mark[index]))


opener.close()



