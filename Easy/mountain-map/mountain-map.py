n = int(input())
*h, = map(int, input().split())
h_max = max(h)
for i in range(h_max):
    print(("".join([(""if h_max-i>x else "/"+" "*((x+i-h_max)*2)+"\\").center(2*x)for x in h])).rstrip())
