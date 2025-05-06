from re import findall

def sieve_num(string: str) -> list[str]:

     return findall('\d+', string)   

def sieve_num_(string: str) -> list[str]:

    value = 0
    list_string = []

    while value < len(string):
        string_1 = ""
        
        for i in range(value, len(string)):

            if string[value] >= "0" and string[value] <= "9":
                string_1 += string[value]
                value = i + 1

            else:
                value += 1
                break

        list_string += [string_1]                
                      
    return [str for str in list_string if str != ""]

string = "Abc def12mnk 37ijq 0987453215 abcc"

with open("./đề thầy nam/bai1.inp", "r") as file:
    string = file.read()

with open("./đề thầy nam/bai1.out", "w") as file:

    tmp = sieve_num(string)
    for str in tmp:
        print(str, file = file)