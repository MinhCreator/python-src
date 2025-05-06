

def search(list_int: list, target: int) -> int:
   first_index = list_int.index(target) 
   output = []
   if first_index != -1:
      
      for i in range(first_index, len(list_int)):

         if list_int[i] == target:
            first_index = i
            output.append(i)
         
   return output


list = [1, 2, 3, 4, 7, 8, 6, 5, 8, 5, 10]
target = 5
print(search(list, target))   


