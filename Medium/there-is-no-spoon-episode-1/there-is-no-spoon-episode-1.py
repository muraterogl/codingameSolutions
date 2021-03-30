import sys
import math


width = int(input())
height = int(input())
nodes = []

for i in range(height):
    line = input()
    nodes += [[*line]]

for i in range(height):
    for j in range(width):
        if nodes[i][j] == "0":
            output = [j, i]

            rightNotFound = True
            for k in range(j+1,width):
                if nodes[i][k] == "0":
                    rightNotFound = False
                    output += [k, i]
                    break
            if rightNotFound:
                output += [-1, -1]


            bottomNotFound = True
            for k in range(i+1,height):
                if nodes[k][j] == "0":
                    bottomNotFound = False
                    output += [j, k]
                    break
            if bottomNotFound:
                output += [-1, -1]
            
            print(*output)
