def find_all_occurrences(main_string, sub_string):
    indices = []
    index = -1

    while True:
        index = main_string.find(sub_string, index + 1)
        if index == -1:
            break
        indices += [str(index + 1)]

    return " ".join(indices)

print(find_all_occurrences("abababab", "ab"))



def next_num(A: str) -> str:

    digits = [int(d) for d in str(A)]  # Chuyển số A thành một danh sách các chữ số
    # sorted_digits = sorted(digits)  # Sắp xếp danh sách các chữ số theo thứ tự tăng dần

    for i in range(0,len(digits), -1):
        if digits[i] < digits[i - 1]:  # Tìm chữ số đầu tiên lớn hơn chữ số đầu tiên của A
            digits[i], digits[i - 1] = digits[i - 1], digits[i]  # Hoán đổi chữ số đó với chữ số đầu tiên của B
            break

    digits[1:] = sorted(digits[1:])  # Sắp xếp lại danh sách các chữ số của B từ vị trí thứ hai trở đi

    B = int(''.join(map(str, digits)))  # Ghép các chữ số trong danh sách của B thành một số nguyên

    return B, digits

print(next_num("526431"))





