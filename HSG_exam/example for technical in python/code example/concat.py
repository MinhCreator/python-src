def concat(string1: str, string2: str) -> str:
   return string1 + string2

def procces(list_condition: list, list_num: list) -> int:

   left = int(list_condition[1])
   right = int(list_condition[2])

   count = 0
   for index in range(len(list_num)):
      for ind in range(len(list_num)):
            if left <= int(concat(list_num[index], list_num[ind])) <= right:
               count += 1


   return count

with open('./concat.inp', 'r') as file:

   num = int(file.readline())
   file2 = open('./concat.out', 'w')

   for x in range(num):
      list_condition = list(map(str, file.readline().split()))
      list_num = list(map(str, file.readline().split()))
      print(procces(list_condition, list_num), file= file2)
                  

