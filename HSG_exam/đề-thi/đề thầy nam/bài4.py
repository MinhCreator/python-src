
from math import sqrt, floor

def prime(n) -> bool:
    if n == 2 or n == 3: 
        return True

    elif n == 1 or n % 2 == 0 or n % 3 == 0: 
        return False
        
    elif n == 0: return False
    
    else:
        k = 5
        t = sqrt(n)
        tmp = floor(t)
        
        while k <= tmp:
            if n % k == 0 or n % (k + 2) == 0:
                return False
            k += 6
                
    return True

with open("./đề thầy nam/bai4.inp", "r") as file:
    num_a, num_b = list(map(int, file.readline().split()))

with open("./đề thầy nam/bai4.out", "w") as file:

    tmp = [str(num) for num in range(num_a, num_b) if str(num)[::-1] == str(num)]
    list_sieve = [int(num) for num in tmp if prime(int(num))]

    sum = 0
    for num in list_sieve:
        sum+= 1

    print(sum, file=file)

