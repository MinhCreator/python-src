def special_num():
   with open('./SDB.INP', 'r') as file:
      len_num = int(file.readline())
      string = file.read()
      num_before = int(string)

      list_num = [int(x) for x in string]

      # cal sum
      sums = sum(list_num)
               
      return sums, list_num 
print(special_num())