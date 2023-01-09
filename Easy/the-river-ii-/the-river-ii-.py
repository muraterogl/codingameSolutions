n = int(input())
print(["NO","YES"][any(i+sum(map(int,str(i)))==n for i in range(n))])
