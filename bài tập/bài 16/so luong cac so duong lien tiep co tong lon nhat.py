def sl_so_duong_lien_tiep_co_tong_lon_nhat(lst):

    Max_sum_sl = 0
    sl_sum_hientai = 0
    Max_sum = 0
    hien_tai_sum = 0


    for num in lst:

        if num > 0:
            hien_tai_sum += 1
            sl_sum_hientai += 1

        else:
            hien_tai_sum = 0
            sl_sum_hientai = 0
        
        if hien_tai_sum > Max_sum_sl:
            Max_sum_sl = hien_tai_sum
            Max_sum = hien_tai_sum
        return Max_sum_sl

lst = []