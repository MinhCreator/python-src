
def find_friend_num(num, lst):
  

    list_du = [0] * num 

    # loop compute divide 3 by list
    for value in lst:
        
        list_du[value % 3] += 1

    sum_A = (list_du[0] * (list_du[0] - 1 ) // 2) + list_du[1] * list_du[2]


    return sum_A
  
  
      

  

# print(find_friend_num(4,[15, 6, 9, 3]))
# print(find_friend_num(5,[4, 3, 2, 3, 4]))
with open("./FRIENDNUM.INP", "r") as file:
    num = int(file.readline())
    lst = [int(i) for i in file.readline().split()]
# 
with open("./FRIENDNUM.OUT", "w") as file:
    print(find_friend_num(num, lst), file=file)
# 