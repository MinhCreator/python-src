data_input = open("sapxep4.inp", "r")
data_output = open("filesapxep4.out", "w")
# read the first line into file
temp = int(data_input.readline())
# read the next lines into file 
temp2 = data_input.read().split()
data_input.close()
lst_number = list(map(int, temp2))

lst_copy = lst_number.copy() # copy the lst_number 
print('the initial list: ', lst_copy)
# sort the list to max -> min and reverse list
lst_number.sort(reverse=True)
# convert list number to string
str_temp = ','.join([str(i) for i in lst_number])
lst_tmp = []

for i in lst_number:
    # duyệt ngược list
    for t in range(len(lst_number)-1, -1, -1):
        if (i == lst_copy[t]) and not(t + 1 in lst_tmp):
            # +1 để ra số thứ tự các phần tử
            lst_tmp.append(t + 1)
# chuyển list thành string
str2 = ",".join([str(i) for i in lst_tmp])

data_output.write(str_temp)
data_output.write("\n")
data_output.write(str2)
data_output.close()
