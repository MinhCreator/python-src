def tup(str1: str) -> tuple:

    tmp = str1.split(",")

    return tuple(tmp), tmp

value = input("Enter value: ")
print(tup(value))