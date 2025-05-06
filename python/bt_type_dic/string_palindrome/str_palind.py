def palind(left: int , right: int, strs: str):

    tmp = 1

    if right - left == 3:

        if strs[left + 1] == strs[right - 1]: tmp = 2
       
        else: return 1

    while strs[left] == strs[right] and left >= 1 and right <= len(strs) - 1:

        left -= 1

        right += 1

        tmp += 2   

    return tmp

strs = "Fhjabgthettiyryittehtgbayutuyioe"
# strs = "atta"

strs = "0" + strs
ans = 1

for i in range(1, len(strs) - 1):
    ans = max(ans, palind(i - 1, i + 1, strs))

    # if i + 2 <= len(strs) - 1:
    ans = max(ans, palind(i - 1, i + 2, strs))
print(ans)
# strs = "abgthettiyryittehtgba"
# print(True if strs == strs[::-1] else False)
