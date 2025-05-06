def counts(lists: list):
   list_count = []

   for index, num in enumerate(lists):

      if lists.count(num) > 1 and [num,lists.count(num)] not in list_count:
         list_count.append([num,lists.count(num)])
   
   return sorted(list_count)

with open('./de_thay_nam/de_42/TSMAX.INP', 'r') as file:
   number = int(file.readline())
   list_data = list(map(int, file.read().split()))

with open('./de_thay_nam/de_42/TSMAX.OUT', 'w') as file:

   for num in counts(list_data):

      print(f"{num[0]} {num[1]}",file=file)