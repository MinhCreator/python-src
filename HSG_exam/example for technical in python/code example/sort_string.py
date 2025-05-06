from re import findall

def sieve_num(string: str) -> list[int]:
    
    take_num = findall(r"\d", string)

    return take_num

def sort_string(list_str: list) -> list[str]:
        
    return sorted(list_str, key= lambda x: len(sieve_num(x)))
   

with open("SAPXEP.INP", "r") as file:
    num = int(file.readline())
    list_string = list(map(str, file.read().split("\n")))

with open("SAPXEP.OUT", "w") as file:

        t = sort_string(list_string)
        for i in t:

            print(i, file = file)