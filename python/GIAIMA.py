def decript(s : str, lst_key : list) -> str:

    lst_s = s.split()
    st_tmp = ""

    for code in lst_key:

        st_tmp += lst_s[code - 1] + " "

    return st_tmp

s = "luon chuc hoc ban gioi luon"

lst = [2, 4, 1, 6, 3, 5]

print(decript(s, lst))

