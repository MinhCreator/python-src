def dict_frequency(string: str):

    dict = {}

    for x in string:

        if x not in dict: 

            dict[x] = 1
        else:

            dict[x] += 1
    return dict


def ascII_frequency(string: str):

    lst= [0] * 256
   
    for x in string:

        lst[ord(x)] += 1


    for strs in range(256):

        if lst[strs] != 0:

            print(f"{chr(strs)}: {lst[strs]}")


def VD2(str: str):

    t = [0] * 256

    for i in range(len(str)):
        print(t[ord(str[i])] , end=" ")
        t[ord(str[i])] += 1

    return t #[x for x in t if x != 0]
    

print(VD2('system running then to self destroyed'))
