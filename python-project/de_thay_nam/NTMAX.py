# prime fucntion
def prime(num: int)-> bool:
    
    if num == 2 or num == 3: return True

    if num % 2 == 0 or num % 3 == 0 or num == 0 or num == 1: return False

    else:
        from math import sqrt, floor
        k = 5
        f = floor(sqrt(num))

        while k <= f:
            if num % k == 0 or num % (k + 2) == 0:
                return False
            k += 6
    return True


def NTMAX(string: str) -> int:

    from re import findall
    count_lst = len(findall(r'\d', string))

    format_num = [int(x) for x in findall(r'\d+', string)]

    return (count_lst, max([x for x in format_num if prime(x)])) if any(prime(x) for x in format_num) else (count_lst, 0)


with open('./NTMAX.INP', 'r') as file:
    string = file.read().strip()

with open('./NTMAX.OUT', 'w') as file:
    sl_num, max_prime = NTMAX(string)

    print(f'{sl_num}\n{max_prime}', file=file)
    

