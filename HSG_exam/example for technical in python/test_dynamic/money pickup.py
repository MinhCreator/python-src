

def pick_up(list_coin: list[int]) -> int:

    length = len(list_coin)

    list_store = [0] * (length + 1)

    list_store[0] = 0

    list_store[1] = list_coin[0]

    for num_k in range(2, length + 1):

        list_store[num_k] = max(list_store[num_k - 1],
                                list_coin[num_k - 1] + list_store[num_k - 2])

    return list_store[length]


def pick_up_optimize(list_coin: list[int]) -> int:

    length = len(list_coin)

    list_store = [0] * (length + 1)

    list_store[0] = 0

    list_store[1] = list_coin[0]

    # variables
    """ 
    result optimize 
    form:
    f[k] = sa
    f[k - 1] = sb
    f[k - 2] = sc
    """
    sc = []

    sb = [list_coin[0]]

    for num_k in range(2, length + 1):

        if list_store[num_k - 1] > list_store[num_k - 2] + list_coin[num_k - 1]:
            list_store[num_k] = list_store[num_k - 1]
            sa = sb

        else:
            list_store[num_k] = list_store[num_k - 2] + list_coin[num_k - 1]
            sa = sc + [list_coin[num_k - 1]]

        sc = sb
        sb = sa

    return list_store[length], sa


with open("./test_dynamic/pickup.inp", "r") as files:

    list_pickup = list(map(int, files.read().split()))


with open("./test_dynamic/pickup.out", "w") as files:

    print(str(pick_up(list_pickup)) + "\n" +
          str(pick_up_optimize(list_pickup)), file=files)


# print(pick_up_optimize([5, 1, 2, 10, 7, 2]))
