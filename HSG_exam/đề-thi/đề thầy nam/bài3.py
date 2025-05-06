def _sieve_(num: int) -> list[int]:

    prime = [True] * (num + 1)
    run = 2

    while run * run <= num:

        if prime[run]:
            for i in range(run * run, num + 1, run):
                 prime[i] = False

        run += 1

    return [i for i in range(2, num + 1) if prime[i]]

def find_num_prime(num : int) -> int:

    prime = _sieve_(num)
    D = 0
    
    for nums in prime:

        if num % nums == 0 and nums > D:
            D = nums
            
    return D

with open("./đề thầy nam/bai3.inp", "r") as file:
    nums = int(file.readline())
    list_num = [int(i) for i in file.read().split()]

with open("./đề thầy nam/bai3.out", "w") as file:

    
    for num in list_num:
        print(find_num_prime(num), file = file)        