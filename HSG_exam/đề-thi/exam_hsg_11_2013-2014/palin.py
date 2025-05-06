def find_longest_palindrome_subarray(arr):
    """1.len_array = len(arr): Đoạn code này dùng để lấy độ dài của mảng arr và lưu vào biến n.
    
    2.max_len = 1: Biến max_len ban đầu được đặt là 1, đại diện cho độ dài chuỗi con đối xứng dài nhất tìm được.

    3.start = 0: Ban đầu, đặt start là 0, đại diện cho vị trí bắt đầu của chuỗi đối xứng dài nhất.

    4.Vòng lặp for: Duyệt qua từng phần tử trong mảng arr.

    5.Dưới vòng lặp for là vòng lặp while đầu tiên để tìm chuỗi đối xứng bắt đầu từ một số. Với mỗi index, chúng ta kiểm tra các số ở vị trí index - 1 và index + 1, nếu chúng đối xứng ta mở rộng chuỗi con đối xứng đó.

    6.Vòng lặp while thứ hai dùng để tìm chuỗi đối xứng bắt đầu từ một cặp số giống nhau, tức là mở rộng chuỗi con đối xứng từ vị trí index và index + 1.

    7.Trong cả hai vòng lặp while, ta kiểm tra nếu độ dài chuỗi con đối xứng lớn hơn max_len, ta cập nhật max_len và start.

    8.Cuối cùng, trả về mảng con đối xứng dài nhất từ vị trí start đến start + max_len."""

    len_array = len(arr)
    max_len = 1
    start = 0

    for index in range(len_array):
        # Tìm dãy đối xứng bắt đầu từ một số
        low = index - 1
        high = index + 1
        
        while low >= 0 and high < len_array and arr[low] == arr[high]:
            
            if high - low + 1 > max_len:
                start = low
                max_len = high - low + 1
                # print(start,low, high, max_len)
                
            low -= 1
            high += 1

        # Tìm dãy đối xứng bắt đầu từ một cặp số giống nhau
        low = index
        high = index + 1
        
        while low >= 0 and high < len_array and arr[low] == arr[high]:
            
            if high - low + 1 > max_len:
                start = low
                max_len = high - low + 1
                # print(start,low, high, max_len)

            low -= 1
            high += 1

        # print(arr[start:start + max_len])
        tmp = " ".join(str(x) for x in arr[start:start + max_len])
    return str(len(arr[start:start + max_len])) + "\n" +  tmp

# print(find_longest_palindrome_subarray([2,  3,  4,  5,  4,  3,  1,  7]))

with open('./exam_hsg_11_2013-2014/PALIN.INP', 'r') as file:
    num = int(file.readline())
    list_find = [int(x) for x in file.read() if x != " "]
    

with open('./exam_hsg_11_2013-2014/PALIN.OUT', 'w') as file:

    print(find_longest_palindrome_subarray(list_find), file=file)