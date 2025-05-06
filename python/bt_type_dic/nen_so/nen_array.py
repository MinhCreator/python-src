def compressing(lst: list):
    

    """
    copy list and remove duplicate number and sort list """
    
    copy_B_list = lst.copy()
    # remove_dup_and_sort = sorted(list(set(lst)))

    new = {sorted(list(set(lst)))[i - 1]: i for i in range(1, len(sorted(list(set(lst)))) + 1)}

    """
    compress array and return new compressed list """
    
    compress_arr = []
    for i in copy_B_list:
        compress_arr += [new[i]]

    return compress_arr #new_l

# print(compressing([-4, 16, 8, 10, -4, 5, 12, 8]))

"""way of teacher"""                  

def compressings():

    import sys
    sys.stdin = open('./nen_so/arrayzip.inp', 'r')
    sys.stdout = open('./nen_so/arrayzip.out', 'w')

    n = int(input())
    a = list(map(int, input().split()))
    b = sorted(a)
    dt = {}

    for x in b:

        if x not in dt:
            dt[x] = len(dt) + 1

    for x in a:
        print(dt[x], end=" ")
    
    return ""
print(compressings())
