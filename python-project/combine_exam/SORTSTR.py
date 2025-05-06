from re import findall

def extract_int(string: str):
   return findall(r'\d+', string)

def find_index(string: str):
   tmp = extract_int(string)
   index = []

   for var in tmp:

      if binary_search(string, var) != -1:
         index.append(binary_search(string, var))
      else:
         index.append(-1)
   return index

def binary_search(string: str, num: str):
   left = 0
   right = len(string) - 1

   while left <= right:
      mid = (left + right) // 2
      if string[mid] == num:
         return mid
      elif string[mid] < num:
         left = mid + 1
      else:
         right = mid - 1
   return -1

string = "Anh24ch12abc1cd8"
print(find_index(string))