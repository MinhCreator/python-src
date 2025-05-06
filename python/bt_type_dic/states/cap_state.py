""" Mistake code :"""
def state(dic: dict):

    ls = list(dic.values())
    counts = 0
    for x in range(0, len(ls) - 2):

        for y in range(x + 1, len(ls) - 1):

            if x + y == y + x:

                counts += 1

    
    return counts, dic

    
"""Correct code:"""
def couple_staes():

    with open ('./states/input.inp', 'r') as file:
        n = int(file.readline())

        """init dictionary state and state code from file"""
        dic = {}
        counts = 0
        
        for i in range(n):
            
            x, y= file.readline().split()
            y = y.replace("\n", "")
            
            dic[x] = y

            tmp = x[:2]

            if tmp != y:
                
                if tmp + y in dic:
                    counts += dic[tmp + y]
                
                if y + tmp not in dic:
                    dic[y + tmp] = 1
                
                else:
                   dic[y + tmp] += 1                     
    return counts

print(couple_staes())


def couple_staes1():

    with open ('./states/input.inp', 'r') as file:
        n = int(file.readline())

        """init dictionary state and state code from file"""
        dic = {}
        counts = 0
        
        for i in range(n):
            
            x, y= file.readline().split()
            y = y.replace("\n", "")

            if x != y:
                
                if x + y not in dic:
                    dic[x + y] = 1
                else:
                    dic[x + y] += 1
        
        # bug code here
        ans = 0
        for key, value in dic.items():
            ng = key[2:4] + key[:2]
            
            if ng in dic:
                ans = ans + dic[key] * dic[ng]   
                dic.pop(ng)

    return dic, ans

print(couple_staes1())

