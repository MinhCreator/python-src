def find_and_remove(str, ch):

    string = str.replace(ch, "")

    return string


str_st = input("Enter a string: ")
ch = input("Enter a character: ")

print(find_and_remove(str_st, ch))
