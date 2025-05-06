def del_symble(string: str):

    length = len(string)
    matrix = [[0] * length for _ in range(length)]

    for indx in range(length):
        matrix[indx][indx] = 0

    for indx in range(length - 1):
        if string[indx] == string[indx + 1]:
            matrix[indx][indx + 1] = 0

        else: matrix[indx][indx + 1] = 1

    for long in range(3 , length + 1):

        for indx in range(length - long + 1):
            jndx = indx + long - 1

            if string[indx] == string[jndx]:
                matrix[indx][jndx] = matrix[indx + 1][jndx - 1]
                 
            else: matrix[indx][jndx] = 1 + min(matrix[indx + 1][jndx], matrix[indx][jndx - 1])


    return matrix[0][length - 1]

print(del_symble("abcdabcdef"))