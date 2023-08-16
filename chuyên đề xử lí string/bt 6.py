
import re


def remove_space(str1: str) -> str:
    # Way 1
    # store = str1.strip()

    # while "  " in store :
    #     store = store.replace("  ", " ")

    # Way 2
    store = " ".join(str1.split())

    return store


def _fix_punctuation_(str1: str) -> str:

    # Way 1
    pattern = r"([,.?!;:])"  # pattern để tìm tất cả các dấu trong string
    # tìm và xóa space trước dấu câu và thêm space vào sau dấu câu
    return re.sub(pattern, r"\1 ", str1)

    # Way 2
    symbol = [",", ".", "!", "?", ";"]
    for i in symbol:
        strs = str1.replace(" " + i, i)
        strs = strs.replace(i, i + " ")

    return strs


def Upper(str1: str) -> str:

    symbols_bold = [".", "!", "?"]
    list_str = str1.split()
    list_str[0] = list_str[0].upper()

    for index, value in enumerate(list_str):

        if value in symbols_bold:
            list_str[index + 2] = list_str[index + 2].upper()

    str2 = "".join(list_str)
    return str2


def _correction_(str1: str) -> str:

    correct_string = Upper(remove_space(_fix_punctuation_(str1)))

    return correct_string


string = input("enter a string: ")
print(_correction_(string))
