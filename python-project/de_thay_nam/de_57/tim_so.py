def prime(n: int) -> bool:

    if n == 2 or n == 3: return True

    if n % 2 == 0 or n % 3 == 0 or n == 0 or n == 1: return False

    else:
        from math import sqrt, floor
        k = 5
        f = floor(sqrt(n))

        while k <= f:
            if n % k == 0 or n % (k + 2) == 0:
                return False
            k += 6
        return True

def find_num(n: int):

    from math import trunc, sqrt, floor
    arr = []
    lens = 3
    # for x in range(n):
        
    arr_prime = []
    for index in range(2, n + 1):

        for x in range(2, trunc(sqrt(n)) + 1):

            if index != x and prime(index) and prime(x):
                z = n - index - x
                if prime(z):
                    if sorted([index, x, z]) not in arr:
                        arr_prime.append(sorted([index, x, z]))
                break
    arr = [x for x in arr_prime if x not in arr]
    
    return arr #, arr_prime
    

# code đang bị lỗi 
print(find_num(100000))