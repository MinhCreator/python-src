from re import findall

def teen(string: str) -> None:
   strings = "TEEN"
   lst_s = findall(r'\D', strings)
   lst = findall(r'\D', string)
   tmp = []
   for x in lst:
      for t in lst_s:
         if x == t:
            luu = lst.count(x)

            if luu not in tmp :
               tmp += [luu]

   result = [x for x in tmp[::-1]]
   count_E = 0
   count_N = 0
   counts = 0
   for i in range(result[0]):
      for j in range(result[1]):
         count_E += 1
         if count_E == 2:
            break
      for o in range(result[2]):
         count_N += 1
         if count_N == 1:
               break
      counts += 1 

   return result, counts - 1

string = 'CONNECT CONNECT EEET'
print(teen(string))