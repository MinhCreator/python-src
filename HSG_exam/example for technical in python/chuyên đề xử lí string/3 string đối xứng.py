def string_doi_xuong(str):

    if str == str[::-1]:
        return True
    else:
        return False


string = input("Enter a string: ")
print(string_doi_xuong(string))
