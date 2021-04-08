import sys
import math
import re

asteroids1 = {}
asteroids2 = {}
asteroids3 = {}

w, h, t1, t2, t3 = [int(i) for i in input().split()]
for i in range(h):
    first_row, second_row = input().split()
    for ast in re.findall(r"[A-Z]",first_row):
        asteroids1[ast] = (i, first_row.find(ast))
    for ast in re.findall(r"[A-Z]",second_row):
        asteroids2[ast] = (i, second_row.find(ast))

for ast in asteroids1:
    dy = (asteroids2[ast][0] - asteroids1[ast][0]) / (t2 - t1)
    dx = (asteroids2[ast][1] - asteroids1[ast][1]) / (t2 - t1)
    y3 = math.floor((t3 - t1) * dy + asteroids1[ast][0])
    x3 = math.floor((t3 - t1) * dx + asteroids1[ast][1])
    asteroids3[ast] = (y3, x3)

sky = [["."]*w for i in range(h)]

for ast in sorted(asteroids3.keys(), reverse=True):
    y, x = asteroids3[ast]
    if 0 <= y < h and 0 <= x < w:
        sky[y][x] = ast

for row in sky:
    print("".join(row))