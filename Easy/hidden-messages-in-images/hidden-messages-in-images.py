import sys
import math

w, h = [int(i) for i in input().split()]
extracted = ""
for i in range(h):
    for j in input().split():
        pixel = int(j)
        extracted += bin(pixel)[-1]

while len(extracted)%8 !=0: extracted = "0" + extracted

result = ""

for i in range(0,len(extracted),8):
    result += chr(int(extracted[i:i+8],2))

print(result)
