def _sort_(list: list) -> list[str] :

    return sorted(list, key=lambda x: (x.split(" ")[-1], x.split(" ")[0], x.split(" ")[1:len(x) - 2]))

def data_name(qos: int) -> list[str] : 
    
    tmp = []
    
    for i in range(qos) :
        name = input("Enter name student " + str(i + 1) + ": ")
        tmp.append(name)
    return _sort_(tmp)

int_input = 2

with open("./chuyên đề xử lí string/Hoten.out", 'w') as file:
    
    for i in data_name(int_input):
            i = input("Enter name student " + str(i + 1) + ": ")
            print("{} \n", format(data_name(i)))

file.close()