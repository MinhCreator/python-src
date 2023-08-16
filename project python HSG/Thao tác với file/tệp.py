# file = open('filedoc.txt')
# t_read = file.read()
# lst_tmp = t_read.split()
# n_lst = list(map(int, lst_tmp))
# tmp = 0 
# for i in n_lst :
#     tmp += i 
# create_new_file = open('file after procces.txt', 'w')
# tmp2 = create_new_file.write(str(tmp))
# file.close()
# create_new_file.close()

#BT 2: CHO DÃY SỐ INT GỒM N PHẦN TỪ (N < 1000). EM HÃY TÍNH VÀ XUẤT RA MÀN HÌNH TỔNG CỦA
#5 PHẦN TỬ CÓ GTLN TRONG DÃY 
doc = open('filesapxep.inp')
nhan = int(doc.readline())
tmp = doc.read()
lst = tmp.split()
lst_int = list(map(int,lst))
lst_int.sort()
plus = 0
for i in range(nhan - 5, nhan):
     plus += lst_int[i]
tao_moi = open('filesapxep2.out', 'w')
tao_moi.write(str(plus))
doc.close()
tao_moi.close()





