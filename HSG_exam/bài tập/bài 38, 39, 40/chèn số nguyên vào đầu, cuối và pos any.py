def _end_insert_(list,a):
    list.append(a)
    return list

def _start_insert_(list,a):
    list.insert(0,a)
    return list

def _insert_any_(list,a,pos):
    list.insert(pos,a)
    return list
    
M_any = int(input('nhập m : '))
pos = int(input('nhập vị trí k : '))
test = [32,34,35,36,37,38,39]
print(_end_insert_(test,M_any))
print(_start_insert_(test,M_any))
print(_insert_any_(test,M_any,pos))