def sievep_prime(n):
    prime = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if prime[p] == True:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    primes = []
    for p in range(2, n + 1):
        if prime[p] is True:
            primes.append(p)
    return primes



def count_prime(x: int) -> int:

    list_sieve_prime = sievep_prime(x)
    N = 10 ** 4
    dp = [-10000] * (N + 3)
    dp[0] = 0
    
    if x == 1:
        return 1

    else:
        for x in list_sieve_prime:

            for value in range(N, x - 1, -1):

                for limit in range(1, 3):

                    dp[value] = max(dp[value], dp[value - limit * x] + limit)
                    tmp = dp[value]

        return tmp
# print(count_prime(int(input())))

with open('./COUNTPRIME.INP', 'r') as file:
    x = [int(line) for line in file]
    
with open('./COUNTPRIME.OUT', 'w') as file:
    for tmp in x:
        print(count_prime(tmp), file = file)