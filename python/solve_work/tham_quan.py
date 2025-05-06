
def extract_data(path : str):
    
    with open(path, 'r') as f :

        n, m = map(int, f.readline().split())

        d = [int(f.readline().strip()) for _ in range(1, n + 1)]

        v = [int(f.readline().strip()) for _ in range(1, m + 1)]

    return n , m, sorted(d), sorted(v)


def tham_quan(doan: int, 
              xe : int, 
              khoang_cach: list[int], 
              fuel: list[int]
              )-> int:

    n = doan
    m = xe
    d = [0] + khoang_cach
    v = [0] + fuel

    dv = [0] * 30000
    # ans = 0
    
    for i in range(1, n + 1):
        
        for j in range(1, m + 1):

            dv[j - i] += d[i] * v[j]
        # mins = max(pre_min, mins)
            # print(i, j, dv[j - i],d[i] * v[j] )
        # pre_min = 0
    
    return dv[j - i]


def tham_quan2(n: int, m: int, d: list[int], v: list[int]) -> int:

    l = 0
    ans = 0
    for i in range(n - 1, - 1, -1):
        ans += d[i] * v[l]
        l += 1

    return ans


path = "./tham_quan.inp"
n, m, d, v = extract_data(path)
# print(d, v)
print(tham_quan2(n, m, d, v))
print(tham_quan(n, m, d, v))

