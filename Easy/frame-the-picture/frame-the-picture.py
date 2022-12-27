p = input()  # the ASCII art pattern to use to frame the picture
# h: the height of the picture
# w: the width  of the picture
h, w = [int(i) for i in input().split()]
l = len(p)
for i in range(l):
    s = p[:i+1]
    print(s+p[i]*(w+2+(l-len(s))*2)+s[::-1])
print(p + " "*(w+2) + p[::-1])
for i in range(h):
    line = input()  # the ASCII art picture line by line
    print(p+" "+line+" "+p[::-1])
print(p + " "*(w+2) + p[::-1])
for i in range(l-1,-1,-1):
    s = p[:i+1]
    print(s+p[i]*(w+2+(l-len(s))*2)+s[::-1])
