
def sieve(num) -> list:
    """_summary_

    Args:
        num (_type_): _description_

    Returns:
        list: _description_
    """
    prime = [True for i in range(num + 1)]
    p = 2
    while (p * p <= num):

        if prime[p] == True:
            for i in range(p * p, num + 1, p):
                prime[i] = False

        p += 1

    return [t for t in range(2, num + 1) if prime[t] == True]

print(sieve.__doc__)


# print(.__doc__)