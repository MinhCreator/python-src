def level_multiplier(n : int, q: int) -> int:
   Un = 0
   u1 = 1
   
   for i in range(1, n + 1):
      Un += u1 * pow(q, i - 1)
   return Un

