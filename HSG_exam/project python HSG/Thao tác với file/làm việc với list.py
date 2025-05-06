# số lớn thứ nhì
array = [6,3,1,2,4,5,6]
max = float('-inf')
max_tmp2 = float('-inf') 
max_cs = []
max_tmp2_cs = []
for i in range(len(array)):
    if array[i] > max:
        max_tmp2 = max
        max_tmp2_cs = max_cs
        max_cs = array[i]
        max_tmp2_cs = [i]
    elif array[i] == max:
        max_tmp2_cs.append(i)
    elif array[i] > max_tmp2:
        max_tmp2 = array[i]
        max_tmp2_cs = [i]
    elif array[i] == max_tmp2:
        max_tmp2_cs.append(i)
print('so lon thứ nhì: ',max_tmp2,'chi so cua no: ',max_tmp2_cs)


# số bé thứ nhì
#array = [56,90,45,23,34,12]
#min = float('inf')
#min_tmp2 = float('inf') 
#min_cs = []
#min_tmp2_cs = []
#for i in range(len(array)):
#    if array[i] < min:
#        min_tmp2 = min
#        min_tmp2_cs = min_cs
#        min = array[i]
#        min_tmp2_cs = [i]
#    elif array[i] == min:
#        min_cs.append(i)
#    elif array[i] < min_tmp2:
#        min_tmp2 = array[i]
#        min_tmp2_cs = [i]
#    elif array[i] == min_tmp2:
#        min_tmp2_cs.append(i)
#print('so be thứ nhi:', min_tmp2 ,'  chi so cua no:', min_tmp2_cs)



