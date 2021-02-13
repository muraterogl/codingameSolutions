import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
exts = []
mts = []
for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    exts.append(ext.lower())
    mts.append(mt)
for i in range(q):
    fname = input().split('.')  # One file name per line.
    #print(fname)
    if len(fname) < 2:
        print("UNKNOWN")
    else:
        try:
            print(mts[exts.index(fname[-1].lower())])
        except:
            print("UNKNOWN") 
