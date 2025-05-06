def decompress_str(str1: str):

   from re import findall
   stra = findall(r'(\d+)?(\D)', str1)
   str1 = ''
   
   for i in range(len(stra)):

         if stra[i][0].isdigit():
            str1 += int(stra[i][0]) * stra[i][-1]   
         else:
            str1 += stra[i][-1]

   return str1

# import re

# def decompress_str(str1: str):
#     pattern = re.compile(r'(\d+)?(\D)')
#     tokens = pattern.findall(str1)
#     decompressed = ''.join(int(count or 1) * char for count, char in tokens)
#     return decompressed
print(decompress_str('12a5bk2c'))