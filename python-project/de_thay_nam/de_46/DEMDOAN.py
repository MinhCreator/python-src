def count_subarray(arr, m):
    count = 0
    sum_lst = 0
    j = 0
    
    for i in range(len(arr)):
        
        while j < len(arr) and sum_lst + arr[j] <= m:
            
            sum_lst += arr[j]
            j += 1

        count += len(arr) - j
        sum_lst -= arr[i]
    
    return count


print(count_subarray([1, 5, 2, 5], 4))

