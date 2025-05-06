# độ đo

def do_do(string1, string2):
    str1 = string1
    str2 = string2

    mark_1 = [0] * 123
    mark_2 = [0] * 123

    for x in str1:
        mark_1[ord(x)] += 1
    for x in str2:
        mark_2[ord(x)] += 1


    ans = 0

    for x in range(97, 123):
        ans += abs(mark_1[x] - mark_2[x])

    return ans

print(do_do(input(), input()))