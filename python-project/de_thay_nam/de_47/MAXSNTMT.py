from math import sqrt, floor

def is_prime(num: int):
    if num == 2 or num == 3: return True

    if num % 2 == 0 or num % 3 == 0 or num == 0 or num == 1: return False

    else:
        k = 5
        f = floor(sqrt(num))

        while k <= f:
            if num % k == 0 or num % (k + 2) == 0:
                return False
            k += 6

        return True


#matrix = [[2, 4, 1, 5, 7], [2, 2, 8, 3, 5], [1, 7, 2, 8, 0], [9, 6, 4, 7, 3]]

with open('./de_47/MAXSNTMT.INP', 'r') as file:
   line, row = map(int, file.readline().split())

   matrix = [int(x) for x in file.read().strip().split() if is_prime(int(x))]

   most_num = max(matrix, key=matrix.count)
   ocurrs = matrix.count(most_num)

with open('./de_47/MAXSNTMT.OUT', 'w') as file:
   print(most_num, ocurrs,file=file)