

def plus(a: str, b: str) -> str:

    max_length = max(len(a), len(b))

    a = a.zfill(max_length)
    b = b.zfill(max_length)

    memory = 0
    result_plus = ""

    for value in range(max_length - 1, - 1, -1):

        results = int(a[value]) + int(b[value]) + memory
        memory = results // 10
        result_plus = str(results % 10) + result_plus

    if memory != 0:
        result_plus = str(memory) + result_plus

    return result_plus

# print(plus('123', '456'))


def minus(a: str, b: str) -> str:

    max_length = max(len(a), len(b))

    a = a.zfill(max_length)
    b = b.zfill(max_length)

    lent = 0
    result_minus = ""

    for value in range(max_length - 1, - 1, -1):

        results = int(a[value]) - int(b[value]) - lent

        if results < 0:
            results += 10
            lent = 1
        else:
            lent = 0

        result_minus = str(results) + result_minus

    result_minus = result_minus.lstrip("0")

    if not result_minus:
        result_minus = "0"

    return result_minus


# print(minus('789', '456'))

# multiply for larger number to smaller number
def multiply(a: str, b: str) -> str:

    if b == "0":
        return "0"

    tich = 0
    re = "0"
    b = int(b)

    for value in reversed(a):

        tich = int(value) * b
        re = plus(re, str(tich))
        b *= 10

    return re

# print(multiply('5', '100'))


# multiply for larger number to larger number

def multiply2(a: str, b: str) -> str:

    if a == "0" or b == "0":
        return "0"

    tra_ve = "0"
    b = b[::-1]

    for index, value in enumerate(b):

        compute = multiply(a, value) + "0" * index
        tra_ve = plus(tra_ve, compute)

    return tra_ve

# print(multiply2("725", "125"))

# chia số lớn vs số lớn, chia số lớn vs số nhỏ


def divide(so_chia, so_bi_chia):

    thuong = ""
    du = 0

    for value in so_chia:

        value_so = int(value)

        tmp = du * 10 + value_so

        thuong_tmp = tmp // int(so_bi_chia)

        du = tmp % int(so_bi_chia)

        thuong += str(thuong_tmp)

    return thuong.lstrip("0"), str(du)


print(divide("123", "92"))
