def count_str(str1: str, str2: str) -> int:

    count = str1.count(str2)

    return count


string = input("Enter a string one: ")

str2 = input("Enter a string two: ")

print(count_str(string, str2))
