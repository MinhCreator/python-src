def palin(n: str):

    if n == n[:: -1]:
        return 'YES'

    return 'NO'

