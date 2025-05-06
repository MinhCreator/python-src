def string_finding(string1: str) -> int:

   length, reverseds = len(string1), string1[::-1]
   length_reverseds = len(reverseds)
   matrix = [[False] * (length + 1) for _ in range(length + 1)]

   string1, reverseds = '.' + string1, '.' + reverseds
   
   for i in range(1, length + 1):

      for j in range(1, length_reverseds + 1):
         
         if string1[i] == reverseds[j]:
            matrix[i][j] = matrix[i - 1][j - 1] + 1

         else: matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])
            

   return matrix[length][length], matrix

def trace_string(string1: str, i: int, j: int, dp: list) -> str:
   x, y, save = '_' + string1, '_' + string1[::-1], []

   while i > 0 and j > 0:
      
      if x[i] == y[j]:
         save.append(x[i])
         i, j = i - 1, j - 1
         print(x[i], y[j])

      else:
         if dp[i - 1][j] > dp[i][j - 1]: i -= 1
         else: j -= 1

   return save #''.join(save[::-1])

str_before = "lmevexeyzl"
str_reversed =  str_before[::-1]
x, y = len(str_before), len(str_reversed)
max_len, dp = string_finding(str_before)
letter_finding = x + y - 2 * max_len
print(letter_finding)
print(trace_string(str_before, x, y , dp))
      