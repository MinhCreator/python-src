
def _sort_increase_(lst):
    lst.sort()
    return lst

def _sort_decrease_(lst):
    lst.sort(reverse=True)
    return lst

list = [7,4,8,3,2,1]
print(_sort_increase_(list))
print(_sort_decrease_(list))