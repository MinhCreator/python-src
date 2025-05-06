def cmd_robot(lst_cmd: list):

    right = 1
    left = 0
    step = 0

    for cmd in lst_cmd:

        if cmd == right:
            step += 1
        elif cmd == left:
            step += 1

    return step

lst = [1, 1, 1, 0, 0, 1, 0, 1, 0, 1]
print(cmd_robot(lst))
