r = int(input())
v = int(input())
vs = []

for i in range(v):
    c, n = [int(j) for j in input().split()]
    vs += 10**n*5**(c-n),

t = 0

while vs:
    shortest = min(vs[:r])
    for i in range(min(len(vs),r)):
        vs[i]-=shortest
    t += shortest
    vs = [x for x in vs if x!=0]

print(t)
