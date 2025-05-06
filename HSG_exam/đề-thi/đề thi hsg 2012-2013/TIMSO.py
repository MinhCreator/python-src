from math import sqrt, floor

def prime(n) -> bool:
    if n == 2 or n == 3: 
        return True

    elif n == 1 or n % 2 == 0 or n % 3 == 0: 
        return False
        
    elif n == 0: 
        return False
    
    else:
        k = 5
        t = sqrt(n)
        tmp = floor(t)
        
        while k <= tmp:
            if n % k == 0 or n % (k + 2) == 0:
                return False
            k += 6
                
    return True

def reverse_num(num: int): 

    string = str(num)
    return int(string[::-1])

def check_re_num(P: int, Q: int):
    
    store_num = []
    
    for value in range(P, Q + 1):

        if prime(reverse_num(value)) == True:
            store_num.append(value)

    return store_num

with open("./đề thi hsg 2012-2013/TIMSO.INP", "r") as file:
    num_P, num_Q = map(int, file.read().split(" "))

with open("./đề thi hsg 2012-2013/TIMSO.OUT", "w") as file:
    result = check_re_num(num_P, num_Q)
    for var in result:
        print(var, file= file)


    

