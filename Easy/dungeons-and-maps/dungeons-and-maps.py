import sys
import math


w, h = [int(i) for i in input().split()]
start_row, start_col = [int(i) for i in input().split()]
results = []
n = int(input())
for i in range(n):
    currentMap=[list(input())for j in range(h)]

    currentX=start_col
    currentY=start_row
    length = 0
    roundCount = 0
    while currentMap[currentY][currentX]!="T" and currentMap[currentY][currentX]!=".":
        
        if currentMap[currentY][currentX]=="^":
            currentY -= 1
            length += 1
        elif currentMap[currentY][currentX]=="v":
            currentY += 1
            length += 1
        elif currentMap[currentY][currentX]=="<":
            currentX -= 1
            length += 1
        elif currentMap[currentY][currentX]==">":
            currentX += 1
            length += 1
        
        if currentX == start_col and currentY == start_row:
            roundCount += 1
            
        if roundCount > 0 or currentX >= w or currentY >=h:
            results.append([i, 999999999999])
            break

        if not currentMap[currentY][currentX] in '^v<>':
            if currentMap[currentY][currentX]!="T":
                length = 999999999999
            results.append([i, length])

if all([result[1]==999999999999 for result in results]):
    print("TRAP")
else:
    results.sort(key = lambda result: result[1])
    print(results[0][0])
