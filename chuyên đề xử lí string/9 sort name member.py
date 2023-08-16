
def sort_list_name(lst_full_name: list) -> list:  # function sort name

    return sorted(lst_full_name, key=lambda x: (x.split(" ")[-1], x.split(" ")[0], x.split(" ")[1:len(x) - 2]))


def input_name(num: int) -> list:  # function input name

    lst_full_name = []

    for index in range(num):

        mem = input(f"enter student {index + 1} name: ")

        lst_full_name.append(mem)

    return sort_list_name(lst_full_name)


lst_name = [
    "Nguyễn Thị Thùy Dung",
    "Phạm Thị Thùy Dung",
    "Mai Ánh Dương",
    "Dương Thị Hương Giang",
    "Nguyễn Thị Hải",
    "Nguyễn Thị Mỹ Hạnh",
    "Phạm Thị Thu Hoài",
    "Võ Ngọc Hoài",
    "Đỗ Thị Thanh Huế",
    "Nguyễn Thị Thu Huyền",
    "Tưởng Thị Thu Huyền",
    "Lê Thị Lan Hương",
    "Dương Thị Hoài Linh",
    "Nguyễn Chiêu Linh",
    "Nguyễn Thị Kim Loan",
    "Trịnh Thị Xuân Lộc",
    "Từ Thảo Mai",
    "Bùi Uyển My",
    "Cao Thị Trà My",
    "Lê Nguyễn Trà My",
    "Trình Thị Trà My",
    "Trần Thị Lan Phương",
    "Hồ Đỗ Tài",
    "Nguyễn Thị Thanh",
    "Hồ Huyền Trang",
    "Dương Thị Kiều Trâm",
    "Nguyễn Hoàng Mai Trinh",]

print(input_name(3))
