
def flower(number: int, lst: list[int]) -> int :
    
    n = number
    long_lst = 0
    lst = [0] + lst
    for i in range(1, n - 1):
   
        for j in range(i + 2, n):
                if lst[j] != lst[j - 1] or lst[j] != lst[j - 2]:
                    long_lst = max(long_lst, j - i + 1)

    return long_lst

n = 6
l = [5, 6, 6, 6, 23, 9] # 6, 6, 6, 7]

print(flower(n, l))



