def mark_cut_tree(n : int, tree: list[int], k : int):
    
    re = n
    tree = [0] + tree

    height = tree[1]

    for i in range(1, 1001):
        trees = i
        count = 0

        if trees != tree[1]: count += 1

        for j in range(2 , n + 1):
            trees += k
            
            if trees != tree[j]:
                count += 1

        if count < re :
            re = count
            height = i

    print(re)

    for i in range(1, n + 1):

            if tree[i] > height :
               print ("-", i, tree[i] - height)

            else:
                if tree[i] < height:
                    print ("+", i, height - tree[i])
            height += k
    return 0
    
print(mark_cut_tree(4, [1, 2, 1, 5], 1))

            
