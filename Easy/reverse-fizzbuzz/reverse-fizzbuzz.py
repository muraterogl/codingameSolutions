import sys
import math

def gcd(l):
    result = l[0]
    for i in l[1:]:
        result = math.gcd(result, i)
    return result

q = []
index = None
for i in range(int(input())):
    line = input()
    if line.isdecimal():
        index = int(line)
        q += [None, int(line)],
    else:
        if index:
            index+=1
        q += [line, index],


index = None
f = []
b = []
fb = []

for i in q[::-1]:
    if index==None and i[1]==None:
        i[1] = len(q)
        index = i[1]
    elif index==None:
        index = i[1]
    elif i[1]==None:
        i[1] = index

    if i[0]=="Fizz": f += i[1],
    if i[0]=="Buzz": b += i[1],
    if i[0]=="FizzBuzz": fb += i[1],
    index -= 1

if f: f=gcd(f)
if b: b=gcd(b)
if fb: fb=gcd(fb)

if not f and not b: f=b=fb
if not f:f=fb//b
if not b:b=fb//f

print(f,b)