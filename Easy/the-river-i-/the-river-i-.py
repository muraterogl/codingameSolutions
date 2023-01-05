r1 = int(input())
r2 = int(input())
set1 = set([r1])
set2 = set([r2])
while True:
    r1 += sum(map(int,str(r1)))
    r2 += sum(map(int,str(r2)))
    if r1 in set2:
        print(r1)
        break
    if r2 in set1:
        print(r2)
        break
    set1.add(r1)
    set2.add(r2)
