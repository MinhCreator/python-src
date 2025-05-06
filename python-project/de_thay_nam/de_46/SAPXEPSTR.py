def sort_string(list_str: list):

   return sorted(list_str, key = lambda x: len([int(i) for i in x if i.isdigit()]))

with open('./de_46/SAPXEPSTR.INP', 'r') as file:
   num = int(file.readline())
   data = list(map(str, file.read().split('\n')))


with open('./de_46/SAPXEPSTR.OUT', 'w') as file:

   print("\n".join(sort_string(data)),file=file)