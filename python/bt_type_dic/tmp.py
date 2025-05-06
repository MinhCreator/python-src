
def dic_init(lst):
    dt = {}

    for i in lst:
        if i in dt:
            dt[i] += 1
        else:
            dt[i] = 1
    
    var = tsmax(dt)

    return {
            
            "tan so max": var, 
            "key max": dt_max(dt, var), 
            "key min": dt_min(dt, var), 
            "cac phan tu cung tan so": elements_have_same_frequency(dt, var), 
            "phan tu dau dau tien co tan so max": pt_first_in_lst(dt, var)
            
            }
            

def tsmax(dt):

    tsmax = -1
    for y in dt.values():
        if y > tsmax:
            tsmax = y
            
    return tsmax

def dt_max(dt, tsmax):
    
    maxs = -1   

    for x, y in dt.items():
        if y  == tsmax:
            if x > maxs:
                maxs = x
    
    return maxs

def dt_min(dt, tsmax):

    mins = 2*(10**6)

    for x, y in dt.items():
        if y == tsmax:
            if x < mins:
                mins = x
                
    return mins

def elements_have_same_frequency(dt, tsmax):

    ans = []
    
    for x, y in dt.items():
        if y == tsmax:
            ans.append(x)
            
    return ans

def pt_first_in_lst(dt, tsmax):

    for x, y in dt.items():
        if y == tsmax:
            return x

    pass


l = [5, 3, 9, 7, 3, 4, 2, 7, 4, 5, 4, 7, 2, 9, 5, 8, 2, 8, 4, 1, 9, 6, 2, 8, 4, 7, 6, 6, 4, 5, 7, 5, 2, 9, 5, 9, 4, 1, 3, 1, 5, 8, 9, 7, 7, 3, 5, 7, 9, 8, 6, 1, 5, 5, 5, 6, 5, 9, 8, 4, 3, 4, 6, 3, 4, 4, 7, 5, 2, 6, 7, 6, 6, 2, 2, 5, 5, 2, 9, 1, 5, 5, 6, 5, 1, 6, 2, 9, 2, 5, 3, 5, 8, 4, 6, 1, 7, 3, 8, 7]
# lst = [4,23,6547,2,4,87,2,3,94,1,2,3,86,7,1,4,5,7,1,9,0,67,6,4,2]
print(dic_init(l))



