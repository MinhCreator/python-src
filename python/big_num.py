def big_num(s: str, k: int) -> str:
    from re import findall

    save = []
    fill = findall(r"\d", s)

    if len(fill) < k:
        return "INVALID"

    else:
        sl_del = len(fill) - k

        for i in range(1, len(fill)):
            while sl_del > 0 and save != [] and save[-1] < fill[i]:
                sl_del -= 1
                del save[-1]

            save.append(fill[i])
        save = "".join(save[: k + 1])

    return save


print(big_num("A79C3e8", 2))
print(big_num("Tinhoc95Tre68nam2023", 3))
