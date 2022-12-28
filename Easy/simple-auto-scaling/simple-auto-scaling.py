import math

s, m = [int(i) for i in input().split()]
*max_clients, = map(int, input().split())
open_clients = [0 for _ in range(s)]
for i in range(m):
    *clients, = map(int, input().split())
    l = []
    for j in range(s):
        r = math.ceil(clients[j] / max_clients[j])
        l += r-open_clients[j],
        open_clients[j] = r
    print(*l)
