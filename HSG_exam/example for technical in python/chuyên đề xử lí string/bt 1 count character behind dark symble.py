
def count_character(str1: str) -> int:

    counts = 0
    char = "."

    counts += str1.count(char)
        
    return counts


    
# print(count_character("tinh.than.vuot.kho."))
files = open("./chuyên đề xử lí string/CH.inp", "r")

extract_str = files.read()

with open("./chuyên đề xử lí string/CH.out", "w") as files:
    print(count_character(extract_str), file=files)
files.close()
