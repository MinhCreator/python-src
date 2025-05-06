

def max_element(str1: str) -> str:

    element = str1.split()

    if element != []:
        return max(element, key=len)

    else:
        return False


str = input("Enter a string: ")
longest_word = max_element(str)

if longest_word is str or bool:
    print("Longest word: ", longest_word)
else:
    print("longest word not found!")
