# bài tập 1
#nhập vào 2 cạnh của hình chữ nhật. Đưa ra màn hình chu vi, diện tích của hình chữ nhật đó với yêu cầu sau:
#các kết quả in ra trên 1 hàng 
#mỗi kết quả trên từng hàng
'''length = float(input('nhập chiều dài: '))
width = float(input('nhập chiều rộng: '))
# chu vi 
cv = (length + width) * 2 
# diện tích
dt = length * width 
# trên 1 hàng
print('chu vi = ', cv, 'diện tích = ', dt)
# trên 2 hàng riêng biệt
print('chu vi = ', cv, '\ndiện tích = ', dt)
'''

# bài tập 2 
#nhập vào 3 cạnh tam giác. đưa ra screen chu vi, diện tích của tam giác đó trên cùng 1 hàng
'''import math
c1 = float(input('nhập cạnh thứ nhất: '))
c2 = float(input('nhập cạnh thứ hai: '))
c3 = float(input('nhập cạnh thứ ba: '))
# chu vi 
z = c1 + c2 + c3 
# nửa chu vi 
p = (c1 + c2 + c3) / 2 
#diện tích
temp = p * (p - c1) * (p - c2) * (p - c3)
x = math.sqrt(temp)
# làm tròn 
dt = round(x, 2)
cv = round(z, 2)
print('chu vi =', cv, 'diện tích =', dt)'''

# bài tập 3
# nhập bán kính R của đường tròn. in ra screen S của đường tròn đó
'''import math
R = float(input('nhập bán kính đường tròn = '))
# diện tích hình tròn
dt = R * math.pi
print('diện tích đường tròn là ', dt)'''

#phần chuỗi
# bài tập 1
# cho chuỗi s được nhập từ bàn phím, bạn hãy viết chương trình tạo ra 1 chuỗi nối 2 kí tự đầu và 2 kí tự cuối của chuỗi s và hiện thị ra màn hình
# nếu chuỗi s có độ dài < 2 thì hiện thị chuỗi rỗng
'''t = input('nhap chuoi s: ')
if len(t) > 2 :
    x = t[0:2] + t[-2:]
    print('chuoi moi la:', x)
if len(t) < 2 :
    print('chuoi rong')'''

# bài tập 2
'''nhập vào chuỗi s rồi đưa ra màn hình chuỗi s theo thứ tự đảo ngược'''
#cách 1
'''s = input('nhap chuoi s: ')
l = list(s) 
l.reverse() # hàm đảo ngược các kí tự có trong chuỗi s
x= "".join(l)
print('chuoi moi la:', x)'''
#cách 2
'''s = input('nhập s: ')
s1 = ""
for i in range (1, len(s)+1):
    s1 += s[-i]
print('chuỗi đảo ngược là:', s1)'''
# bài tập 3 
'''cho trước chuỗi s1 và s2 nhập từ bàn phím, hãy viết chương trình đổi chỗ 2 kí tự đầu tiên của s1 và s2 cho nhau. sau đó
hiện thị ra màn hình chuỗi mới có giá trị s1 + "" + s2'''
#cách 1
'''s1 = input('nhap chuoi s1: ')
s2 = input('nhap chuoi s2: ')
tmp = s1[0:2] + s2[2:]
tmp1 = s2[0:2] + s1[2:]
s3 = tmp
print('chuoi moi la:', tmp1 + "," + s3)'''
#cách 2
# s1 = input('nhap s1:')
# s2 = input('nhap s2:')
# x = s1.replace(s1[0:2],s2[0:2])
# y = s2.replace(s2[0:2],s1[0:2])
# print('chuỗi mới là:', x + y)

#bài tập 4 
'''nhập vào chuỗi s1, tạo chuỗi s2 gồm tất cả các chữ số có trong s1(giữ nguyên thứ tự xuất hiện của chúng) và đưa ra screen
số và chữ in thường/hoa trên mỗi hàng'''
# s1 = input('nhập s1: ')
# s2 = ""
# s3 = ""
# s4 = ""
# for i in s1 :
#     if i.isupper() == True :
#         s2 += i
#     if i.isnumeric() == True :
#         s3 += i
#     if i.islower() == True :
#         s4 += i
# print('chữ hoa:', s2, '\nsố:', s3, '\nchữ thường', s4)

#bài tập 5 
'''nhập vào 1 chuỗi s, in ra màn hình tần số xuất hiện của các kí tự trong s'''
#cách 1
# def ky_tu_khong_trung_lap(s):
#     xau_moi = ""
#     for ki_tu in s:
#         if ki_tu not in xau_moi:
#             xau_moi += ki_tu
#     return xau_moi

# def dem_ki_tu(s):
#     chuoi_ki_tu = ky_tu_khong_trung_lap(s)
#     for ki_tu in chuoi_ki_tu:
#         dem = s.count(ki_tu)
#         print("'{} lặp lại: {} lần, ".format(ki_tu, dem), end = '')

# s = input('nhap chuoi s: ')

# dem_ki_tu(s)
#cách 2
# s = input('nhập s: ')
# s1 = ""
# for i in s:
#     if i not in s1:
#         s1 += i
# for i in s1:
#     print(i, ':', s.count(i), 'lần') 
#bài tập 6
'''nhập vào xâu s, kiểm tra xem s có đối xứng không, biết s đối xứng khi đọc từ trái -> phải cũng giống như đọc từ phải sang trái '''
# s = input('nhap chuoi s: ')
# if s[::-1] == s :
#     print('chuoi s da nhap doi xung')
# else:
#     print('chuoi s da nhap khong doi xung')

#bài tập 7
'''nhập vào bàn phím xâu s, thực hiện thay thế các cụm kí tự anh bằng cụm kí tự em'''
# s = input('nhap chuoi s: ')
# while s.count('anh') != 0:
#     x = s.replace('anh', 'em')
#     print(x)
#     exit()
# bài tập 8
'''từ 1 chuỗi ko dấu cách. nhập vào xâu s. hãy đếm xem xâu s có bao nhiêu từ'''
# bài tập 9,10 để làm sau
#bài tập 11 
'''nhập chuỗi s nhập vào từ bàn phím, hãy viết chương trình đếm số
chữ in hoa/thường và chữ số, rồi in ra màn hình'''
# s = input('nhập s: ')
# dem = 0
# dem1 = 0 
# dem2 = 0 
# for i in s:
#     if i.islower() == True:
#         dem += 1
#     if i.isupper() == True:
#         dem1 += 1
#     if i.isnumeric() == True:
#         dem2 += 1
# print('số chữ thường xuất hiện:', dem,'lần', '\nsố chữ hoa xuất hiện: ', dem1,'lần', '\nsố xuất hiện:', dem2,'lần')





array = [1,2,3,4,5,6,7,8,9,10]
for i in range(len(array)-1, -1, -1):
    print(array[i])
