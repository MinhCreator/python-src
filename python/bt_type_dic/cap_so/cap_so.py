# cặp số  

def num_couple(lst , S):

    f = [0] * 1001

    ans = 0
    
    
    # init and add frequency to mark array
    for x in lst:

        f[x] += 1

    # find couple in list using mark array with formula 
    for index in lst:
        
        if index <= S:
            """
            inline using f[i] * f[s - i] because i != s - i
            """
            if index != S - index: 
                ans += f[index] * f[S - index]
           
            """
            using f[i] * (f[i] - 1) / 2 because i == s - i
            """
        else: 
                ans += f[index] * (f[index] - 1) // 2
           
        f[index] = 0

    return ans

lst = [1, 2, 3, 4, 0, 5, 1, 3]
s = 5

print(num_couple(lst, s))