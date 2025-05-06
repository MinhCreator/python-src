from math import gcd


length = int('3')
def max_beautiful_array(arr: list, length: int):
    n = len(arr)
    dp = [1] * n
    cal = 0

    
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] % arr[j] == 0 :
                dp[i] = max(dp[i], dp[j] + 1)
                cal = 
                print(arr[i], arr[j])
    if max(dp) == length:
       return max(dp), dp, cal

print(max_beautiful_array([4, 4, 4, 3, 1, 3], 3))