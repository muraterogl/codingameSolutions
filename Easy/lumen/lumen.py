import sys
import math

n = int(input())
l = int(input())

cells = []
candles = []

for i in range(n):
    row = input().split()
    rowHold = []
    for j in range(len(row)):
        if row[j] == "C": candles.append((j,i))
        rowHold.append(0)
    cells.append(rowHold)

for candle in candles:
    for i in range(n):
        for j in range(n):
            cells[j][i] = max(cells[j][i], max(0,l - max(abs(candle[0]-j), abs(candle[1]-i))))


darkCount = 0

for i in range(n):
    for j in range(n):
        if cells[j][i] == 0:
            darkCount += 1

print(darkCount) 
