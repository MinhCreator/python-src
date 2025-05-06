def dict(x):
    
    dicts = {}

    for tmp in range(1, x+1):
        dicts[tmp] = tmp*tmp

    return dicts

print(dict(8)) 