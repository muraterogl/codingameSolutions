import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def printLetter(alph, word):
    for i in range(h):
        for c in word:
            print(alph[i][ord(c.lower())-97 if c.isalpha() else 26],end="")
        print("")

l = int(input())
h = int(input())
t = input()
alph = [[] for i in range(h)]
for i in range(h):
    row = input()
    alph[i] = [row[j:j+l] for j in range(0, len(row), l)]

printLetter(alph, t)


 
