import math
import os
import time

A, B, C = 0.0, 0.0, 0.0

cubeWidth = 20
width, height = 160, 44
zBuffer = [0.0] * (width * height)
buffer = [' '] * (width * height)
backgroundASCIICode = '.'
distanceFromCam = 100
horizontalOffset = 0
K1 = 40

incrementSpeed = 0.6

def calculateX(i, j, k):
    return (j * math.sin(A) * math.sin(B) * math.cos(C) - k * math.cos(A) * math.sin(B) * math.cos(C) +
            j * math.cos(A) * math.sin(C) + k * math.sin(A) * math.sin(C) + i * math.cos(B) * math.cos(C))

def calculateY(i, j, k):
    return (j * math.cos(A) * math.cos(C) + k * math.sin(A) * math.cos(C) -
            j * math.sin(A) * math.sin(B) * math.sin(C) + k * math.cos(A) * math.sin(B) * math.sin(C) -
            i * math.cos(B) * math.sin(C))

def calculateZ(i, j, k):
    return k * math.cos(A) * math.cos(B) - j * math.sin(A) * math.cos(B) + i * math.sin(B)

def calculateForSurface(cubeX, cubeY, cubeZ, ch):
    global horizontalOffset, K1, distanceFromCam, width, height, zBuffer, buffer
    x = calculateX(cubeX, cubeY, cubeZ)
    y = calculateY(cubeX, cubeY, cubeZ)
    z = calculateZ(cubeX, cubeY, cubeZ) + distanceFromCam

    ooz = 1 / z

    xp = int(width / 2 + horizontalOffset + K1 * ooz * x * 2)
    yp = int(height / 2 + K1 * ooz * y)

    idx = xp + yp * width
    if 0 <= idx < width * height:
        if ooz > zBuffer[idx]:
            zBuffer[idx] = ooz
            buffer[idx] = ch

def main():
    global A, B, C, cubeWidth, horizontalOffset, incrementSpeed, width, height, buffer, zBuffer, backgroundASCIICode
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        buffer = [backgroundASCIICode] * (width * height)
        zBuffer = [0.0] * (width * height)
        cubeWidth = 20
        horizontalOffset = -2 * cubeWidth
        # first cube
        for cubeX in range(int(-cubeWidth / incrementSpeed), int(cubeWidth / incrementSpeed)):
            for cubeY in range(int(-cubeWidth / incrementSpeed), int(cubeWidth / incrementSpeed)):
                calculateForSurface(cubeX * incrementSpeed, cubeY * incrementSpeed, -cubeWidth, '@')
                calculateForSurface(cubeWidth, cubeY * incrementSpeed, cubeX * incrementSpeed, '$')
                calculateForSurface(-cubeWidth, cubeY * incrementSpeed, -cubeX * incrementSpeed, '~')
                calculateForSurface(-cubeX * incrementSpeed, cubeY * incrementSpeed, cubeWidth, '#')
                calculateForSurface(cubeX * incrementSpeed, -cubeWidth, -cubeY * incrementSpeed, ';')
                calculateForSurface(cubeX * incrementSpeed, cubeWidth, cubeY * incrementSpeed, '+')

        cubeWidth = 10
        horizontalOffset = 1 * cubeWidth
        # second cube
        for cubeX in range(int(-cubeWidth / incrementSpeed), int(cubeWidth / incrementSpeed)):
            for cubeY in range(int(-cubeWidth / incrementSpeed), int(cubeWidth / incrementSpeed)):
                calculateForSurface(cubeX * incrementSpeed, cubeY * incrementSpeed, -cubeWidth, '@')
                calculateForSurface(cubeWidth, cubeY * incrementSpeed, cubeX * incrementSpeed, '$')
                calculateForSurface(-cubeWidth, cubeY * incrementSpeed, -cubeX * incrementSpeed, '~')
                calculateForSurface(-cubeX * incrementSpeed, cubeY * incrementSpeed, cubeWidth, '#')
                calculateForSurface(cubeX * incrementSpeed, -cubeWidth, -cubeY * incrementSpeed, ';')
                calculateForSurface(cubeX * incrementSpeed, cubeWidth, cubeY * incrementSpeed, '+')

        cubeWidth = 5
        horizontalOffset = 8 * cubeWidth
        # third cube
        for cubeX in range(int(-cubeWidth / incrementSpeed), int(cubeWidth / incrementSpeed)):
            for cubeY in range(int(-cubeWidth / incrementSpeed), int(cubeWidth / incrementSpeed)):
                calculateForSurface(cubeX * incrementSpeed, cubeY * incrementSpeed, -cubeWidth, '@')
                calculateForSurface(cubeWidth, cubeY * incrementSpeed, cubeX * incrementSpeed, '$')
                calculateForSurface(-cubeWidth, cubeY * incrementSpeed, -cubeX * incrementSpeed, '~')
                calculateForSurface(-cubeX * incrementSpeed, cubeY * incrementSpeed, cubeWidth, '#')
                calculateForSurface(cubeX * incrementSpeed, -cubeWidth, -cubeY * incrementSpeed, ';')
                calculateForSurface(cubeX * incrementSpeed, cubeWidth, cubeY * incrementSpeed, '+')

        os.system('cls' if os.name == 'nt' else 'clear')
        for k in range(width * height):
            print(buffer[k] if k % width else '\n', end='')

        A += 0.05
        B += 0.05
        C += 0.01
        time.sleep(0.008)

if __name__ == "__main__":
    main()

