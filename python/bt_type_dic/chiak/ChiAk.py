def sub_child_consecutive(num, k, lists):
  
    counts = 0

    f = [0] * (num + 1) 

    for i in range(1, num + 1):

        f[i] = f[i - 1] + lists[i]

    for i in range(1, num + 1): 
        
        for j in range(i, num + 1):

            t = f[j] - f[i - 1]
            #print(t)
            
            if t < 0 and t % k != 0:
                du = k - (-t % k) 
                # print("t: ",t)
                # print("du: ",du)
                
                    # print(counts)

            else : 
                du = t % k

            if du == 0: counts += 1

    return counts

print(sub_child_consecutive(5, 3, [0, 2, -6, 1, 9, -3]))



