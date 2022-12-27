import re

d = {"um":1,"mm":10**3,"cm":10**4,"dm":10**5,"m":10**6,"km":10**9}
a, u1, b, u2 = re.findall(r'(\d+\.?\d*)(\w+) \+ (\d+\.?\d*)(\w+)',input())[0]
a=float(a)
b=float(b)
u=u1 if d[u1]<=d[u2] else u2

print(f"{(a*d[u1]+b*d[u2])/d[u]:g}{u}")
