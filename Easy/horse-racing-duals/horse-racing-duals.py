import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
result = 99999
pis = []
for i in range(n):
    pi = int(input())
    pis.append(pi)
pis.sort()
for i in range(len(pis)):
    if abs(pis[i]-pis[i-1]) < result: result = abs(pis[i]-pis[i-1])

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(result)
 
