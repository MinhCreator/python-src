def find_pass(date: int, month: int, list: list):

    increase = 0
    for num in list:

        if num % date == 0 or num % month == 0:

            increase += 1

    return increase


lists = [16, 40, 15, 76, 80]
date = 3
month = 10
print(find_pass(date, month, lists))



