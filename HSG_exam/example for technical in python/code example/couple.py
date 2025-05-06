def int_couple(lists: list) -> int:
   count = 0
   indx = 0

   for x in range(len(lists)):
      tmp = lists.count(lists[x])
      
      if lists[indx] != lists[x]:

         if tmp == 2 :     
            count += tmp
         indx = x

   return count      

lists = [6, 2, 4, 2, 4, 3, 4]
print(int_couple(lists))