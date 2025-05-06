from re import findall

def extract_int(string: str):
   return sum([ int(x) for x in findall(r'\d+', string) ])

def return_values(string: str) -> int:

   tmp = extract_int(string)
   if tmp != 0:
      return tmp
   
   return 0

print(extract_int('aaaaaaAAA'))
