import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = str(int(input())+1)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
found = False
while not found:
    isOk = True
    for i in range(1,len(n)):
        if n[i] < n[i-1]:
            n = (n[:i] + n[i-1]).ljust(len(n), "0")
            isOk = False
            break
    if isOk:
        found = True
        print(n)
         
