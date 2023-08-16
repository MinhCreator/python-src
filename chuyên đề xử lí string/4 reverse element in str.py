def reverse_element(str1: str):

    lst_word = str1.split()

    store = " ".join(lst_word[::-1])

    return store


string = input("Enter a string: ")

print(reverse_element(string))
