with open('./de_thay_nam/de_57/TAPCON.INP', 'r') as file:
    number = int(file.readline())
    list_data = list(map(str, file.read().split()))

with open('./de_thay_nam/de_57/TAPCON.OUT', 'w') as file:
    re_dup = " ".join(sorted(list(set(list_data))))
    print(re_dup)
    lens = len(list(set(list_data)))
    print(f"{lens}\n{re_dup}", file=file)