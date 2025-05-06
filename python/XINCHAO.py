def del_let(pat: str, main: str):
    first = main.find(pat[0])

    return main[first : len(pat) - len(main) + 1]


print(del_let("hello", "ahhellllloou"))


# this main code is not working and i don't know why
