import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
results = []
operations=[]
arg1s = []
arg2s = []
isOk = False
for i in range(n):
    operation, arg_1, arg_2 = input().split()
    operations.append(operation)
    arg1s.append(arg_1)
    arg2s.append(arg_2)
    results.append(None)
while not isOk:
    for i in range(n):
        if "$" in arg1s[i] and results[int(arg1s[i].split("$")[1])]:
            arg1s[i] = results[int(arg1s[i].split("$")[1])]
        if "$" in arg2s[i] and results[int(arg2s[i].split("$")[1])]:
            arg2s[i] = results[int(arg2s[i].split("$")[1])]

        if operations[i] == "VALUE":
            if not "$" in arg1s[i]:
                results[i] = arg1s[i]
        else:
            operation = "+" if operations[i] == "ADD" else "-" if operations[i] == "SUB" else "*"
            if not "$" in arg1s[i] and not "$" in arg2s[i]:
                results[i] = str(eval(arg1s[i] + operation + arg2s[i]))
        if not None in results:
            isOk = True

for result in results:
    print(result)
 
