import sys
import math
import re


n = int(input())
arrays = {}
arrayOffsets = {}
for i in range(n):
    array, values = input().split(" = ")
    values = values.split()
    identifier = re.findall(r"(.+)\[", array)[0]
    arrayOffsets[identifier] = int(re.findall(r"(-?\d+)", array)[0])
    arrays[identifier] = values

result = input()

def changer(c):
    identifier, value = c[1], c[2]
    value = int(value) - arrayOffsets[identifier]
    return arrays[identifier][value]

while "[" in result:
    result = re.sub(r"([^\[\]]+)\[(-?\d+)\]", changer, result)

print(result)
