def word(s : str):
    n = len(s)
    s = "0" + s
    
    f = [0] * (n + 1)
    p = [0] * (n + 1)
    results = 0

    for i in range(1, n + 1):

        if s[i] == "C":
            
            f[i] = f[i - 1] + 1
        else:

            f[i] = f[i - 1]

        # print(f[i])
        
    if s[n] == "W": p[n] = 1

    for i in range(n - 1, 1, -1): 

        if s[i] == "W":

            p[i] = p[i + 1] + 1

        else: 
            p[i] = p[i + 1]

        # print(p[i])
    
    for i in range(2, n):

        if s[i] == "O":

            results = results + f[i] * p[i]
            # print(results)
    return results #f, p
    
""""""

print(word("COOWWW")) 
print(word("CWOWOW"))
print(word("COWOWOW"))           

def count_word(string : str):
    string = "0" + string
    sl_c = 0
    sl_co = 0
    ans = 0

    for i in range(1, len(string)):

        if string[i] == "C": 

            sl_c += 1

        elif string[i] == "O":

            sl_co += sl_c
        else: ans += sl_co

    return ans

# print(count_word("COOWWW"))
# # print(count_word("COWOWOW"))
