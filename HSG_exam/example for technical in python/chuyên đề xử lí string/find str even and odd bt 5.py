
def find_str_even_odd(data : str) -> str:

    # variable
    maker = [0] * 26
   
    for alpha in data:

        ASCII_code = ord(alpha.lower()) - 97
        maker[ASCII_code] += 1

    even = all(count % 2 == 0 for count in maker if count > 0)
    odd = all(count % 2 != 0 for count in maker if count > 0)

    return even, odd
    

data = ""

with open("./chuyên đề xử lí string/StrCHCK.out", 'w') as file:
    even, odd = find_str_even_odd(data)

    if even:
        print("CHUOICHAN", file=file)
    
    elif odd:
        print("CHUOILE", file=file)
    
    else:
        print("*", file=file)
    
    file.close()




   
