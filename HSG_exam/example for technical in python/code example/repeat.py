def find_char(string1: str, sub_string: str) -> list[int] or int:
   
   list_index = [] 
   for x in range(len(string1)):

      tmp = string1.find(sub_string, x, len(string1) + len(sub_string))

      if tmp != -1 and tmp not in list_index:
         list_index.append(tmp)

   if list_index == []:
      return -1
   
   return " ".join([str(x + 1) for x in list_index ])

print(find_char('aaaaaa', 'bbbbb'))