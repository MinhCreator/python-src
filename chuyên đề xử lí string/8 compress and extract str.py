



def compress(str1: str) -> str:

    store = ""
    counter = 1
    
    for character in range(1, len(str1)):

        #module one
        if str1[character] == str1[character - 1]:
            counter += 1
             
        else:
            if counter > 1 :
                store += str(counter)
            store += str1[character - 1]    
            counter = 1

    #module two
    if counter > 1 :
        store += str(counter)
    store += str1[-1]

    return store

def extract(str1: str) -> str:

    store = ""
    ints = ""

    for value in str1:

        if value.isdigit() : 
            ints += value
        
        else:
            if ints:
                store += int(ints) * value
                ints = ""
            else:
                store += value

    return store
   

string = "AAAAAAAVVVVVVVVCDDDDDF"
strings = "4A2SD"

# print(extract(string))

print(extract(strings))
# print(compress(string))


