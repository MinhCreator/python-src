from math import gcd

def PTHUONG():
   with open('./de_46/PTHUONG.INP', 'r') as file:
      number = int(file.readline())
      list_data = list(map(int, file.read().split()))

   with open('./de_46/PTHUONG.OUT', 'w') as file:
      print(gcd(*list_data), file=file)

PTHUONG()

