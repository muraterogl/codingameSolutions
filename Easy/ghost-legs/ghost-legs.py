import sys
import math

w, h = [int(i) for i in input().split()]
roads = []

for i in range(h):
    line = input()
    roads.append(line)

alps = roads[0].split()
dests = roads[-1].split()

for a in alps:
    cIndex = roads[0].split().index(a)
    for i in range(1,len(roads)-1):
        cr = roads[i].split("|")[1:-1]
        #print(cr)
        if cIndex == 0:
            if cr[0]=="--":
                cIndex+=1
        elif cIndex == len(alps)-1:
            if cr[-1]=="--":
                cIndex-=1
        else:
            if cr[cIndex-1]=="--":
                cIndex -=1
            elif cr[cIndex]=="--":
                cIndex+=1
    print(a+dests[cIndex])
 
