def unknown_function(str1: list) -> str:
    
    for index, value in enumerate(str1):

        if str1.count(value) == 1:
            return value

    return "error non found special line"


files = open("./Special.inp", "r")
all = files.read().split("\n")

with open("./Special.out", "w") as files:
    print(unknown_function(all), file=files)

files.close()


        
        

