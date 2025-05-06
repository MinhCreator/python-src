def del_symble(string: str) -> str:
   lists = string.split()
   s = ""

   for x in range(len(lists)):
      if lists.count(lists[x]) == 1:
         s += lists[x] + " "      

   return s


print(del_symble("thi  khao sat hoc sinh   gioi mon  tin  mon"))