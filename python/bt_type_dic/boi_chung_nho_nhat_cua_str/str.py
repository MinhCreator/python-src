def BCNNC_str(s, t):
    
    a = s
    b = t

    while len(a) != len(b):

        if len(a) < len(b):
            a += s

        else: b += t

    if a == b: return a 
    
    else: return -1
    

print(BCNNC_str("aba", "ab"))