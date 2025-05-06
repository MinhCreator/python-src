def square(n : int, k : int) -> int:

    from math import floor, ceil, sqrt

    x = ceil(sqrt(k))
    y = floor(sqrt(n))

    return y - x + 1
    
print(square(10 ** 9, 1))
# with open('./SQUARE.INP', 'r') as file:

#     n, k = map(int, file.readline().split())

# with open('./SQUARE.OUT', 'w') as file:
#     print(square(n, k),file=file)    