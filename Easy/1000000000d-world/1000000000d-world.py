import sys
import math

def pair(s):
    *array, = map(int,s.split())
    return [[i,y]for i,y in zip(array[::2], array[1::2])]

a = pair(input())
b = pair(input())
result = 0

while a and b:
    if a[0][0] > b[0][0]:
        result += b[0][0] * a[0][1] * b[0][1]
        a[0][0] -= b[0][0]
        b.pop(0)
    elif a[0][0] < b[0][0]:
        result += a[0][0] * a[0][1] * b[0][1]
        b[0][0] -= a[0][0]
        a.pop(0)
    else:
        result += a[0][0] * a[0][1] * b[0][1]
        a.pop(0)
        b.pop(0)

print(result)