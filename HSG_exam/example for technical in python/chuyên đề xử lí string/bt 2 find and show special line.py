def unknown_function(lst: list) -> str:
    
    for value in lst:

        if lst.count(value) == 1:
            return value



files = open("./chuyên đề xử lí string/Special.inp", "r")

all = files.read().split("\n")

with open("./chuyên đề xử lí string/Special.out", "w") as files:
    
    print(unknown_function(all), file=files)

files.close()


        
        

