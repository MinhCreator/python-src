

# Way 1 before optimizing performance code run time
def calculate_distance_way1(commands):
    x = 0
    y = 0

    for command in commands:
        if command == 'W':
            y += 1  # Di chuyển về phía tây
        elif command == 'S':
            y -= 1  # Di chuyển về phía nam
        elif command == 'E':
            x += 1  # Di chuyển về phía đông
        elif command == 'N':
            x -= 1  # Di chuyển về phía bắc

    distance = ((x - 0) ** 2 + (y - 0) ** 2) ** 0.5
    return round(distance, 2)


# Way 2 after optimizing performance code run time
def calculate_distance(commands):

    # Bắc, Nam, Đông, Tây
    coordinates = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}
    x, y = 0, 0

    for command in commands:
        dx, dy = coordinates[command]
        x += dx
        y += dy
    distance = ((x - 0) ** 2 + (y - 0) ** 2) ** 0.5
    return round(distance, 2)

# Đọc dữ liệu từ file input
with open('Distance.inp', 'r') as f:
    commands = f.read().strip()

# Tính toán khoảng cách và ghi kết quả vào file output
distance = calculate_distance(commands)
with open('Distance.out', 'w') as f:
    print(distance, file=f)



