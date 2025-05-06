def noodle(opens , closes):

    files = opens
    n_thia, m_dua, k_khach = map(int, files.readline().split())

    time_t = [0] * (10**5)
    time_d = [0] * (10**5)
    last_t = 0

    for _ in range(k_khach):
        t_den, d_t_di, a_mon = map(int,files.readline().split())

        for j in range(last_t, t_den + 1):
            n_thia += time_t[j]
            time_t[j] = 0
            m_dua += time_d[j]
            time_d[j] = 0
            
        if a_mon == 0:
            if n_thia > 0:
                n_thia -= 1
                time_t[t_den + d_t_di] += 1
                time_d[t_den + d_t_di] += 1
                print("Yes", file=closes)
            
            else:
                print("No", file=closes)
        
        else:
        
            if n_thia > 0 and m_dua > 0:
                n_thia -= 1
                m_dua -= 1
                time_t[t_den + d_t_di] += 1
                time_d[t_den + d_t_di] += 1
                print("Yes", file=closes)
        
            else:
                print("No", file=closes)

        last_t = t_den


opens = open("./chao_va_pho.inp", "r")
closes = open("./chao_va_pho.out", "w")
noodle(opens, closes)
