def process(n: int, lst: list[int]) -> int:

    """kiểm tra và return số phần tử khác nhau"""
    tmp = abs_lst(lst)
    convert_set = set(tmp)

    return len(list(convert_set))

def abs_lst(lst: list[int]) -> list[int]:

    """return giá trị tuyệt đối của các phần tử có trong list"""
    return [abs(i) for i in lst]

# print(process(5, [2, 3, 3, 2, 2]))

"""cách của cô"""

def tmps(n: int, lst: list):

    new_dict = {}

    for x in lst:
        if x in new_dict:
            new_dict[x] += 1
        else:
            new_dict[x] = 1
    return len(new_dict)

#print(tmps(5, [2, 3, 3, 2, 2]))

with open('./bt_type_dic/phan_tu_khac_nhau/input.inp', 'r') as file:
    n = int(file.readline())

    lst = list(map(int, file.read().split()))
   
with open('./bt_type_dic/phan_tu_khac_nhau/output.out', 'w') as file:
    print(process(n, lst),file=file)

