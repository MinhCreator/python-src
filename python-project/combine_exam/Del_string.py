
def del_string(string: str):
   list_str = string.split()
   extra_str = max(list_str, key=list_str.count)

   list_str = [i for i in list_str if i != extra_str]
   return " ".join(list_str) 

with open('./DELETESTR.INP', 'r') as file:
   string = file.read()


with open('./DELETESTR.OUT', 'w') as file:
   print(del_string(string),file=file)