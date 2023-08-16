# bài này áp dụng cho cả số trùng nhau 
# bằng cách thêm set(map(int, lst)) -> sẽ bỏ đi cách số lặp lại trong list
# có thể use cho file 
def _mark_(lst):
    n = len(lst)
    list_mark = [False] * 1000000
    
    for num in lst:
        list_mark[num] = True
        
    for i in range(1,1000000):
        if not list_mark[i]:
            return i
        
    
    return n + 2


lst =[ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20]
kc = _mark_(lst)
print(kc)
