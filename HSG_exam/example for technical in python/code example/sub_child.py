def _sub_child_(lst: list) ->list[int]:

    mark = [0] * 32001
    
    for run in lst:
        mark[run] += 1

    filter = [x for x in range(32001) if mark[x] != 0]

    return filter
    

print(_sub_child_([1, 9, 4, 5, 9, 5, 8, 9]))