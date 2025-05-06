def tro_choi(lst: list):

    """init and defind variable"""
    maxs = -1e6
    f = [0] * (len(lst) + 1)
    p = [0] * (len(lst) + 1)

    """process"""
    for i in range(1, len(lst)):

        f[i] = max(f[i - 1], lst[i - 1])
        # print(f[i])
   
    p[len(lst) - 1] = 1e6 
    for i in range(len(lst) - 2, 1, -1):
       
        p[i] = min(p[i + 1], lst[i + 1])
        # print(p[i])

    for i in range(2, len(lst) - 1):
        maxs = max(maxs, (2 * f[i]) - lst[i] - p[i])
        
    if maxs < 0 : maxs = 0 
    
    return maxs

print(tro_choi([1, 20, 2, 21, 7, 4]))
print(tro_choi([1, 2, 7, 4, 21, 20]))