def trace_num():
   
    out_put = open('./trace_sum/output.out', 'w')

    with open('./trace_sum/input.inp', 'r') as file:

        n, q = map(int, file.readline().split())
        
        lst = list(map(int, file.readline().split()))
        
        lst = [0] + lst
        f = [0] * (len(lst) + 1)
        
        for i in range(1, len(lst)):

                f[i] = f[i - 1] + lst[i]

        for trace in range(0, q):

            a, b = map(int, file.readline().split())
            
            print(f[b] - f[a - 1], file=out_put)


print(trace_num())






    