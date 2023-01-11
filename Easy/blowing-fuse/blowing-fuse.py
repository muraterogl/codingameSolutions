n, m, c = map(int, input().split())
*d, = map(int, input().split())
d_w = [False for _ in d]
max_used = 0
for i in input().split():
    mx = int(i)
    d_w[mx-1] = not d_w[mx-1]
    total = sum(x*y for x,y in zip(d,d_w))
    if total > c:
        print("Fuse was blown.")
        exit()
    max_used = max(max_used, total)

print("Fuse was not blown.")
print(f"Maximal consumed current was {max_used} A.")
