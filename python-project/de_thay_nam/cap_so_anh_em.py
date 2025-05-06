def sievep1(n):
    prime = [True] * (n + 1)
    prime_start = 2
    
    while prime_start * prime_start <= n:
        if prime[prime_start] == True:
            
            for i in range(prime_start * prime_start, n + 1, prime_start):
                prime[i] = False
                
        prime_start += 1
        
    prime_s = []
    
    for primes in range(2, n + 1):
        if prime[primes] == True:
            prime_s.append(primes)
    return prime_s

def couple_prime(n: int, k: int):
    
    prime = sievep1(n)
    count = 0

    for i in range(len(prime)):

        for j in range(i + 1, len(prime)):

            if prime[j] - prime[i] == k or prime[i] - prime[j] == k:
                count += 1

    return count
