import sys
import math

speed = int(input())
light_count = int(input())
lights = [[*map(int,input().split())]for i in range(light_count)]

while True:
    currentSpeed = speed
    for distance, duration in lights:
        timeToArrive = 3.6 * distance/speed
        if (timeToArrive / duration) % 2 >= 1:
            speed-=1
            break
    if currentSpeed == speed:
        break
print(speed)