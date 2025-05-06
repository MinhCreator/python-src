from re import findall

def test(str1: str):
   return findall(r'[\d+]?..[1-9]', str1)


string = "aB0011cd230d124ab17"
print(test(string))

import re

input_str = "aB0011cd230d124ab17"
numbers = re.findall(r'\d+', input_str)
print(numbers)
result = [int(num) for num in numbers if num.split("0")]
print(result)