import math

def prime(n):
    if n == 2 or n == 3: 
        return True

    elif n == 1 or n % 2 == 0 or n % 3 == 0: 
        return False
        
    elif n == 0: return False
    
    else:
        k = 5
        t = math.sqrt(n)
        tmp = math.floor(t)
        
        while k <= tmp:
            if n % k == 0 or n % (k + 2) == 0:
                return False
            k += 6
                
    return True

def super_prime(n):
    
    if not prime(n): 
        return False
        
    elif prime(n) == True:
        digits = [int(s) for s in str(n)]
        
    for digit in digits:
        
        if prime(digit) == True:
            return True

        elif not prime(digit):
            return False


n = int(input("Nhap n: "))
print(super_prime(n))


