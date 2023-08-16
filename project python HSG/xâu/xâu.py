#bài 2


# hàm sắp xếp string 
def sort_string(s):
    string_Upper = ''
    str_lower = ''
    for i in s:
        if i >= 'A' and i <= "Z":       
            string_Upper += i
        if i >= 'a' and i <= 'z':
            str_lower += i
    str_up = ''.join(sorted(string_Upper, reverse=True))
    str_low = ''.join(sorted(str_lower,reverse=True))
    str_new = str_up + str_low
    return str_new

def input_string():
    s = input('nhap xau chua ki tu chu cai: ')
    print('the string before to sort:', s)
    if s.isalpha():
        print("the string after sorted", sort_string(s))
    else:
        print('the string is not alphabet')

input_string()