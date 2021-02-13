import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
def distance(uLo, uLa, Lo, La):
    uLa = float(uLa.replace(',','.'))*math.pi/180
    uLo = float(uLo.replace(',','.'))*math.pi/180
    La = float(La.replace(',','.'))*math.pi/180
    Lo = float(Lo.replace(',','.'))*math.pi/180
    x = (Lo - uLo)*math.cos((uLa + La)/2)
    y = La - uLa
    return math.sqrt(x**2+y**2)*6371

lon = input()
lat = input()
n = int(input())
dis = []
defibs = []
for i in range(n):
    defib = input().split(';')
    dis.append(distance(lon,lat,defib[-2], defib[-1]))
    defibs.append(defib)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(defibs[dis.index(min(dis))][1])
 
