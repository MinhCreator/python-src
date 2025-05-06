def sub_child(num, s, lists):
  
    counts = 0

    f = [0] * (num + 1) 

    for i in range(1, num + 1):

        f[i] = f[i - 1] + lists[i]

    for i in range(1, num + 1): 
        
        for j in range(i, num + 1):

            t = f[j] - f[i - 1]
            
            if t == s:
                counts += 1

    return counts

