n = int(input())
m = [input()for _ in range(n)]
for y in range(n):
    for x in range(n):
        if m[y][x]=="a":
            q = [(ord("a"), [(y,x)])]
            while q:
                o, path = q.pop(0)
                if o==ord("z"):
                    path = set(path)
                    for j in range(n):
                        row = ""
                        for i in range(n):
                            if (j,i) in path:
                                row += m[j][i]
                            else:
                                row += "-"
                        print(row)

                    exit()
                no = o+1
                cy,cx = path[-1]
                for dy,dx in ((0,1),(0,-1),(1,0),(-1,0)):
                    if 0<=cy+dy<n and 0<=cx+dx<n and ord(m[cy+dy][cx+dx])==no:
                        q += [(no, path+[(cy+dy,cx+dx)])]
