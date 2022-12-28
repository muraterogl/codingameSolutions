n = int(input())
for i in range(n):
    r = input()+"...."
    c = 0
    last = -2
    for j in range(1,len(r)):
        if r[j-1]=="f" and j>last+2:
            c+=1
            last=j
    print(c)
