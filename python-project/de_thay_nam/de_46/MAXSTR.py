def filter_str(strings: str):
   with open('./de_46/maxstr.INP', 'r') as file:

      from re import findall
      string_n = findall(r'\d', file.readline().strip())
      l = len(string_n)
      right = 1
      max_r = min(string_n)

      while l - right + 1 > 4:   

         if string_n[right] > max_r:
            max_r = string_n[right]

         right += 1
      
      string_n = string_n[string_n.index(max_r): l]
   
   with open('./de_46/maxstr.OUT', 'w') as file:
      
      if len(string_n) == 4:
         print("".join(string_n),file=file)
      else:
         right = 1

         while len(string_n) > 4:
            if string_n[right] < string_n[right + 1]:
               del string_n[right:right + 1]

            right += 1
         print("".join(string_n),file=file)

   return None

string1 = '123aaddgg7ss8dd63dd9'
string2 = '5698173'
print(filter_str(string2))


   
