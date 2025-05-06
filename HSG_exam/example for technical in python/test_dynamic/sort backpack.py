


def creating_matrix(matrix_size, W) -> list[list[int]]:
    
    matrix = []

    for run in range(matrix_size + 1):

        matrix.append([0] * (W + 1))

    return matrix

def choose_object(n, W, list_w, list_v) -> list[list[int]]:

    V = creating_matrix(n, W)

    for i in range(1, n + 1):

        for j in range(1, W + 1):

            if j < list_w[i]:
                V[i][j] = V[i - 1][j]

            else:
                V[i][j] = max(V[i - 1][j], V[i - 1][j - list_w[i]] + list_v[i])


    return V

def loot_in_bag(i, j, list_w, V) -> list[int]:

    if i == 0:
        return []
    
    else:
        if V[i][j] > V[i - 1][j]:
            return loot_in_bag(i - 1, j - list_w[i], list_w, V) + [i]
        
        else:
            return loot_in_bag(i - 1, j, list_w, V)
        




# mass_object = [0, 2, 1, 3, 2]
# value = [0, 12, 10, 20, 15]
# quantity_object = 4
# back_pack_max_store = 5
# V = choose_object(quantity_object, back_pack_max_store, mass_object, value)
# s = loot_in_bag(quantity_object, back_pack_max_store, mass_object, V)
# print(V[quantity_object][back_pack_max_store])
# print("\n",s)

with open("./test_dynamic/backpack.inp") as file :
    
    n, w = map(int,file.readline().split())

    kl = [0] + list(map(int, file.readline().split()))

    gia_tri = [0] + list(map(int, file.readline().split()))
    
with open("./test_dynamic/backpack.out", "w") as file :

    V = choose_object(n, w, kl, gia_tri)
    V1 = V[n][w]
    print(V1, file=file)
    
    s = loot_in_bag(n, w, kl, V)
    # for i in s:
    #     print(i, end=" ", file=file)
    print(" ".join(map(str, s)), file=file)
    

