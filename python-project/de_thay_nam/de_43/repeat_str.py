def slice_str(pattern: str, str2: str):

   counter = 0

   for index in range(len(pattern)):

      for jndex in range(len(str2)):

         if str2[index] == str2[jndex] and str2[index: jndex + 1] == pattern:
            counter += 1 
   return counter


with open('./de_thay_nam/de_43/REPEATSTR.INP', 'r') as file:
   pattern = file.readline().strip()
   str2 = file.readline().strip()
with open('./de_thay_nam/de_43/REPEATSTR.OUT', 'w') as file:
   print(slice_str(pattern, str2), file = file)