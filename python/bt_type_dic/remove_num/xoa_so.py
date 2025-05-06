def odd_and_even(num):
    odd = [x for x in num if x % 2 != 0]
    even = [x for x in num if x % 2 == 0]
    return odd, even

def num(num):

    c = len(odd_and_even(num)[1])
    l = len(odd_and_even(num)[0])
    ans = 0

    
    
    if sum(num) % 2 == 0:
        ans = (c * (c - 1) // 2) + (l * (l - 1) // 2)

    if sum(num) % 2 != 0:
        ans = (l) * (c)


    return ans


print(num([1, 2, 3, 4, 5]))
