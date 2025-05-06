with open('maxstr.inp') as f:
    s=f.readline().strip()
import re
s=list(re.findall('\d',s))
j=1
maxs=min(s)
while (len(s)-j+1)>4:
    if s[j]>maxs:
        maxs=s[j]
    j+=1
s=s[s.index(maxs):len(s)]
with open('maxstr.out','w') as g:
    if len(s)==4:
        g.write(''.join(s))
    else:
        j=1
        while len(s)>4:
            if s[j]<s[j+1]:
                del s[j:j+1]
            j+=1
        g.write(''.join(s))
    
