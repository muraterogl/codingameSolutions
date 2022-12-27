w,h = map(int,input().split())
first = step = int(input())
obs = set()
cy=cx=-1
d=0
dd=lambda:[(-1,0),(0,1),(1,0),(0,-1)][d]
seen={}
for y in range(h):
    row = input()
    for x in range(w):
        if row[x]=='#':
            obs.add((y,x))
        elif row[x]=='O':
            cy=y
            cx=x     
while step>0:
    dy,dx = dd()
    while (cy+dy,cx+dx) in obs:
        d = (d+1)%4
        dy,dx = dd()
    cy+=dy
    cx+=dx
    step-=1
    if (cy,cx,d) in seen:
        prev_step = seen[(cy,cx,d)]
        step %= prev_step-step
    else:
        seen[(cy,cx,d)] = step


print(cx,cy)
