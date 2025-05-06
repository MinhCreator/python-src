
def find_consecutive_overlapping_segments(N, segments):
    max_len = 0
    tmp = sorted(list, key=lambda x: (x[1],x[0]))
    index_segment = [i + 1 for i in range(len(segments))]
    for y in range(len(tmp) + 1):
        for t in range(len(segments[y])):

            if segments[y - 1][1] == segments[y][0]:
                max_len += 1
                
           
    return max_len

with open('./exam_hsg_11_2013-2014/LINES.INP', 'r') as file:
    num = int(file.readline())
    list = [list(map(int, line.split())) for line in file.readlines()]
    print(find_consecutive_overlapping_segments(num, list))    
    print(sorted(list, key=lambda x: (x[1],x[0])))

with open('./exam_hsg_11_2013-2014/LINES.OUT', 'w') as file:
    pass

