def TONG(lst_a: str, lst_b: str):
   num_a, num_b = int(lst_a), int(lst_b)
   return " ".join([x for x in str(num_a + num_b)]), len(str(num_a + num_b))

with open('./TONG.INP', 'r') as file:
   s_a = int(file.readline())
   a = "".join(file.readline().strip().split())
   s_b = int(file.readline())
   b = "".join(file.readline().strip().split())

with open('./TONG.OUT', 'w') as file:
   lens, so = TONG(a, b)
   print(f"{so}\n{lens}",file= file)
   
