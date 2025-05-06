def sau(f):
    s_num = ''
    space = f +' '
    for i in range(len(space)-1):
        if space[i].isnumeric():
            if not (space[i+1].isnumeric()):
                s_num += f[i]+ ' '
            else:
                s_num += f[i]

    s_numb = s_num.rstrip(' ')
    l_num = list(map(int, s_numb.split()))
    l_num.sort()
    #print(l_num)

    n_str = ''
    st = f+' '

    i, j = 0, 0
    while i <= len(st)-2:
        if st[i].isnumeric():
            if j <= len(l_num):
                n_str += str(l_num[j])
                j += 1
            i += 1
            while st[i].isnumeric():
                i += 1
        else:
            n_str += st[i]
            i += 1
    return n_str

s = open('sau.txt', 'r') 
f = s.read()
p = open('saumoi.txt', 'w')
p.write(sau(f))
p.close()
s.close()