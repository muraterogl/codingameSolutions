l = []
x = 0
for c in input():
    if c == "<":
        x -= 1
    elif c == ">":
        x += 1
    elif c == "-":
        if x > -len(l):
            l.pop(x-1)
    elif x==0:
        l += c,
    else:
        l.insert(x, c)
    x = min(0, max(-len(l), x))

print("".join(l))
