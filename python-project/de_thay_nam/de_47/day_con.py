def sub_list(lst: list, sublst: list) -> list:

   conditions = True
   for index, value in enumerate(sublst):

      if value in lst:
         conditions = True
      else:
         conditions = False

   if conditions == False: return 'N'
   
   return 'Y'
   
with open('./DAYCON.INP', 'r') as file:   
   len_sub = int(file.readline())
   sublst = list(map(int, file.readline().strip().split()))
   len_main = int(file.readline())
   lst = list(map(int, file.readline().strip().split()))


with open('./DAYCON.OUT', 'w') as file:

   print(sub_list(lst, sublst),file=file)