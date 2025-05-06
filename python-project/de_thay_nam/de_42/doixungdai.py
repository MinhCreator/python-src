def longest_palindromic_substring(list_palind: list[int]):
   n = len(list_palind)
   start = 0
   max_len = 1
   dp = [[False] * n for _ in range(n)]

   for i in range(n):
       dp[i][i] = True
   
   for length in range(2, n + 1):
       for i in range(n - length + 1):
   
           j = i + length - 1
   
           if length == 2:
               dp[i][j] = list_palind[i] == list_palind[j]
   
           else:
               dp[i][j] = list_palind[i] == list_palind[j] and dp[i + 1][j - 1]
   
           if dp[i][j] and length > max_len:
               start = i
               max_len = length
   end = start + max_len   
   return start + 1, end,list_palind[start:start + max_len]

with open('./de_thay_nam/de_42/DOIXUNGDAY.INP', 'r') as file:
   number = int(file.readline())
   list_data = list(map(int, file.read().split()))


with open('./de_thay_nam/de_42/DOIXUNGDAY.OUT', 'w') as file:
   start, end, palindrome = longest_palindromic_substring(list_data)
   print(f"{start} {end}\n{" ".join(str(x) for x in palindrome)}",file=file)