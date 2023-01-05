from string import ascii_uppercase as letters

a,b,c = input().split("-")
n = int(input())

def next_str(d):
    x, y = [letters.index(i) for i in d]
    y += 1
    if y>25:
        y = 0
        x += 1
        if x>25:
            return "AAA"
    return letters[x] + letters[y]

while n:
    x = min(n, 1000-int(b))
    b = str(int(b) + x).rjust(3, "0")
    if b == "1000":
        b = "001"
        c = next_str(c)
        if c == "AAA":
            c = "AA"
            a = next_str(a)
    n -= x

print(a,b,c,sep="-")
