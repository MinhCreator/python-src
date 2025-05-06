def difference(lst_book: list, bn: int) -> int:

    d_save = []    

    for tmp in range(len(lst_book)):

        for i in range(len(lst_book)):

            if lst_book[tmp] < lst_book[i]:

                d_save.append(lst_book[i] - lst_book[tmp])
            else: 
                d_save.append(lst_book[tmp] - lst_book[i])
    
    return set(d_save)
#    return max(lst_book) - min(lst_book)

lst = [4, 7, 2, 9, 3]

print(difference(lst, 3))