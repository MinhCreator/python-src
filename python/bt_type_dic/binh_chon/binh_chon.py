def _read_and_sort(lst: list):

    dt = {}
    tmp = sorted(lst)

    for x in tmp:

        if x not in dt:
            dt[x] = 1
        else:
            dt[x] += 1

    return find_tsmax(dt), dt

def find_tsmax(dt: dict):

    tsmax = -1
    for y in dt.values():
        if y > tsmax:
            tsmax = y
    return tsmax



def print_result(tsmax: int, dt: dict):
    
   with open('./binh_chon/output.out', 'w') as file:

            for key, item in dt.items():
            
                if item == tsmax:
                    print(key, file = file)

   return ""

   

"""Process"""

with open('./binh_chon/input.inp', 'r') as file:

    n = int(file.readline())

    lst = list(map(int, file.read().split()))

    var = _read_and_sort(lst)

    print(print_result(var[0], var[1]))

