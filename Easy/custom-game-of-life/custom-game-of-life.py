import sys
import math

h, w, n = [int(i) for i in input().split()]
alive = input()
dead = input()
cells = [list(input())for i in range(h)]

for _ in range(n):
    newCells = []
    for i in range(h):
        newRow = []
        for j in range(w):
            currentCell = cells[i][j]
            neighborCount = 0
            for k in range(max(0, i-1), min(h, i+2)):
                for l in range(max(0, j-1), min(w, j+2)):
                    neighborCount += cells[k][l] == "O"
            if currentCell == "O":
                neighborCount -= 1
                if alive[neighborCount]=="0":
                    currentCell = "."
            else:
                if dead[neighborCount]=="1":
                    currentCell = "O"
            newRow.append(currentCell)
        newCells.append(newRow)
    cells = newCells

for cell in cells:
    print("".join(cell))
