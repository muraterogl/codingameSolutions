import sys
import math

l = int(input())
n = int(input())
results = [[0,l]]
for i in range(n):
    st, ed = [int(j) for j in input().split()]
    newResults = []
    
    for result in results:
        if ed <= result[0] or st >= result[1]:
            newResults.append(result)
        
        elif st <= result[0] and ed >= result[0] and ed < result[1]:
            newResults.append([ed, result[1]])

        elif st > result[0] and ed < result[1]:
            newResults.append([result[0], st])
            newResults.append([ed, result[1]])

        elif st > result[0] and st < result[1] and ed >= result[1]:
            newResults.append([result[0], st])

    results = newResults
            

for result in results:
    print(*result)

if len(results) == 0:
    print("All painted") 
