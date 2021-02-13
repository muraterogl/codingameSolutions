n = int(input())
d={}
for i in range(n):
    inputs = input().split()
    b = inputs[0]
    c = int(inputs[1])
    d[b]=chr(c)
text = input()

res = ""
i=0
while text:
    l=len(text)
    for k in d:
        if text.startswith(k):
            res += d[k]
            text = text[len(k):]
    if l==len(text):
        print(f"DECODE FAIL AT INDEX {i}")
        exit()
    i+=l-len(text)
print(res) 
