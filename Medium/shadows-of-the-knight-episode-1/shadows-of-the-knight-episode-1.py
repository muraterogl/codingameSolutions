import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]

ld, rd, lu, ru = [0,h], [w,h], [0,0], [w,0] 

# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

    if bomb_dir == "U":
        ld = [x0, y0]
        rd = [x0, y0]
        lu[0] = x0
        ru[0] = x0
        y0 = y0 - math.ceil((y0 - lu[1]) / 2)
    elif bomb_dir == "UR":
        ld = [x0, y0]
        rd[1] = y0
        lu[0] = x0
        ru = ru
        x0 = x0 + math.ceil((ru[0] - x0) / 2)
        y0 = y0 - math.ceil((y0 - ru[1]) / 2)
    elif bomb_dir == "R":
        ld = [x0, y0]
        rd[1] = y0
        lu = [x0, y0]
        ru[1] = y0
        x0 = x0 + math.ceil((ru[0] - x0) / 2)
    elif bomb_dir == "DR":
        ld[0] = x0
        rd = rd
        lu = [x0, y0]
        ru[1] = y0
        x0 = x0 + math.ceil((rd[0] - x0) / 2)
        y0 = y0 + math.ceil((rd[1] - y0) / 2)
    elif bomb_dir == "D":
        ld[0] = x0
        rd[0] = x0
        lu = [x0, y0]
        ru = [x0, y0]
        y0 = y0 + math.ceil((ld[1] - y0) / 2)
    elif bomb_dir == "DL":
        ld = ld
        rd[0] = x0
        lu[1] = y0
        ru = [x0, y0]
        x0 = x0 - math.ceil((x0 - ld[0]) / 2)
        y0 = y0 + math.ceil((ld[1] - y0) / 2)
    elif bomb_dir == "L":
        ld[1] = y0
        rd = [x0, y0]
        lu[1] = y0
        ru = [x0, y0]
        x0 = x0 - math.ceil((x0 - ld[0]) / 2)
    elif bomb_dir == "UL":
        ld[1] = y0
        rd = [x0, y0]
        lu = lu
        ru[0] = x0
        x0 = x0 - math.ceil((x0 - lu[0]) / 2)
        y0 = y0 - math.ceil((y0 - lu[1]) / 2)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)


    # the location of the next window Batman should jump to.
    print(str(x0) + " " + str(y0))
 
