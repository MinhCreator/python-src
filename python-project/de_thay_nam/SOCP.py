# init function 

def check_CP(lst: list):
   from math import sqrt
   cp = [x for x in lst if sqrt(x)**2 == x]
   return f"{len(cp)}\n{" ".join(str(x) for x in cp)}"


# open and read file 
with open('./SOCP.INP', 'r') as file:
   number = int(file.readline())
   list_data = list(map(int, file.readline().split()))

# open and write file
with open('./SOCP.OUT', 'w') as file:
   print(check_CP(list_data), file=file)