



def Xmod(k: int, tmp: list) -> int:

    #variables
    counter = 0
    list_mark = [False] * k

    for num in tmp:
        if not list_mark[num % k]:
            
            list_mark[num % k] = True

            counter += 1



    return counter 


file = open("bài 2.7 phép chia lấy dư/Xmod.INP", "r")

n , k = map(int, file.readline().split())
lst = list(map(int, file.read().split()))

with open("bài 2.7 phép chia lấy dư/Xmod.OUT", "w") as file:
    print(Xmod(n, k, lst), file=file)

file.close()
