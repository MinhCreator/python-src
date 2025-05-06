def fast_encode(data: str) -> str:

    if data.islower() == True:
        data = data.upper()

    integer = [str(ord(var)) for var in data]

    return "".join(integer)


def fast_decode(data: int) -> str:

    data_string = str(data)

    # OPTIMIZATION CODE RUNTIME AND SHORT CODE LINE BUT MORE DIFFICULT TO UNDERSTAND, READ
    char = [ chr(int(data_string[value:value + 2])) for value in range(0,len(data_string), 2)]
    
    return "".join(char)
    

    

with open('./chuyên đề xử lí string/mahoa.inp', "r") as files:
    string_line = files.readline().rstrip(" ","\n")
    num_code = int(files.readline().rstrip(" ","\n"))
    
with open("./chuyên đề xử lí string/mahoa.out", "w") as files:
    print("{}\n{}".format(fast_encode(string_line), fast_decode(num_code)), file=files)

files.close()


def slow_encode(data: str) -> str:
    data_store = ""

    for value in data:
        data_store += str(ord(value))

    return data_store 

def slow_decode(data: int) -> str:
    data_string = str(data)
    
    # CODE EASY TO READ AND UNDERSTAND BUT SLOW RUNTIME SPEED  
    result = ""

    for var2 in range(0, len(data_string), 2):

        output = chr(int(data_string[var2:var2 + 2]))
        result += output
        
    return result
    


