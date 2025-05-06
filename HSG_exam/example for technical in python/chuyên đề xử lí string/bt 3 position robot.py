# Way 2: after optimizing performance code run time
'''bài của tôi'''
def calculate_distance(commands: str) -> float:
    # Define a dictionary to map each command to its corresponding coordinates
    # Bắc, Nam, Đông, Tây
    coordinates = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}

    # Initialize the starting point coordinates
    x, y = 0, 0

    # Iterate through each command in the input string
    for command in commands:
        # Get the change in x and y coordinates for the current command
        dx, dy = coordinates[command] 

        # Update the current x and y coordinates by adding the change in coordinates
        x += dx
        y += dy
        print("toa độ X: ",x, "toa độ Y: ", y)
    # Calculate the Euclidean distance from the starting point to the final position
    # công thức tính khoảng cách Euclid giữa điểm hiện tại và điểm xuất phát (0, 0) trong hệ tọa độ 2D
    # công thức Pythagoras
    distance = ((x - 0) ** 2 + (y - 0) ** 2) ** 0.5 # mũ 0.5 tương ứng = mũ 1/2

    # Round the distance to 2 decimal places and return it
    return round(distance, 2)
    

'''bài của cô'''

def distances(commands: str) -> float:
    
    x, y = 0, 0

    for command in commands:

        if command == 'N':
            y += 1
        elif command == 'S':
            y -= 1
        elif command == 'E':
            x += 1
        elif command == 'W':
            x -= 1
        
    return round((x ** 2 + y ** 2) ** 0.5, 2)
    


# Đọc dữ liệu từ file input
with open('./chuyên đề xử lí string/Distance.inp', 'r') as files:
    commands = files.read().strip()

# Tính toán khoảng cách và ghi kết quả vào file output
distance = calculate_distance(commands)
with open('./chuyên đề xử lí string/Distance.out', 'w') as files:
    print(distance, file=files)



