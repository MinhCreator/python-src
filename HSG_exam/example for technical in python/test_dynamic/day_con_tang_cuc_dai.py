def tim_sub_list(A):

    # l(k)= max(1 + l(j)) condition: j < k and A[j] < A[k]
    # A[j] = P[k]|    
    n = len(A)
    mark_lst = [1] * n 
    P_truy_van = [None] * n

    for k in range(n):
        max_lst = 1
        index = None

        for i in range(k):
            
            if A[i] < A[k] and max_lst < mark_lst[i] + 1:
                max_lst = mark_lst[i] + 1
                index = i

        mark_lst[k] = max_lst
        P_truy_van[k] = index

    maxt = mark_lst[0]
    index_max = 0

    for k in range(n):
        if mark_lst[k] > maxt:
            maxt = mark_lst[k]
            index_max = k

    return index_max , maxt, P_truy_van 

def truy_vet(list_input):
    result = ""
    store_lst = []
    index, maxt, P_truy_van = tim_sub_list(list_input)    

    while index != None:
        store_lst.append(index)
        index = P_truy_van[index]

    for index2 in range(len(store_lst) - 1, -1, -1):
        result +=  " " + str(list_input[store_lst[index2]])

   
    return result
         

# list_input = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 19, 18]
#list_input = [1 ,0, 3 , -4, 9 , 4, 5]

with open("./test_dynamic/sub_list.inp") as file:
    list_input = list(map(int, file.readline().split(",")))

with open("./test_dynamic/sub_list.out", "w") as file:
    print(truy_vet(list_input), file= file)

print(tim_sub_list(list_input))
print("\n", truy_vet(list_input))

