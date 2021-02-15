import re
counts = []

b = input()

for i in range(len(b)):
    newBits = b[:i] + "1" + b[i+1:]
    counts.append(max(map(len,re.findall(r"1+", newBits))))

print(max(counts))