def string_standardize():


   with open('./CHXAU.INP', 'r') as file:
      num = int(file.readline())
      strings = file.read().split('\n')
   
   format_string = [x.split() for x in strings]
   
   for inx, string in enumerate(format_string):
      format_string[inx] = " ".join(string) + "\n"

   return format_string 

with open('./CHXAU.OUT', 'w') as file:
   print("".join(string_standardize()), file=file)
   