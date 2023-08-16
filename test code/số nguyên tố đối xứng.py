from asyncio.format_helpers import _format_callback_source
import math

def prime(n):
    if n == 2 or n == 3:
        return True 
    elif n == 1 or n % 2 == 0 or n % 3 == 0:
        return False
    else:
       k = 5 
       can = math.sqrt(n)
       lam_tron_xuong = math.floor(can)
       while k <= lam_tron_xuong:
           if n % k == 0 or n % (k + 2) == 0:
               return False
           k += 6
    return True


def super_prime(n):
    if not prime(n):
        return False
    else:
        while n > 0 :
            if not prime(n):
                return False
            n //= 10
    return True


def kt_đối_xứng(n):
    # flag = True => số đối xứng
    # flag = False => không phải số đối xứng
    flag = False
    if ( str(n)[::-1] == str(n)):
      flag = True
    return flag


def find_the_next_super_prime(n):
    #sàng số nguyên tố  
    tmp = 1000000
    t = [True] * tmp
    for i in range(2, tmp // 2+1 ):
        for w in range(i * 2, tmp, i):
            t[w] = False
    
    #list số nguyên tố từ n => 1000000
    tmp2 = []
    for a in range(2, tmp):
        if t[a]:
            tmp2.append(a)
    #tìm số nguyên tố lớn hơn n và số nguyên tố đó phải là số đối xứng
    for i in tmp2:
        if i > n and kt_đối_xứng(i) == True:
            return i


def tìm_số_siêu_nguyên_tố_đối_xứng(n):
    t = []
    tmp = 1000000
    for i in range(2, tmp // 2 + 1):
        if prime(i) == True:
            t.append(i)
    for a in t:
        if a > n and kt_đối_xứng(a) == True:
            return a

n = open("PRPA.inp", 'r')
doc = n.read()
t = doc.split('\n')
n.close()
n2 = open("PRPA.out", 'w')
for i in t:
   #t = find_the_next_super_prime(int(i))
   t = tìm_số_siêu_nguyên_tố_đối_xứng(int(i))
   n2.write(str(t))
   n2.write('\n')

n2.close()



