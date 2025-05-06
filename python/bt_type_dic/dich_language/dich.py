"""
example:

method 1 :
my_list = ['apple', 'banana', 'cherry']
my_dict = {i: item for i, item in enumerate(my_list)}
or my_dict = {item : i for i, item in enumerate(my_list)}
 
print(my_dict) 

method 2 : 
my_list = ['apple', 'banana', 'cherry']
my_dict = {key: value for key, value in zip(['a', 'b', 'c'], my_list)}
print(my_dict)
"""

def dictionary() -> str:
    import sys
    

 
    sys.stdin = open('./dich_language/output.out', 'r')
    sys.stdout = open('./dich_language/output.out', 'w')
   

    num = int(input())
    dic = {}

    """init dictionary from file"""
    for i in range(num):
        x, y = input().split()
        y = y.replace("\n", "")
        dic[y] = x
   

    num2 = int(input())
    """return meaning from dictionary"""
    for tmp in range(num2):
        meaning = input().replace("\n", "")

        if meaning in dic: print(dic[meaning])
        else: print("eh")

    return ""



print(dictionary())
       



