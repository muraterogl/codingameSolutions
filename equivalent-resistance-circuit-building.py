import sys
import math
import re


n = int(input())
r = {}

#Resistor names and values
for i in range(n):
    x=input().split()
    r[x[0]]=int(x[1])


c = input()

def findElements(resString):
    elements = []
    paranthesis = []
    hold = ""

    for character in resString:

        if character == " ":
            #If paranthesis' are matched append to elements
            if len(paranthesis) == 0:
                elements.append(hold)
                hold = ""

            else:
                hold += character

        elif character == "(" or character == "[":
            paranthesis.append(character)
            hold += character

        elif character == ")" or character == "]":
            paranthesis.pop(-1)
            hold += character

        else:
            hold += character

    if hold != "":
        elements.append(hold)

    return elements

def findRes(s):
    if s in r:
        return r[s]
    else:
        #elements = re.findall(r"\[.*\]|\(.*\)|\w+",s[2:-2])
        elements = findElements(s[2:-2])

        #Series
        if s[0] == "(":
            return sum([findRes(element) for element in elements])
        
        #Parallel
        else:
            return 1/sum([1/findRes(element) for element in elements])
        
        

print(f"{findRes(c):.1f}")
