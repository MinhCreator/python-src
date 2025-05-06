def _height_(lst: list) -> list[int]:
    store = []
    sum = 0
    for num in lst:

        for letter in num :
            sum += int(letter)

        store.append(sum)
        sum = 0

    return store

print(_height_(["247", '5', '32000', '334', '27']))