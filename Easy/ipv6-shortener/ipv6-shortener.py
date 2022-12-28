import re
ip = input()
zeros = re.findall(r'((0000:?)+)',ip)
if zeros:
    m = max(zeros,key=lambda x:len(x[0]))[0]
    if len(m) > 5:
        ip = ip.replace(m,":",1)
for x in re.findall(r'\w+',ip):
    n = x.lstrip("0")
    if n=="":
        n = "0"
    ip = ip.replace(x, n, 1)
if ip[0]==":":
    ip = ":"+ip
print(ip)
