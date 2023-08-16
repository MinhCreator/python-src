# require
# file input: Khoahoc.inp
# file output: Khoahoc.out




def compess_group(num_mem: int, lst_mem: list) -> int:

    # variables
    num_group = 0
    lst_group = [False] * len(lst_mem)

    # mark members in group
    for mem in range(len(lst_mem)):
        
        if not lst_group[mem]:

            lst_group[mem] = True
            num_group += 1
            limit = 1

        # count group
            for member in range(mem + 1, len(lst_mem)):
                
                if lst_mem[mem] == lst_mem[member]:
                    limit += 1

                    if limit <= lst_mem[mem]:
                        lst_group[member] = True
                        
    return num_group 


# check and read data into file
file = open("bài 2.5 nhóm đề án\Khoahoc.inp", "r")

# data 
num_mem = int(file.readline())
list_member = list(map(int, file.readline().split()))

# write data into file
with open("bài 2.5 nhóm đề án\Khoahoc.out", "w") as file:
    file.write(str(compess_group(num_mem, list_member)))
