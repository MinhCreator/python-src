
def so_duong_lien_tiep(lst):
    
    Max_soluong = 0
    
    so_hientai = 0
    
    for num in lst:
        if num > 0:
            so_hientai += 1
            
        else:
            so_hientai = 0
        
        if so_hientai > Max_soluong:
            Max_soluong = so_hientai
    
    return Max_soluong


lst = [ 1
    ,4
    ,-2
    ,3
    ,-8
    ,5
    ,9
    ,2
]
print(so_duong_lien_tiep(lst))
        