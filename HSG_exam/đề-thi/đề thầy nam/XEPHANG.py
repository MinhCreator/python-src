def sorts(list: list):
   return max(set(list), key=list.count)

def find(list: list):
   return list.count(sorts(list))   

with open('./XEPHANG.INP', 'r') as file:
  num = int(file.readline())
  list = [int(num) for num in file.read().split()]

with open('./XEPHANG.OUT', 'w') as file:
  print("{} {}".format(find(list), sorts(list)), file=file)

print(find([160, 158, 158, 160, 159, 158, 159, 160, 158, 161]))